CREATE TABLE IF NOT EXISTS `empresa` (
  `cnpj` varchar(80) NOT NULL,
  `nome_empresa` varchar(80) DEFAULT NULL,
  `logradouro` varchar(80) DEFAULT NULL,
  `numero` varchar(80) DEFAULT NULL,
  `complemento` varchar(80) DEFAULT NULL,
  `bairro` varchar(80) DEFAULT NULL,
  `municipio` varchar(80) DEFAULT NULL,
  `uf` varchar(80) DEFAULT NULL,
  `cep` varchar(80) DEFAULT NULL,
  `telefone` varchar(80) DEFAULT NULL,
  `email` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`cnpj`),
  CONSTRAINT `chk_cep` CHECK (cep REGEXP '^[0-9]{8}$'),
  CONSTRAINT `chk_cnpj` CHECK (cnpj REGEXP '^[0-9]{14}$'),
  CONSTRAINT `chk_uf` CHECK (uf REGEXP '^[A-Z]{2}$')
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
