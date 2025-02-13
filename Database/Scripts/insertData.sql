-- Início da transação
BEGIN;

-----------------------------------------------------------
-- 1. Inserções nas tabelas de apoio
-----------------------------------------------------------

-- Tipo_Usuario
INSERT INTO Tipo_Usuario (id_tipo_usuario, descricao) VALUES
(1, 'ADMIN'),
(2, 'APOSTADOR'),
(3, 'FISCAL'),
(4, 'VISITANTE'),
(5, 'CONVIDADO');

-- Tipo_Notificacao
INSERT INTO Tipo_Notificacao (id_tipo_notificacao, descricao) VALUES
(1, 'PARTIDA_QUASE_INICIANDO'),
(2, 'PARTIDA_INICIADA'),
(3, 'PARTIDA_ENCERRADA'),
(4, 'VOCE_GANHOU'),
(5, 'VOCE_PERDEU'),
(6, 'MUDANCA_ODDS'),
(7, 'BEM_VINDO'),
(8, 'VOCE_RECEBEU_BONUS');

-- Status_Carteira
INSERT INTO Status_Carteira (id_status_carteira, descricao) VALUES
(1, 'ATIVO'),
(2, 'INATIVO'),
(3, 'SUSPENSO'),
(4, 'BLOQUEADO'),
(5, 'PENDENTE');

-- Tipo_Transacao
INSERT INTO Tipo_Transacao (id_tipo_transacao, descricao) VALUES
(1, 'PAGAMENTO'),
(2, 'DEPOSITO'),
(3, 'RETIRADA'),
(4, 'BONUS'),
(5, 'REEMBOLSO'),
(6, 'APOSTA'),
(7, 'AUMENTO_APOSTA'),
(8, 'REDUCAO_APOSTA');

-- Tipo_Competicao
INSERT INTO Tipo_Competicao (id_tipo_competicao, descricao) VALUES
(1, 'CAMPEONATO'),
(2, 'TORNEIO'),
(3, 'COPA'),
(4, 'LIGA'),
(5, 'AMISTOSO');

-- Tipo_Partida
INSERT INTO Tipo_Partida (id_tipo_partida, descricao) VALUES
(1, 'REGULAR'),
(2, 'AMISTOSO'),
(3, 'ELIMINATORIA'),
(4, 'FINAL'),
(5, 'SEMIFINAL');

-- Status_Partida
INSERT INTO Status_Partida (id_status_partida, descricao) VALUES
(1, 'Agendada'),
(2, 'Em andamento'),
(3, 'Encerrada'),
(4, 'Cancelada'),
(5, 'Adiada');

-- Status_Resultado_Aposta
INSERT INTO Status_Resultado_Aposta (id_status_resultado_aposta, descricao) VALUES
(1, 'GANHO'),
(2, 'PERDA'),
(3, 'REEMBOLSADO'),
(4, 'CANCELADO'),
(5, 'AGUARDANDO_RESULTADO');


-----------------------------------------------------------
-- 2. Inserções nas tabelas principais
-----------------------------------------------------------

-- Usuario
INSERT INTO Usuario (id_usuario, nome, cpf, email, senha, id_tipo_usuario, status, dt_nascimento)
VALUES
(1, 'Alice Silva', '12345678901', 'alice@example.com', 'senha123', 2, 'ativo', '1990-01-01'),
(2, 'Bruno Souza', '23456789012', 'bruno@example.com', 'senha123', 2, 'ativo', '1985-05-15'),
(3, 'Carla Mendes', '34567890123', 'carla@example.com', 'senha123', 2, 'ativo', '1992-08-20'),
(4, 'Daniela Lima', '45678901234', 'daniela@example.com', 'senha123', 2, 'ativo', '1988-12-10'),
(5, 'Eduardo Costa', '56789012345', 'eduardo@example.com', 'senha123', 2, 'ativo', '1995-07-07'),
(6, 'Adm Master', '67890123456', 'adm@example.com', 'senha123', 1, 'ativo', '1981-01-01'),
(7, 'Fiscal das Bets', '78901234567', 'fiscal@example.com', 'senha123', 3, 'ativo', '1982-02-02'),
(8, 'Visitante das Bets', '89012345678', 'visitante@example.com', 'senha123', 4, 'ativo', '1983-03-03'),
(9, 'Convidado das Bets', '90123456789', 'convidado@example.com', 'senha123', 5, 'ativo', '1984-04-04'),
(10, 'Jose da Silva', '01234567890', 'joseSilva@example.com', 'senha123', 2, 'ativo', '1994-04-04');

