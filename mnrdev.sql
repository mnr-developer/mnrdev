-- phpMyAdmin SQL Dump
-- version 4.9.5deb1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 01, 2020 at 01:37 AM
-- Server version: 8.0.19-0ubuntu0.19.10.3
-- PHP Version: 7.3.11-0ubuntu0.19.10.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mnrdev`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_caseStudy`
--

CREATE TABLE `tbl_caseStudy` (
  `id` int NOT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `link` varchar(255) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `date` timestamp NULL DEFAULT NULL,
  `uid` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_clientFeedback`
--

CREATE TABLE `tbl_clientFeedback` (
  `id` int NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `quote` varchar(255) DEFAULT NULL,
  `job` varchar(50) DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_contact`
--

CREATE TABLE `tbl_contact` (
  `id` int NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` bigint DEFAULT NULL,
  `message` varchar(255) DEFAULT NULL,
  `dated` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tbl_contact`
--

INSERT INTO `tbl_contact` (`id`, `name`, `email`, `phone`, `message`, `dated`) VALUES
(1, 'test', 'test@gmail.com', 1234567890, 'ajashf kdfhjkd dhfjkds hfjksd jkdjkfn sdjk jkdfjk sdjkfnjk jkdjkf dsjknf k jkdfksdnfk kjdkfndsk fkjhjkd fjkdsn kk sdjkfsdk fjkjk jsk.', '2020-04-22 19:57:41.779769');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_fact`
--

CREATE TABLE `tbl_fact` (
  `id` int NOT NULL,
  `funFact` varchar(255) DEFAULT NULL,
  `uid` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_links`
--

CREATE TABLE `tbl_links` (
  `id` int NOT NULL,
  `fb` varchar(50) DEFAULT NULL,
  `github` varchar(50) DEFAULT NULL,
  `linkinId` varchar(50) DEFAULT NULL,
  `outlook` varchar(50) DEFAULT NULL,
  `yahoo` varchar(50) DEFAULT NULL,
  `twitter` varchar(50) DEFAULT NULL,
  `website_1` varchar(50) DEFAULT NULL,
  `website_2` varchar(50) DEFAULT NULL,
  `uid` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_myWork`
--

CREATE TABLE `tbl_myWork` (
  `id` int NOT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `site_name` varchar(50) DEFAULT NULL,
  `site_description` varchar(255) DEFAULT NULL,
  `link` varchar(100) DEFAULT NULL,
  `dated` varchar(100) DEFAULT NULL,
  `uid` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_subscribers`
--

CREATE TABLE `tbl_subscribers` (
  `id` int NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `dated` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_user`
--

CREATE TABLE `tbl_user` (
  `id` int NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `pswd` varchar(50) DEFAULT NULL,
  `login_time` varchar(100) DEFAULT NULL,
  `site_title` varchar(50) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `about_p1` varchar(255) DEFAULT NULL,
  `about_p2` varchar(255) DEFAULT NULL,
  `contact_no` bigint DEFAULT NULL,
  `updated_date` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tbl_user`
--

INSERT INTO `tbl_user` (`id`, `name`, `email`, `pswd`, `login_time`, `site_title`, `description`, `address`, `photo`, `about_p1`, `about_p2`, `contact_no`, `updated_date`) VALUES
(1, NULL, 'admin@admin.com', 'admin', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_whatido`
--

CREATE TABLE `tbl_whatido` (
  `id` int NOT NULL,
  `title` varchar(50) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `uid` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_caseStudy`
--
ALTER TABLE `tbl_caseStudy`
  ADD PRIMARY KEY (`id`),
  ADD KEY `uid` (`uid`);

--
-- Indexes for table `tbl_clientFeedback`
--
ALTER TABLE `tbl_clientFeedback`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_contact`
--
ALTER TABLE `tbl_contact`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `tbl_fact`
--
ALTER TABLE `tbl_fact`
  ADD PRIMARY KEY (`id`),
  ADD KEY `uid` (`uid`);

--
-- Indexes for table `tbl_links`
--
ALTER TABLE `tbl_links`
  ADD PRIMARY KEY (`id`),
  ADD KEY `uid` (`uid`);

--
-- Indexes for table `tbl_myWork`
--
ALTER TABLE `tbl_myWork`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `site_name` (`site_name`),
  ADD UNIQUE KEY `link` (`link`),
  ADD KEY `uid` (`uid`);

--
-- Indexes for table `tbl_subscribers`
--
ALTER TABLE `tbl_subscribers`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `tbl_user`
--
ALTER TABLE `tbl_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `tbl_whatido`
--
ALTER TABLE `tbl_whatido`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`),
  ADD KEY `uid` (`uid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_caseStudy`
--
ALTER TABLE `tbl_caseStudy`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_clientFeedback`
--
ALTER TABLE `tbl_clientFeedback`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_contact`
--
ALTER TABLE `tbl_contact`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_fact`
--
ALTER TABLE `tbl_fact`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_links`
--
ALTER TABLE `tbl_links`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_myWork`
--
ALTER TABLE `tbl_myWork`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_subscribers`
--
ALTER TABLE `tbl_subscribers`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tbl_user`
--
ALTER TABLE `tbl_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tbl_whatido`
--
ALTER TABLE `tbl_whatido`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tbl_caseStudy`
--
ALTER TABLE `tbl_caseStudy`
  ADD CONSTRAINT `tbl_caseStudy_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `tbl_user` (`id`);

--
-- Constraints for table `tbl_fact`
--
ALTER TABLE `tbl_fact`
  ADD CONSTRAINT `tbl_fact_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `tbl_user` (`id`);

--
-- Constraints for table `tbl_links`
--
ALTER TABLE `tbl_links`
  ADD CONSTRAINT `tbl_links_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `tbl_user` (`id`);

--
-- Constraints for table `tbl_myWork`
--
ALTER TABLE `tbl_myWork`
  ADD CONSTRAINT `tbl_myWork_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `tbl_user` (`id`);

--
-- Constraints for table `tbl_whatido`
--
ALTER TABLE `tbl_whatido`
  ADD CONSTRAINT `tbl_whatido_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `tbl_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
