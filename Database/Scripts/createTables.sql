-- Criação do banco de dados
-- CREATE DATABASE sistema_apostas;

-- Conectando ao banco de dados criado
-- \c sistema_apostas;

-- Script para limpar as tabelas antes de criar novamente (removendo dependências)
DROP TABLE IF EXISTS Resultado_Aposta CASCADE;
DROP TABLE IF EXISTS Aposta CASCADE;
DROP TABLE IF EXISTS Odd CASCADE;
DROP TABLE IF EXISTS Mercado_Aposta CASCADE;
DROP TABLE IF EXISTS Resultado_Partida_Equipe CASCADE;
DROP TABLE IF EXISTS Partida CASCADE;
DROP TABLE IF EXISTS Competicao CASCADE;
DROP TABLE IF EXISTS Equipe CASCADE;
DROP TABLE IF EXISTS Transacao CASCADE;
DROP TABLE IF EXISTS Carteira CASCADE;
DROP TABLE IF EXISTS Arquivo CASCADE;
DROP TABLE IF EXISTS Notificacao CASCADE;
DROP TABLE IF EXISTS Notificacao_Lote CASCADE;
DROP TABLE IF EXISTS Login CASCADE;
DROP TABLE IF EXISTS Usuario CASCADE;
DROP TABLE IF EXISTS Tipo_Usuario CASCADE;
DROP TABLE IF EXISTS Tipo_Notificacao CASCADE;
DROP TABLE IF EXISTS Status_Carteira CASCADE;
DROP TABLE IF EXISTS Tipo_Transacao CASCADE;
DROP TABLE IF EXISTS Tipo_Competicao CASCADE;
DROP TABLE IF EXISTS Tipo_Partida CASCADE;
DROP TABLE IF EXISTS Status_Resultado_Aposta CASCADE;

-- Criação da tabela de apoio Tipo_Usuario
CREATE TABLE Tipo_Usuario (
    id_tipo_usuario SERIAL PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL
);

-- Criação da tabela de apoio Tipo_Notificacao
CREATE TABLE Tipo_Notificacao (
    id_tipo_notificacao SERIAL PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL
);

-- Criação da tabela de apoio Status_Carteira
CREATE TABLE Status_Carteira (
    id_status_carteira SERIAL PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL
);

-- Criação da tabela de apoio Tipo_Transacao
CREATE TABLE Tipo_Transacao (
    id_tipo_transacao SERIAL PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL
);

-- Criação da tabela de apoio Tipo_Competicao
CREATE TABLE Tipo_Competicao (
    id_tipo_competicao SERIAL PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL
);

-- Criação da tabela de apoio Tipo_Partida
CREATE TABLE Tipo_Partida (
    id_tipo_partida SERIAL PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL
);

-- Criação da tabela de apoio Status_Resultado_Aposta
CREATE TABLE Status_Resultado_Aposta (
    id_status_resultado_aposta SERIAL PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL
);