-- Login
INSERT INTO Login (id_login, id_usuario, dt_hora_login, endereco_ip, sucesso)
VALUES
(1, 1, CURRENT_TIMESTAMP, '192.168.1.1', TRUE),
(2, 2, CURRENT_TIMESTAMP, '192.168.1.2', TRUE),
(3, 3, CURRENT_TIMESTAMP, '192.168.1.3', FALSE),
(4, 4, CURRENT_TIMESTAMP, '192.168.1.4', TRUE),
(5, 5, CURRENT_TIMESTAMP, '192.168.1.5', TRUE);

-- Notificacao
INSERT INTO Notificacao (id_usuario, id_tipo_notificacao, titulo, conteudo, status_leitura)
VALUES
(1, 1, 'Alerta de Partida', 'A partida está prestes a começar.', FALSE),
(2, 1, 'Início da Partida', 'A partida começou.', TRUE),
(3, 1, 'Fim da Partida', 'A partida terminou com resultados.', FALSE),
(4, 2, 'Parabéns!', 'Você ganhou a aposta!', FALSE),
(5, 2, 'Atenção!', 'Você perdeu a aposta.', TRUE);

-- Arquivo
INSERT INTO Arquivo (id_arquivo, id_usuario, nome, descricao, mime_type, size_mb, binary_data)
VALUES
(1, 1, 'arquivo1.pdf', 'Documento PDF exemplo.', 'application/pdf', 0.50, '\\xdeadbeef'),
(2, 2, 'imagem1.jpg', 'Imagem de exemplo.', 'image/jpeg', 1.25, '\\xdeadbeef'),
(3, 3, 'audio1.mp3', 'Arquivo de áudio.', 'audio/mpeg', 3.40, '\\xdeadbeef'),
(4, 4, 'video1.mp4', 'Arquivo de vídeo.', 'video/mp4', 10.00, '\\xdeadbeef'),
(5, 5, 'documento1.docx', 'Documento Word exemplo.', 'application/document', 0.75, '\\xdeadbeef');

-- Carteira
INSERT INTO Carteira (id_carteira, id_usuario, tipo, saldo, id_status_carteira)
VALUES
(1, 1, 'principal', 100.00, 1),
(2, 2, 'principal', 200.00, 1),
(3, 3, 'principal', 300.00, 1),
(4, 4, 'principal', 400.00, 1),
(5, 5, 'principal', 500.00, 1);

-- Transacao
INSERT INTO Transacao (id_transacao, id_carteira, id_tipo_transacao, valor, descricao)
VALUES
(1, 1, 1, 50.00, 'Pagamento realizado.'),
(2, 2, 2, 150.00, 'Depósito efetuado.'),
(3, 3, 3, 70.00, 'Retirada solicitada.'),
(4, 4, 4, 30.00, 'Bônus concedido.'),
(5, 5, 5, 20.00, 'Reembolso processado.');

-- Competicao
INSERT INTO Competicao (id_competicao, nome, organizacao, id_tipo_competicao)
VALUES
(1, 'Campeonato Brasileiro', 'CBF', 1),
(2, 'Mundial de Clubes', 'FIFA', 2),
(3, 'Copa do Mundo', 'FIFA', 3),
(4, 'Liga dos Campeões', 'UEFA', 4),
(5, 'Amistosos Regionais', 'Confederação Regional', 5);

-- Equipe (Clubes do Brasileirão Série A)
INSERT INTO Equipe (id_equipe, nome, pais)
VALUES
(1, 'Flamengo', 'Brasil'),
(2, 'Palmeiras', 'Brasil'),
(3, 'São Paulo', 'Brasil'),
(4, 'Corinthians', 'Brasil'),
(5, 'Atlético Mineiro', 'Brasil'),
(6, 'Internacional', 'Brasil'),
(7, 'Grêmio', 'Brasil'),
(8, 'Fluminense', 'Brasil'),
(9, 'Botafogo', 'Brasil'),
(10, 'Cruzeiro', 'Brasil');

-- Partida
INSERT INTO Partida (id_partida, id_competicao, id_time_mandante, id_time_visitante, estadio, dt_hora_inicio, id_tipo_partida, id_status_partida)
VALUES
-- Partida 1
(1, 1, 1, 2, 'Maracanã', '2025-03-01 15:00:00', 1, 1),
-- Partida 2
(2, 2, 2, 3, 'Camp Nou', '2025-03-02 16:00:00', 1, 1),
-- Partida 3
(3, 3, 3, 4, 'Wembley', '2025-03-03 17:00:00', 1, 1),
-- Partida 4
(4, 4, 4, 5, 'Santiago Bernabéu', '2025-03-04 18:00:00', 1, 1),
-- Partida 5
(5, 5, 5, 1, 'San Siro', '2025-03-05 19:00:00', 1, 1),
-- Partida 6
(6, 1, 6, 7, 'Mineirão', '2025-03-06 20:00:00', 1, 1),
-- Partida 7
(7, 3, 8, 9, 'Estádio do Maracanã', '2025-03-07 21:00:00', 1, 1);

-- Resultados das Partidas
INSERT INTO Resultado_Partida_Equipe (id_resultado, id_partida, id_equipe, gols_marcados, gols_sofridos, cartoes_amarelos, cartoes_vermelhos, escanteios, impedimentos, faltas_cometidas)
VALUES
-- Partida 1
(1, 1, 1, 2, 1, 1, 0, 3, 0, 10),  -- Time 1
(2, 1, 2, 1, 2, 2, 0, 2, 1, 12),  -- Time 2
-- Partida 2
(3, 2, 2, 0, 0, 2, 1, 4, 1, 12),  -- Time 2
(4, 2, 3, 0, 0, 1, 0, 3, 0, 9),   -- Time 3
-- Partida 3
(5, 3, 3, 3, 2, 0, 0, 5, 0, 8),   -- Time 3
(6, 3, 4, 2, 3, 1, 1, 4, 1, 11),  -- Time 4
-- Partida 4
(7, 4, 4, 1, 1, 1, 1, 2, 0, 9),   -- Time 4
(8, 4, 5, 1, 1, 2, 0, 3, 0, 10),  -- Time 5
-- Partida 5
(9, 5, 5, 0, 1, 0, 0, 3, 0, 7),   -- Time 5
(10, 5, 1, 1, 0, 1, 0, 4, 1, 8),  -- Time 1
-- Partida 6
(11, 6, 6, 2, 1, 1, 0, 3, 0, 10), -- Time 6
(12, 6, 7, 1, 2, 2, 0, 2, 1, 12), -- Time 7
-- Partida 7
(13, 7, 8, 3, 0, 1, 0, 4, 0, 8),  -- Time 8
(14, 7, 9, 0, 3, 2, 1, 3, 0, 10);  -- Time 9

-- Inserção de Mercado_Aposta (já definidos os 6 tipos)
INSERT INTO Mercado_Aposta (id_mercado, tipo_aposta, descricao)
VALUES
(1, 'Total de Gols', 'Aposta no total de gols marcados.'),
(2, 'Escanteios', 'Aposta no número total de escanteios.'),
(3, 'Número de Cartões Amarelos', 'Aposta no total de cartões amarelos na partida.'),
(4, 'Número de Cartões Vermelhos', 'Aposta no total de cartões vermelhos na partida.'),
(5, 'Número de Impedimentos', 'Aposta na quantidade de impedimentos na partida.'),
(6, 'Quantidade de Faltas', 'Aposta na quantidade total de faltas cometidas na partida.');

-- Inserção de Odds para cada partida (todos os 6 mercados)

-- Partida 1: odds de id 1 a 6
INSERT INTO Odd (id_odd, id_partida, id_mercado, valor, descricao)
VALUES
(1, 1, 1, 1.50, 'Odd para Total de Gols'),
(2, 1, 2, 2.75, 'Odd para Escanteios'),
(3, 1, 3, 1.95, 'Odd para Número de Cartões Amarelos'),
(4, 1, 4, 2.10, 'Odd para Número de Cartões Vermelhos'),
(5, 1, 5, 2.50, 'Odd para Número de Impedimentos'),
(6, 1, 6, 2.80, 'Odd para Quantidade de Faltas');

