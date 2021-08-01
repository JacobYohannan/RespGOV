-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 27, 2021 at 06:39 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `respgov`
--

-- --------------------------------------------------------

--
-- Table structure for table `complaint_reg`
--

CREATE TABLE `complaint_reg` (
  `comid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `did` int(11) NOT NULL,
  `district` varchar(20) NOT NULL,
  `complaint` varchar(50) NOT NULL,
  `cdate` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `complaint_reg`
--

INSERT INTO `complaint_reg` (`comid`, `cid`, `did`, `district`, `complaint`, `cdate`, `status`) VALUES
(1, 5, 4, 'Kottayam', 'Connection Problem', '2021-04-24', 'Forwarded'),
(2, 5, 1, 'Ernakulam', 'Connection Problem', '2021-04-24', 'Forwarded'),
(3, 5, 4, 'Ernakulam', 'Jacob Yohannan', '2021-04-24', 'Forwarded'),
(4, 5, 2, 'Ernakulam', 'Alwin Paul', '2021-04-24', 'Solved');

-- --------------------------------------------------------

--
-- Table structure for table `cust_reg`
--

CREATE TABLE `cust_reg` (
  `cid` int(11) NOT NULL,
  `cname` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `district` varchar(50) NOT NULL,
  `location` varchar(50) NOT NULL,
  `mobile` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `aadhar` varchar(50) NOT NULL,
  `ksebcno` varchar(50) NOT NULL,
  `waternum` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cust_reg`
--

INSERT INTO `cust_reg` (`cid`, `cname`, `address`, `district`, `location`, `mobile`, `email`, `aadhar`, `ksebcno`, `waternum`, `password`) VALUES
(1, 'Jithu', 'LCC', 'Ernakulam', 'Kochi', '9685741200', 'jithin@gmail.com', '778812330099', '232323', '787878', '123'),
(2, 'cera', 'clayhome', 'thrissur', 'mala', '8080808080', 'cera@gmail.com', '878787878787', '55555', '44444', 'cera@gmail.com'),
(3, 'carolin', '543', 'thrissur', 'kumbidy', '3333333333', 'carolin@gmail.com', '6768798787', '666666', '888888', 'carolin@123'),
(5, 'mm', 'Kandamchirayil', 'Ernakulam', 'Muvattupuzha', '08848983074', 'mm@gmail.com', '123456789123', '123334426737', '11233444', '123');

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `deid` int(11) NOT NULL,
  `dename` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`deid`, `dename`) VALUES
(1, 'KSEB'),
(2, 'Water'),
(3, 'irrigation'),
(4, 'KFONE');

-- --------------------------------------------------------

--
-- Table structure for table `dept_head`
--

