-- Safe, schema-only version for portfolio practice.
-- It does not DROP a database and contains no sample names, phone numbers, emails, or addresses.
-- MySQL 8 required for the utf8mb4_0900_ai_ci collation.
CREATE DATABASE IF NOT EXISTS healthcare_analytics_practice CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE healthcare_analytics_practice;

CREATE TABLE IF NOT EXISTS departments (
  department_id INT PRIMARY KEY AUTO_INCREMENT,
  department_name VARCHAR(100) NOT NULL,
  city VARCHAR(80) NOT NULL,
  location_floor VARCHAR(20) NOT NULL,
  phone_extension VARCHAR(10) NOT NULL,
  total_staff INT NOT NULL DEFAULT 0,
  budget_allocation DECIMAL(12,2) NOT NULL DEFAULT 0,
  established_year INT NOT NULL,
  shift_timing VARCHAR(50) NOT NULL,
  head_doctor_id INT NULL
) ENGINE=InnoDB;
CREATE TABLE IF NOT EXISTS doctors (
  doctor_id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  gender ENUM('Male','Female','Other') NOT NULL,
  specialization VARCHAR(100) NOT NULL,
  department_id INT NOT NULL,
  city VARCHAR(80) NOT NULL,
  experience_years INT NOT NULL CHECK (experience_years >= 0),
  phone VARCHAR(15) NOT NULL UNIQUE,
  email VARCHAR(100) NOT NULL UNIQUE,
  joining_date DATE NOT NULL,
  consultation_fee DECIMAL(10,2) NOT NULL CHECK (consultation_fee >= 0),
  status ENUM('Active','On Leave','Retired') NOT NULL DEFAULT 'Active',
  CONSTRAINT fk_doc_dept FOREIGN KEY (department_id) REFERENCES departments(department_id)
) ENGINE=InnoDB;
CREATE TABLE IF NOT EXISTS patients (
  patient_id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  gender ENUM('Male','Female','Other') NOT NULL,
  date_of_birth DATE NOT NULL,
  phone VARCHAR(15) NOT NULL UNIQUE,
  email VARCHAR(100) NOT NULL UNIQUE,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(80) NOT NULL,
  blood_group ENUM('A+','A-','B+','B-','AB+','AB-','O+','O-') NOT NULL,
  admission_date DATE NULL,
  discharge_date DATE NULL,
  doctor_id INT NULL,
  insurance_provider VARCHAR(100) NULL,
  CONSTRAINT fk_patient_doctor FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
) ENGINE=InnoDB;
CREATE TABLE IF NOT EXISTS appointments (
  appointment_id INT PRIMARY KEY AUTO_INCREMENT,
  patient_id INT NOT NULL,
  doctor_id INT NOT NULL,
  department_id INT NOT NULL,
  appointment_date DATE NOT NULL,
  appointment_time TIME NOT NULL,
  purpose VARCHAR(100) NOT NULL,
  diagnosis VARCHAR(255) NULL,
  status ENUM('Scheduled','Completed','Cancelled') NOT NULL,
  follow_up_required BOOLEAN NOT NULL DEFAULT FALSE,
  follow_up_date DATE NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_appt_patient FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
  CONSTRAINT fk_appt_doctor FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id),
  CONSTRAINT fk_appt_department FOREIGN KEY (department_id) REFERENCES departments(department_id)
) ENGINE=InnoDB;
CREATE TABLE IF NOT EXISTS bills (
  bill_id INT PRIMARY KEY AUTO_INCREMENT,
  appointment_id INT NOT NULL UNIQUE,
  patient_id INT NOT NULL,
  doctor_id INT NOT NULL,
  total_amount DECIMAL(10,2) NOT NULL CHECK (total_amount >= 0),
  discount DECIMAL(10,2) NOT NULL DEFAULT 0 CHECK (discount >= 0),
  insurance_amount DECIMAL(10,2) NULL CHECK (insurance_amount >= 0),
  net_amount DECIMAL(10,2) NOT NULL,
  payment_mode ENUM('Cash','Card','Insurance','UPI') NOT NULL,
  payment_status ENUM('Paid','Pending','Rejected') NOT NULL DEFAULT 'Pending',
  billing_date DATE NOT NULL,
  due_date DATE NOT NULL,
  insurance_claimed BOOLEAN NOT NULL DEFAULT FALSE,
  CONSTRAINT fk_bill_appt FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id),
  CONSTRAINT fk_bill_patient FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
  CONSTRAINT fk_bill_doctor FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
) ENGINE=InnoDB;
CREATE TABLE IF NOT EXISTS medications (
  medication_id INT PRIMARY KEY AUTO_INCREMENT,
  appointment_id INT NOT NULL,
  patient_id INT NOT NULL,
  doctor_id INT NOT NULL,
  generic_name VARCHAR(100) NOT NULL,
  brand_name VARCHAR(100) NOT NULL,
  dosage VARCHAR(50) NOT NULL,
  frequency VARCHAR(50) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NULL,
  notes VARCHAR(255) NULL,
  status ENUM('Active','Completed') NOT NULL DEFAULT 'Active',
  prescribed_date DATE NOT NULL,
  CONSTRAINT fk_meds_appt FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id),
  CONSTRAINT fk_meds_patient FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
  CONSTRAINT fk_meds_doctor FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
) ENGINE=InnoDB;
