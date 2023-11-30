CREATE TABLE IF NOT EXISTS produtos(
    codigo INT(4) UNSIGNED ZEROFILL NOT NULL,
    nome CHAR(50),
    estoque INT NOT NULL,
    valor FLOAT,
    id_categoria tinyint NULL,
    PRIMARY KEY(codigo)
);

CREATE TABLE IF NOT EXISTS categorias(
    id tinyint NOT NULL,
    nome CHAR(50) NOT NULL,
    descricao VARCHAR(200),
    PRIMARY KEY(id)
);

ALTER TABLE produtos ADD FOREIGN KEY(id_categoria)REFERENCES categorias(id);