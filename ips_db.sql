-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 15-07-2025 a las 14:36:46
-- Versión del servidor: 8.0.30
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ips_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `agenda`
--

CREATE TABLE `agenda` (
  `id` bigint NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date DEFAULT NULL,
  `hora_inicio` time(6) NOT NULL,
  `hora_fin` time(6) NOT NULL,
  `horas_por_dia` smallint UNSIGNED NOT NULL,
  `medico_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `agenda`
--

INSERT INTO `agenda` (`id`, `fecha_inicio`, `fecha_fin`, `hora_inicio`, `hora_fin`, `horas_por_dia`, `medico_id`) VALUES
(1, '2025-07-07', '2025-07-12', '12:00:00.000000', '18:00:00.000000', 6, 2),
(2, '2025-07-14', '2025-07-19', '12:00:00.000000', '18:00:00.000000', 5, 2),
(3, '2025-07-28', '2025-08-02', '12:00:00.000000', '18:00:00.000000', 6, 2),
(4, '2025-11-03', '2025-11-08', '06:00:00.000000', '12:00:00.000000', 2, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add usuario', 6, 'add_usuario'),
(22, 'Can change usuario', 6, 'change_usuario'),
(23, 'Can delete usuario', 6, 'delete_usuario'),
(24, 'Can view usuario', 6, 'view_usuario'),
(25, 'Can add Agenda semanal', 7, 'add_agenda'),
(26, 'Can change Agenda semanal', 7, 'change_agenda'),
(27, 'Can delete Agenda semanal', 7, 'delete_agenda'),
(28, 'Can view Agenda semanal', 7, 'view_agenda'),
(29, 'Can add ciudad', 8, 'add_ciudad'),
(30, 'Can change ciudad', 8, 'change_ciudad'),
(31, 'Can delete ciudad', 8, 'delete_ciudad'),
(32, 'Can view ciudad', 8, 'view_ciudad'),
(33, 'Can add departamento', 9, 'add_departamento'),
(34, 'Can change departamento', 9, 'change_departamento'),
(35, 'Can delete departamento', 9, 'delete_departamento'),
(36, 'Can view departamento', 9, 'view_departamento'),
(37, 'Can add especialidad', 10, 'add_especialidad'),
(38, 'Can change especialidad', 10, 'change_especialidad'),
(39, 'Can delete especialidad', 10, 'delete_especialidad'),
(40, 'Can view especialidad', 10, 'view_especialidad'),
(41, 'Can add estado cita', 11, 'add_estadocita'),
(42, 'Can change estado cita', 11, 'change_estadocita'),
(43, 'Can delete estado cita', 11, 'delete_estadocita'),
(44, 'Can view estado cita', 11, 'view_estadocita'),
(45, 'Can add aux admin', 12, 'add_auxadmin'),
(46, 'Can change aux admin', 12, 'change_auxadmin'),
(47, 'Can delete aux admin', 12, 'delete_auxadmin'),
(48, 'Can view aux admin', 12, 'view_auxadmin'),
(49, 'Can add paciente', 13, 'add_paciente'),
(50, 'Can change paciente', 13, 'change_paciente'),
(51, 'Can delete paciente', 13, 'delete_paciente'),
(52, 'Can view paciente', 13, 'view_paciente'),
(53, 'Can add lugar atencion', 14, 'add_lugaratencion'),
(54, 'Can change lugar atencion', 14, 'change_lugaratencion'),
(55, 'Can delete lugar atencion', 14, 'delete_lugaratencion'),
(56, 'Can view lugar atencion', 14, 'view_lugaratencion'),
(57, 'Can add slot cita', 15, 'add_slotcita'),
(58, 'Can change slot cita', 15, 'change_slotcita'),
(59, 'Can delete slot cita', 15, 'delete_slotcita'),
(60, 'Can view slot cita', 15, 'view_slotcita'),
(61, 'Can add medico', 16, 'add_medico'),
(62, 'Can change medico', 16, 'change_medico'),
(63, 'Can delete medico', 16, 'delete_medico'),
(64, 'Can view medico', 16, 'view_medico'),
(65, 'Can add cita', 17, 'add_cita'),
(66, 'Can change cita', 17, 'change_cita'),
(67, 'Can delete cita', 17, 'delete_cita'),
(68, 'Can view cita', 17, 'view_cita');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `aux_admin`
--

CREATE TABLE `aux_admin` (
  `usuario_ptr_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `aux_admin`
--

INSERT INTO `aux_admin` (`usuario_ptr_id`) VALUES
(1),
(4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cita`
--

CREATE TABLE `cita` (
  `id` bigint NOT NULL,
  `fecha` date NOT NULL,
  `hora` time(6) NOT NULL,
  `estado` varchar(10) NOT NULL,
  `lugar_atencion_id` bigint DEFAULT NULL,
  `medico_id` bigint NOT NULL,
  `paciente_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `cita`
--

INSERT INTO `cita` (`id`, `fecha`, `hora`, `estado`, `lugar_atencion_id`, `medico_id`, `paciente_id`) VALUES
(1, '2025-07-08', '12:00:00.000000', 'PENDIENTE', NULL, 2, 1),
(2, '2025-07-11', '12:20:00.000000', 'PENDIENTE', NULL, 2, 3),
(3, '2025-07-12', '13:00:00.000000', 'PENDIENTE', NULL, 2, 3),
(4, '2025-11-08', '07:00:00.000000', 'PENDIENTE', NULL, 2, 1),
(5, '2025-07-09', '12:00:00.000000', 'PENDIENTE', 1, 2, 1),
(6, '2025-07-10', '12:00:00.000000', 'PENDIENTE', 1, 2, 1),
(7, '2025-07-15', '12:00:00.000000', 'PENDIENTE', 1, 2, 1),
(8, '2025-07-31', '12:20:00.000000', 'PENDIENTE', 1, 2, 1),
(9, '2025-07-16', '13:20:00.000000', 'PENDIENTE', 1, 2, 1),
(10, '2025-07-09', '12:20:00.000000', 'CANCELADA', 1, 2, 3),
(11, '2025-07-30', '12:00:00.000000', 'CANCELADA', 1, 2, 3),
(12, '2025-07-31', '12:00:00.000000', 'CANCELADA', 1, 2, 3),
(13, '2025-07-28', '12:00:00.000000', 'PENDIENTE', 1, 2, 3),
(14, '2025-07-30', '12:20:00.000000', 'PENDIENTE', 1, 2, 5),
(15, '2025-08-01', '12:00:00.000000', 'CANCELADA', 1, 2, 3),
(16, '2025-08-01', '12:20:00.000000', 'PENDIENTE', 1, 2, 5),
(17, '2025-08-02', '12:00:00.000000', 'PENDIENTE', 1, 2, 3),
(18, '2025-08-02', '12:20:00.000000', 'PENDIENTE', 1, 2, 5),
(19, '2025-07-10', '13:00:00.000000', 'PENDIENTE', 1, 2, 3),
(20, '2025-07-08', '12:20:00.000000', 'PENDIENTE', 1, 2, 5),
(21, '2025-07-29', '12:20:00.000000', 'PENDIENTE', 1, 2, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ciudad`
--

CREATE TABLE `ciudad` (
  `codigo_municipio` varchar(10) NOT NULL,
  `nombre_ciudad` varchar(255) NOT NULL,
  `codigo_departamento_id` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `ciudad`
--

INSERT INTO `ciudad` (`codigo_municipio`, `nombre_ciudad`, `codigo_departamento_id`) VALUES
('05001', 'MEDELLÍN', '05'),
('05002', 'ABEJORRAL', '05'),
('05004', 'ABRIAQUÍ', '05'),
('05021', 'ALEJANDRÍA', '05'),
('05030', 'AMAGÁ', '05'),
('05031', 'AMALFI', '05'),
('05034', 'ANDES', '05'),
('05036', 'ANGELÓPOLIS', '05'),
('05038', 'ANGOSTURA', '05'),
('05040', 'ANORÍ', '05'),
('05042', 'SANTA FÉ DE ANTIOQUIA', '05'),
('05044', 'ANZÁ', '05'),
('05045', 'APARTADÓ', '05'),
('05051', 'ARBOLETES', '05'),
('05055', 'ARGELIA', '05'),
('05059', 'ARMENIA', '05'),
('05079', 'BARBOSA', '05'),
('05086', 'BELMIRA', '05'),
('05088', 'BELLO', '05'),
('05091', 'BETANIA', '05'),
('05093', 'BETULIA', '05'),
('05101', 'CIUDAD BOLÍVAR', '05'),
('05107', 'BRICEÑO', '05'),
('05113', 'BURITICÁ', '05'),
('05120', 'CÁCERES', '05'),
('05125', 'CAICEDO', '05'),
('05129', 'CALDAS', '05'),
('05134', 'CAMPAMENTO', '05'),
('05138', 'CAÑASGORDAS', '05'),
('05142', 'CARACOLÍ', '05'),
('05145', 'CARAMANTA', '05'),
('05147', 'CAREPA', '05'),
('05148', 'EL CARMEN DE VIBORAL', '05'),
('05150', 'CAROLINA', '05'),
('05154', 'CAUCASIA', '05'),
('05172', 'CHIGORODÓ', '05'),
('05190', 'CISNEROS', '05'),
('05197', 'COCORNÁ', '05'),
('05206', 'CONCEPCIÓN', '05'),
('05209', 'CONCORDIA', '05'),
('05212', 'COPACABANA', '05'),
('05234', 'DABEIBA', '05'),
('05237', 'DONMATÍAS', '05'),
('05240', 'EBÉJICO', '05'),
('05250', 'EL BAGRE', '05'),
('05264', 'ENTRERRÍOS', '05'),
('05266', 'ENVIGADO', '05'),
('05282', 'FREDONIA', '05'),
('05284', 'FRONTINO', '05'),
('05306', 'GIRALDO', '05'),
('05308', 'GIRARDOTA', '05'),
('05310', 'GÓMEZ PLATA', '05'),
('05313', 'GRANADA', '05'),
('05315', 'GUADALUPE', '05'),
('05318', 'GUARNE', '05'),
('05321', 'GUATAPÉ', '05'),
('05347', 'HELICONIA', '05'),
('05353', 'HISPANIA', '05'),
('05360', 'ITAGÜÍ', '05'),
('05361', 'ITUANGO', '05'),
('05364', 'JARDÍN', '05'),
('05368', 'JERICÓ', '05'),
('05376', 'LA CEJA', '05'),
('05380', 'LA ESTRELLA', '05'),
('05390', 'LA PINTADA', '05'),
('05400', 'LA UNIÓN', '05'),
('05411', 'LIBORINA', '05'),
('05425', 'MACEO', '05'),
('05440', 'MARINILLA', '05'),
('05467', 'MONTEBELLO', '05'),
('05475', 'MURINDÓ', '05'),
('05480', 'MUTATÁ', '05'),
('05483', 'NARIÑO', '05'),
('05490', 'NECOCLÍ', '05'),
('05495', 'NECHÍ', '05'),
('05501', 'OLAYA', '05'),
('05541', 'PEÑOL', '05'),
('05543', 'PEQUE', '05'),
('05576', 'PUEBLORRICO', '05'),
('05579', 'PUERTO BERRÍO', '05'),
('05585', 'PUERTO NARE', '05'),
('05591', 'PUERTO TRIUNFO', '05'),
('05604', 'REMEDIOS', '05'),
('05607', 'RETIRO', '05'),
('05615', 'RIONEGRO', '05'),
('05628', 'SABANALARGA', '05'),
('05631', 'SABANETA', '05'),
('05642', 'SALGAR', '05'),
('05647', 'SAN ANDRÉS DE CUERQUÍA', '05'),
('05649', 'SAN CARLOS', '05'),
('05652', 'SAN FRANCISCO', '05'),
('05656', 'SAN JERÓNIMO', '05'),
('05658', 'SAN JOSÉ DE LA MONTAÑA', '05'),
('05659', 'SAN JUAN DE URABÁ', '05'),
('05660', 'SAN LUIS', '05'),
('05664', 'SAN PEDRO DE LOS MILAGROS', '05'),
('05665', 'SAN PEDRO DE URABÁ', '05'),
('05667', 'SAN RAFAEL', '05'),
('05670', 'SAN ROQUE', '05'),
('05674', 'SAN VICENTE FERRER', '05'),
('05679', 'SANTA BÁRBARA', '05'),
('05686', 'SANTA ROSA DE OSOS', '05'),
('05690', 'SANTO DOMINGO', '05'),
('05697', 'EL SANTUARIO', '05'),
('05736', 'SEGOVIA', '05'),
('05756', 'SONSÓN', '05'),
('05761', 'SOPETRÁN', '05'),
('05789', 'TÁMESIS', '05'),
('05790', 'TARAZÁ', '05'),
('05792', 'TARSO', '05'),
('05809', 'TITIRIBÍ', '05'),
('05819', 'TOLEDO', '05'),
('05837', 'TURBO', '05'),
('05842', 'URAMITA', '05'),
('05847', 'URRAO', '05'),
('05854', 'VALDIVIA', '05'),
('05856', 'VALPARAÍSO', '05'),
('05858', 'VEGACHÍ', '05'),
('05861', 'VENECIA', '05'),
('05873', 'VIGÍA DEL FUERTE', '05'),
('05885', 'YALÍ', '05'),
('05887', 'YARUMAL', '05'),
('05890', 'YOLOMBÓ', '05'),
('05893', 'YONDÓ', '05'),
('05895', 'ZARAGOZA', '05'),
('08001', 'BARRANQUILLA', '08'),
('08078', 'BARANOA', '08'),
('08137', 'CAMPO DE LA CRUZ', '08'),
('08141', 'CANDELARIA', '08'),
('08296', 'GALAPA', '08'),
('08372', 'JUAN DE ACOSTA', '08'),
('08421', 'LURUACO', '08'),
('08433', 'MALAMBO', '08'),
('08436', 'MANATÍ', '08'),
('08520', 'PALMAR DE VARELA', '08'),
('08549', 'PIOJÓ', '08'),
('08558', 'POLONUEVO', '08'),
('08560', 'PONEDERA', '08'),
('08573', 'PUERTO COLOMBIA', '08'),
('08606', 'REPELÓN', '08'),
('08634', 'SABANAGRANDE', '08'),
('08638', 'SABANALARGA', '08'),
('08675', 'SANTA LUCÍA', '08'),
('08685', 'SANTO TOMÁS', '08'),
('08758', 'SOLEDAD', '08'),
('08770', 'SUAN', '08'),
('08832', 'TUBARÁ', '08'),
('08849', 'USIACURÍ', '08'),
('11001', 'BOGOTÁ, D.C.', '11'),
('13001', 'CARTAGENA DE INDIAS', '13'),
('13006', 'ACHÍ', '13'),
('13030', 'ALTOS DEL ROSARIO', '13'),
('13042', 'ARENAL', '13'),
('13052', 'ARJONA', '13'),
('13062', 'ARROYOHONDO', '13'),
('13074', 'BARRANCO DE LOBA', '13'),
('13140', 'CALAMAR', '13'),
('13160', 'CANTAGALLO', '13'),
('13188', 'CICUCO', '13'),
('13212', 'CÓRDOBA', '13'),
('13222', 'CLEMENCIA', '13'),
('13244', 'EL CARMEN DE BOLÍVAR', '13'),
('13248', 'EL GUAMO', '13'),
('13268', 'EL PEÑÓN', '13'),
('13300', 'HATILLO DE LOBA', '13'),
('13430', 'MAGANGUÉ', '13'),
('13433', 'MAHATES', '13'),
('13440', 'MARGARITA', '13'),
('13442', 'MARÍA LA BAJA', '13'),
('13458', 'MONTECRISTO', '13'),
('13468', 'SANTA CRUZ DE MOMPOX', '13'),
('13473', 'MORALES', '13'),
('13490', 'NOROSÍ', '13'),
('13549', 'PINILLOS', '13'),
('13580', 'REGIDOR', '13'),
('13600', 'RÍO VIEJO', '13'),
('13620', 'SAN CRISTÓBAL', '13'),
('13647', 'SAN ESTANISLAO', '13'),
('13650', 'SAN FERNANDO', '13'),
('13654', 'SAN JACINTO', '13'),
('13655', 'SAN JACINTO DEL CAUCA', '13'),
('13657', 'SAN JUAN NEPOMUCENO', '13'),
('13667', 'SAN MARTÍN DE LOBA', '13'),
('13670', 'SAN PABLO', '13'),
('13673', 'SANTA CATALINA', '13'),
('13683', 'SANTA ROSA', '13'),
('13688', 'SANTA ROSA DEL SUR', '13'),
('13744', 'SIMITÍ', '13'),
('13760', 'SOPLAVIENTO', '13'),
('13780', 'TALAIGUA NUEVO', '13'),
('13810', 'TIQUISIO', '13'),
('13836', 'TURBACO', '13'),
('13838', 'TURBANA', '13'),
('13873', 'VILLANUEVA', '13'),
('13894', 'ZAMBRANO', '13'),
('15001', 'TUNJA', '15'),
('15022', 'ALMEIDA', '15'),
('15047', 'AQUITANIA', '15'),
('15051', 'ARCABUCO', '15'),
('15087', 'BELÉN', '15'),
('15090', 'BERBEO', '15'),
('15092', 'BETÉITIVA', '15'),
('15097', 'BOAVITA', '15'),
('15104', 'BOYACÁ', '15'),
('15106', 'BRICEÑO', '15'),
('15109', 'BUENAVISTA', '15'),
('15114', 'BUSBANZÁ', '15'),
('15131', 'CALDAS', '15'),
('15135', 'CAMPOHERMOSO', '15'),
('15162', 'CERINZA', '15'),
('15172', 'CHINAVITA', '15'),
('15176', 'CHIQUINQUIRÁ', '15'),
('15180', 'CHISCAS', '15'),
('15183', 'CHITA', '15'),
('15185', 'CHITARAQUE', '15'),
('15187', 'CHIVATÁ', '15'),
('15189', 'CIÉNEGA', '15'),
('15204', 'CÓMBITA', '15'),
('15212', 'COPER', '15'),
('15215', 'CORRALES', '15'),
('15218', 'COVARACHÍA', '15'),
('15223', 'CUBARÁ', '15'),
('15224', 'CUCAITA', '15'),
('15226', 'CUÍTIVA', '15'),
('15232', 'CHÍQUIZA', '15'),
('15236', 'CHIVOR', '15'),
('15238', 'DUITAMA', '15'),
('15244', 'EL COCUY', '15'),
('15248', 'EL ESPINO', '15'),
('15272', 'FIRAVITOBA', '15'),
('15276', 'FLORESTA', '15'),
('15293', 'GACHANTIVÁ', '15'),
('15296', 'GÁMEZA', '15'),
('15299', 'GARAGOA', '15'),
('15317', 'GUACAMAYAS', '15'),
('15322', 'GUATEQUE', '15'),
('15325', 'GUAYATÁ', '15'),
('15332', 'GÜICÁN DE LA SIERRA', '15'),
('15362', 'IZA', '15'),
('15367', 'JENESANO', '15'),
('15368', 'JERICÓ', '15'),
('15377', 'LABRANZAGRANDE', '15'),
('15380', 'LA CAPILLA', '15'),
('15401', 'LA VICTORIA', '15'),
('15403', 'LA UVITA', '15'),
('15407', 'VILLA DE LEYVA', '15'),
('15425', 'MACANAL', '15'),
('15442', 'MARIPÍ', '15'),
('15455', 'MIRAFLORES', '15'),
('15464', 'MONGUA', '15'),
('15466', 'MONGUÍ', '15'),
('15469', 'MONIQUIRÁ', '15'),
('15476', 'MOTAVITA', '15'),
('15480', 'MUZO', '15'),
('15491', 'NOBSA', '15'),
('15494', 'NUEVO COLÓN', '15'),
('15500', 'OICATÁ', '15'),
('15507', 'OTANCHE', '15'),
('15511', 'PACHAVITA', '15'),
('15514', 'PÁEZ', '15'),
('15516', 'PAIPA', '15'),
('15518', 'PAJARITO', '15'),
('15522', 'PANQUEBA', '15'),
('15531', 'PAUNA', '15'),
('15533', 'PAYA', '15'),
('15537', 'PAZ DE RÍO', '15'),
('15542', 'PESCA', '15'),
('15550', 'PISBA', '15'),
('15572', 'PUERTO BOYACÁ', '15'),
('15580', 'QUÍPAMA', '15'),
('15599', 'RAMIRIQUÍ', '15'),
('15600', 'RÁQUIRA', '15'),
('15621', 'RONDÓN', '15'),
('15632', 'SABOYÁ', '15'),
('15638', 'SÁCHICA', '15'),
('15646', 'SAMACÁ', '15'),
('15660', 'SAN EDUARDO', '15'),
('15664', 'SAN JOSÉ DE PARE', '15'),
('15667', 'SAN LUIS DE GACENO', '15'),
('15673', 'SAN MATEO', '15'),
('15676', 'SAN MIGUEL DE SEMA', '15'),
('15681', 'SAN PABLO DE BORBUR', '15'),
('15686', 'SANTANA', '15'),
('15690', 'SANTA MARÍA', '15'),
('15693', 'SANTA ROSA DE VITERBO', '15'),
('15696', 'SANTA SOFÍA', '15'),
('15720', 'SATIVANORTE', '15'),
('15723', 'SATIVASUR', '15'),
('15740', 'SIACHOQUE', '15'),
('15753', 'SOATÁ', '15'),
('15755', 'SOCOTÁ', '15'),
('15757', 'SOCHA', '15'),
('15759', 'SOGAMOSO', '15'),
('15761', 'SOMONDOCO', '15'),
('15762', 'SORA', '15'),
('15763', 'SOTAQUIRÁ', '15'),
('15764', 'SORACÁ', '15'),
('15774', 'SUSACÓN', '15'),
('15776', 'SUTAMARCHÁN', '15'),
('15778', 'SUTATENZA', '15'),
('15790', 'TASCO', '15'),
('15798', 'TENZA', '15'),
('15804', 'TIBANÁ', '15'),
('15806', 'TIBASOSA', '15'),
('15808', 'TINJACÁ', '15'),
('15810', 'TIPACOQUE', '15'),
('15814', 'TOCA', '15'),
('15816', 'TOGÜÍ', '15'),
('15820', 'TÓPAGA', '15'),
('15822', 'TOTA', '15'),
('15832', 'TUNUNGUÁ', '15'),
('15835', 'TURMEQUÉ', '15'),
('15837', 'TUTA', '15'),
('15839', 'TUTAZÁ', '15'),
('15842', 'ÚMBITA', '15'),
('15861', 'VENTAQUEMADA', '15'),
('15879', 'VIRACACHÁ', '15'),
('15897', 'ZETAQUIRA', '15'),
('17001', 'MANIZALES', '17'),
('17013', 'AGUADAS', '17'),
('17042', 'ANSERMA', '17'),
('17050', 'ARANZAZU', '17'),
('17088', 'BELALCÁZAR', '17'),
('17174', 'CHINCHINÁ', '17'),
('17272', 'FILADELFIA', '17'),
('17380', 'LA DORADA', '17'),
('17388', 'LA MERCED', '17'),
('17433', 'MANZANARES', '17'),
('17442', 'MARMATO', '17'),
('17444', 'MARQUETALIA', '17'),
('17446', 'MARULANDA', '17'),
('17486', 'NEIRA', '17'),
('17495', 'NORCASIA', '17'),
('17513', 'PÁCORA', '17'),
('17524', 'PALESTINA', '17'),
('17541', 'PENSILVANIA', '17'),
('17614', 'RIOSUCIO', '17'),
('17616', 'RISARALDA', '17'),
('17653', 'SALAMINA', '17'),
('17662', 'SAMANÁ', '17'),
('17665', 'SAN JOSÉ', '17'),
('17777', 'SUPÍA', '17'),
('17867', 'VICTORIA', '17'),
('17873', 'VILLAMARÍA', '17'),
('17877', 'VITERBO', '17'),
('18001', 'FLORENCIA', '18'),
('18029', 'ALBANIA', '18'),
('18094', 'BELÉN DE LOS ANDAQUÍES', '18'),
('18150', 'CARTAGENA DEL CHAIRÁ', '18'),
('18205', 'CURILLO', '18'),
('18247', 'EL DONCELLO', '18'),
('18256', 'EL PAUJÍL', '18'),
('18410', 'LA MONTAÑITA', '18'),
('18460', 'MILÁN', '18'),
('18479', 'MORELIA', '18'),
('18592', 'PUERTO RICO', '18'),
('18610', 'SAN JOSÉ DEL FRAGUA', '18'),
('18753', 'SAN VICENTE DEL CAGUÁN', '18'),
('18756', 'SOLANO', '18'),
('18785', 'SOLITA', '18'),
('18860', 'VALPARAÍSO', '18'),
('19001', 'POPAYÁN', '19'),
('19022', 'ALMAGUER', '19'),
('19050', 'ARGELIA', '19'),
('19075', 'BALBOA', '19'),
('19100', 'BOLÍVAR', '19'),
('19110', 'BUENOS AIRES', '19'),
('19130', 'CAJIBÍO', '19'),
('19137', 'CALDONO', '19'),
('19142', 'CALOTO', '19'),
('19212', 'CORINTO', '19'),
('19256', 'EL TAMBO', '19'),
('19290', 'FLORENCIA', '19'),
('19300', 'GUACHENÉ', '19'),
('19318', 'GUAPI', '19'),
('19355', 'INZÁ', '19'),
('19364', 'JAMBALÓ', '19'),
('19392', 'LA SIERRA', '19'),
('19397', 'LA VEGA', '19'),
('19418', 'LÓPEZ DE MICAY', '19'),
('19450', 'MERCADERES', '19'),
('19455', 'MIRANDA', '19'),
('19473', 'MORALES', '19'),
('19513', 'PADILLA', '19'),
('19517', 'PÁEZ', '19'),
('19532', 'PATÍA', '19'),
('19533', 'PIAMONTE', '19'),
('19548', 'PIENDAMÓ - TUNÍA', '19'),
('19573', 'PUERTO TEJADA', '19'),
('19585', 'PURACÉ', '19'),
('19622', 'ROSAS', '19'),
('19693', 'SAN SEBASTIÁN', '19'),
('19698', 'SANTANDER DE QUILICHAO', '19'),
('19701', 'SANTA ROSA', '19'),
('19743', 'SILVIA', '19'),
('19760', 'SOTARÁ PAISPAMBA', '19'),
('19780', 'SUÁREZ', '19'),
('19785', 'SUCRE', '19'),
('19807', 'TIMBÍO', '19'),
('19809', 'TIMBIQUÍ', '19'),
('19821', 'TORIBÍO', '19'),
('19824', 'TOTORÓ', '19'),
('19845', 'VILLA RICA', '19'),
('20001', 'VALLEDUPAR', '20'),
('20011', 'AGUACHICA', '20'),
('20013', 'AGUSTÍN CODAZZI', '20'),
('20032', 'ASTREA', '20'),
('20045', 'BECERRIL', '20'),
('20060', 'BOSCONIA', '20'),
('20175', 'CHIMICHAGUA', '20'),
('20178', 'CHIRIGUANÁ', '20'),
('20228', 'CURUMANÍ', '20'),
('20238', 'EL COPEY', '20'),
('20250', 'EL PASO', '20'),
('20295', 'GAMARRA', '20'),
('20310', 'GONZÁLEZ', '20'),
('20383', 'LA GLORIA', '20'),
('20400', 'LA JAGUA DE IBIRICO', '20'),
('20443', 'MANAURE BALCÓN DEL CESAR', '20'),
('20517', 'PAILITAS', '20'),
('20550', 'PELAYA', '20'),
('20570', 'PUEBLO BELLO', '20'),
('20614', 'RÍO DE ORO', '20'),
('20621', 'LA PAZ', '20'),
('20710', 'SAN ALBERTO', '20'),
('20750', 'SAN DIEGO', '20'),
('20770', 'SAN MARTÍN', '20'),
('20787', 'TAMALAMEQUE', '20'),
('23001', 'MONTERÍA', '23'),
('23068', 'AYAPEL', '23'),
('23079', 'BUENAVISTA', '23'),
('23090', 'CANALETE', '23'),
('23162', 'CERETÉ', '23'),
('23168', 'CHIMÁ', '23'),
('23182', 'CHINÚ', '23'),
('23189', 'CIÉNAGA DE ORO', '23'),
('23300', 'COTORRA', '23'),
('23350', 'LA APARTADA', '23'),
('23417', 'LORICA', '23'),
('23419', 'LOS CÓRDOBAS', '23'),
('23464', 'MOMIL', '23'),
('23466', 'MONTELÍBANO', '23'),
('23500', 'MOÑITOS', '23'),
('23555', 'PLANETA RICA', '23'),
('23570', 'PUEBLO NUEVO', '23'),
('23574', 'PUERTO ESCONDIDO', '23'),
('23580', 'PUERTO LIBERTADOR', '23'),
('23586', 'PURÍSIMA DE LA CONCEPCIÓN', '23'),
('23660', 'SAHAGÚN', '23'),
('23670', 'SAN ANDRÉS DE SOTAVENTO', '23'),
('23672', 'SAN ANTERO', '23'),
('23675', 'SAN BERNARDO DEL VIENTO', '23'),
('23678', 'SAN CARLOS', '23'),
('23682', 'SAN JOSÉ DE URÉ', '23'),
('23686', 'SAN PELAYO', '23'),
('23807', 'TIERRALTA', '23'),
('23815', 'TUCHÍN', '23'),
('23855', 'VALENCIA', '23'),
('25001', 'AGUA DE DIOS', '25'),
('25019', 'ALBÁN', '25'),
('25035', 'ANAPOIMA', '25'),
('25040', 'ANOLAIMA', '25'),
('25053', 'ARBELÁEZ', '25'),
('25086', 'BELTRÁN', '25'),
('25095', 'BITUIMA', '25'),
('25099', 'BOJACÁ', '25'),
('25120', 'CABRERA', '25'),
('25123', 'CACHIPAY', '25'),
('25126', 'CAJICÁ', '25'),
('25148', 'CAPARRAPÍ', '25'),
('25151', 'CÁQUEZA', '25'),
('25154', 'CARMEN DE CARUPA', '25'),
('25168', 'CHAGUANÍ', '25'),
('25175', 'CHÍA', '25'),
('25178', 'CHIPAQUE', '25'),
('25181', 'CHOACHÍ', '25'),
('25183', 'CHOCONTÁ', '25'),
('25200', 'COGUA', '25'),
('25214', 'COTA', '25'),
('25224', 'CUCUNUBÁ', '25'),
('25245', 'EL COLEGIO', '25'),
('25258', 'EL PEÑÓN', '25'),
('25260', 'EL ROSAL', '25'),
('25269', 'FACATATIVÁ', '25'),
('25279', 'FÓMEQUE', '25'),
('25281', 'FOSCA', '25'),
('25286', 'FUNZA', '25'),
('25288', 'FÚQUENE', '25'),
('25290', 'FUSAGASUGÁ', '25'),
('25293', 'GACHALÁ', '25'),
('25295', 'GACHANCIPÁ', '25'),
('25297', 'GACHETÁ', '25'),
('25299', 'GAMA', '25'),
('25307', 'GIRARDOT', '25'),
('25312', 'GRANADA', '25'),
('25317', 'GUACHETÁ', '25'),
('25320', 'GUADUAS', '25'),
('25322', 'GUASCA', '25'),
('25324', 'GUATAQUÍ', '25'),
('25326', 'GUATAVITA', '25'),
('25328', 'GUAYABAL DE SÍQUIMA', '25'),
('25335', 'GUAYABETAL', '25'),
('25339', 'GUTIÉRREZ', '25'),
('25368', 'JERUSALÉN', '25'),
('25372', 'JUNÍN', '25'),
('25377', 'LA CALERA', '25'),
('25386', 'LA MESA', '25'),
('25394', 'LA PALMA', '25'),
('25398', 'LA PEÑA', '25'),
('25402', 'LA VEGA', '25'),
('25407', 'LENGUAZAQUE', '25'),
('25426', 'MACHETÁ', '25'),
('25430', 'MADRID', '25'),
('25436', 'MANTA', '25'),
('25438', 'MEDINA', '25'),
('25473', 'MOSQUERA', '25'),
('25483', 'NARIÑO', '25'),
('25486', 'NEMOCÓN', '25'),
('25488', 'NILO', '25'),
('25489', 'NIMAIMA', '25'),
('25491', 'NOCAIMA', '25'),
('25506', 'VENECIA', '25'),
('25513', 'PACHO', '25'),
('25518', 'PAIME', '25'),
('25524', 'PANDI', '25'),
('25530', 'PARATEBUENO', '25'),
('25535', 'PASCA', '25'),
('25572', 'PUERTO SALGAR', '25'),
('25580', 'PULÍ', '25'),
('25592', 'QUEBRADANEGRA', '25'),
('25594', 'QUETAME', '25'),
('25596', 'QUIPILE', '25'),
('25599', 'APULO', '25'),
('25612', 'RICAURTE', '25'),
('25645', 'SAN ANTONIO DEL TEQUENDAMA', '25'),
('25649', 'SAN BERNARDO', '25'),
('25653', 'SAN CAYETANO', '25'),
('25658', 'SAN FRANCISCO', '25'),
('25662', 'SAN JUAN DE RIOSECO', '25'),
('25718', 'SASAIMA', '25'),
('25736', 'SESQUILÉ', '25'),
('25740', 'SIBATÉ', '25'),
('25743', 'SILVANIA', '25'),
('25745', 'SIMIJACA', '25'),
('25754', 'SOACHA', '25'),
('25758', 'SOPÓ', '25'),
('25769', 'SUBACHOQUE', '25'),
('25772', 'SUESCA', '25'),
('25777', 'SUPATÁ', '25'),
('25779', 'SUSA', '25'),
('25781', 'SUTATAUSA', '25'),
('25785', 'TABIO', '25'),
('25793', 'TAUSA', '25'),
('25797', 'TENA', '25'),
('25799', 'TENJO', '25'),
('25805', 'TIBACUY', '25'),
('25807', 'TIBIRITA', '25'),
('25815', 'TOCAIMA', '25'),
('25817', 'TOCANCIPÁ', '25'),
('25823', 'TOPAIPÍ', '25'),
('25839', 'UBALÁ', '25'),
('25841', 'UBAQUE', '25'),
('25843', 'VILLA DE SAN DIEGO DE UBATÉ', '25'),
('25845', 'UNE', '25'),
('25851', 'ÚTICA', '25'),
('25862', 'VERGARA', '25'),
('25867', 'VIANÍ', '25'),
('25871', 'VILLAGÓMEZ', '25'),
('25873', 'VILLAPINZÓN', '25'),
('25875', 'VILLETA', '25'),
('25878', 'VIOTÁ', '25'),
('25885', 'YACOPÍ', '25'),
('25898', 'ZIPACÓN', '25'),
('25899', 'ZIPAQUIRÁ', '25'),
('27001', 'QUIBDÓ', '27'),
('27006', 'ACANDÍ', '27'),
('27025', 'ALTO BAUDÓ', '27'),
('27050', 'ATRATO', '27'),
('27073', 'BAGADÓ', '27'),
('27075', 'BAHÍA SOLANO', '27'),
('27077', 'BAJO BAUDÓ', '27'),
('27099', 'BOJAYÁ', '27'),
('27135', 'EL CANTÓN DEL SAN PABLO', '27'),
('27150', 'CARMEN DEL DARIÉN', '27'),
('27160', 'CÉRTEGUI', '27'),
('27205', 'CONDOTO', '27'),
('27245', 'EL CARMEN DE ATRATO', '27'),
('27250', 'EL LITORAL DEL SAN JUAN', '27'),
('27361', 'ISTMINA', '27'),
('27372', 'JURADÓ', '27'),
('27413', 'LLORÓ', '27'),
('27425', 'MEDIO ATRATO', '27'),
('27430', 'MEDIO BAUDÓ', '27'),
('27450', 'MEDIO SAN JUAN', '27'),
('27491', 'NÓVITA', '27'),
('27493', 'NUEVO BELÉN DE BAJIRÁ *', '27'),
('27495', 'NUQUÍ', '27'),
('27580', 'RÍO IRÓ', '27'),
('27600', 'RÍO QUITO', '27'),
('27615', 'RIOSUCIO', '27'),
('27660', 'SAN JOSÉ DEL PALMAR', '27'),
('27745', 'SIPÍ', '27'),
('27787', 'TADÓ', '27'),
('27800', 'UNGUÍA', '27'),
('27810', 'UNIÓN PANAMERICANA', '27'),
('41001', 'NEIVA', '41'),
('41006', 'ACEVEDO', '41'),
('41013', 'AGRADO', '41'),
('41016', 'AIPE', '41'),
('41020', 'ALGECIRAS', '41'),
('41026', 'ALTAMIRA', '41'),
('41078', 'BARAYA', '41'),
('41132', 'CAMPOALEGRE', '41'),
('41206', 'COLOMBIA', '41'),
('41244', 'ELÍAS', '41'),
('41298', 'GARZÓN', '41'),
('41306', 'GIGANTE', '41'),
('41319', 'GUADALUPE', '41'),
('41349', 'HOBO', '41'),
('41357', 'ÍQUIRA', '41'),
('41359', 'ISNOS', '41'),
('41378', 'LA ARGENTINA', '41'),
('41396', 'LA PLATA', '41'),
('41483', 'NÁTAGA', '41'),
('41503', 'OPORAPA', '41'),
('41518', 'PAICOL', '41'),
('41524', 'PALERMO', '41'),
('41530', 'PALESTINA', '41'),
('41548', 'PITAL', '41'),
('41551', 'PITALITO', '41'),
('41615', 'RIVERA', '41'),
('41660', 'SALADOBLANCO', '41'),
('41668', 'SAN AGUSTÍN', '41'),
('41676', 'SANTA MARÍA', '41'),
('41770', 'SUAZA', '41'),
('41791', 'TARQUI', '41'),
('41797', 'TESALIA', '41'),
('41799', 'TELLO', '41'),
('41801', 'TERUEL', '41'),
('41807', 'TIMANÁ', '41'),
('41872', 'VILLAVIEJA', '41'),
('41885', 'YAGUARÁ', '41'),
('44001', 'RIOHACHA', '44'),
('44035', 'ALBANIA', '44'),
('44078', 'BARRANCAS', '44'),
('44090', 'DIBULLA', '44'),
('44098', 'DISTRACCIÓN', '44'),
('44110', 'EL MOLINO', '44'),
('44279', 'FONSECA', '44'),
('44378', 'HATONUEVO', '44'),
('44420', 'LA JAGUA DEL PILAR', '44'),
('44430', 'MAICAO', '44'),
('44560', 'MANAURE', '44'),
('44650', 'SAN JUAN DEL CESAR', '44'),
('44847', 'URIBIA', '44'),
('44855', 'URUMITA', '44'),
('44874', 'VILLANUEVA', '44'),
('47001', 'SANTA MARTA', '47'),
('47030', 'ALGARROBO', '47'),
('47053', 'ARACATACA', '47'),
('47058', 'ARIGUANÍ', '47'),
('47161', 'CERRO DE SAN ANTONIO', '47'),
('47170', 'CHIVOLO', '47'),
('47189', 'CIÉNAGA', '47'),
('47205', 'CONCORDIA', '47'),
('47245', 'EL BANCO', '47'),
('47258', 'EL PIÑÓN', '47'),
('47268', 'EL RETÉN', '47'),
('47288', 'FUNDACIÓN', '47'),
('47318', 'GUAMAL', '47'),
('47460', 'NUEVA GRANADA', '47'),
('47541', 'PEDRAZA', '47'),
('47545', 'PIJIÑO DEL CARMEN', '47'),
('47551', 'PIVIJAY', '47'),
('47555', 'PLATO', '47'),
('47570', 'PUEBLOVIEJO', '47'),
('47605', 'REMOLINO', '47'),
('47660', 'SABANAS DE SAN ÁNGEL', '47'),
('47675', 'SALAMINA', '47'),
('47692', 'SAN SEBASTIÁN DE BUENAVISTA', '47'),
('47703', 'SAN ZENÓN', '47'),
('47707', 'SANTA ANA', '47'),
('47720', 'SANTA BÁRBARA DE PINTO', '47'),
('47745', 'SITIONUEVO', '47'),
('47798', 'TENERIFE', '47'),
('47960', 'ZAPAYÁN', '47'),
('47980', 'ZONA BANANERA', '47'),
('50001', 'VILLAVICENCIO', '50'),
('50006', 'ACACÍAS', '50'),
('50110', 'BARRANCA DE UPÍA', '50'),
('50124', 'CABUYARO', '50'),
('50150', 'CASTILLA LA NUEVA', '50'),
('50223', 'CUBARRAL', '50'),
('50226', 'CUMARAL', '50'),
('50245', 'EL CALVARIO', '50'),
('50251', 'EL CASTILLO', '50'),
('50270', 'EL DORADO', '50'),
('50287', 'FUENTE DE ORO', '50'),
('50313', 'GRANADA', '50'),
('50318', 'GUAMAL', '50'),
('50325', 'MAPIRIPÁN', '50'),
('50330', 'MESETAS', '50'),
('50350', 'LA MACARENA', '50'),
('50370', 'URIBE', '50'),
('50400', 'LEJANÍAS', '50'),
('50450', 'PUERTO CONCORDIA', '50'),
('50568', 'PUERTO GAITÁN', '50'),
('50573', 'PUERTO LÓPEZ', '50'),
('50577', 'PUERTO LLERAS', '50'),
('50590', 'PUERTO RICO', '50'),
('50606', 'RESTREPO', '50'),
('50680', 'SAN CARLOS DE GUAROA', '50'),
('50683', 'SAN JUAN DE ARAMA', '50'),
('50686', 'SAN JUANITO', '50'),
('50689', 'SAN MARTÍN', '50'),
('50711', 'VISTAHERMOSA', '50'),
('52001', 'PASTO', '52'),
('52019', 'ALBÁN', '52'),
('52022', 'ALDANA', '52'),
('52036', 'ANCUYA', '52'),
('52051', 'ARBOLEDA', '52'),
('52079', 'BARBACOAS', '52'),
('52083', 'BELÉN', '52'),
('52110', 'BUESACO', '52'),
('52203', 'COLÓN', '52'),
('52207', 'CONSACÁ', '52'),
('52210', 'CONTADERO', '52'),
('52215', 'CÓRDOBA', '52'),
('52224', 'CUASPUD CARLOSAMA', '52'),
('52227', 'CUMBAL', '52'),
('52233', 'CUMBITARA', '52'),
('52240', 'CHACHAGÜÍ', '52'),
('52250', 'EL CHARCO', '52'),
('52254', 'EL PEÑOL', '52'),
('52256', 'EL ROSARIO', '52'),
('52258', 'EL TABLÓN DE GÓMEZ', '52'),
('52260', 'EL TAMBO', '52'),
('52287', 'FUNES', '52'),
('52317', 'GUACHUCAL', '52'),
('52320', 'GUAITARILLA', '52'),
('52323', 'GUALMATÁN', '52'),
('52352', 'ILES', '52'),
('52354', 'IMUÉS', '52'),
('52356', 'IPIALES', '52'),
('52378', 'LA CRUZ', '52'),
('52381', 'LA FLORIDA', '52'),
('52385', 'LA LLANADA', '52'),
('52390', 'LA TOLA', '52'),
('52399', 'LA UNIÓN', '52'),
('52405', 'LEIVA', '52'),
('52411', 'LINARES', '52'),
('52418', 'LOS ANDES', '52'),
('52427', 'MAGÜÍ', '52'),
('52435', 'MALLAMA', '52'),
('52473', 'MOSQUERA', '52'),
('52480', 'NARIÑO', '52'),
('52490', 'OLAYA HERRERA', '52'),
('52506', 'OSPINA', '52'),
('52520', 'FRANCISCO PIZARRO', '52'),
('52540', 'POLICARPA', '52'),
('52560', 'POTOSÍ', '52'),
('52565', 'PROVIDENCIA', '52'),
('52573', 'PUERRES', '52'),
('52585', 'PUPIALES', '52'),
('52612', 'RICAURTE', '52'),
('52621', 'ROBERTO PAYÁN', '52'),
('52678', 'SAMANIEGO', '52'),
('52683', 'SANDONÁ', '52'),
('52685', 'SAN BERNARDO', '52'),
('52687', 'SAN LORENZO', '52'),
('52693', 'SAN PABLO', '52'),
('52694', 'SAN PEDRO DE CARTAGO', '52'),
('52696', 'SANTA BÁRBARA', '52'),
('52699', 'SANTACRUZ', '52'),
('52720', 'SAPUYES', '52'),
('52786', 'TAMINANGO', '52'),
('52788', 'TANGUA', '52'),
('52835', 'SAN ANDRÉS DE TUMACO', '52'),
('52838', 'TÚQUERRES', '52'),
('52885', 'YACUANQUER', '52'),
('54001', 'SAN JOSÉ DE CÚCUTA', '54'),
('54003', 'ÁBREGO', '54'),
('54051', 'ARBOLEDAS', '54'),
('54099', 'BOCHALEMA', '54'),
('54109', 'BUCARASICA', '54'),
('54125', 'CÁCOTA', '54'),
('54128', 'CÁCHIRA', '54'),
('54172', 'CHINÁCOTA', '54'),
('54174', 'CHITAGÁ', '54'),
('54206', 'CONVENCIÓN', '54'),
('54223', 'CUCUTILLA', '54'),
('54239', 'DURANIA', '54'),
('54245', 'EL CARMEN', '54'),
('54250', 'EL TARRA', '54'),
('54261', 'EL ZULIA', '54'),
('54313', 'GRAMALOTE', '54'),
('54344', 'HACARÍ', '54'),
('54347', 'HERRÁN', '54'),
('54377', 'LABATECA', '54'),
('54385', 'LA ESPERANZA', '54'),
('54398', 'LA PLAYA', '54'),
('54405', 'LOS PATIOS', '54'),
('54418', 'LOURDES', '54'),
('54480', 'MUTISCUA', '54'),
('54498', 'OCAÑA', '54'),
('54518', 'PAMPLONA', '54'),
('54520', 'PAMPLONITA', '54'),
('54553', 'PUERTO SANTANDER', '54'),
('54599', 'RAGONVALIA', '54'),
('54660', 'SALAZAR', '54'),
('54670', 'SAN CALIXTO', '54'),
('54673', 'SAN CAYETANO', '54'),
('54680', 'SANTIAGO', '54'),
('54720', 'SARDINATA', '54'),
('54743', 'SILOS', '54'),
('54800', 'TEORAMA', '54'),
('54810', 'TIBÚ', '54'),
('54820', 'TOLEDO', '54'),
('54871', 'VILLA CARO', '54'),
('54874', 'VILLA DEL ROSARIO', '54'),
('63001', 'ARMENIA', '63'),
('63111', 'BUENAVISTA', '63'),
('63130', 'CALARCÁ', '63'),
('63190', 'CIRCASIA', '63'),
('63212', 'CÓRDOBA', '63'),
('63272', 'FILANDIA', '63'),
('63302', 'GÉNOVA', '63'),
('63401', 'LA TEBAIDA', '63'),
('63470', 'MONTENEGRO', '63'),
('63548', 'PIJAO', '63'),
('63594', 'QUIMBAYA', '63'),
('63690', 'SALENTO', '63'),
('66001', 'PEREIRA', '66'),
('66045', 'APÍA', '66'),
('66075', 'BALBOA', '66'),
('66088', 'BELÉN DE UMBRÍA', '66'),
('66170', 'DOSQUEBRADAS', '66'),
('66318', 'GUÁTICA', '66'),
('66383', 'LA CELIA', '66'),
('66400', 'LA VIRGINIA', '66'),
('66440', 'MARSELLA', '66'),
('66456', 'MISTRATÓ', '66'),
('66572', 'PUEBLO RICO', '66'),
('66594', 'QUINCHÍA', '66'),
('66682', 'SANTA ROSA DE CABAL', '66'),
('66687', 'SANTUARIO', '66'),
('68001', 'BUCARAMANGA', '68'),
('68013', 'AGUADA', '68'),
('68020', 'ALBANIA', '68'),
('68051', 'ARATOCA', '68'),
('68077', 'BARBOSA', '68'),
('68079', 'BARICHARA', '68'),
('68081', 'BARRANCABERMEJA', '68'),
('68092', 'BETULIA', '68'),
('68101', 'BOLÍVAR', '68'),
('68121', 'CABRERA', '68'),
('68132', 'CALIFORNIA', '68'),
('68147', 'CAPITANEJO', '68'),
('68152', 'CARCASÍ', '68'),
('68160', 'CEPITÁ', '68'),
('68162', 'CERRITO', '68'),
('68167', 'CHARALÁ', '68'),
('68169', 'CHARTA', '68'),
('68176', 'CHIMA', '68'),
('68179', 'CHIPATÁ', '68'),
('68190', 'CIMITARRA', '68'),
('68207', 'CONCEPCIÓN', '68'),
('68209', 'CONFINES', '68'),
('68211', 'CONTRATACIÓN', '68'),
('68217', 'COROMORO', '68'),
('68229', 'CURITÍ', '68'),
('68235', 'EL CARMEN DE CHUCURÍ', '68'),
('68245', 'EL GUACAMAYO', '68'),
('68250', 'EL PEÑÓN', '68'),
('68255', 'EL PLAYÓN', '68'),
('68264', 'ENCINO', '68'),
('68266', 'ENCISO', '68'),
('68271', 'FLORIÁN', '68'),
('68276', 'FLORIDABLANCA', '68'),
('68296', 'GALÁN', '68'),
('68298', 'GÁMBITA', '68'),
('68307', 'GIRÓN', '68'),
('68318', 'GUACA', '68'),
('68320', 'GUADALUPE', '68'),
('68322', 'GUAPOTÁ', '68'),
('68324', 'GUAVATÁ', '68'),
('68327', 'GÜEPSA', '68'),
('68344', 'HATO', '68'),
('68368', 'JESÚS MARÍA', '68'),
('68370', 'JORDÁN', '68'),
('68377', 'LA BELLEZA', '68'),
('68385', 'LANDÁZURI', '68'),
('68397', 'LA PAZ', '68'),
('68406', 'LEBRIJA', '68'),
('68418', 'LOS SANTOS', '68'),
('68425', 'MACARAVITA', '68'),
('68432', 'MÁLAGA', '68'),
('68444', 'MATANZA', '68'),
('68464', 'MOGOTES', '68'),
('68468', 'MOLAGAVITA', '68'),
('68498', 'OCAMONTE', '68'),
('68500', 'OIBA', '68'),
('68502', 'ONZAGA', '68'),
('68522', 'PALMAR', '68'),
('68524', 'PALMAS DEL SOCORRO', '68'),
('68533', 'PÁRAMO', '68'),
('68547', 'PIEDECUESTA', '68'),
('68549', 'PINCHOTE', '68'),
('68572', 'PUENTE NACIONAL', '68'),
('68573', 'PUERTO PARRA', '68'),
('68575', 'PUERTO WILCHES', '68'),
('68615', 'RIONEGRO', '68'),
('68655', 'SABANA DE TORRES', '68'),
('68669', 'SAN ANDRÉS', '68'),
('68673', 'SAN BENITO', '68'),
('68679', 'SAN GIL', '68'),
('68682', 'SAN JOAQUÍN', '68'),
('68684', 'SAN JOSÉ DE MIRANDA', '68'),
('68686', 'SAN MIGUEL', '68'),
('68689', 'SAN VICENTE DE CHUCURÍ', '68'),
('68705', 'SANTA BÁRBARA', '68'),
('68720', 'SANTA HELENA DEL OPÓN', '68'),
('68745', 'SIMACOTA', '68'),
('68755', 'SOCORRO', '68'),
('68770', 'SUAITA', '68'),
('68773', 'SUCRE', '68'),
('68780', 'SURATÁ', '68'),
('68820', 'TONA', '68'),
('68855', 'VALLE DE SAN JOSÉ', '68'),
('68861', 'VÉLEZ', '68'),
('68867', 'VETAS', '68'),
('68872', 'VILLANUEVA', '68'),
('68895', 'ZAPATOCA', '68'),
('70001', 'SINCELEJO', '70'),
('70110', 'BUENAVISTA', '70'),
('70124', 'CAIMITO', '70'),
('70204', 'COLOSÓ', '70'),
('70215', 'COROZAL', '70'),
('70221', 'COVEÑAS', '70'),
('70230', 'CHALÁN', '70'),
('70233', 'EL ROBLE', '70'),
('70235', 'GALERAS', '70'),
('70265', 'GUARANDA', '70'),
('70400', 'LA UNIÓN', '70'),
('70418', 'LOS PALMITOS', '70'),
('70429', 'MAJAGUAL', '70'),
('70473', 'MORROA', '70'),
('70508', 'OVEJAS', '70'),
('70523', 'PALMITO', '70'),
('70670', 'SAMPUÉS', '70'),
('70678', 'SAN BENITO ABAD', '70'),
('70702', 'SAN JUAN DE BETULIA', '70'),
('70708', 'SAN MARCOS', '70'),
('70713', 'SAN ONOFRE', '70'),
('70717', 'SAN PEDRO', '70'),
('70742', 'SAN LUIS DE SINCÉ', '70'),
('70771', 'SUCRE', '70'),
('70820', 'SANTIAGO DE TOLÚ', '70'),
('70823', 'SAN JOSÉ DE TOLUVIEJO', '70'),
('73001', 'IBAGUÉ', '73'),
('73024', 'ALPUJARRA', '73'),
('73026', 'ALVARADO', '73'),
('73030', 'AMBALEMA', '73'),
('73043', 'ANZOÁTEGUI', '73'),
('73055', 'ARMERO', '73'),
('73067', 'ATACO', '73'),
('73124', 'CAJAMARCA', '73'),
('73148', 'CARMEN DE APICALÁ', '73'),
('73152', 'CASABIANCA', '73'),
('73168', 'CHAPARRAL', '73'),
('73200', 'COELLO', '73'),
('73217', 'COYAIMA', '73'),
('73226', 'CUNDAY', '73'),
('73236', 'DOLORES', '73'),
('73268', 'ESPINAL', '73'),
('73270', 'FALAN', '73'),
('73275', 'FLANDES', '73'),
('73283', 'FRESNO', '73'),
('73319', 'GUAMO', '73'),
('73347', 'HERVEO', '73'),
('73349', 'HONDA', '73'),
('73352', 'ICONONZO', '73'),
('73408', 'LÉRIDA', '73'),
('73411', 'LÍBANO', '73'),
('73443', 'SAN SEBASTIÁN DE MARIQUITA', '73'),
('73449', 'MELGAR', '73'),
('73461', 'MURILLO', '73'),
('73483', 'NATAGAIMA', '73'),
('73504', 'ORTEGA', '73'),
('73520', 'PALOCABILDO', '73'),
('73547', 'PIEDRAS', '73'),
('73555', 'PLANADAS', '73'),
('73563', 'PRADO', '73'),
('73585', 'PURIFICACIÓN', '73'),
('73616', 'RIOBLANCO', '73'),
('73622', 'RONCESVALLES', '73'),
('73624', 'ROVIRA', '73'),
('73671', 'SALDAÑA', '73'),
('73675', 'SAN ANTONIO', '73'),
('73678', 'SAN LUIS', '73'),
('73686', 'SANTA ISABEL', '73'),
('73770', 'SUÁREZ', '73'),
('73854', 'VALLE DE SAN JUAN', '73'),
('73861', 'VENADILLO', '73'),
('73870', 'VILLAHERMOSA', '73'),
('73873', 'VILLARRICA', '73'),
('76001', 'SANTIAGO DE CALI', '76'),
('76020', 'ALCALÁ', '76'),
('76036', 'ANDALUCÍA', '76'),
('76041', 'ANSERMANUEVO', '76'),
('76054', 'ARGELIA', '76'),
('76100', 'BOLÍVAR', '76'),
('76109', 'BUENAVENTURA', '76'),
('76111', 'GUADALAJARA DE BUGA', '76'),
('76113', 'BUGALAGRANDE', '76'),
('76122', 'CAICEDONIA', '76'),
('76126', 'CALIMA', '76'),
('76130', 'CANDELARIA', '76'),
('76147', 'CARTAGO', '76'),
('76233', 'DAGUA', '76'),
('76243', 'EL ÁGUILA', '76'),
('76246', 'EL CAIRO', '76'),
('76248', 'EL CERRITO', '76'),
('76250', 'EL DOVIO', '76'),
('76275', 'FLORIDA', '76'),
('76306', 'GINEBRA', '76'),
('76318', 'GUACARÍ', '76'),
('76364', 'JAMUNDÍ', '76'),
('76377', 'LA CUMBRE', '76'),
('76400', 'LA UNIÓN', '76'),
('76403', 'LA VICTORIA', '76'),
('76497', 'OBANDO', '76'),
('76520', 'PALMIRA', '76'),
('76563', 'PRADERA', '76'),
('76606', 'RESTREPO', '76'),
('76616', 'RIOFRÍO', '76'),
('76622', 'ROLDANILLO', '76'),
('76670', 'SAN PEDRO', '76'),
('76736', 'SEVILLA', '76'),
('76823', 'TORO', '76'),
('76828', 'TRUJILLO', '76'),
('76834', 'TULUÁ', '76'),
('76845', 'ULLOA', '76'),
('76863', 'VERSALLES', '76'),
('76869', 'VIJES', '76'),
('76890', 'YOTOCO', '76'),
('76892', 'YUMBO', '76'),
('76895', 'ZARZAL', '76'),
('81001', 'ARAUCA', '81'),
('81065', 'ARAUQUITA', '81'),
('81220', 'CRAVO NORTE', '81'),
('81300', 'FORTUL', '81'),
('81591', 'PUERTO RONDÓN', '81'),
('81736', 'SARAVENA', '81'),
('81794', 'TAME', '81'),
('85001', 'YOPAL', '85'),
('85010', 'AGUAZUL', '85'),
('85015', 'CHÁMEZA', '85'),
('85125', 'HATO COROZAL', '85'),
('85136', 'LA SALINA', '85'),
('85139', 'MANÍ', '85'),
('85162', 'MONTERREY', '85'),
('85225', 'NUNCHÍA', '85'),
('85230', 'OROCUÉ', '85'),
('85250', 'PAZ DE ARIPORO', '85'),
('85263', 'PORE', '85'),
('85279', 'RECETOR', '85'),
('85300', 'SABANALARGA', '85'),
('85315', 'SÁCAMA', '85'),
('85325', 'SAN LUIS DE PALENQUE', '85'),
('85400', 'TÁMARA', '85'),
('85410', 'TAURAMENA', '85'),
('85430', 'TRINIDAD', '85'),
('85440', 'VILLANUEVA', '85'),
('86001', 'MOCOA', '86'),
('86219', 'COLÓN', '86'),
('86320', 'ORITO', '86'),
('86568', 'PUERTO ASÍS', '86'),
('86569', 'PUERTO CAICEDO', '86'),
('86571', 'PUERTO GUZMÁN', '86'),
('86573', 'PUERTO LEGUÍZAMO', '86'),
('86749', 'SIBUNDOY', '86'),
('86755', 'SAN FRANCISCO', '86'),
('86757', 'SAN MIGUEL', '86'),
('86760', 'SANTIAGO', '86'),
('86865', 'VALLE DEL GUAMUEZ', '86'),
('86885', 'VILLAGARZÓN', '86'),
('88001', 'SAN ANDRÉS **', '88'),
('88564', 'PROVIDENCIA', '88'),
('91001', 'LETICIA', '91'),
('91263', 'EL ENCANTO', '91'),
('91405', 'LA CHORRERA', '91'),
('91407', 'LA PEDRERA', '91'),
('91430', 'LA VICTORIA', '91'),
('91460', 'MIRITÍ - PARANÁ', '91'),
('91530', 'PUERTO ALEGRÍA', '91'),
('91536', 'PUERTO ARICA', '91'),
('91540', 'PUERTO NARIÑO', '91'),
('91669', 'PUERTO SANTANDER', '91'),
('91798', 'TARAPACÁ', '91'),
('94001', 'INÍRIDA', '94'),
('94343', 'BARRANCOMINAS', '94'),
('94883', 'SAN FELIPE', '94'),
('94884', 'PUERTO COLOMBIA', '94'),
('94885', 'LA GUADALUPE', '94'),
('94886', 'CACAHUAL', '94'),
('94887', 'PANA PANA', '94'),
('94888', 'MORICHAL', '94'),
('95001', 'SAN JOSÉ DEL GUAVIARE', '95'),
('95015', 'CALAMAR', '95'),
('95025', 'EL RETORNO', '95'),
('95200', 'MIRAFLORES', '95'),
('97001', 'MITÚ', '97'),
('97161', 'CARURÚ', '97'),
('97511', 'PACOA', '97'),
('97666', 'TARAIRA', '97'),
('97777', 'PAPUNAHUA', '97'),
('97889', 'YAVARATÉ', '97'),
('99001', 'PUERTO CARREÑO', '99'),
('99524', 'LA PRIMAVERA', '99'),
('99624', 'SANTA ROSALÍA', '99'),
('99773', 'CUMARIBO', '99');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamento`
--

CREATE TABLE `departamento` (
  `codigo_departamento` varchar(10) NOT NULL,
  `nombre_departamento` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `departamento`
--

INSERT INTO `departamento` (`codigo_departamento`, `nombre_departamento`) VALUES
('91', 'AMAZONAS'),
('05', 'ANTIOQUIA'),
('81', 'ARAUCA'),
('88', 'ARCHIPIÉLAGO DE SAN ANDRÉS, PROVIDENCIA Y SANTA CATALINA'),
('08', 'ATLÁNTICO'),
('11', 'BOGOTÁ, D.C.'),
('13', 'BOLÍVAR'),
('15', 'BOYACÁ'),
('17', 'CALDAS'),
('18', 'CAQUETÁ'),
('85', 'CASANARE'),
('19', 'CAUCA'),
('20', 'CESAR'),
('27', 'CHOCÓ'),
('23', 'CÓRDOBA'),
('25', 'CUNDINAMARCA'),
('94', 'GUAINÍA'),
('95', 'GUAVIARE'),
('41', 'HUILA'),
('44', 'LA GUAJIRA'),
('47', 'MAGDALENA'),
('50', 'META'),
('52', 'NARIÑO'),
('54', 'NORTE DE SANTANDER'),
('86', 'PUTUMAYO'),
('63', 'QUINDÍO'),
('66', 'RISARALDA'),
('68', 'SANTANDER'),
('70', 'SUCRE'),
('73', 'TOLIMA'),
('76', 'VALLE DEL CAUCA'),
('97', 'VAUPÉS'),
('99', 'VICHADA');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(7, 'proyecto_ips_app', 'agenda'),
(12, 'proyecto_ips_app', 'auxadmin'),
(17, 'proyecto_ips_app', 'cita'),
(8, 'proyecto_ips_app', 'ciudad'),
(9, 'proyecto_ips_app', 'departamento'),
(10, 'proyecto_ips_app', 'especialidad'),
(11, 'proyecto_ips_app', 'estadocita'),
(14, 'proyecto_ips_app', 'lugaratencion'),
(16, 'proyecto_ips_app', 'medico'),
(13, 'proyecto_ips_app', 'paciente'),
(15, 'proyecto_ips_app', 'slotcita'),
(6, 'proyecto_ips_app', 'usuario'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-06-30 19:58:06.310060'),
(2, 'contenttypes', '0002_remove_content_type_name', '2025-06-30 19:58:06.354476'),
(3, 'auth', '0001_initial', '2025-06-30 19:58:06.519795'),
(4, 'auth', '0002_alter_permission_name_max_length', '2025-06-30 19:58:06.571427'),
(5, 'auth', '0003_alter_user_email_max_length', '2025-06-30 19:58:06.577966'),
(6, 'auth', '0004_alter_user_username_opts', '2025-06-30 19:58:06.582062'),
(7, 'auth', '0005_alter_user_last_login_null', '2025-06-30 19:58:06.587195'),
(8, 'auth', '0006_require_contenttypes_0002', '2025-06-30 19:58:06.590477'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2025-06-30 19:58:06.595055'),
(10, 'auth', '0008_alter_user_username_max_length', '2025-06-30 19:58:06.600074'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2025-06-30 19:58:06.607804'),
(12, 'auth', '0010_alter_group_name_max_length', '2025-06-30 19:58:06.625590'),
(13, 'auth', '0011_update_proxy_permissions', '2025-06-30 19:58:06.630136'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2025-06-30 19:58:06.633594'),
(15, 'proyecto_ips_app', '0001_initial', '2025-06-30 19:58:07.441152'),
(16, 'admin', '0001_initial', '2025-06-30 19:58:07.521826'),
(17, 'admin', '0002_logentry_remove_auto_add', '2025-06-30 19:58:07.529289'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2025-06-30 19:58:07.536494'),
(19, 'sessions', '0001_initial', '2025-06-30 19:58:07.559502'),
(20, 'proyecto_ips_app', '0002_alter_cita_lugar_atencion', '2025-07-02 23:16:54.288510');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('01fqq2xaeqskcnl1mq9jods72bnzrawl', '.eJxVjDsOwjAQBe_iGln-JWtT0nMGa9dr4wBypDipEHeHSCmgfTPzXiLitta49bzEicVZaHH63QjTI7cd8B3bbZZpbusykdwVedAurzPn5-Vw_w4q9vqtrQoDK_Kgg_NFa0zJIg8ADNZ5pmRKAAjkDfqxWM3GKhgzGUWcnTHi_QHPrjd1:1uWOlR:IWjyMErQSTryNdcR2DPpsgbw4XqD-lwQ7nA67vr4c5I', '2025-07-01 00:34:21.484674'),
('0k36mc1a9zfsq6ib4rp316276gz6o11n', '.eJxVjEEOwiAQAP_C2ZCFLi149N43EJZdbNW0SWlPxr8bkh70OjOZt4rp2Kd4VNnizOqqjLr8Mkr5KUsT_EjLfdV5XfZtJt0Sfdqqx5XldTvbv8GU6tS2BMV6RnY2mN6JAUsoyAMy8CBg-w7LkC0ZMEAhOyQTUEIB33lkrz5fx_I3BQ:1uX6hS:L_Jid2dbVSceGxDLjRN6Qa5ClZafVZlcb6s78B1HsdI', '2025-07-02 23:29:10.334425'),
('0pb3vtzzjqp0ab5h5b9grzajwr79kl7z', '.eJxVjDsOwjAQBe_iGln-JWtT0nMGa9dr4wBypDipEHeHSCmgfTPzXiLitta49bzEicVZaHH63QjTI7cd8B3bbZZpbusykdwVedAurzPn5-Vw_w4q9vqtrQoDK_Kgg_NFa0zJIg8ADNZ5pmRKAAjkDfqxWM3GKhgzGUWcnTHi_QHPrjd1:1uWKeY:VwACsUsE9nChixXJiD-VDP7obi9B3XtpFUSz03KIWaA', '2025-06-30 19:59:08.447050'),
('4nkanktkoj61tn610objoq0el5ymv7y7', '.eJxVjDsOwjAQBe_iGln-m1DS5wzWeneNA8iR4qRC3B0ipYD2zcx7iQTbWtPWeUkTiYvQ4vS7ZcAHtx3QHdptlji3dZmy3BV50C7Hmfh5Pdy_gwq9fmvDXmdrBrLKESAw2RgJjSGKxTK6okKIJgblgQszZq2885rOg3LMVrw_-Dw4VQ:1uZgu7:aZ8GhsDVYdtgyQs_Cj6MzkZ96YAAQYvVyTkVy_RpUkw', '2025-07-10 02:32:55.783254'),
('5oopkurmxft46hyq218whsraigd6n0f8', '.eJxVjDsOwjAQBe_iGln-JWtT0nMGa9dr4wBypDipEHeHSCmgfTPzXiLitta49bzEicVZaHH63QjTI7cd8B3bbZZpbusykdwVedAurzPn5-Vw_w4q9vqtrQoDK_Kgg_NFa0zJIg8ADNZ5pmRKAAjkDfqxWM3GKhgzGUWcnTHi_QHPrjd1:1uWKpY:Stw1TuF9AfMQyKJinWXFnTQCxSMuZqfGXD0mCiD3O8U', '2025-06-30 20:10:30.117581'),
('5qore630kkbdcedbgbavj6tn5s4ytnhs', '.eJxVjEEOwiAQAP_C2ZCFLi149N43EJZdbNW0SWlPxr8bkh70OjOZt4rp2Kd4VNnizOqqjLr8Mkr5KUsT_EjLfdV5XfZtJt0Sfdqqx5XldTvbv8GU6tS2BMV6RnY2mN6JAUsoyAMy8CBg-w7LkC0ZMEAhOyQTUEIB33lkrz5fx_I3BQ:1uX71k:BNSFx4UAx1D8Db5mfMYQWPD3m7msvG2EdO8JkRfC2QQ', '2025-07-02 23:50:08.586697'),
('638kcw1kxbg2c5qp8vwckmq1ki8cm951', '.eJxVjMsKwyAQAP_FcxFdHyE99t5vkNVda9qiEJNT6L8XIYf2OjPMIQLuWwl75zUsJK5Ci8svi5heXIegJ9ZHk6nVbV2iHIk8bZf3Rvy-ne3foGAvY8tWETj2cTaAbkpAU-bEzpBSyYON2Wlllcqz9kZHSxQzeDRgkkdtxecL4Ag3qg:1uX5yt:jwvUJXM0vy4iGhr9tQE4M7zPoNU_l4muSUfQp01CImg', '2025-07-02 22:43:07.847368'),
('6qnpwf5jacpa1kri6q3qce5xbav9nfbl', '.eJxVjDsOwjAQBe_iGln-JWtT0nMGa9dr4wBypDipEHeHSCmgfTPzXiLitta49bzEicVZaHH63QjTI7cd8B3bbZZpbusykdwVedAurzPn5-Vw_w4q9vqtrQoDK_Kgg_NFa0zJIg8ADNZ5pmRKAAjkDfqxWM3GKhgzGUWcnTHi_QHPrjd1:1uWPrt:_BIFpXf4NduC6gx25T4bw6q_47kNwT-N16AvTQn33c0', '2025-07-01 01:45:05.572156'),
('7pubpsgzx7165dgyp5u3iuizshm7i3h9', '.eJxVjDsOwjAQBe_iGln-JWtT0nMGa9dr4wBypDipEHeHSCmgfTPzXiLitta49bzEicVZaHH63QjTI7cd8B3bbZZpbusykdwVedAurzPn5-Vw_w4q9vqtrQoDK_Kgg_NFa0zJIg8ADNZ5pmRKAAjkDfqxWM3GKhgzGUWcnTHi_QHPrjd1:1uWKn3:pCx9rea1kruTM9hkD0jkraugtkWhr8eX4kBgw_Z2fus', '2025-06-30 20:07:55.367120'),
('8t00lbmqtvcdgvoyihzd8g8sbpcbewpj', '.eJxVjDsOwjAQBe_iGlk4_lPS5wzWer2LA8iR4qRC3B0ipYD2zcx7iQTbWtPWaUlTERehxel3y4APajsod2i3WeLc1mXKclfkQbsc50LP6-H-HVTo9Vu7aBSTPjvQnhRj0BY0hhIhGsoDeRrYe6ez9xyRC4ItlK3jqBiCMeL9AfMnOLY:1uZl6d:A_9h8FzBVQ5jIqDR9fgSFXc8x0pnkvwEb_gJWs4A2n4', '2025-07-24 06:50:07.925485'),
('9u87wg3sy0lmfxob4jqqfuupykur0ohw', 'e30:1uZgiS:K8CLGWMQ5ICpgifij8Ds_HZAOgvjlRiiVnbTW6mvpEc', '2025-07-10 02:20:52.452098'),
('ata2u12nw755hhyycehgesc371vj3yky', '.eJxVjDsOwjAQBe_iGlmbxb9Q0nMGa9decADZUpxUiLtDpBTQvpl5LxVpXUpcu8xxyuqkrDr8bkzpIXUD-U711nRqdZkn1puid9r1pWV5nnf376BQL98aDAsYQAieHQwuMCPB1Qwogay3wQgFykcDVtzobEo8WgooiEiGvXp_AMHhNy8:1uZhW5:GDhrEYHClVTlx3H6RUetd7SVBMe46LLVdP5Bm2UYncU', '2025-07-10 03:12:09.938015'),
('atq131ruvc4nj9vjunoz1bw5969t64qe', '.eJxVjEEOwiAQAP_C2ZCFLi149N43EJZdbNW0SWlPxr8bkh70OjOZt4rp2Kd4VNnizOqqjLr8Mkr5KUsT_EjLfdV5XfZtJt0Sfdqqx5XldTvbv8GU6tS2BMV6RnY2mN6JAUsoyAMy8CBg-w7LkC0ZMEAhOyQTUEIB33lkrz5fx_I3BQ:1uX8wE:r5AVAW018mpr72IyLFhRE9L5vnrMaUsXMf8jD-LUm8E', '2025-07-03 01:52:34.229683'),
('b9lojsqzvprn5zdjp7i9bkivd7t4kype', '.eJxVjDsOwjAQBe_iGlk4_lPS5wzWer2LA8iR4qRC3B0ipYD2zcx7iQTbWtPWaUlTERehxel3y4APajsod2i3WeLc1mXKclfkQbsc50LP6-H-HVTo9Vu7aBSTPjvQnhRj0BY0hhIhGsoDeRrYe6ez9xyRC4ItlK3jqBiCMeL9AfMnOLY:1uZiK5:P8t7TdagrcObzxgTW7RHrvDG4hrCdADsBW88rvcOd8E', '2025-07-10 04:03:49.743441'),
('d69ffxasev0n8uh8d217v5jimfigmx2p', '.eJxVjEEOwiAQRe_C2hBgSlpcuvcMZGBmpGpoUtqV8e5K0oVu_3v_vVTEfStxb7zGmdRZWXX63RLmB9cO6I71tui81G2dk-6KPmjT14X4eTncv0DBVnrWIE-CbBxkDuQnEAo8imULwl6EXDZuRGsFwAwpBBgQvHwP3pCQen8AA9Q4hg:1uZhvU:7O3b63hhtYaVf6D_LmuxYPLxL2IX20BIDrINsKzrcvU', '2025-07-10 03:38:24.993622'),
('d83zydwb58sm3gimdcn1r105048ljfny', '.eJxVjDsOwjAQBe_iGln-JWtT0nMGa9dr4wBypDipEHeHSCmgfTPzXiLitta49bzEicVZaHH63QjTI7cd8B3bbZZpbusykdwVedAurzPn5-Vw_w4q9vqtrQoDK_Kgg_NFa0zJIg8ADNZ5pmRKAAjkDfqxWM3GKhgzGUWcnTHi_QHPrjd1:1uWQH0:haZOu5m-U00Nw_sn_YmLm0BMFdvi7QNyzL6vgE4skRg', '2025-07-01 02:11:02.986088'),
('e92u345btt4wfe7o56q6cw2ks7z9ihbn', '.eJxVjEEOwiAURO_C2hAKHygu3fcM5PMBqRpISrsy3t026UJXk8x7M2_mcVuL33pa_BzZlQG7_HYB6ZnqAeID671xanVd5sAPhZ-086nF9Lqd7t9BwV72NcKotLXklMCEZBF0tsYZDUOQNqssQFIeJYIzIpCVaCRQiMOeFEiyzxfVDDfI:1uWQgd:eoly9_Hx2h1ql0Oppeg6nmY2QM-KRNnm1uvT3Io87EY', '2025-07-01 02:37:31.256727'),
('ewxnb3g64kwi0707sz15csu2ld5i1j93', '.eJxVjDsOwjAQBe_iGln-m1DS5wzWeneNA8iR4qRC3B0ipYD2zcx7iQTbWtPWeUkTiYvQ4vS7ZcAHtx3QHdptlji3dZmy3BV50C7Hmfh5Pdy_gwq9fmvDXmdrBrLKESAw2RgJjSGKxTK6okKIJgblgQszZq2885rOg3LMVrw_-Dw4VQ:1uZgLI:EWj0nkOyYDo0F3OjwZL9wSmz_t3tWb7FpVDgWWMI8D8', '2025-07-10 01:56:56.746783'),
('gc77gt2tqzw2s5syaty30l4m9tr4csb7', '.eJxVjMsKwyAQAP_FcxFdHyE99t5vkNVda9qiEJNT6L8XIYf2OjPMIQLuWwl75zUsJK5Ci8svi5heXIegJ9ZHk6nVbV2iHIk8bZf3Rvy-ne3foGAvY8tWETj2cTaAbkpAU-bEzpBSyYON2Wlllcqz9kZHSxQzeDRgkkdtxecL4Ag3qg:1uX5D1:2Bh4gq9WLZWP_plCAQVHCd4lepQDWkMuvfRqZfDmf14', '2025-07-02 21:53:39.118186'),
('guyq0axcp3nm2bkk7oluogaytaohrf9r', '.eJxVjMsKwyAQAP_FcxFdHyE99t5vkNVda9qiEJNT6L8XIYf2OjPMIQLuWwl75zUsJK5Ci8svi5heXIegJ9ZHk6nVbV2iHIk8bZf3Rvy-ne3foGAvY8tWETj2cTaAbkpAU-bEzpBSyYON2Wlllcqz9kZHSxQzeDRgkkdtxecL4Ag3qg:1uWSkl:5A0VKnQdNAMJoutNjmy0yoRyo-iKm5fo8JxTAOsZ8XQ', '2025-07-01 04:49:55.406353'),
('lcrt9ixbysus2az77rpfop66apry4hm8', '.eJxVjEEOwiAQAP_C2ZCFLi149N43EJZdbNW0SWlPxr8bkh70OjOZt4rp2Kd4VNnizOqqjLr8Mkr5KUsT_EjLfdV5XfZtJt0Sfdqqx5XldTvbv8GU6tS2BMV6RnY2mN6JAUsoyAMy8CBg-w7LkC0ZMEAhOyQTUEIB33lkrz5fx_I3BQ:1uX7bg:263qi6T8DpW-Cx-72iGnGQDUdRMZl3B8vxm3xmVdJQI', '2025-07-03 00:27:16.339650'),
('lejo6qo2cr6ng4oqmu1nq85pjx64l5z1', 'e30:1uZgfL:2bQ-ZXUmKJMLN5Q6y2VZccfdYhETJwrIESMaWcBup7Y', '2025-07-10 02:17:39.926727'),
('lsjobnoe6uv2vunoo0qjspla8aeot7j1', '.eJxVjEEOwiAQAP_C2ZCFLi149N43EJZdbNW0SWlPxr8bkh70OjOZt4rp2Kd4VNnizOqqjLr8Mkr5KUsT_EjLfdV5XfZtJt0Sfdqqx5XldTvbv8GU6tS2BMV6RnY2mN6JAUsoyAMy8CBg-w7LkC0ZMEAhOyQTUEIB33lkrz5fx_I3BQ:1uX9Ig:HmIaq2YTUGB6ZxbJ454_rxHzYu1bWAMpS-tjn8NOEd4', '2025-07-03 02:15:46.229890'),
('qrasfxov5g5rtf6cw929s12kicoaio3r', '.eJxVjMsKwyAQAP_FcxFdHyE99t5vkNVda9qiEJNT6L8XIYf2OjPMIQLuWwl75zUsJK5Ci8svi5heXIegJ9ZHk6nVbV2iHIk8bZf3Rvy-ne3foGAvY8tWETj2cTaAbkpAU-bEzpBSyYON2Wlllcqz9kZHSxQzeDRgkkdtxecL4Ag3qg:1uX4iW:ggZ7fLbBLdVBwHLGwyJXBHWo9yh9Yj0H_Z4Oy-A21mg', '2025-07-02 21:22:08.047690'),
('r0owe5ewvlfia8bargsiltmjqsvj7o6q', 'e30:1uZgfL:2bQ-ZXUmKJMLN5Q6y2VZccfdYhETJwrIESMaWcBup7Y', '2025-07-10 02:17:39.283926'),
('tdj06j8ne0td0pmxwz9fqkruz19z2war', '.eJxVjEEOwiAQAP_C2ZCFLi149N43EJZdbNW0SWlPxr8bkh70OjOZt4rp2Kd4VNnizOqqjLr8Mkr5KUsT_EjLfdV5XfZtJt0Sfdqqx5XldTvbv8GU6tS2BMV6RnY2mN6JAUsoyAMy8CBg-w7LkC0ZMEAhOyQTUEIB33lkrz5fx_I3BQ:1uX6Kk:fgTM3NoArqb-G1g4Sq8Wl7QP2k6_LRE1EdnWy8VKa1M', '2025-07-02 23:05:42.080907'),
('vfdfqk9ntd359majk72jzbfy9mfp6cst', '.eJxVjDsOwjAQBe_iGlnxrn-hpOcM1tpr4wBypDipEHeHSCmgfTPzXiLQttaw9byEicVZoDj9bpHSI7cd8J3abZZpbusyRbkr8qBdXmfOz8vh_h1U6vVb--yKYpWiyqxsMgAJldfWjh51dENxRIYHTWhMRqBiEbw3pA2MCRjF-wPZyTc9:1uWSBN:OdlQOJRZpd6DtaasxkrJhrO98MrjmnujDE36vTw9FXo', '2025-07-01 04:13:21.445354'),
('w90z4wcglcb40s9b41laadcg7ezp803l', '.eJxVjDsOwjAQBe_iGln-JWtT0nMGa9dr4wBypDipEHeHSCmgfTPzXiLitta49bzEicVZaHH63QjTI7cd8B3bbZZpbusykdwVedAurzPn5-Vw_w4q9vqtrQoDK_Kgg_NFa0zJIg8ADNZ5pmRKAAjkDfqxWM3GKhgzGUWcnTHi_QHPrjd1:1uWKrw:y7T1GLVvmYyXwrrZDAzsASIkBkZqmrKMMzqDX5Yf21E', '2025-06-30 20:12:58.467480'),
('xlxehs2newtrv3yfg8izmrfputdgcy8v', '.eJxVjEEOwiAQAP_C2ZCFLi149N43EJZdbNW0SWlPxr8bkh70OjOZt4rp2Kd4VNnizOqqjLr8Mkr5KUsT_EjLfdV5XfZtJt0Sfdqqx5XldTvbv8GU6tS2BMV6RnY2mN6JAUsoyAMy8CBg-w7LkC0ZMEAhOyQTUEIB33lkrz5fx_I3BQ:1uX9fm:4fat9K7OE5mnDY33_zw1yg7Zscnvg28ykn8TwvNgixY', '2025-07-03 02:39:38.038962'),
('yrddv28jhfmz9195eocv8srsr2j9pwpl', '.eJxVjMsKwyAQAP_FcxFdHyE99t5vkNVda9qiEJNT6L8XIYf2OjPMIQLuWwl75zUsJK5Ci8svi5heXIegJ9ZHk6nVbV2iHIk8bZf3Rvy-ne3foGAvY8tWETj2cTaAbkpAU-bEzpBSyYON2Wlllcqz9kZHSxQzeDRgkkdtxecL4Ag3qg:1uX4uy:U_fx5AkJLCj-MFEyYw0bvcwov2ko7KdFySvAov2Cao0', '2025-07-02 21:35:00.779668'),
('zgluupjt6jnqib7nfc7ytf1fchv5oz78', '.eJxVjDsOwjAQBe_iGln-JWtT0nMGa9dr4wBypDipEHeHSCmgfTPzXiLitta49bzEicVZaHH63QjTI7cd8B3bbZZpbusykdwVedAurzPn5-Vw_w4q9vqtrQoDK_Kgg_NFa0zJIg8ADNZ5pmRKAAjkDfqxWM3GKhgzGUWcnTHi_QHPrjd1:1uWP3x:vZDlJyS1VlmbpOAziBpHiexaF9EgijDdHm-7JimfMEg', '2025-07-01 00:53:29.212643'),
('ztsxmfglhtm76m3awjmytmqaqdy2m8pg', '.eJxVjDsOwjAQBe_iGln-JWtT0nMGa9dr4wBypDipEHeHSCmgfTPzXiLitta49bzEicVZaHH63QjTI7cd8B3bbZZpbusykdwVedAurzPn5-Vw_w4q9vqtrQoDK_Kgg_NFa0zJIg8ADNZ5pmRKAAjkDfqxWM3GKhgzGUWcnTHi_QHPrjd1:1uWKsK:xnLDRKPEvyhUmzZyobU3cqRbHz0mvyF8IgvDnqhQoKc', '2025-06-30 20:13:22.882557'),
('zz3888na80hzcm8pn9avqbo6vfa6vis7', 'e30:1uZgim:i_8Y-NTcNBU6g1HoC7B5qFIayrF1y4NlhRVgvRp9AAA', '2025-07-10 02:21:12.414840');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `especialidad`
--

CREATE TABLE `especialidad` (
  `id` bigint NOT NULL,
  `nombre_especialidad` varchar(200) NOT NULL,
  `descripcion` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `especialidad`
--

INSERT INTO `especialidad` (`id`, `nombre_especialidad`, `descripcion`) VALUES
(1, 'Medicina General', 'Medicina General');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado_cita`
--

CREATE TABLE `estado_cita` (
  `id` bigint NOT NULL,
  `nombre_estado` varchar(20) NOT NULL,
  `descripcion` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `lugar_atencion`
--

CREATE TABLE `lugar_atencion` (
  `id` bigint NOT NULL,
  `nombre_lugar` varchar(255) NOT NULL,
  `direccion_lugar` varchar(255) NOT NULL,
  `ciudad_id` varchar(10) DEFAULT NULL,
  `departamento_id` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `lugar_atencion`
--

INSERT INTO `lugar_atencion` (`id`, `nombre_lugar`, `direccion_lugar`, `ciudad_id`, `departamento_id`) VALUES
(1, 'Asistir Salud LTDA', 'Calle 25 #45-99', '25754', '25');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medico`
--

CREATE TABLE `medico` (
  `usuario_ptr_id` bigint NOT NULL,
  `tarjeta_profesional` varchar(15) NOT NULL,
  `especializacion_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `medico`
--

INSERT INTO `medico` (`usuario_ptr_id`, `tarjeta_profesional`, `especializacion_id`) VALUES
(2, '39667727A', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paciente`
--

CREATE TABLE `paciente` (
  `usuario_ptr_id` bigint NOT NULL,
  `tipo_regimen` varchar(20) NOT NULL,
  `ocupacion` varchar(100) NOT NULL,
  `eps` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `paciente`
--

INSERT INTO `paciente` (`usuario_ptr_id`, `tipo_regimen`, `ocupacion`, `eps`) VALUES
(3, 'CONTR', 'Analista de Inventarios', 'SURA'),
(5, 'CONTR', 'Programador', 'FAMISANAR');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `slot_cita`
--

CREATE TABLE `slot_cita` (
  `id` bigint NOT NULL,
  `fecha` date NOT NULL,
  `hora_inicio` time(6) NOT NULL,
  `hora_fin` time(6) NOT NULL,
  `disponible` tinyint(1) NOT NULL,
  `agenda_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` bigint NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `username` varchar(150) NOT NULL,
  `rol` varchar(20) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `tipo_doc` varchar(2) NOT NULL,
  `documento` varchar(10) NOT NULL,
  `genero` varchar(1) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `password` varchar(100) NOT NULL,
  `ciudad_id` varchar(10) DEFAULT NULL,
  `departamento_id` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `last_login`, `is_superuser`, `is_staff`, `is_active`, `date_joined`, `username`, `rol`, `first_name`, `last_name`, `email`, `telefono`, `tipo_doc`, `documento`, `genero`, `fecha_nacimiento`, `direccion`, `imagen`, `password`, `ciudad_id`, `departamento_id`) VALUES
(1, '2025-07-10 06:17:36.068318', 0, 0, 1, '2025-06-30 19:58:50.267473', '1000604018', 'AUX', 'Juan Pablo', 'Cantillo', 'cantillojuanpablo14@gmail.com', '3004372432', 'CC', '1000604018', 'M', '2002-09-14', 'Calle 23 A SUR', '', 'pbkdf2_sha256$1000000$F1wBApFNwGSTMgZkgu9oHU$O+HvEJLr2mbEuQA4bSuLQ06ogQMJ1ZgEX6WxHd85LN0=', '05042', '25'),
(2, '2025-07-10 06:46:02.097602', 0, 0, 1, '2025-06-30 22:13:11.176384', '39667727', 'MED', 'Martha', 'Huerfano', 'mhuerfano@gmail.com', '3058183070', 'CC', '39667727', 'F', '1971-08-29', 'Calle 23 A SUR 15I-40', '', 'pbkdf2_sha256$1000000$qZaPi8MqSu5LpqvzLRltxV$fDhiwdJZ8rpNtsjEYZKASB8LnmbRbeJHbpzLRZc/fUA=', NULL, NULL),
(3, '2025-07-10 06:50:07.910365', 0, 0, 1, '2025-06-30 22:14:12.538726', '91437590', 'PAC', 'Edwin', 'Cantillo', 'edcajican@gmail.com', '3018882327', 'CC', '91437590', 'M', '1971-06-30', 'Calle 23 A SUR', '', 'pbkdf2_sha256$1000000$iVMxvdiLVtkn67loy5eaQD$abjHexqGS4J7yGMtUakWZvoTHZhjqFcy1ClHlnSKW3s=', NULL, NULL),
(4, '2025-07-01 02:25:31.251460', 0, 0, 1, '2025-07-01 02:25:19.849866', '1000604019', 'AUX', 'Kevin', 'Sotelo', 'kev@gmail.com', '3004372431', 'CC', '1000604019', 'M', '2004-08-06', 'Calle 23 A SUR', 'usuario/img/None_8502f933d53e85928d80a057118b23f8.jpg', 'pbkdf2_sha256$1000000$qyw12jyYHEFPoW0r4OwC3T$OsHHYRZSbL2nH4GUSnrVTQyj8bgXaQYzGVPR+NYoMls=', NULL, NULL),
(5, '2025-07-10 03:00:09.932656', 0, 0, 1, '2025-07-10 02:49:11.643636', '1023456789', 'PAC', 'Kevin', 'Sotelo', 'kevindrivertruck@gmail.com', '3004372434', 'CC', '1023456789', 'M', '2004-08-06', 'Calle 23 A SUR', '', 'pbkdf2_sha256$870000$RrUXRAQRHdqwLJM9VScbj4$M06elaItDHZ1nTV+UL4cVSxpWxk3lpiaxlwtNukmH1o=', '25754', '25');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios_groups`
--

CREATE TABLE `usuarios_groups` (
  `id` bigint NOT NULL,
  `usuario_id` bigint NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios_user_permissions`
--

CREATE TABLE `usuarios_user_permissions` (
  `id` bigint NOT NULL,
  `usuario_id` bigint NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `agenda`
--
ALTER TABLE `agenda`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `agenda_medico_id_fecha_inicio_6d1dc6a8_uniq` (`medico_id`,`fecha_inicio`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `aux_admin`
--
ALTER TABLE `aux_admin`
  ADD PRIMARY KEY (`usuario_ptr_id`);

--
-- Indices de la tabla `cita`
--
ALTER TABLE `cita`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `cita_medico_id_fecha_hora_e2c1a4f1_uniq` (`medico_id`,`fecha`,`hora`),
  ADD KEY `cita_paciente_id_3a19100a_fk_usuarios_id` (`paciente_id`),
  ADD KEY `cita_lugar_atencion_id_d39d5b9c` (`lugar_atencion_id`);

--
-- Indices de la tabla `ciudad`
--
ALTER TABLE `ciudad`
  ADD PRIMARY KEY (`codigo_municipio`),
  ADD KEY `ciudad_codigo_departamento__71b269b7_fk_departame` (`codigo_departamento_id`);

--
-- Indices de la tabla `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`codigo_departamento`),
  ADD UNIQUE KEY `nombre_departamento` (`nombre_departamento`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_usuarios_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `especialidad`
--
ALTER TABLE `especialidad`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `estado_cita`
--
ALTER TABLE `estado_cita`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `lugar_atencion`
--
ALTER TABLE `lugar_atencion`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre_lugar` (`nombre_lugar`),
  ADD KEY `lugar_atencion_ciudad_id_8d743901_fk_ciudad_codigo_municipio` (`ciudad_id`),
  ADD KEY `lugar_atencion_departamento_id_98908a70_fk_departame` (`departamento_id`);

--
-- Indices de la tabla `medico`
--
ALTER TABLE `medico`
  ADD PRIMARY KEY (`usuario_ptr_id`),
  ADD UNIQUE KEY `tarjeta_profesional` (`tarjeta_profesional`),
  ADD KEY `medico_especializacion_id_c9f4cc41_fk_especialidad_id` (`especializacion_id`);

--
-- Indices de la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`usuario_ptr_id`);

--
-- Indices de la tabla `slot_cita`
--
ALTER TABLE `slot_cita`
  ADD PRIMARY KEY (`id`),
  ADD KEY `slot_cita_agenda_id_ab70f460_fk_agenda_id` (`agenda_id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `documento` (`documento`),
  ADD KEY `usuarios_ciudad_id_3cc16b6e_fk_ciudad_codigo_municipio` (`ciudad_id`),
  ADD KEY `usuarios_departamento_id_d5efa5ee_fk_departame` (`departamento_id`);

--
-- Indices de la tabla `usuarios_groups`
--
ALTER TABLE `usuarios_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuarios_groups_usuario_id_group_id_a66c5ef3_uniq` (`usuario_id`,`group_id`),
  ADD KEY `usuarios_groups_group_id_18c61092_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `usuarios_user_permissions`
--
ALTER TABLE `usuarios_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuarios_user_permissions_usuario_id_permission_id_474b33a5_uniq` (`usuario_id`,`permission_id`),
  ADD KEY `usuarios_user_permis_permission_id_af615ca1_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `agenda`
--
ALTER TABLE `agenda`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT de la tabla `cita`
--
ALTER TABLE `cita`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `especialidad`
--
ALTER TABLE `especialidad`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `estado_cita`
--
ALTER TABLE `estado_cita`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `lugar_atencion`
--
ALTER TABLE `lugar_atencion`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `slot_cita`
--
ALTER TABLE `slot_cita`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `usuarios_groups`
--
ALTER TABLE `usuarios_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios_user_permissions`
--
ALTER TABLE `usuarios_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `agenda`
--
ALTER TABLE `agenda`
  ADD CONSTRAINT `agenda_medico_id_e6b3cc13_fk_medico_usuario_ptr_id` FOREIGN KEY (`medico_id`) REFERENCES `medico` (`usuario_ptr_id`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `aux_admin`
--
ALTER TABLE `aux_admin`
  ADD CONSTRAINT `aux_admin_usuario_ptr_id_436bf1cf_fk_usuarios_id` FOREIGN KEY (`usuario_ptr_id`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `cita`
--
ALTER TABLE `cita`
  ADD CONSTRAINT `cita_lugar_atencion_id_d39d5b9c_fk_lugar_atencion_id` FOREIGN KEY (`lugar_atencion_id`) REFERENCES `lugar_atencion` (`id`),
  ADD CONSTRAINT `cita_medico_id_2e0b6fbb_fk_usuarios_id` FOREIGN KEY (`medico_id`) REFERENCES `usuarios` (`id`),
  ADD CONSTRAINT `cita_paciente_id_3a19100a_fk_usuarios_id` FOREIGN KEY (`paciente_id`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `ciudad`
--
ALTER TABLE `ciudad`
  ADD CONSTRAINT `ciudad_codigo_departamento__71b269b7_fk_departame` FOREIGN KEY (`codigo_departamento_id`) REFERENCES `departamento` (`codigo_departamento`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_usuarios_id` FOREIGN KEY (`user_id`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `lugar_atencion`
--
ALTER TABLE `lugar_atencion`
  ADD CONSTRAINT `lugar_atencion_ciudad_id_8d743901_fk_ciudad_codigo_municipio` FOREIGN KEY (`ciudad_id`) REFERENCES `ciudad` (`codigo_municipio`),
  ADD CONSTRAINT `lugar_atencion_departamento_id_98908a70_fk_departame` FOREIGN KEY (`departamento_id`) REFERENCES `departamento` (`codigo_departamento`);

--
-- Filtros para la tabla `medico`
--
ALTER TABLE `medico`
  ADD CONSTRAINT `medico_especializacion_id_c9f4cc41_fk_especialidad_id` FOREIGN KEY (`especializacion_id`) REFERENCES `especialidad` (`id`),
  ADD CONSTRAINT `medico_usuario_ptr_id_dc9ade6f_fk_usuarios_id` FOREIGN KEY (`usuario_ptr_id`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD CONSTRAINT `paciente_usuario_ptr_id_d93e58de_fk_usuarios_id` FOREIGN KEY (`usuario_ptr_id`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `slot_cita`
--
ALTER TABLE `slot_cita`
  ADD CONSTRAINT `slot_cita_agenda_id_ab70f460_fk_agenda_id` FOREIGN KEY (`agenda_id`) REFERENCES `agenda` (`id`);

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ciudad_id_3cc16b6e_fk_ciudad_codigo_municipio` FOREIGN KEY (`ciudad_id`) REFERENCES `ciudad` (`codigo_municipio`),
  ADD CONSTRAINT `usuarios_departamento_id_d5efa5ee_fk_departame` FOREIGN KEY (`departamento_id`) REFERENCES `departamento` (`codigo_departamento`);

--
-- Filtros para la tabla `usuarios_groups`
--
ALTER TABLE `usuarios_groups`
  ADD CONSTRAINT `usuarios_groups_group_id_18c61092_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `usuarios_groups_usuario_id_1132ca50_fk_usuarios_id` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `usuarios_user_permissions`
--
ALTER TABLE `usuarios_user_permissions`
  ADD CONSTRAINT `usuarios_user_permis_permission_id_af615ca1_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `usuarios_user_permissions_usuario_id_232fd58d_fk_usuarios_id` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