-- Partida 2: odds de id 7 a 12
INSERT INTO Odd (id_odd, id_partida, id_mercado, valor, descricao)
VALUES
(7, 2, 1, 1.55, 'Odd para Total de Gols'),
(8, 2, 2, 2.80, 'Odd para Escanteios'),
(9, 2, 3, 2.00, 'Odd para Número de Cartões Amarelos'),
(10, 2, 4, 2.15, 'Odd para Número de Cartões Vermelhos'),
(11, 2, 5, 2.55, 'Odd para Número de Impedimentos'),
(12, 2, 6, 2.90, 'Odd para Quantidade de Faltas');

-- Partida 3: odds de id 13 a 18
INSERT INTO Odd (id_odd, id_partida, id_mercado, valor, descricao)
VALUES
(13, 3, 1, 1.60, 'Odd para Total de Gols'),
(14, 3, 2, 2.85, 'Odd para Escanteios'),
(15, 3, 3, 2.05, 'Odd para Número de Cartões Amarelos'),
(16, 3, 4, 2.20, 'Odd para Número de Cartões Vermelhos'),
(17, 3, 5, 2.60, 'Odd para Número de Impedimentos'),
(18, 3, 6, 2.95, 'Odd para Quantidade de Faltas');

-- Partida 4: odds de id 19 a 24
INSERT INTO Odd (id_odd, id_partida, id_mercado, valor, descricao)
VALUES
(19, 4, 1, 1.65, 'Odd para Total de Gols'),
(20, 4, 2, 2.90, 'Odd para Escanteios'),
(21, 4, 3, 2.10, 'Odd para Número de Cartões Amarelos'),
(22, 4, 4, 2.25, 'Odd para Número de Cartões Vermelhos'),
(23, 4, 5, 2.65, 'Odd para Número de Impedimentos'),
(24, 4, 6, 3.00, 'Odd para Quantidade de Faltas');

-- Partida 5: odds de id 25 a 30
INSERT INTO Odd (id_odd, id_partida, id_mercado, valor, descricao)
VALUES
(25, 5, 1, 1.70, 'Odd para Total de Gols'),
(26, 5, 2, 2.95, 'Odd para Escanteios'),
(27, 5, 3, 2.15, 'Odd para Número de Cartões Amarelos'),
(28, 5, 4, 2.30, 'Odd para Número de Cartões Vermelhos'),
(29, 5, 5, 2.70, 'Odd para Número de Impedimentos'),
(30, 5, 6, 3.05, 'Odd para Quantidade de Faltas');

-- Partida 6: odds de id 31 a 36
INSERT INTO Odd (id_odd, id_partida, id_mercado, valor, descricao)
VALUES
(31, 6, 1, 1.80, 'Odd para Total de Gols'),
(32, 6, 2, 3.00, 'Odd para Escanteios'),
(33, 6, 3, 2.20, 'Odd para Número de Cartões Amarelos'),
(34, 6, 4, 2.35, 'Odd para Número de Cartões Vermelhos'),
(35, 6, 5, 2.75, 'Odd para Número de Impedimentos'),
(36, 6, 6, 3.10, 'Odd para Quantidade de Faltas');

-- Partida 7: odds de id 37 a 42
INSERT INTO Odd (id_odd, id_partida, id_mercado, valor, descricao)
VALUES
(37, 7, 1, 1.75, 'Odd para Total de Gols'),
(38, 7, 2, 2.85, 'Odd para Escanteios'),
(39, 7, 3, 2.25, 'Odd para Número de Cartões Amarelos'),
(40, 7, 4, 2.40, 'Odd para Número de Cartões Vermelhos'),
(41, 7, 5, 2.80, 'Odd para Número de Impedimentos'),
(42, 7, 6, 3.15, 'Odd para Quantidade de Faltas');

