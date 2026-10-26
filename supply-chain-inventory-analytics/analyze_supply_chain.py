from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / 'data' / 'supply_chain_orders.csv'
OUTPUT_DIR = BASE_DIR / 'outputs'
REQUIRED = {'order_id', 'order_date', 'region', 'warehouse', 'category', 'sku', 'quantity', 'unit_price', 'unit_cost', 'lead_time_days', 'stock_on_hand', 'reorder_point'}
NUMERIC_COLUMNS = ['quantity', 'unit_price', 'unit_cost', 'lead_time_days', 'stock_on_hand', 'reorder_point']


def main():
    df = pd.read_csv(DATA_PATH)
    missing = REQUIRED.difference(df.columns)
    if missing:
        raise ValueError('Missing required columns: {}'.format(sorted(missing)))

    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    for column in NUMERIC_COLUMNS:
        df[column] = pd.to_numeric(df[column], errors='coerce')
    if df['order_date'].isna().any():
        raise ValueError('Some order_date values could not be parsed.')
    if df[NUMERIC_COLUMNS].isna().any().any():
        raise ValueError('Numeric columns contain missing or invalid values.')
    if (df[NUMERIC_COLUMNS] < 0).any().any():
        raise ValueError('Numeric quantity, price, lead-time, and stock fields must not be negative.')
    if df['order_id'].isna().any() or df['order_id'].duplicated().any():
        raise ValueError('order_id contains blank or duplicate values.')
    if df['sku'].isna().any():
        raise ValueError('sku contains blank values.')
    if (df['unit_cost'] > df['unit_price']).any():
        print('Warning: some rows have unit cost greater than unit price.')

    df['sales'] = df['quantity'] * df['unit_price']
    df['estimated_cost'] = df['quantity'] * df['unit_cost']
    df['gross_profit'] = df['sales'] - df['estimated_cost']
    df['gross_margin_pct'] = df['gross_profit'].div(df['sales'].where(df['sales'].ne(0))).mul(100)
    df['month'] = df['order_date'].dt.to_period('M').astype(str)
    df['reorder_flag'] = df['stock_on_hand'] <= df['reorder_point']
    total_sales = df['sales'].sum()
    total_profit = df['gross_profit'].sum()
    total_cost = df['estimated_cost'].sum()
    kpis = pd.DataFrame([
        {'metric': 'order_count', 'value': int(df['order_id'].nunique())},
        {'metric': 'total_units', 'value': int(df['quantity'].sum())},
        {'metric': 'total_sales', 'value': round(total_sales, 2)},
        {'metric': 'estimated_cost', 'value': round(total_cost, 2)},
        {'metric': 'estimated_gross_profit', 'value': round(total_profit, 2)},
        {'metric': 'estimated_gross_margin_pct', 'value': round(total_profit / total_sales * 100, 2) if total_sales else 0},
        {'metric': 'unique_skus', 'value': int(df['sku'].nunique())},
    ])
    OUTPUT_DIR.mkdir(exist_ok=True)
    kpis.to_csv(OUTPUT_DIR / 'kpi_summary.csv', index=False)

    category = df.groupby('category', as_index=False).agg(order_count=('order_id', 'nunique'), units=('quantity', 'sum'), sales=('sales', 'sum'), estimated_cost=('estimated_cost', 'sum'), estimated_gross_profit=('gross_profit', 'sum'))
    category['estimated_gross_margin_pct'] = category['estimated_gross_profit'].div(category['sales'].where(category['sales'].ne(0))).mul(100).round(2)
    category = category.sort_values('sales', ascending=False)
    category.to_csv(OUTPUT_DIR / 'category_summary.csv', index=False)

    monthly = df.groupby('month', as_index=False).agg(order_count=('order_id', 'nunique'), units=('quantity', 'sum'), sales=('sales', 'sum'), estimated_gross_profit=('gross_profit', 'sum')).sort_values('month')
    monthly.to_csv(OUTPUT_DIR / 'monthly_sales.csv', index=False)

    region = df.groupby('region', as_index=False).agg(order_count=('order_id', 'nunique'), sales=('sales', 'sum'), estimated_gross_profit=('gross_profit', 'sum')).sort_values('sales', ascending=False)
    region.to_csv(OUTPUT_DIR / 'region_summary.csv', index=False)

    warehouse = df.groupby('warehouse', as_index=False).agg(order_count=('order_id', 'nunique'), sales=('sales', 'sum'), average_lead_time_days=('lead_time_days', 'mean')).sort_values('sales', ascending=False)
    warehouse.to_csv(OUTPUT_DIR / 'warehouse_summary.csv', index=False)

    # Inventory values repeat on order rows. Keep one latest row per SKU/warehouse for this demo.
    inventory = df.sort_values('order_date').drop_duplicates(['sku', 'warehouse'], keep='last')
    alerts = inventory.loc[inventory['reorder_flag'], ['sku', 'category', 'warehouse', 'stock_on_hand', 'reorder_point', 'lead_time_days']].sort_values(['warehouse', 'category', 'sku'])
    alerts.to_csv(OUTPUT_DIR / 'inventory_reorder_alerts.csv', index=False)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(category['category'], category['sales'])
    ax.set_title('Sales by Product Category')
    ax.set_xlabel('Category')
    ax.set_ylabel('Sales (demo currency units)')
    ax.tick_params(axis='x', rotation=25)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / 'sales_by_category.png', dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(monthly['month'], monthly['sales'], marker='o', label='Sales')
    ax.plot(monthly['month'], monthly['estimated_gross_profit'], marker='o', label='Estimated gross profit')
    ax.set_title('Monthly Sales and Estimated Gross Profit')
    ax.set_xlabel('Month')
    ax.set_ylabel('Amount (demo currency units)')
    ax.tick_params(axis='x', rotation=45)
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / 'monthly_sales_trend.png', dpi=160)
    plt.close(fig)

    print('Analysis completed: {} rows processed.'.format(len(df)))
    print(kpis.to_string(index=False))
    print('Outputs saved to: {}'.format(OUTPUT_DIR))


if __name__ == '__main__':
    main()
