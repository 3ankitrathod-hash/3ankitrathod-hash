-- Healthcare Analytics SQL practice queries (MySQL 8)
-- Run after healthcare_schema.sql. Tables remain empty until you add synthetic/authorized data.
USE healthcare_analytics_practice;

-- 1. Patients in Bengaluru or Bangalore.
SELECT patient_id, first_name, last_name, city
FROM patients
WHERE LOWER(city) IN ('bengaluru', 'bangalore')
ORDER BY last_name, first_name;

-- 2. Active doctors with more than ten years of experience.
SELECT doctor_id, first_name, last_name, specialization, experience_years, city
FROM doctors
WHERE status = 'Active' AND experience_years > 10
ORDER BY experience_years DESC;

-- 3. Patient count per doctor, including doctors with no assigned patients.
SELECT d.doctor_id, CONCAT(d.first_name, ' ', d.last_name) AS doctor_name,
       COUNT(p.patient_id) AS patient_count
FROM doctors AS d
LEFT JOIN patients AS p ON p.doctor_id = d.doctor_id
GROUP BY d.doctor_id, d.first_name, d.last_name
ORDER BY patient_count DESC, doctor_name;

-- 4. Paid bills summarized by payment mode.
SELECT payment_mode, COUNT(*) AS paid_bill_count, SUM(net_amount) AS total_paid_amount
FROM bills
WHERE payment_status = 'Paid'
GROUP BY payment_mode
ORDER BY total_paid_amount DESC;

-- 5. Top departments by paid revenue.
SELECT dep.department_id, dep.department_name, SUM(b.net_amount) AS paid_revenue
FROM departments AS dep
JOIN doctors AS d ON d.department_id = dep.department_id
JOIN bills AS b ON b.doctor_id = d.doctor_id
WHERE b.payment_status = 'Paid'
GROUP BY dep.department_id, dep.department_name
ORDER BY paid_revenue DESC
LIMIT 10;

-- 6. Reusable doctor revenue view.
CREATE OR REPLACE VIEW vw_doctor_revenue AS
SELECT d.doctor_id, CONCAT(d.first_name, ' ', d.last_name) AS doctor_name,
       dep.department_name,
       COUNT(CASE WHEN b.payment_status = 'Paid' THEN b.bill_id END) AS paid_bill_count,
       COALESCE(SUM(CASE WHEN b.payment_status = 'Paid' THEN b.net_amount ELSE 0 END), 0) AS total_paid_revenue
FROM doctors AS d
LEFT JOIN departments AS dep ON dep.department_id = d.department_id
LEFT JOIN bills AS b ON b.doctor_id = d.doctor_id
GROUP BY d.doctor_id, d.first_name, d.last_name, dep.department_name;

SELECT * FROM vw_doctor_revenue ORDER BY total_paid_revenue DESC, doctor_name;
