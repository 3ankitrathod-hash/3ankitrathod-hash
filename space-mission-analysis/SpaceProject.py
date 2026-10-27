#!/usr/bin/env python
# coding: utf-8

# In[76]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[77]:


pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 100)


# In[78]:


sns.set_style("whitegrid")


# In[79]:


from pathlib import Path

possible_paths = [Path("data") / "space_mission_data.csv", Path("space_mission_data.csv")]
DATA_PATH = next((path for path in possible_paths if path.exists()), None)
if DATA_PATH is None:
    raise FileNotFoundError(
        "Dataset not found. Place space_mission_data.csv in this project's data/ folder "
        "or beside this script. The repository includes a small synthetic demo dataset; see the README for its limitations."
    )

df = pd.read_csv(DATA_PATH)
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

required_columns = ["Date", "Mission_Status", "Price", "Organisation", "Rocket_Status", "Location"]
missing_columns = [column for column in required_columns if column not in df.columns]
if missing_columns:
    raise KeyError(f"Dataset is missing required columns: {missing_columns}")

df["Price"] = (
    df["Price"].astype("string").str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False).str.strip()
)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")


# In[9]:


df.describe(include = 'all')


# In[10]:


df.head()


# In[11]:


df.tail()


# In[12]:


df.shape


# In[13]:


df.columns


# In[14]:


df.info()


# In[15]:


missing_data = pd.DataFrame({
    'Missing Values': df.isnull().sum(),
    'Percentage': (df.isnull().sum() / len(df)) * 100})

missing_data.sort_values(
    by='Missing Values',
    ascending=False)


# In[80]:


df.duplicated().sum()


# In[17]:


for column in df.columns:
    print("\n", column)
    print("Unique values:", df[column].nunique())


# In[18]:


# Optional exported index column is removed safely during loading if present.


# In[19]:


df["Date"].dtype


# In[20]:


df['Date'] = pd.to_datetime(
    df['Date'],
    errors='coerce',
    utc=True)


# In[21]:


df['Date'].isnull().sum() # There are 126 missing date and time.


# In[22]:


df[df['Date'].isnull()].head(20)


# In[23]:


df[df['Date'].isnull()]['Mission_Status'].value_counts() 
# this will how many details are missing for success,failure, prelaunch failure.


# In[24]:


df['Year'] = df['Date'].dt.year


# In[25]:


df['Month'] = df['Date'].dt.month


# In[26]:


df['Month_Name'] = df['Date'].dt.month_name()


# In[27]:


