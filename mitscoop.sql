-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 18, 2025 at 04:06 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mitscoop`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_users`
--

CREATE TABLE `admin_users` (
  `admin_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `age` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL,
  `contact_no` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_users`
--

INSERT INTO `admin_users` (`admin_id`, `name`, `age`, `gender`, `address`, `status`, `contact_no`, `username`, `password`) VALUES
(5, 'loyd Almonte', '4', 'Male', 'hghaghaghagh', 'Single', '0999999', 'Admin', 'cuteboy'),
(6, '6', '6', '6', '6', '6', '6', 'Admin', '6'),
(7, '6', '6', '6', '6', '6', '6', '6', '6'),
(8, 'nata', '78', 'Female', 'abong', 'Female', '09999', 'nTTTT', '6'),
(9, 'loyd', '34', 'male', 'koko', 'single', '1222', 'cuteboy', '123');

-- --------------------------------------------------------

--
-- Table structure for table `message_report`
--

CREATE TABLE `message_report` (
  `id` int(11) NOT NULL,
  `sender_id` varchar(255) NOT NULL,
  `message` mediumtext NOT NULL DEFAULT '"',
  `sender` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `message_report`
--

INSERT INTO `message_report` (`id`, `sender_id`, `message`, `sender`, `image`) VALUES
(28, '37', '2312', 'Alarcon', NULL),
(29, '37', '2312', 'Alarcon', NULL),
(30, '37', '3', 'Alarcon', NULL),
(31, '37', '32', 'Alarcon', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(100) NOT NULL,
  `name` varchar(255) NOT NULL,
  `age` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL,
  `contact_no` varchar(255) NOT NULL,
  `work_post` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `name`, `age`, `gender`, `address`, `status`, `contact_no`, `work_post`, `username`, `password`) VALUES
(37, 'Alarcon', '12', 'male', 'Abong', 'Male', '09565', 'employee', 'nanat', '123'),
(38, 'loyd', '21', 'male', 'oton', 'single', '09519716644', 'lawe', '1', '1'),
(39, 'loyd', '21', '1', '1', '1', '2', 'driver', '11', '22'),
(40, 'loyd', '2121', 'male', '22', 'single', '111', 'Admin', '2', '22'),
(41, 'loyd', '21', 'male', 'oton', 'single', '1', 'driver', '7', '1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_users`
--
ALTER TABLE `admin_users`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `message_report`
--
ALTER TABLE `message_report`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_users`
--
ALTER TABLE `admin_users`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `message_report`
--
ALTER TABLE `message_report`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
