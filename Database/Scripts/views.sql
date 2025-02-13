-- Início da transação
BEGIN;

-- Dropar as views caso existam
DROP VIEW IF EXISTS vw_historico_apostas CASCADE;
DROP VIEW IF EXISTS vw_resumo_financeiro CASCADE;
DROP VIEW IF EXISTS vw_detalhes_times CASCADE;
DROP VIEW IF EXISTS vw_apostas_em_andamento CASCADE;

-- Criar a view: Histórico de Apostas do Usuário
CREATE OR REPLACE VIEW vw_historico_apostas AS
SELECT
  u.id_usuario         AS "ID Usuário",
  u.nome               AS "Nome do Usuário",
  a.id_aposta          AS "ID Aposta",
  a.valor              AS "Valor Apostado",
  a.resultado          AS "Resultado Previsto",
  a.status             AS "Status da Aposta",
  o.valor              AS "Odd",
  o.descricao          AS "Descrição da Odd",
  p.estadio            AS "Estádio",
  p.dt_hora_inicio     AS "Data/Hora da Partida",
  comp.nome            AS "Competição",
  COALESCE(ra.valor_recebido, 0) AS "Valor Recebido",
  sra.descricao        AS "Resultado da Aposta"
FROM Usuario u
JOIN Aposta a ON u.id_usuario = a.id_usuario
JOIN Odd o ON a.id_odd = o.id_odd
JOIN Partida p ON o.id_partida = p.id_partida
JOIN Competicao comp ON p.id_competicao = comp.id_competicao
LEFT JOIN Resultado_Aposta ra ON a.id_aposta = ra.id_aposta
LEFT JOIN Status_Resultado_Aposta sra ON ra.id_status_resultado_aposta = sra.id_status_resultado_aposta;


-- Criar a view: Resumo Financeiro do Usuário
CREATE OR REPLACE VIEW vw_resumo_financeiro AS
SELECT
  u.id_usuario AS "ID Usuário",
  u.nome AS "Nome do Usuário",
  c.saldo AS "Saldo Atual",
  COUNT(t.id_transacao) AS "Total de Transações",
  SUM(CASE WHEN t.id_tipo_transacao = 2 THEN t.valor ELSE 0 END) AS "Total de Depósitos",
  SUM(CASE WHEN t.id_tipo_transacao = 3 THEN t.valor ELSE 0 END) AS "Total de Retiradas",
  SUM(CASE WHEN t.id_tipo_transacao NOT IN (2, 3) THEN t.valor ELSE 0 END) AS "Total de Outras Operações",
  (SUM(CASE WHEN t.id_tipo_transacao = 2 THEN t.valor ELSE 0 END)
   - SUM(CASE WHEN t.id_tipo_transacao = 3 THEN t.valor ELSE 0 END)
   + SUM(CASE WHEN t.id_tipo_transacao NOT IN (2, 3) THEN t.valor ELSE 0 END)) AS "Fluxo Líquido",
  CASE 
    WHEN COUNT(t.id_transacao) > 0 
      THEN SUM(t.valor) / COUNT(t.id_transacao)
    ELSE 0 
  END AS "Média Valor Transação"
FROM Usuario u
JOIN Carteira c ON u.id_usuario = c.id_usuario
LEFT JOIN Transacao t ON c.id_carteira = t.id_carteira
GROUP BY u.id_usuario, u.nome, c.saldo;


-- Criar a view: Resumo de Estatísticas dos Times
CREATE OR REPLACE VIEW vw_detalhes_times AS
WITH dados AS (
  SELECT 
    p.id_partida,
    t1.id_equipe AS id_time,
    t1.nome     AS time_nome,
    rpe1.gols_marcados,
    rpe2.gols_marcados AS gols_sofridos,
    rpe1.cartoes_amarelos,
    rpe1.cartoes_vermelhos
  FROM Partida p
  JOIN Equipe t1 ON p.id_time_mandante = t1.id_equipe
  JOIN Equipe t2 ON p.id_time_visitante = t2.id_equipe
  JOIN Resultado_Partida_Equipe rpe1 ON p.id_partida = rpe1.id_partida AND rpe1.id_equipe = t1.id_equipe
  JOIN Resultado_Partida_Equipe rpe2 ON p.id_partida = rpe2.id_partida AND rpe2.id_equipe = t2.id_equipe
  UNION ALL
  SELECT 
    p.id_partida,
    t2.id_equipe AS id_time,
    t2.nome     AS time_nome,
    rpe2.gols_marcados,
    rpe1.gols_marcados AS gols_sofridos,
    rpe2.cartoes_amarelos,
    rpe2.cartoes_vermelhos
  FROM Partida p
  JOIN Equipe t1 ON p.id_time_mandante = t1.id_equipe
  JOIN Equipe t2 ON p.id_time_visitante = t2.id_equipe
  JOIN Resultado_Partida_Equipe rpe1 ON p.id_partida = rpe1.id_partida AND rpe1.id_equipe = t1.id_equipe
  JOIN Resultado_Partida_Equipe rpe2 ON p.id_partida = rpe2.id_partida AND rpe2.id_equipe = t2.id_equipe
)
SELECT 
  time_nome                                 AS "Time",
  COUNT(*)                                  AS "Partidas Jogadas",
  SUM(CASE WHEN gols_marcados > gols_sofridos THEN 1 ELSE 0 END) AS "Vitórias",
  SUM(CASE WHEN gols_marcados = gols_sofridos THEN 1 ELSE 0 END) AS "Empates",
  SUM(CASE WHEN gols_marcados < gols_sofridos THEN 1 ELSE 0 END) AS "Derrotas",
  SUM(gols_marcados)                        AS "Gols Marcados",
  SUM(gols_sofridos)                        AS "Gols Sofridos",
  SUM(gols_marcados) - SUM(gols_sofridos)     AS "Saldo de Gols",
  SUM(cartoes_amarelos)                     AS "Cartões Amarelos",
  SUM(cartoes_vermelhos)                    AS "Cartões Vermelhos"
FROM dados
GROUP BY time_nome
ORDER BY "Vitórias" DESC, "Saldo de Gols" DESC;


-- Criar a view: Apostas em Andamento da Partida
CREATE OR REPLACE VIEW vw_apostas_em_andamento AS
SELECT
  p.id_partida                                   AS "ID Partida",
  comp.nome                                      AS "Campeonato",
  tp.descricao                                   AS "Tipo de Partida",
  t1.nome                                        AS "Time Mandante",
  t2.nome                                        AS "Time Visitante",
  COUNT(a.id_aposta)                             AS "Quantidade de Apostas",
  COALESCE(SUM(a.valor), 0)                      AS "Total Apostado"
FROM Partida p
JOIN Competicao comp ON p.id_competicao = comp.id_competicao
JOIN Tipo_Partida tp ON p.id_tipo_partida = tp.id_tipo_partida
JOIN Equipe t1 ON p.id_time_mandante = t1.id_equipe
JOIN Equipe t2 ON p.id_time_visitante = t2.id_equipe
JOIN Odd o ON p.id_partida = o.id_partida
LEFT JOIN Aposta a ON o.id_odd = a.id_odd
JOIN Status_Partida sp ON p.id_status_partida = sp.id_status_partida
WHERE sp.descricao = 'Em andamento'
GROUP BY 
  p.id_partida, 
  comp.nome, 
  tp.descricao, 
  t1.nome, 
  t2.nome;

-- Confirma a transação
COMMIT;

-- roolback;