df['Decade'] = (df['Year'] //10)*10


# In[28]:


df['Price'].head(5)


# In[29]:


# Price was cleaned and converted before the first analysis.


# In[30]:


df['Price'].dtype


# In[31]:


df['Price'].isnull().sum()


# In[32]:


df['Price'].isnull().mean()* 100


# In[33]:


(df.isnull().sum()/ len(df)) *100


# In[34]:


df['Organisation'].value_counts()


# In[35]:


df['Rocket_Status'].value_counts()


# In[36]:


df['Mission_Status'].value_counts()


# In[37]:


df.info()


# In[38]:


df.shape


# ## Univariate Analysis

# In[39]:


df['Mission_Status'].value_counts()


# In[40]:


df['Mission_Status'].value_counts(normalize = True)*100


# In[41]:


plt.figure(figsize=(8,4))

sns.countplot(
    color="steelblue",
    data=df,
    x='Mission_Status',
    order=df['Mission_Status'].value_counts().index
)

plt.title('Distribution of Mission Status')
plt.xlabel('Mission Status')
plt.ylabel('Number of Missions')
plt.xticks(rotation=20)

plt.show()


# In[42]:


plt.figure(figsize=(7,5))

sns.countplot(
    color="steelblue",
    data=df,
    x='Rocket_Status'
)

plt.title('Distribution of Rocket Status')
plt.xlabel('Rocket Status')
plt.ylabel('Number of Missions')

plt.show()


# In[43]:


top_orgs = df['Organisation'].value_counts().head(10)

plt.figure(figsize=(10,6))

sns.barplot(
    color="steelblue",
    x=top_orgs.values,
    y=top_orgs.index
)

plt.title('Top 10 Organisations by Number of Missions')
plt.xlabel('Number of Missions')
plt.ylabel('Organisation')

plt.show()


# In[ ]:





# In[44]:


price_data = df.dropna(subset=['Price'])


# In[ ]:





# In[45]:


top_locations = df['Location'].value_counts().head(10)

plt.figure(figsize=(8,7))

sns.barplot(
    color="steelblue",
    x=top_locations.values,
    y=top_locations.index
)

plt.title('Top 10 Launch Locations')
plt.xlabel('Number of Missions')
plt.ylabel('Location')

plt.show()


# In[46]:


price_data = df.dropna(subset = ['Price'])


# In[47]:


missions_per_year = df.groupby('Year').size()

plt.figure(figsize=(14,6))

plt.plot(
    missions_per_year.index,
    missions_per_year.values
)

plt.title('Number of Space Missions by Year')
plt.xlabel('Year')
plt.ylabel('Number of Missions')

plt.show()


# In[48]:


missions_per_decade = df.groupby('Decade').size()

plt.figure(figsize=(12,6))

sns.barplot(
    color="steelblue",
    x=missions_per_decade.index,
    y=missions_per_decade.values
)

plt.title('Number of Space Missions by Decade')
plt.xlabel('Decade')
plt.ylabel('Number of Missions')

plt.show()


# In[49]:


mission_year = pd.crosstab(
    df['Year'],
    df['Mission_Status']
)

mission_year.plot(
    figsize=(14,6)
)

plt.title('Mission Outcomes Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Missions')

plt.show()


# In[50]:


df['Successful'] = df['Mission_Status'].map(
    lambda status: 1.0 if status == 'Success' else (0.0 if pd.notna(status) else np.nan)
)


# In[51]:


success_rate_year = (
    df.groupby('Year')['Successful']
      .mean() * 100
)


# In[52]:


plt.figure(figsize=(14,6))

plt.plot(
    success_rate_year.index,
    success_rate_year.values
)

plt.title('Mission Success Rate Over Time')
plt.xlabel('Year')
plt.ylabel('Success Rate (%)')

plt.ylim(0, 100)

plt.show()


# ### Organisational Analysis: 

# In[53]:


org_missions = (
    df['Organisation']
    .value_counts()
)

org_missions.head(15)


# In[54]:


org_success = (
    df.groupby('Organisation')['Successful']
      .agg(['count', 'mean'])
)

org_success['Success_Rate'] = org_success['mean'] * 100

org_success = org_success.drop(columns='mean')

org_success.sort_values(
    'count',
    ascending=False
).head(20)


# In[55]:


org_success_20 = org_success[
    org_success['count'] >= 20
].sort_values(
    'Success_Rate',
    ascending=False
)
org_success_20


# In[56]:


plt.figure(figsize=(12,8))

sns.barplot(
    color="steelblue",
    data=org_success_20.head(10),
    x='Success_Rate',
    y=org_success_20.head(10).index)

plt.title('Success Rate of Organisations with at Least 20 Missions')

plt.xlabel('Success Rate (%)')
plt.ylabel('Organisation')

plt.xlim(0, 100)

plt.show()


# ## Organisation vs Mission Status

# In[57]:


top_10_orgs = df['Organisation'].value_counts().head(10).index

top_org_data = df[
    df['Organisation'].isin(top_10_orgs)
]


# In[58]:


org_status = pd.crosstab(
    top_org_data['Organisation'],
    top_org_data['Mission_Status'],
    normalize='index'
) * 100

org_status 
if 'Success' in org_status.columns:
    org_status = org_status.sort_values(by='Success', ascending=False)


# In[59]:


plt.figure(figsize=(8,4))

sns.heatmap(
    org_status,
    annot=True,
    fmt='.1f'
)

plt.title('Mission Status Distribution by Top Organisations')
plt.xlabel('Mission Status')
plt.ylabel('Organisation')

plt.show()


# In[60]:


# 1. Prepare crosstab data (as proportions 0 to 100)
org_status = pd.crosstab(
    top_org_data['Organisation'],
    top_org_data['Mission_Status'],
    normalize='index'
) * 100

# 2. Sort by success rate so the best performers appear on top
if 'Success' in org_status.columns:
    org_status = org_status.sort_values(by='Success', ascending=True)

# 3. Plot horizontal stacked bar chart
ax = org_status.plot(
    kind='barh',
    stacked=True,
    figsize=(12, 6),
    colormap='viridis'  # or 'coolwarm', 'RdYlGn'
)

plt.title('Mission Status Distribution by Top Organisations (%)', fontsize=14)
plt.xlabel('Percentage (%)', fontsize=12)
plt.ylabel('Organisation', fontsize=12)
plt.legend(title='Mission Status', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()
plt.show()


# ### Cost Analysis

# In[61]:


df['Price'].describe()


# In[62]:


# Price was cleaned before numeric conversion to avoid losing currency-formatted values.

# Now print safely
print("Mean:", df['Price'].mean())
print("Median:", df['Price'].median())


# In[63]:


price_data = df.dropna(subset=['Price']).copy()


# In[64]:


plt.figure(figsize=(8,5))

sns.boxplot(
    color="steelblue",
    x=df['Price']
)

plt.title('Distribution and Outliers of Mission Cost')
plt.xlabel('Mission Cost ($ million)')

plt.show()


# ### Top 10 Most Expensive Missions

# In[65]:


df[
    ['Organisation', 'Location', 'Date', 'Price', 'Mission_Status']
].sort_values(
    'Price',
    ascending=False
).head(10)


# ### Average Cost by Organisation

# In[66]:


org_cost = (
    price_data
    .groupby('Organisation')['Price']
    .agg(['count', 'mean', 'median'])
)

org_cost = org_cost[
    org_cost['count'] >= 10
]

org_cost.sort_values(
    'median',
    ascending=False
).head(15)


# ### Mission Cost vs Mission Status

# In[67]:


plt.figure(figsize=(10,6))

sns.boxplot(
    color="steelblue",
    data=price_data,
    x='Mission_Status',
    y='Price'
)

plt.title('Mission Cost by Mission Status')
plt.xlabel('Mission Status')
plt.ylabel('Mission Cost ($ million)')

plt.xticks(rotation=20)

plt.show()


# ### Relationship Analysis

# #Rocket Status vs Mission Status

# In[68]:


rocket_mission = pd.crosstab(
    df['Rocket_Status'],
    df['Mission_Status'],
    normalize='index'
) * 100

rocket_mission


# In[69]:


plt.figure(figsize=(10,6))

sns.heatmap(
    rocket_mission,
    annot=True,
    fmt='.1f'
)

plt.title('Mission Outcomes by Rocket Status')
plt.xlabel('Mission Status')
plt.ylabel('Rocket Status')

plt.show()


# ### Rocket Status vs Success

# In[70]:


df['Successful'] = np.where(
    df['Mission_Status'] == 'Success',
    1,
    0
)


# In[71]:


rocket_success = (
    df.groupby('Rocket_Status')['Successful']
      .mean() * 100
)

rocket_success


# In[72]:


plt.figure(figsize=(8,5))

sns.barplot(
    color="steelblue",
    x=rocket_success.index,
    y=rocket_success.values
)

plt.title('Mission Success Rate by Rocket Status')
plt.xlabel('Rocket Status')
plt.ylabel('Success Rate (%)')

plt.ylim(0,100)

plt.show()


# ## Cost vs Success

# In[73]:


price_data.groupby('Mission_Status')['Price'].agg(
    ['count', 'mean', 'median']
)


# In[ ]:





# ### Cost Distribution by Success

# In[74]:


plt.figure(figsize=(10,6))

sns.boxplot(
    color="steelblue",
    data=price_data,
    x='Mission_Status',
    y='Price'
)

plt.title('Mission Cost vs Mission Outcome')
plt.xlabel('Mission Status')
plt.ylabel('Mission Cost ($ million)')

plt.xticks(rotation=20)

plt.show()


# ### Organisation vs Cost vs Success

# In[75]:


top_cost_orgs = (
    price_data['Organisation']
    .value_counts()
    .head(10)
    .index
)

cost_org_data = price_data[
    price_data['Organisation'].isin(top_cost_orgs)
]

plt.figure(figsize=(12,7))

sns.boxplot(
    color="steelblue",
    data=cost_org_data,
    x='Organisation',
    y='Price'
)

plt.title('Mission Cost Distribution Across Major Organisations')
plt.xlabel('Organisation')
plt.ylabel('Mission Cost ($ million)')

plt.xticks(rotation=45)

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:



