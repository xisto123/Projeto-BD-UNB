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
(5, 'REEMBOLSO');

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
(5, 'Adiantada');

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
(9, 'Convidado das Bets', '90123456789', 'convidado@example.com', 'senha123', 5, 'ativo', '1984-04-04');

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

-- Equipe (Clubes do Brasileirão Série A e Seleções Campeãs da Copa do Mundo)
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
(10, 'Cruzeiro', 'Brasil'),
(11, 'Seleção Brasileira', 'Brasil'),
(12, 'Seleção Argentina', 'Argentina'),
(13, 'Seleção Alemã', 'Alemanha'),
(14, 'Seleção Espanhola', 'Espanha'),
(15, 'Seleção Italiana', 'Itália'),
(16, 'Seleção Francesa', 'França'),
(17, 'Seleção Inglesa', 'Inglaterra'),
(18, 'Seleção Uruguaia', 'Uruguai');

-- Partida
INSERT INTO Partida (id_partida, id_competicao, id_time_mandante, id_time_visitante, estadio, dt_hora_inicio, id_tipo_partida, id_status_partida)
VALUES
(1, 1, 1, 2, 'Maracanã', '2025-03-01 15:00:00', 1, 1),
(2, 2, 2, 3, 'Camp Nou', '2025-03-02 16:00:00', 1, 1),
(3, 3, 3, 4, 'Wembley', '2025-03-03 17:00:00', 1, 1),
(4, 4, 4, 5, 'Santiago Bernabéu', '2025-03-04 18:00:00', 1, 1),
(5, 5, 5, 1, 'San Siro', '2025-03-05 19:00:00', 1, 1);

-- Resultado_Partida_Equipe
INSERT INTO Resultado_Partida_Equipe (id_resultado, id_partida, id_equipe, gols_marcados, gols_sofridos, cartoes_amarelos, cartoes_vermelhos, escanteios, impedimentos, faltas_cometidas)
VALUES
(1, 1, 1, 2, 1, 1, 0, 3, 0, 10), -- Partida 1, Time 1
(2, 1, 2, 1, 2, 2, 0, 2, 1, 12), -- Partida 1, Time 2
(3, 2, 2, 0, 0, 2, 1, 4, 1, 12), -- Partida 2, Time 2
(4, 2, 3, 0, 0, 1, 0, 3, 0, 9),  -- Partida 2, Time 3
(5, 3, 3, 3, 2, 0, 0, 5, 0, 8),  -- Partida 3, Time 3
(6, 3, 4, 2, 3, 1, 1, 4, 1, 11), -- Partida 3, Time 4
(7, 4, 4, 1, 1, 1, 1, 2, 0, 9),  -- Partida 4, Time 4
(8, 4, 5, 1, 1, 2, 0, 3, 0, 10), -- Partida 4, Time 5
(9, 5, 5, 0, 1, 0, 0, 3, 0, 7),  -- Partida 5, Time 5
(10, 5, 1, 1, 0, 1, 0, 4, 1, 8); -- Partida 5, Time 1

INSERT INTO Mercado_Aposta (id_mercado, tipo_aposta, descricao)
VALUES
(1, 'Total de Gols', 'Aposta no total de gols marcados.'),
(2, 'Escanteios', 'Aposta no número total de escanteios.'),
(3, 'Número de Cartões Amarelos', 'Aposta no total de cartões amarelos/ na partida.'),
(4, 'Número de Cartões Vermelhos', 'Aposta no total de cartões vermelhos na partida.'),
(5, 'Número de Impedimentos', 'Aposta na quantidade de impedimentos na partida.'),
(6, 'Quantidade de Faltas', 'Aposta na quantidade total de faltas cometidas na partida.');

-- Odd
-- Para cada partida, inserimos 5 registros (um para cada mercado)
-- Partida 1 (id_partida = 1)
INSERT INTO Odd (id_odd, id_partida, id_mercado, valor, descricao)
VALUES
(1, 1, 1, 1.50, 'Odd para Total de Gols'),
(2, 1, 2, 2.75, 'Odd para Escanteios'),
(3, 1, 3, 1.95, 'Odd para Número de Cartões'),
(4, 1, 4, 2.10, 'Odd para Gols no Primeiro Tempo'),
(5, 1, 5, 2.50, 'Odd para Quantidade de Faltas');

-- Partida 2 (id_partida = 2)
INSERT INTO Odd (id_odd, id_partida, id_mercado, valor, descricao)
VALUES
(6, 2, 1, 1.55, 'Odd para Total de Gols'),
(7, 2, 2, 2.80, 'Odd para Escanteios'),
(8, 2, 3, 2.00, 'Odd para Número de Cartões'),
(9, 2, 4, 2.15, 'Odd para Gols no Primeiro Tempo'),
(10, 2, 5, 2.55, 'Odd para Quantidade de Faltas');

-- Partida 3 (id_partida = 3)
INSERT INTO Odd (id_odd, id_partida, id_mercado, valor, descricao)
VALUES
(11, 3, 1, 1.60, 'Odd para Total de Gols'),
(12, 3, 2, 2.85, 'Odd para Escanteios'),
(13, 3, 3, 2.05, 'Odd para Número de Cartões'),
(14, 3, 4, 2.20, 'Odd para Gols no Primeiro Tempo'),
(15, 3, 5, 2.60, 'Odd para Quantidade de Faltas');

INSERT INTO Aposta (id_aposta, id_usuario, id_odd, valor, resultado, status)
VALUES
(1, 1, 1, 50.00, 3, 'ativa'),
(2, 2, 7, 75.00, 8, 'ativa'),
(3, 3, 13, 100.00, 5, 'ativa'),
(4, 4, 4, 125.00, 2, 'ativa'),
(5, 5, 10, 150.00, 12, 'ativa');

-- Resultado_Aposta
INSERT INTO Resultado_Aposta (id_resultado_aposta, id_aposta, valor_recebido, id_status_resultado_aposta)
VALUES
(1, 1, 100.00, 1),
(2, 2, 0.00, 2),
(3, 3, 50.00, 3),
(4, 4, 0.00, 4),
(5, 5, 75.00, 5);

-- Fim da transação
COMMIT;

-- ROLLBACK;
