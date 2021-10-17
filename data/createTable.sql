--CREATING PATIENTS TABLE
-- db name - IncubyteHospital
-- table name - PATIENTS
-- holds data for every patient that has been vaccinated
Create TABLE PATIENTS
(
    CUSTOMER_NAME VARCHAR(255) NOT NULL,
    CUSTOMER_ID vARCHAR(18) PRIMARY KEY,
    CUSTOMER_OPEN_DATE DATE NOT NULL,
    LAST_CONSULTED_DATE DATE,
    VACCINATION_TYPE CHAR(5),
    DOCTOR_CONSULTED CHAR(255),
    STATE CHAR(5),
    COUNTRY CHAR(5),
    DOB DATE,
    FLAG CHAR(1)
);
--adding dummy data for test cases
INSERT INTO IncubyteHospital.PATIENTS 
VALUES(
    'ABHI','1','2021-10-10','2021-10-10','CVS','HARI','UP','IND','1997-05-22','N'),
    'NEHA','2','2021-10-9','2021-10-9','CVS','HARI','SYDNEY','AUS','1996-04-01','N'),
    'JAMES','3','2021-10-1','2021-10-1','CVS','HARI','SYDNEY','AUS','1991-08-01','N'),
    'NAVIN','4','2021-09-1','2021-09-1','CVS','HARI','MP','IND','1967-08-01','N'
    );