-- Criação da tabela Usuario
CREATE TABLE Usuario (
    id_usuario SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    id_tipo_usuario INT REFERENCES Tipo_Usuario(id_tipo_usuario) ON DELETE CASCADE,
    status VARCHAR(20) DEFAULT 'ativo' CHECK (status IN ('ativo', 'inativo')),
    dt_nascimento DATE,
    dt_hora_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela Login
CREATE TABLE Login (
    id_login SERIAL PRIMARY KEY,
    id_usuario INT REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
    dt_hora_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    endereco_ip VARCHAR(45),
    sucesso BOOLEAN
);

-- Criação da tabela Notificacao_Lote
CREATE TABLE Notificacao_Lote (
    id_notificacao_lote SERIAL PRIMARY KEY,
    id_tipo_notificacao INT REFERENCES Tipo_Notificacao(id_tipo_notificacao) ON DELETE CASCADE,
    titulo VARCHAR(100) NOT NULL,
    conteudo TEXT NOT NULL,
    dt_hora_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela Notificacao
CREATE TABLE Notificacao (
    id_notificacao SERIAL PRIMARY KEY,
    id_notificacao_lote INT REFERENCES Notificacao_Lote(id_notificacao_lote) ON DELETE CASCADE,
    id_usuario INT REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
    status_leitura BOOLEAN DEFAULT FALSE,
    dt_hora_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela Arquivo
CREATE TABLE Arquivo (
    id_arquivo SERIAL PRIMARY KEY,
    id_usuario INT REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
    nome VARCHAR(255),
    descricao TEXT,
    mime_type VARCHAR(50),
    size_mb DECIMAL(10, 2),
    binary_data BYTEA,
    dt_hora_upload TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela Carteira
CREATE TABLE Carteira (
    id_carteira SERIAL PRIMARY KEY,
    id_usuario INT REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
    tipo VARCHAR(20) DEFAULT 'principal',
    saldo DECIMAL(12, 2) DEFAULT 0.00,
    id_status_carteira INT REFERENCES Status_Carteira(id_status_carteira) ON DELETE CASCADE,
    dt_hora_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    dt_hora_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela Transacao
CREATE TABLE Transacao (
    id_transacao SERIAL PRIMARY KEY,
    id_carteira INT REFERENCES Carteira(id_carteira) ON DELETE CASCADE,
    id_tipo_transacao INT REFERENCES Tipo_Transacao(id_tipo_transacao) ON DELETE CASCADE,
    valor DECIMAL(12, 2) NOT NULL,
    descricao TEXT,
    dt_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela Competicao
CREATE TABLE Competicao (
    id_competicao SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    organizacao VARCHAR(100),
    id_tipo_competicao INT REFERENCES Tipo_Competicao(id_tipo_competicao) ON DELETE CASCADE
);

-- Criação da tabela Equipe
CREATE TABLE Equipe (
    id_equipe SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    pais VARCHAR(50)
);

-- Criação da tabela Partida
CREATE TABLE Partida (
    id_partida SERIAL PRIMARY KEY,
    id_competicao INT REFERENCES Competicao(id_competicao) ON DELETE CASCADE,
    id_time_mandante INT REFERENCES Equipe(id_equipe) ON DELETE CASCADE,
    id_time_visitante INT REFERENCES Equipe(id_equipe) ON DELETE CASCADE,
    estadio VARCHAR(100),
    dt_hora_inicio TIMESTAMP,
    id_tipo_partida INT REFERENCES Tipo_Partida(id_tipo_partida) ON DELETE CASCADE,
    status VARCHAR(20) DEFAULT 'agendada'
);

-- Criação da tabela Resultado_Partida_Equipe
CREATE TABLE Resultado_Partida_Equipe (
    id_resultado SERIAL PRIMARY KEY,
    id_partida INT REFERENCES Partida(id_partida) ON DELETE CASCADE,
    id_equipe INT REFERENCES Equipe(id_equipe) ON DELETE CASCADE,
    gols_marcados INT DEFAULT 0,
    gols_sofridos INT DEFAULT 0,
    cartoes_amarelos INT DEFAULT 0,
    cartoes_vermelhos INT DEFAULT 0,
    escanteios INT DEFAULT 0,
    impedimentos INT DEFAULT 0,
    faltas_cometidas INT DEFAULT 0
);

-- Criação da tabela Mercado_Aposta
CREATE TABLE Mercado_Aposta (
    id_mercado SERIAL PRIMARY KEY,
    tipo_aposta VARCHAR(50) NOT NULL,
    descricao TEXT
);

-- Criação da tabela Odd
CREATE TABLE Odd (
    id_odd SERIAL PRIMARY KEY,
    id_partida INT REFERENCES Partida(id_partida) ON DELETE CASCADE,
    id_mercado INT REFERENCES Mercado_Aposta(id_mercado) ON DELETE CASCADE,
    valor DECIMAL(5, 2) NOT NULL,
    descricao VARCHAR(255),
    dt_hora_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    dt_hora_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela Aposta
CREATE TABLE Aposta (
    id_aposta SERIAL PRIMARY KEY,
    id_usuario INT REFERENCES Usuario(id_usuario) ON DELETE CASCADE,
    id_odd INT REFERENCES Odd(id_odd) ON DELETE CASCADE,
    valor DECIMAL(12, 2) NOT NULL,
    status VARCHAR(20) DEFAULT 'ativa' CHECK (status IN ('ativa', 'inativa')),
    dt_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela Resultado_Aposta
CREATE TABLE Resultado_Aposta (
    id_resultado_aposta SERIAL PRIMARY KEY,
    id_aposta INT REFERENCES Aposta(id_aposta) ON DELETE CASCADE,
    valor_recebido DECIMAL(12, 2) DEFAULT 0.00,
    id_status_resultado_aposta INT REFERENCES Status_Resultado_Aposta(id_status_resultado_aposta) ON DELETE CASCADE,
    dt_hora_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);