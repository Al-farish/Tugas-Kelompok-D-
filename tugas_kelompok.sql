-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Waktu pembuatan: 13 Jun 2024 pada 03.22
-- Versi server: 10.4.28-MariaDB
-- Versi PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tugas_kelompok`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `anggota_kelompok`
--

CREATE TABLE `anggota_kelompok` (
  `nim` varchar(17) NOT NULL,
  `nama_mahasiswa` varchar(30) DEFAULT NULL,
  `alamat` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `anggota_kelompok`
--

INSERT INTO `anggota_kelompok` (`nim`, `nama_mahasiswa`, `alamat`) VALUES
('I.2210221', 'Sanifa Lihawa', 'Sukabumi'),
('I.2210320', 'Muhammad Fauzan Arkan', 'Tanggerang'),
('I.2210378', 'Ananda Alfiah', 'Sukabumi'),
('I.2211106', 'M Zidan Al-farish', 'Bogor'),
('I.2211108', 'Zidan Baru', 'Bogor baru'),
('I.2211186', 'M Juroihan', 'Ciawi');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `anggota_kelompok`
--
ALTER TABLE `anggota_kelompok`
  ADD PRIMARY KEY (`nim`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
