CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `color` varchar(50) DEFAULT NULL,
  `type_category` varchar(1) DEFAULT NULL,
  `code` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `category_object` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) DEFAULT 0,
  `project_id` int(11) DEFAULT 0,
  `contact_id` int(11) DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `contact` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `name` varchar(150) DEFAULT NULL,
  `firstname` varchar(50) DEFAULT NULL,
  `nickname` varchar(50) DEFAULT NULL,
  `address` text DEFAULT NULL,
  `zip_code` varchar(5) DEFAULT NULL,
  `town` varchar(50) DEFAULT NULL,
  `address_work` text DEFAULT NULL,
  `zip_code_work` varchar(50) DEFAULT NULL,
  `town_work` varchar(50) DEFAULT NULL,
  `code_building` varchar(50) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `company` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `email_work` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `phone_work` varchar(50) DEFAULT NULL,
  `phone_cel` varchar(50) DEFAULT NULL,
  `phone_cel_work` varchar(50) DEFAULT NULL,
  `phone_fax_work` varchar(50) DEFAULT NULL,
  `date_birth` datetime DEFAULT NULL,
  `date_nameday` datetime DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `service` varchar(50) DEFAULT NULL,
  `responsable` text DEFAULT NULL,
  `associate` text DEFAULT NULL,
  `comment` text DEFAULT NULL,
  `site_web` varchar(250) DEFAULT NULL,
  `site_web_work` varchar(50) DEFAULT NULL,
  `schedules_work` varchar(50) DEFAULT NULL,
  `date_delete` datetime DEFAULT NULL,
  `is_visua` int(1) DEFAULT NULL,
  `is_synch` int(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- crvomain.contacts_project definition

CREATE TABLE `contact_project` (
  `project_id` int(11) DEFAULT NULL,
  `contact_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- crvomain.decisional definition

CREATE TABLE `decisional` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `type_decisional` varchar(255) DEFAULT NULL,
  `scoring` int(11) DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  `solution` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- crvomain.etiquettes definition

CREATE TABLE `sticker` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `contain` text DEFAULT NULL,
  `color_back` varchar(255) DEFAULT NULL,
  `date_delete` datetime DEFAULT NULL,
  `color_write` varchar(255) DEFAULT NULL,
  `font` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- crvomain.fleches definition

CREATE TABLE `arrow` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `visuas_org_id` int(11) DEFAULT NULL,
  `visuas_dest_id` int(11) DEFAULT NULL,
  `color` varchar(255) DEFAULT NULL,
  `size` int(11) DEFAULT NULL,
  `y_org` int(11) DEFAULT NULL,
  `y_dest` int(11) DEFAULT NULL,
  `x_org` int(11) DEFAULT NULL,
  `x_dest` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- crvomain.images definition

CREATE TABLE `picture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `filename` text DEFAULT NULL,
  `color_back` varchar(255) DEFAULT NULL,
  `date_delete` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- crvomain.liens definition

CREATE TABLE `link` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `path` varchar(255) DEFAULT NULL,
  `is_ged` int(1) DEFAULT NULL,
  `date_delete` datetime DEFAULT NULL,
  `is_visua` int(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- crvomain.notes definition

CREATE TABLE `note` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `contain` text DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  `date_delete` datetime DEFAULT NULL,
  `is_visua` int(1) DEFAULT NULL,
  `color_fd` varchar(255) DEFAULT NULL,
  `type_note` varchar(255) DEFAULT NULL,
  `is_rich` int(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- crvomain.objectifs definition

CREATE TABLE `goal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `abscon` text DEFAULT NULL,
  `formulation` text DEFAULT NULL,
  `measurable` text DEFAULT NULL,
  `resource` text DEFAULT NULL,
  `ecological` text DEFAULT NULL,
  `circumstantial` text DEFAULT NULL,
  `realistic` text DEFAULT NULL,
  `exciting` text DEFAULT NULL,
  `reward` text DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- crvomain.params definition

CREATE TABLE `params` (
  `node` varchar(255) DEFAULT NULL,
  `key` varchar(255) DEFAULT NULL,
  `second_key` varchar(255) DEFAULT NULL,
  `value` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- crvomain.project definition

CREATE TABLE `project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_projet` varchar(1) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `date_creation` datetime DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  `lieu` varchar(100) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `town` varchar(50) DEFAULT NULL,
  `zip_code` varchar(5) DEFAULT NULL,
  `color` varchar(255) DEFAULT NULL,
  `price_projected` float(16,2) DEFAULT NULL,
  `priority` int(11) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `date_delete` datetime DEFAULT NULL,
  `is_done` int(1) DEFAULT NULL,
  `font` varchar(50) DEFAULT NULL,
  `color_visua` varchar(255) DEFAULT NULL,
  `date_end` datetime DEFAULT NULL,
  `date_begin` datetime DEFAULT NULL,
  `price` float(14,2) DEFAULT NULL,
  `note` int(11) DEFAULT NULL,
  `time` varchar(8) DEFAULT NULL,
  `counter` int(11) DEFAULT NULL,
  `date_done` datetime DEFAULT NULL,
  `is_visua` int(1) DEFAULT NULL,
  `is_synch` int(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- crvomain.rappels definition

CREATE TABLE `reminder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reminder` int(11) DEFAULT NULL,
  `unity_reminder` varchar(10) DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- crvomain.types_categories definition

CREATE TABLE `type_category` (
  `type_category` varchar(3) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- crvomain.types_project definition

CREATE TABLE `type_project` (
  `type_project` varchar(2) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- crvomain.visuas definition

CREATE TABLE `visuas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `position_x` int(11) DEFAULT NULL,
  `position_y` int(11) DEFAULT NULL,
  `height` int(11) DEFAULT NULL,
  `width` int(11) DEFAULT NULL,
  `date_delete` datetime DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  `note_id` int(11) DEFAULT NULL,
  `link_id` int(11) DEFAULT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `sticker_id` int(11) DEFAULT NULL,
  `picture_id` int(11) DEFAULT NULL,
  `action_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;