-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mer. 12 juin 2024 à 20:53
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `hematodisk_data_base`
--

-- --------------------------------------------------------

--
-- Structure de la table `administrateur`
--

CREATE TABLE `administrateur` (
  `matricule_administrateur` int(11) NOT NULL,
  `mot_de_passe` varchar(50) NOT NULL,
  `confirmer_mot_passe` varchar(50) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `date_de_naissance` date NOT NULL,
  `telephone` varchar(50) NOT NULL,
  `wilaya` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `administrateur`
--

INSERT INTO `administrateur` (`matricule_administrateur`, `mot_de_passe`, `confirmer_mot_passe`, `nom`, `prenom`, `date_de_naissance`, `telephone`, `wilaya`) VALUES
(1000, '0000', '0000', 'laouer', 'nour', '2003-06-01', '06666666', '01 Adrar'),
(2000, '1111', '1111', 'afene', 'nourhan', '2004-04-24', '55555555', '31 Oran');

-- --------------------------------------------------------

--
-- Structure de la table `geste_medicale`
--

CREATE TABLE `geste_medicale` (
  `id_geste` int(11) NOT NULL,
  `geste` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `geste_medicale`
--

INSERT INTO `geste_medicale` (`id_geste`, `geste`) VALUES
(1, 'k'),
(2, 'bom');

-- --------------------------------------------------------

--
-- Structure de la table `historique_consultations`
--

CREATE TABLE `historique_consultations` (
  `id_consultation` int(11) NOT NULL,
  `date_de_consultation` date NOT NULL,
  `matricule_patient` int(50) NOT NULL,
  `geste_medical` text NOT NULL,
  `diagnostique` text NOT NULL,
  `matricule_medecin` int(50) NOT NULL,
  `patient` varchar(100) NOT NULL,
  `medecin` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `historique_consultations`
--

INSERT INTO `historique_consultations` (`id_consultation`, `date_de_consultation`, `matricule_patient`, `geste_medical`, `diagnostique`, `matricule_medecin`, `patient`, `medecin`) VALUES
(1, '2024-06-01', 2, 'Transfusion', 'bien\n', 3000, '', '');

-- --------------------------------------------------------

--
-- Structure de la table `medecin`
--

CREATE TABLE `medecin` (
  `matricule_medecin` int(11) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `wilaya` varchar(50) NOT NULL,
  `telephone` varchar(50) NOT NULL,
  `grade` varchar(100) NOT NULL,
  `date_de_naissance` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `medecin`
--

INSERT INTO `medecin` (`matricule_medecin`, `nom`, `prenom`, `wilaya`, `telephone`, `grade`, `date_de_naissance`) VALUES
(3000, 'gada', 'sarra', '31 Oran', '124587', 'Professeur', '2003-12-18'),
(4000, 'berrebih', 'kamilia', '31 Oran', '124598', 'Maître Assistant', '2003-06-22');

-- --------------------------------------------------------

--
-- Structure de la table `patient`
--

CREATE TABLE `patient` (
  `matricule_patient` int(11) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `date_de_naissance` date NOT NULL,
  `age` int(11) GENERATED ALWAYS AS (floor((to_days(current_timestamp()) - to_days(`date_de_naissance`)) / 365)) VIRTUAL,
  `sexe` varchar(10) NOT NULL,
  `wilaya` varchar(50) NOT NULL,
  `telephone` varchar(50) NOT NULL,
  `groupage` varchar(50) NOT NULL,
  `Antecedents` text NOT NULL,
  `création` date NOT NULL DEFAULT current_timestamp(),
  `FKmatricule_administrateur` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `patient`
--

INSERT INTO `patient` (`matricule_patient`, `nom`, `prenom`, `date_de_naissance`, `sexe`, `wilaya`, `telephone`, `groupage`, `Antecedents`, `création`, `FKmatricule_administrateur`) VALUES
(1, 'belal ', 'ikhlas', '2003-01-19', 'Femme', '02 Chlef', '0123654789', 'A+', '\n', '2024-06-01', 1000),
(2, 'boumediene', 'saleha aya', '2004-01-28', 'Femme', '31 Oran', '01236547', 'AB+', '\nanémie\n', '2024-06-01', 1000),
(3, 'khelif', 'faiza', '2003-05-28', 'Femme', '31 Oran', '01245879', 'O+', '\n', '2024-06-01', 1000),
(4, 'derouiche', 'hadjer', '2003-12-04', 'Femme', '31 Oran', '1256987', 'O+', '\n', '2024-06-01', 1000),
(5, 'dahim', 'douaa', '2003-11-11', 'Femme', '31 Oran', '125478', 'A-', 'anémie\n', '2024-06-01', 1000),
(6, 'laouer', 'nour', '2003-06-01', 'Femme', '01 Adrar', '125497', 'A-', '\n', '2024-06-01', 1000),
(7, 'bentouba', 'yassmine', '2003-08-27', 'Femme', '01 Adrar', '0552411020', 'O+', '\n', '2024-06-01', 1000),
(8, 'malki', 'khaoula', '2002-04-04', 'Femme', '31 Oran', '0774324569', 'A+', '\n', '2024-06-01', 1000),
(33, 'rtye', 'grt', '2003-02-23', 'Homme', '01 Adrar', '54654', 'A+', '\n', '2024-06-05', 1000),
(34, 'rtye', 'rtr', '2001-01-23', 'Homme', '01 Adrar', '43634', 'A+', '\n', '2024-06-05', 1000),
(40, 'malki', 'khaoula', '2000-02-23', 'Homme', '01 Adrar', '0569845', 'A+', '\n', '2024-06-06', 1000),
(657, 'gsbsfg', 'nsbfg', '2000-09-23', 'Homme', '01 Adrar', '67567', 'A+', '\n', '2024-06-05', 1000),
(677, 'sdf', 'fase', '2000-02-23', 'Homme', '16 Alger', '5465', 'A+', '\n', '2024-06-05', 1000);

-- --------------------------------------------------------

--
-- Structure de la table `rendez_vous`
--

CREATE TABLE `rendez_vous` (
  `id_rendez_vous` int(11) NOT NULL,
  `date_creation_du_rendez_vous` date NOT NULL,
  `date_du_rendez_vous` date NOT NULL,
  `patient` varchar(50) NOT NULL,
  `matricule_patient` int(11) NOT NULL,
  `geste_medical` varchar(50) NOT NULL,
  `medecin` varchar(50) NOT NULL,
  `matricule_medecin` int(11) NOT NULL,
  `validation` varchar(20) DEFAULT 'non valide'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `rendez_vous`
--

INSERT INTO `rendez_vous` (`id_rendez_vous`, `date_creation_du_rendez_vous`, `date_du_rendez_vous`, `patient`, `matricule_patient`, `geste_medical`, `medecin`, `matricule_medecin`, `validation`) VALUES
(1, '2024-06-01', '2024-06-02', 'belal ikhlas', 0, 'Contrôle', 'gada', 3000, 'Non validé'),
(2, '2024-06-01', '2024-06-02', 'boumediene saleha aya', 0, 'Transfusion', 'berrebih', 4000, 'Non validé'),
(3, '2024-06-01', '2024-06-02', 'khelif faiza', 0, 'Contrôle', 'gada', 3000, 'Non validé'),
(4, '2024-06-01', '2024-06-09', 'derouiche hadjer', 0, 'Contrôle', 'gada', 3000, 'Non validé'),
(5, '2024-06-01', '2024-06-15', 'dahim douaa', 0, 'Transfusion', 'berrebih', 4000, 'Non validé'),
(6, '2024-06-05', '2024-06-29', 'malki khawla', 0, 'Transfusion', 'gada', 3000, 'Non validé'),
(7, '2024-06-05', '2024-06-15', 'malki khawla', 33, 'Transfusion', 'gada', 3000, 'Non validé'),
(8, '2024-06-05', '2024-06-30', 'dzfge fdgzd', 33, 'Transfusion', 'gada', 3000, 'Non validé'),
(9, '2024-06-06', '2024-06-29', 'malki khaoula', 0, 'Transfusion', 'gada', 3000, 'Non validé'),
(10, '2024-06-06', '2024-06-30', 'malki khaoula', 0, 'Transfusion', 'gada', 3000, 'Non validé'),
(11, '2024-06-06', '2024-06-21', 'malki khaoula', 8, 'Transfusion', 'gada', 3000, 'Non validé'),
(12, '2024-06-06', '2024-06-23', 'malki khaoula', 40, 'Transfusion', 'gada', 3000, 'Non validé'),
(13, '2024-06-06', '2024-06-22', 'malki khaoula', 8, 'BOM', 'gada', 3000, 'Non validé');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `administrateur`
--
ALTER TABLE `administrateur`
  ADD PRIMARY KEY (`matricule_administrateur`);

--
-- Index pour la table `geste_medicale`
--
ALTER TABLE `geste_medicale`
  ADD PRIMARY KEY (`id_geste`);

--
-- Index pour la table `historique_consultations`
--
ALTER TABLE `historique_consultations`
  ADD PRIMARY KEY (`id_consultation`),
  ADD KEY `matricule_patient` (`matricule_patient`,`matricule_medecin`);

--
-- Index pour la table `medecin`
--
ALTER TABLE `medecin`
  ADD PRIMARY KEY (`matricule_medecin`);

--
-- Index pour la table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`matricule_patient`),
  ADD KEY `FKmatricule_administrateur` (`FKmatricule_administrateur`);

--
-- Index pour la table `rendez_vous`
--
ALTER TABLE `rendez_vous`
  ADD PRIMARY KEY (`id_rendez_vous`),
  ADD KEY `matricule_patient` (`matricule_patient`,`matricule_medecin`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `administrateur`
--
ALTER TABLE `administrateur`
  MODIFY `matricule_administrateur` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2001;

--
-- AUTO_INCREMENT pour la table `geste_medicale`
--
ALTER TABLE `geste_medicale`
  MODIFY `id_geste` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `historique_consultations`
--
ALTER TABLE `historique_consultations`
  MODIFY `id_consultation` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `medecin`
--
ALTER TABLE `medecin`
  MODIFY `matricule_medecin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4001;

--
-- AUTO_INCREMENT pour la table `rendez_vous`
--
ALTER TABLE `rendez_vous`
  MODIFY `id_rendez_vous` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