CREATE TABLE `dept_head` (
  `deptid` int(11) NOT NULL,
  `dename` varchar(50) NOT NULL,
  `district` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `dept` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dept_head`
--

INSERT INTO `dept_head` (`deptid`, `dename`, `district`, `phone`, `email`, `password`, `dept`) VALUES
(1, 'Prashob', 'Ernakulam', '7418529630', 'prashob@gmail.com', '123', 1),
(2, 'Delna', 'ernakulam', '8086813432', 'delna@gmail.com', 'delna@123', 3),
(3, 'Jacob Yohannan', 'Ernakulam', '08848983074', 'j@gmail.com', '123', 4),
(5, 'dfgh', 'Ernakulam', '08848983074', 'd@gmail.com', '123', 2);

-- --------------------------------------------------------

--
-- Table structure for table `district`
--

CREATE TABLE `district` (
  `did` int(11) NOT NULL,
  `dname` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `district`
--

INSERT INTO `district` (`did`, `dname`) VALUES
(1, 'Trivandrum'),
(2, 'Kollam'),
(3, 'Pathanamthitta'),
(4, 'Alappuzha'),
(5, 'Kottayam'),
(6, 'Idukki'),
(7, 'Ernakulam'),
(8, 'Thrissur'),
(9, 'Palakkad'),
(10, 'Malappuram'),
(11, 'Kozhikkod'),
(12, 'Wayanadu'),
(13, 'Kannur'),
(14, 'Kasargode');

-- --------------------------------------------------------

--
-- Table structure for table `employee_reg`
--

CREATE TABLE `employee_reg` (
  `eid` int(11) NOT NULL,
  `ename` varchar(50) NOT NULL,
  `district` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `dept` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee_reg`
--

INSERT INTO `employee_reg` (`eid`, `ename`, `district`, `phone`, `email`, `password`, `dept`) VALUES
(1, 'Aneesh', 'Ernakulam', '9637412580', 'aneesh@gmail.com', '123', 1),
(2, 'emmanuel', 'ernakulam', '8080808080', 'e@gmail.com', 'e@123', 3),
(3, 'B', 'Ernakulam', '8848983074', 'b@gmail.com', '123', 4),
(5, 'aa', 'Ernakulam', '8848983074', 'aa@gmail.com', '123', 2);

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `fid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `feedback` varchar(50) NOT NULL,
  `fdate` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`fid`, `cid`, `feedback`, `fdate`) VALUES
(1, 1, 'Good website', '2020-01-23'),
(2, 4, 'Connection Problem', '2021-04-22'),
(3, 0, 'dfgh', '2021-04-22'),
(4, 0, 'Connection Problem', '2021-04-22'),
(5, 4, 'Jacob Yohannan', '2021-04-22');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `uname` varchar(50) NOT NULL,
  `pass` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL,
  `status` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`uname`, `pass`, `utype`, `status`) VALUES
('jithin@gmail.com', '123', 'Customer', '1'),
('admin@gmail.com', 'admin', 'Admin', '1'),
('aneesh@gmail.com', '123', 'Employee', '1'),
('prashob@gmail.com', '123', 'DeptHead', '1'),
('delna@gmail.com', 'delna@123', 'DeptHead', '1'),
('cera@gmail.com', 'cera@gmail.com', 'Customer', '1'),
('e@gmail.com', 'e@123', 'Employee', '1'),
('carolin@gmail.com', 'carolin@123', 'Customer', '1'),
('j@gmail.com', '123', 'DeptHead', '1'),
('a@gmail.com', '123', 'DeptHead', '1'),
('686671', '123', 'Customer', '1'),
('b@gmail.com', '123', 'Employee', '1'),
('mm@gmail.com', '123', 'Customer', '1'),
('ann@gmail.com', '123', 'Employee', '1'),
('d@gmail.com', '123', 'DeptHead', '1'),
('aa@gmail.com', '123', 'Employee', '1');

-- --------------------------------------------------------

--
-- Table structure for table `staff_allot`
--

CREATE TABLE `staff_allot` (
  `allot_id` int(11) NOT NULL,
  `compid` int(11) NOT NULL,
  `sid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `staff_allot`
--

INSERT INTO `staff_allot` (`allot_id`, `compid`, `sid`) VALUES
(3, 5, 1),
(4, 7, 2),
(5, 8, 3),
(6, 2, 1),
(7, 2, 1),
(8, 3, 3),
(9, 1, 0),
(10, 4, 5);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `complaint_reg`
--
ALTER TABLE `complaint_reg`
  ADD PRIMARY KEY (`comid`);

--
-- Indexes for table `cust_reg`
--
ALTER TABLE `cust_reg`
  ADD PRIMARY KEY (`cid`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`deid`);

--
-- Indexes for table `dept_head`
--
ALTER TABLE `dept_head`
  ADD PRIMARY KEY (`deptid`);

--
-- Indexes for table `district`
--
ALTER TABLE `district`
  ADD PRIMARY KEY (`did`);

--
-- Indexes for table `employee_reg`
--
ALTER TABLE `employee_reg`
  ADD PRIMARY KEY (`eid`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`fid`);

--
-- Indexes for table `staff_allot`
--
ALTER TABLE `staff_allot`
  ADD PRIMARY KEY (`allot_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `complaint_reg`
--
ALTER TABLE `complaint_reg`
  MODIFY `comid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `cust_reg`
--
ALTER TABLE `cust_reg`
  MODIFY `cid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `department`
--
ALTER TABLE `department`
  MODIFY `deid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `dept_head`
--
ALTER TABLE `dept_head`
  MODIFY `deptid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `district`
--
ALTER TABLE `district`
  MODIFY `did` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `employee_reg`
--
ALTER TABLE `employee_reg`
  MODIFY `eid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `fid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `staff_allot`
--
ALTER TABLE `staff_allot`
  MODIFY `allot_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
