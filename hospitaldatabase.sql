-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 19, 2021 at 08:10 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.3.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hospitaldatabase`
--

-- --------------------------------------------------------

--
-- Table structure for table `admission`
--

CREATE TABLE `admission` (
  `PatientID` int(11) NOT NULL,
  `AdmissionStat` tinyint(1) NOT NULL,
  `RoomID` int(11) NOT NULL,
  `BedNo` int(11) NOT NULL,
  `DocID` int(11) NOT NULL,
  `AdmissionDate` date NOT NULL,
  `AdmissionTime` time NOT NULL,
  `ReleaseDate` date NOT NULL,
  `ReleaseTime` time NOT NULL,
  `Is_deleted` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admission`
--

INSERT INTO `admission` (`PatientID`, `AdmissionStat`, `RoomID`, `BedNo`, `DocID`, `AdmissionDate`, `AdmissionTime`, `ReleaseDate`, `ReleaseTime`, `Is_deleted`) VALUES
(2, 1, 5, 5, 7, '2021-04-23', '12:00:00', '2021-04-26', '02:00:00', 0),
(5, 1, 13, 5, 16, '2021-04-20', '12:00:00', '2021-04-22', '12:00:00', 0),
(6, 1, 14, 5, 12, '2020-02-20', '01:00:00', '2020-02-22', '02:00:00', 0);

-- --------------------------------------------------------

--
-- Table structure for table `diagnosticreport`
--

