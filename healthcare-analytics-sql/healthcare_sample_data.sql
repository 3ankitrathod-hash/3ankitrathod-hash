-- Fictional test records for local practice and automated validation only.
-- Run after healthcare_schema.sql. These are not real patient or provider records.
USE healthcare_analytics_practice;

INSERT INTO departments
(department_id, department_name, city, location_floor, phone_extension, total_staff, budget_allocation, established_year, shift_timing, head_doctor_id)
VALUES
(1, 'Cardiology', 'Bengaluru', '2', '1001', 12, 250000.00, 2010, 'Day', NULL),
(2, 'General Medicine', 'Bengaluru', '1', '1002', 20, 180000.00, 2012, 'Day', NULL);

INSERT INTO doctors
(doctor_id, first_name, last_name, gender, specialization, department_id, city, experience_years, phone, email, joining_date, consultation_fee, status)
VALUES
(101, 'Asha', 'Mehta', 'Female', 'Cardiology', 1, 'Bengaluru', 14, '9000000101', 'asha.test101@example.com', '2015-01-10', 700.00, 'Active'),
(102, 'Rohan', 'Shah', 'Male', 'General Medicine', 2, 'Bengaluru', 8, '9000000102', 'rohan.test102@example.com', '2019-06-15', 450.00, 'Active'),
(103, 'Neha', 'Rao', 'Female', 'General Medicine', 2, 'Pune', 18, '9000000103', 'neha.test103@example.com', '2010-03-20', 600.00, 'On Leave');

INSERT INTO patients
(patient_id, first_name, last_name, gender, date_of_birth, phone, email, address, city, blood_group, admission_date, discharge_date, doctor_id, insurance_provider)
VALUES
(201, 'Sample', 'PatientA', 'Female', '1990-04-12', '9000000201', 'patient201@example.com', 'Test Street 1', 'Bengaluru', 'A+', NULL, NULL, 101, NULL),
(202, 'Sample', 'PatientB', 'Male', '1985-07-21', '9000000202', 'patient202@example.com', 'Test Street 2', 'Mumbai', 'B+', NULL, NULL, 102, 'Demo Insurance'),
(203, 'Sample', 'PatientC', 'Other', '2000-11-03', '9000000203', 'patient203@example.com', 'Test Street 3', 'Bangalore', 'O+', NULL, NULL, 101, NULL);

INSERT INTO appointments
(appointment_id, patient_id, doctor_id, department_id, appointment_date, appointment_time, purpose, diagnosis, status, follow_up_required, follow_up_date, created_at)
VALUES
(401, 201, 101, 1, '2026-01-10', '09:00:00', 'Consultation', NULL, 'Completed', FALSE, NULL, '2026-01-10 08:00:00'),
(402, 202, 102, 2, '2026-01-12', '10:00:00', 'Routine Check', NULL, 'Completed', FALSE, NULL, '2026-01-12 09:00:00'),
(403, 203, 101, 1, '2026-02-05', '11:00:00', 'Consultation', NULL, 'Completed', TRUE, '2026-02-20', '2026-02-05 10:00:00');

INSERT INTO bills
(bill_id, appointment_id, patient_id, doctor_id, total_amount, discount, insurance_amount, net_amount, payment_mode, payment_status, billing_date, due_date, insurance_claimed)
VALUES
(501, 401, 201, 101, 5000.00, 0.00, NULL, 5000.00, 'UPI', 'Paid', '2026-01-10', '2026-01-20', FALSE),
(502, 402, 202, 102, 2500.00, 100.00, NULL, 2400.00, 'Card', 'Paid', '2026-01-12', '2026-01-22', FALSE),
(503, 403, 203, 101, 3500.00, 0.00, NULL, 3500.00, 'UPI', 'Pending', '2026-02-05', '2026-02-15', FALSE);