INSERT INTO Aposta (id_aposta, id_usuario, id_odd, valor, resultado, status)
VALUES
(1, 1, 1, 50.00, 3, 'ativa'),
(2, 2, 7, 75.00, 8, 'ativa'),
(3, 3, 13, 100.00, 5, 'ativa'),
(4, 4, 4, 125.00, 2, 'ativa'),
(5, 5, 10, 150.00, 12, 'ativa'),
(6, 6, 19, 60.00, 4, 'ativa'),
(7, 7, 25, 85.00, 7, 'ativa'),
(8, 8, 31, 95.00, 3, 'ativa'),
(9, 9, 37, 120.00, 10, 'ativa'),
(10, 10, 42, 130.00, 8, 'ativa');

-- Resultado_Aposta
INSERT INTO Resultado_Aposta (id_resultado_aposta, id_aposta, valor_recebido, id_status_resultado_aposta)
VALUES
(1, 1, 100.00, 1),
(2, 2, 0.00, 2),
(3, 3, 50.00, 3),
(4, 4, 0.00, 4),
(5, 5, 75.00, 5),
(6, 6, 120.00, 1),
(7, 7, 0.00, 2),
(8, 8, 50.00, 3),
(9, 9, 100.00, 4),
(10, 10, 65.00, 5);

-- Fim da transação
COMMIT;

-- ROLLBACK;

-- Atualização das sequências para evitar duplicidade de chaves devido a inserção manual
SELECT setval('tipo_usuario_id_tipo_usuario_seq', (SELECT MAX(id_tipo_usuario) FROM Tipo_Usuario));
SELECT setval('tipo_notificacao_id_tipo_notificacao_seq', (SELECT MAX(id_tipo_notificacao) FROM Tipo_Notificacao));
SELECT setval('status_carteira_id_status_carteira_seq', (SELECT MAX(id_status_carteira) FROM Status_Carteira));
SELECT setval('tipo_transacao_id_tipo_transacao_seq', (SELECT MAX(id_tipo_transacao) FROM Tipo_Transacao));
SELECT setval('tipo_competicao_id_tipo_competicao_seq', (SELECT MAX(id_tipo_competicao) FROM Tipo_Competicao));
SELECT setval('tipo_partida_id_tipo_partida_seq', (SELECT MAX(id_tipo_partida) FROM Tipo_Partida));
SELECT setval('status_partida_id_status_partida_seq', (SELECT MAX(id_status_partida) FROM Status_Partida));
SELECT setval('status_resultado_aposta_id_status_resultado_aposta_seq', (SELECT MAX(id_status_resultado_aposta) FROM Status_Resultado_Aposta));
SELECT setval('usuario_id_usuario_seq', (SELECT MAX(id_usuario) FROM Usuario));
SELECT setval('login_id_login_seq', (SELECT MAX(id_login) FROM Login));
SELECT setval('notificacao_id_notificacao_seq', (SELECT MAX(id_notificacao) FROM Notificacao));
SELECT setval('arquivo_id_arquivo_seq', (SELECT MAX(id_arquivo) FROM Arquivo));
SELECT setval('carteira_id_carteira_seq', (SELECT MAX(id_carteira) FROM Carteira));
SELECT setval('transacao_id_transacao_seq', (SELECT MAX(id_transacao) FROM Transacao));
SELECT setval('competicao_id_competicao_seq', (SELECT MAX(id_competicao) FROM Competicao));
SELECT setval('equipe_id_equipe_seq', (SELECT MAX(id_equipe) FROM Equipe));
SELECT setval('partida_id_partida_seq', (SELECT MAX(id_partida) FROM Partida));
SELECT setval('resultado_partida_equipe_id_resultado_seq', (SELECT MAX(id_resultado) FROM Resultado_Partida_Equipe));
SELECT setval('mercado_aposta_id_mercado_seq', (SELECT MAX(id_mercado) FROM Mercado_Aposta));
SELECT setval('odd_id_odd_seq', (SELECT MAX(id_odd) FROM Odd));
SELECT setval('aposta_id_aposta_seq', (SELECT MAX(id_aposta) FROM Aposta));
SELECT setval('resultado_aposta_id_resultado_aposta_seq', (SELECT MAX(id_resultado_aposta) FROM Resultado_Aposta));