CREATE TABLE `diagnosticreport` (
  `PresID` int(11) NOT NULL,
  `DocID` int(11) NOT NULL,
  `Date` date NOT NULL,
  `Time` time NOT NULL,
  `Report` text NOT NULL,
  `Is_deleted` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `diagnosticreport`
--

INSERT INTO `diagnosticreport` (`PresID`, `DocID`, `Date`, `Time`, `Report`, `Is_deleted`) VALUES
(5, 12, '2020-04-20', '12:00:00', '5.00 mgl', 0),
(8, 17, '2020-04-23', '12:00:00', '200mg', 0),
(9, 12, '2020-10-20', '12:00:00', '20mg', 0),
(10, 18, '2020-04-20', '12:00:00', 'Tumor Detected', 0);

-- --------------------------------------------------------

--
-- Table structure for table `diagnostictests`
--

CREATE TABLE `diagnostictests` (
  `TestID` int(11) NOT NULL,
  `Name` text NOT NULL,
  `RoomID` int(11) NOT NULL,
  `Is_deleted` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `diagnostictests`
--

INSERT INTO `diagnostictests` (`TestID`, `Name`, `RoomID`, `Is_deleted`) VALUES
(1, 'X-Ray', 6, 0),
(2, 'ESR', 7, 0),
(3, 'CBC', 7, 0),
(4, 'Tropinin I', 8, 0),
(5, 'Feretin', 8, 0),
(6, 'Bilirubin', 9, 0),
(7, 'Serum HDL', 9, 0),
(8, 'CT Scan', 10, 0),
(9, 'MRI', 11, 0);

-- --------------------------------------------------------

--
-- Table structure for table `doctorsmanagement`
--

CREATE TABLE `doctorsmanagement` (
  `DocID` int(11) NOT NULL,
  `Name` text NOT NULL,
  `Sex` varchar(1) NOT NULL,
  `Expertise` text NOT NULL,
  `Degree` text NOT NULL,
  `Position` text NOT NULL,
  `Chamber` text NOT NULL,
  `Time` time NOT NULL,
  `Fee` int(11) NOT NULL,
  `Contactno` text NOT NULL,
  `Email` text NOT NULL,
  `is_deleted` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `doctorsmanagement`
--

INSERT INTO `doctorsmanagement` (`DocID`, `Name`, `Sex`, `Expertise`, `Degree`, `Position`, `Chamber`, `Time`, `Fee`, `Contactno`, `Email`, `is_deleted`) VALUES
(7, 'Siraj Haque', 'M', 'Medicine', 'Professor', '12th Floor', 'FCPS', '05:00:00', 24000, '0157841264', 'sirajdoc@gmail.com', 0),
(11, 'Mahboob Jahan', 'M', 'Opthalmology', 'Sr. Consultant', '10th Floor', 'MCPS', '12:00:00', 2400, '01759358796', 'mahboob@gmail.com', 0),
(12, 'Bipad Bhajan', 'M', 'Pediatrics', 'Sr. Consultant', '11th Floor', 'DCH', '02:00:00', 1000, '01556333100', 'bipad@yahoo.com', 0),
(13, 'Monirul Islam', 'M', 'Anesthesiology', 'Jr. Consultant', '10th floor', 'DA', '03:00:00', 1000, '01711003283', 'an@hotmail.com', 0),
(14, 'Ayesha Julekha', 'F', 'Orthopedic', 'Jr. Consultant', '2nd Floor', 'MBBS', '03:00:00', 1200, '01732267340', 'ayesha@gmail.com', 0),
(15, 'Nuri Zunnatul Fardous', 'M', 'Radiology', 'Radiologist', '3rd Floor', 'MCPS', '01:00:00', 2000, '01711069461', 'nuri@gmail.com', 0),
(16, 'Md. Shafiqul Islam', 'M', 'Pathology', 'Pathologist', '2nd Floor', 'MBBS', '03:00:00', 1000, '01711061814', 'shafi@gmail.com', 0),
(17, 'Wadud Chowdhury', 'M', 'Cardiology', 'Sr. Consultant', '3rd Floor', 'MCPS', '08:00:00', 2500, '0175698722', 'wadud@gmail.com', 0),
(18, 'Wahab Khan', 'M', 'Nephrology', 'Sr. Consultant', '6th Floor', 'MCPS', '02:00:00', 2400, '01569874223', 'wahab@gmail.com', 0),
(19, 'Farhana Yeasmin', 'F', 'Medicine', 'Sr. Consultant', '2nd Floor', 'MCPS', '02:00:00', 2400, '01698452335', 'yeasmin@gmail.com', 0),
(20, 'Rayda Khanom', 'F', 'Gynecology', 'Sr. Consultant', '7th Floor', 'MCPS', '01:00:00', 1000, '01569872368', 'ray@gmail.com', 0);

-- --------------------------------------------------------

--
-- Table structure for table `emergency`
--

CREATE TABLE `emergency` (
  `PatientID` int(11) NOT NULL,
  `DocID` int(11) NOT NULL,
  `Date` date NOT NULL,
  `Time` time NOT NULL,
  `Is_deleted` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `emergency`
--

INSERT INTO `emergency` (`PatientID`, `DocID`, `Date`, `Time`, `Is_deleted`) VALUES
(3, 12, '2021-05-23', '12:00:00', 0),
(6, 16, '2020-04-20', '12:00:00', 0),
(8, 14, '2020-03-19', '02:00:00', 0);

-- --------------------------------------------------------

--
-- Table structure for table `medequipment`
--

CREATE TABLE `medequipment` (
  `EquipID` int(11) NOT NULL,
  `Name` text NOT NULL,
  `Stock` int(11) NOT NULL,
  `Is_deleted` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `medequipment`
--

INSERT INTO `medequipment` (`EquipID`, `Name`, `Stock`, `Is_deleted`) VALUES
(1, 'Scissors', 5, 0),
(2, 'Microphore Tape', 20, 0),
(3, 'Dialyzer', 50, 0);

-- --------------------------------------------------------

--
-- Table structure for table `medicine`
--

CREATE TABLE `medicine` (
  `MedID` int(11) NOT NULL,
  `BrandName` text NOT NULL,
  `GenericName` text NOT NULL,
  `Manufecturer` text NOT NULL,
  `Literature` text NOT NULL,
  `Stock` int(11) NOT NULL,
  `Is_deleted` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `medicine`
--

INSERT INTO `medicine` (`MedID`, `BrandName`, `GenericName`, `Manufecturer`, `Literature`, `Stock`, `Is_deleted`) VALUES
(1, 'Nidocard', 'Nitrocontin', 'Square', 'Helps liquify blood', 50, 0),
(2, 'Salbutal', 'Salbutamol', 'Square', 'XTZ', 30, 0),
(3, 'Flexi', 'Aceclofenac', 'Square', 'NSAIDS and Antigout Prep', 20, 0),
(4, 'Tylace', 'Acetycysteine USP', 'Square', 'Cough and Cold Preparation', 20, 0),
(5, 'Virux Tablet', 'Aciclovir', 'Square', 'Topical Preparations', 10, 0),
(6, 'Almex', 'Albendazole', 'Beximco', 'AlbendazoleAntiparasite Preparations', 50, 0),
(7, 'Moxacil', 'Amoxicillin', 'Square', '112', 10, 0),
(8, 'Carva', 'Aspirin', 'Square', 'Cardiovascular Preparations', 20, 0),
(9, 'Zimax', 'Azithromycin', 'Beximco', 'Antibacterial', 30, 0),
(10, 'Entacyd Plus', 'Aluminum Hydroxide + Magnesium Hydroxide + Simethicone', 'Square', 'Alimentary Preparation', 70, 0),
(11, 'Ace', 'Paracetamol', 'Square', 'Fever Treatment', 30, 0),
(12, 'Anril', 'Nitroglycerin', 'Square', 'Hypertension treatment', 20, 0);

-- --------------------------------------------------------

--
-- Table structure for table `outdoor`
--

CREATE TABLE `outdoor` (
  `PatientID` int(11) NOT NULL,
  `DocID` int(11) NOT NULL,
  `Date` date NOT NULL,
  `Time` time NOT NULL,
  `Is_deleted` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `outdoor`
--

INSERT INTO `outdoor` (`PatientID`, `DocID`, `Date`, `Time`, `Is_deleted`) VALUES
(5, 16, '2020-01-10', '12:00:00', 0),
(5, 12, '2021-02-20', '05:00:00', 0);

-- --------------------------------------------------------

--
-- Table structure for table `patientmanagement`
--

CREATE TABLE `patientmanagement` (
  `PatientID` int(11) NOT NULL,
  `Name` text NOT NULL,
  `Sex` varchar(1) NOT NULL,
  `Age` int(11) NOT NULL,
  `Bloodgroup` varchar(2) NOT NULL,
  `MedicalHistory` text NOT NULL,
  `Address` text NOT NULL,
  `Contactno` text NOT NULL,
  `Email` text NOT NULL,
  `is_deleted` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patientmanagement`
--

INSERT INTO `patientmanagement` (`PatientID`, `Name`, `Sex`, `Age`, `Bloodgroup`, `MedicalHistory`, `Address`, `Contactno`, `Email`, `is_deleted`) VALUES
(1, 'Jahanara Imam', 'F', 60, 'B+', 'Diabetes, Heart Attack', '10-D2 Station Road, Dhaka', '01536948625', 'jimam@gmail.com', 0),
(2, 'Rizvi Jowardar', 'M', 25, 'A+', 'Lung Cancer, High Blood Pressure', '255/A Station Road, Jamalpur', '01569845115', 'rio@gmail.com', 0),
(3, 'Rokeya Khatun', 'F', 50, 'C+', 'No prior sickness', '12/4, Gajnabi Road, Mohammadpur', '012365879412', 'rok@gmail.com', 0),
(4, 'Raiyaan Abdullah', 'M', 20, 'B+', 'Hypertension, Diabetes takes Cildip twice a day', '10-20/ Station road, Dhaka', '016658816998', 'raiyaan@gmail.com', 0),
(5, 'Saidul Khan', 'M', 26, 'A+', 'Diabetes', '12/22 Rampura, Dhaka', '01569782441', 'sadik@gmail.com', 0),
(6, 'Bushra Khatun', 'F', 25, 'A-', 'Arithmia', '20/Gajnabiroad, Dhaka', '019775632115', 'bushra@yahoo.com', 0),
(7, 'Mumshad Nahiyan', 'M', 22, 'B+', 'Hypertension takes no medications', '122-2 College gate, Dhaka', '015523689442', 'mum@gmail.com', 0),
(8, 'Rita Khatun', 'F', 50, 'A+', 'Lung cancer', '23/Mirpur 2 Dhaka', '01816482369', 'riat@gmail.com', 0),
(9, 'Hena Rahman', 'F', 35, 'B-', 'Diabetes', '12,53/A, Railroad, Dhaka', '01851369478', 'hena@gmail.com', 0);

-- --------------------------------------------------------

--
-- Table structure for table `prescription`
--

CREATE TABLE `prescription` (
  `PresID` int(11) NOT NULL,
  `PatientID` int(11) NOT NULL,
  `DocID` int(11) NOT NULL,
  `Diagnosis` text NOT NULL,
  `MedID` int(11) DEFAULT NULL,
  `TestID` int(11) DEFAULT NULL,
  `Date` date NOT NULL,
  `Time` time NOT NULL,
  `Is_deleted` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `prescription`
--

INSERT INTO `prescription` (`PresID`, `PatientID`, `DocID`, `Diagnosis`, `MedID`, `TestID`, `Date`, `Time`, `Is_deleted`) VALUES
(5, 5, 12, 'Hypertension', 9, 6, '2020-04-20', '12:00:00', 0),
(6, 6, 18, 'Heart attack', 4, 3, '2020-04-20', '01:00:00', 0),
(7, 1, 15, 'Heart attack', 6, 2, '2020-04-23', '12:00:00', 0),
(8, 3, 15, 'Cold', 2, 3, '2020-04-23', '12:00:00', 0),
(9, 4, 12, 'Heart attack', 1, 6, '2020-03-20', '12:00:00', 0),
(10, 7, 17, 'Diabetes', 5, 9, '2020-05-06', '02:00:00', 0),
(11, 8, 19, 'Diabetes', 6, 5, '2020-08-20', '12:00:00', 0);

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `RoomID` int(11) NOT NULL,
  `RoomType` text NOT NULL,
  `BedCount` int(11) NOT NULL,
  `Is_deleted` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`RoomID`, `RoomType`, `BedCount`, `Is_deleted`) VALUES
(1, 'Ward', 20, 0),
(2, 'Cabin', 2, 0),
(3, 'ICU', 10, 0),
(4, 'Ward', 10, 0),
(5, 'Ward', 20, 0),
(6, 'X-Ray', 1, 0),
(7, 'Pathology', 1, 0),
(8, 'Pathology', 1, 0),
(9, 'Pathology', 2, 0),
(10, 'CT Scan', 1, 0),
(11, 'MRI ', 5, 0),
(12, 'Ward', 20, 0),
(13, 'Ward', 30, 0),
(14, 'Ward', 50, 0),
(15, 'Ward', 10, 0),
(16, 'Cabin', 4, 0),
(17, 'Cabin', 4, 0),
(18, 'ICU', 20, 0),
(19, 'CCU', 30, 0),
(20, 'OT', 2, 0);

-- --------------------------------------------------------

--
-- Table structure for table `roomduty`
--

CREATE TABLE `roomduty` (
  `DutyID` int(11) NOT NULL,
  `DocID` int(11) DEFAULT NULL,
  `StaffID` int(11) DEFAULT NULL,
  `RoomID` int(11) NOT NULL,
  `Date` date NOT NULL,
  `Time` time NOT NULL,
  `Is_deleted` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roomduty`
--

INSERT INTO `roomduty` (`DutyID`, `DocID`, `StaffID`, `RoomID`, `Date`, `Time`, `Is_deleted`) VALUES
(7, NULL, 1, 5, '2007-01-10', '12:00:00', 0),
(10, 12, NULL, 13, '2020-04-20', '12:00:00', 0),
(11, 18, NULL, 14, '2021-04-20', '12:00:00', 0),
(12, 17, NULL, 14, '2021-04-10', '02:00:00', 0),
(13, 15, NULL, 14, '2021-03-23', '02:00:00', 0),
(14, NULL, 1, 13, '2020-04-20', '12:00:00', 0),
(15, NULL, 2, 14, '2020-01-23', '12:00:00', 0);

-- --------------------------------------------------------

--
-- Table structure for table `staffmanagement`
--

CREATE TABLE `staffmanagement` (
  `StaffID` int(11) NOT NULL,
  `Name` text NOT NULL,
  `Sex` varchar(1) NOT NULL,
  `Age` int(11) NOT NULL,
  `Position` text NOT NULL,
  `Contactno` text NOT NULL,
  `Email` text NOT NULL,
  `Salary` int(11) NOT NULL,
  `Is_deleted` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `staffmanagement`
--

INSERT INTO `staffmanagement` (`StaffID`, `Name`, `Sex`, `Age`, `Position`, `Contactno`, `Email`, `Salary`, `Is_deleted`) VALUES
(1, 'Bakhtier Rahman', 'M', 20, 'Boy', '01569874669', 'r.anwar@gmail.com', 2400, 0),
(2, 'Jalal Uddin', 'M', 20, 'Gaurd', '01756987556', 'rahim@yahoo.com', 2500, 0),
(3, 'Rabeya Kahtun', 'F', 20, 'Nurse', '01266981226', 'rab@gmail.com', 1200, 0),
(4, 'Mohinuddin Rahim', 'M', 20, 'Nurse', '01915632582', 'Rahm@gmail.com', 1200, 0),
(5, 'Rifat Rajib', 'M', 30, 'Registry', '01698721365', 'Raf@gmail.com', 1200, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admission`
--
ALTER TABLE `admission`
  ADD KEY `doc-ad` (`DocID`),
  ADD KEY `room-ad` (`RoomID`),
  ADD KEY `pat-ad` (`PatientID`);

--
-- Indexes for table `diagnosticreport`
--
ALTER TABLE `diagnosticreport`
  ADD KEY `doc-rep` (`DocID`),
  ADD KEY `pres-rep` (`PresID`);

--
-- Indexes for table `diagnostictests`
--
ALTER TABLE `diagnostictests`
  ADD PRIMARY KEY (`TestID`),
  ADD KEY `room-test` (`RoomID`);

--
-- Indexes for table `doctorsmanagement`
--
ALTER TABLE `doctorsmanagement`
  ADD PRIMARY KEY (`DocID`);

--
-- Indexes for table `emergency`
--
ALTER TABLE `emergency`
  ADD KEY `doc-em` (`DocID`),
  ADD KEY `pat-em` (`PatientID`);

--
-- Indexes for table `medequipment`
--
ALTER TABLE `medequipment`
  ADD PRIMARY KEY (`EquipID`);

--
-- Indexes for table `medicine`
--
ALTER TABLE `medicine`
  ADD PRIMARY KEY (`MedID`);

--
-- Indexes for table `outdoor`
--
ALTER TABLE `outdoor`
  ADD KEY `doc-out` (`DocID`),
  ADD KEY `pat-out` (`PatientID`);

--
-- Indexes for table `patientmanagement`
--
ALTER TABLE `patientmanagement`
  ADD PRIMARY KEY (`PatientID`);

--
-- Indexes for table `prescription`
--
ALTER TABLE `prescription`
  ADD PRIMARY KEY (`PresID`),
  ADD KEY `doc-pres` (`DocID`),
  ADD KEY `med-pres` (`MedID`),
  ADD KEY `test-pres` (`TestID`),
  ADD KEY `pat-pres` (`PatientID`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`RoomID`);

--
-- Indexes for table `roomduty`
--
ALTER TABLE `roomduty`
  ADD PRIMARY KEY (`DutyID`),
  ADD KEY `doc-duty` (`DocID`),
  ADD KEY `staff-duty` (`StaffID`),
  ADD KEY `room-duty` (`RoomID`);

--
-- Indexes for table `staffmanagement`
--
ALTER TABLE `staffmanagement`
  ADD PRIMARY KEY (`StaffID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `diagnostictests`
--
ALTER TABLE `diagnostictests`
  MODIFY `TestID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `doctorsmanagement`
--
ALTER TABLE `doctorsmanagement`
  MODIFY `DocID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `medequipment`
--
ALTER TABLE `medequipment`
  MODIFY `EquipID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `medicine`
--
ALTER TABLE `medicine`
  MODIFY `MedID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `patientmanagement`
--
ALTER TABLE `patientmanagement`
  MODIFY `PatientID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `prescription`
--
ALTER TABLE `prescription`
  MODIFY `PresID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `room`
--
ALTER TABLE `room`
  MODIFY `RoomID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `roomduty`
--
ALTER TABLE `roomduty`
  MODIFY `DutyID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `staffmanagement`
--
ALTER TABLE `staffmanagement`
  MODIFY `StaffID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admission`
--
ALTER TABLE `admission`
  ADD CONSTRAINT `doc-ad` FOREIGN KEY (`DocID`) REFERENCES `doctorsmanagement` (`DocID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `pat-ad` FOREIGN KEY (`PatientID`) REFERENCES `patientmanagement` (`PatientID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `room-ad` FOREIGN KEY (`RoomID`) REFERENCES `room` (`RoomID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `diagnosticreport`
--
ALTER TABLE `diagnosticreport`
  ADD CONSTRAINT `doc-rep` FOREIGN KEY (`DocID`) REFERENCES `doctorsmanagement` (`DocID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `pres-rep` FOREIGN KEY (`PresID`) REFERENCES `prescription` (`PresID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `diagnostictests`
--
ALTER TABLE `diagnostictests`
  ADD CONSTRAINT `room-test` FOREIGN KEY (`RoomID`) REFERENCES `room` (`RoomID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `emergency`
--
ALTER TABLE `emergency`
  ADD CONSTRAINT `doc-em` FOREIGN KEY (`DocID`) REFERENCES `doctorsmanagement` (`DocID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `pat-em` FOREIGN KEY (`PatientID`) REFERENCES `patientmanagement` (`PatientID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `outdoor`
--
ALTER TABLE `outdoor`
  ADD CONSTRAINT `doc-out` FOREIGN KEY (`DocID`) REFERENCES `doctorsmanagement` (`DocID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `pat-out` FOREIGN KEY (`PatientID`) REFERENCES `patientmanagement` (`PatientID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `prescription`
--
ALTER TABLE `prescription`
  ADD CONSTRAINT `doc-pres` FOREIGN KEY (`DocID`) REFERENCES `doctorsmanagement` (`DocID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `med-pres` FOREIGN KEY (`MedID`) REFERENCES `medicine` (`MedID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `pat-pres` FOREIGN KEY (`PatientID`) REFERENCES `patientmanagement` (`PatientID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `test-pres` FOREIGN KEY (`TestID`) REFERENCES `diagnostictests` (`TestID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `roomduty`
--
ALTER TABLE `roomduty`
  ADD CONSTRAINT `doc-duty` FOREIGN KEY (`DocID`) REFERENCES `doctorsmanagement` (`DocID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `room-duty` FOREIGN KEY (`RoomID`) REFERENCES `room` (`RoomID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `staff-duty` FOREIGN KEY (`StaffID`) REFERENCES `staffmanagement` (`StaffID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
