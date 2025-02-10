DROP PROCEDURE IF EXISTS encerrar_partida;
DROP PROCEDURE IF EXISTS cadastrar_usuario_completo;

CREATE OR REPLACE PROCEDURE encerrar_partida(
    p_id_partida                INTEGER,
    p_gols_mandante             INTEGER,
    p_gols_visitante            INTEGER,
    p_cartoes_amarelos_mandante INTEGER,
    p_cartoes_amarelos_visitante INTEGER,
    p_cartoes_vermelhos_mandante INTEGER,
    p_cartoes_vermelhos_visitante INTEGER,
    p_escanteios_mandante       INTEGER,
    p_escanteios_visitante      INTEGER,
    p_impedimentos_mandante     INTEGER,
    p_impedimentos_visitante    INTEGER,
    p_faltas_mandante           INTEGER,
    p_faltas_visitante          INTEGER
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_id_time_mandante  INTEGER;
    v_id_time_visitante INTEGER;
    rec                 RECORD;
    v_id_carteira       INTEGER;
    v_saldo             NUMERIC;
    v_payout            NUMERIC;
    v_expected_result   INTEGER;
BEGIN
    -- 1. Atualiza o status da partida para "Encerrada" (supondo que id_status_partida = 3 é "Encerrada")
    UPDATE Partida
      SET id_status_partida = 3
    WHERE id_partida = p_id_partida;
    
    -- 2. Obtém os IDs dos times da partida
    SELECT id_time_mandante, id_time_visitante
      INTO v_id_time_mandante, v_id_time_visitante
      FROM Partida
     WHERE id_partida = p_id_partida;
    
    -- 3. Insere os resultados completos da partida para cada equipe
    INSERT INTO Resultado_Partida_Equipe (
         id_partida, id_equipe, gols_marcados, gols_sofridos, 
         cartoes_amarelos, cartoes_vermelhos, escanteios, impedimentos, faltas_cometidas
    )
    VALUES
      (
        p_id_partida, v_id_time_mandante, p_gols_mandante, p_gols_visitante,
        p_cartoes_amarelos_mandante, p_cartoes_vermelhos_mandante, p_escanteios_mandante,
        p_impedimentos_mandante, p_faltas_mandante
      ),
      (
        p_id_partida, v_id_time_visitante, p_gols_visitante, p_gols_mandante,
        p_cartoes_amarelos_visitante, p_cartoes_vermelhos_visitante, p_escanteios_visitante,
        p_impedimentos_visitante, p_faltas_visitante
      );
    
    -- 4. Processamento das apostas associadas à partida
    FOR rec IN
        SELECT a.id_aposta, a.id_usuario, a.valor, a.resultado, o.id_odd, o.id_mercado, o.valor AS odd_valor
          FROM Aposta a
          JOIN Odd o ON a.id_odd = o.id_odd
         WHERE o.id_partida = p_id_partida AND a.status = 'ativa'
    LOOP
        -- Calcula o resultado esperado conforme o mercado
        v_expected_result := CASE rec.id_mercado
            WHEN 1 THEN (p_gols_mandante + p_gols_visitante) 
            WHEN 2 THEN (p_escanteios_mandante + p_escanteios_visitante)
            WHEN 3 THEN (p_cartoes_amarelos_mandante + p_cartoes_amarelos_visitante)
            WHEN 4 THEN (p_cartoes_vermelhos_mandante + p_cartoes_vermelhos_visitante)
            WHEN 5 THEN (p_impedimentos_mandante + p_impedimentos_visitante)
            WHEN 6 THEN (p_faltas_mandante + p_faltas_visitante)
            ELSE NULL
        END;
        
        IF rec.resultado = v_expected_result THEN
            -- Aposta vencedora: calcula o pagamento (valor apostado × odd)
            v_payout := rec.valor * rec.odd_valor;
            
            -- Recupera a carteira do usuário
            SELECT id_carteira, saldo
              INTO v_id_carteira, v_saldo
              FROM Carteira
             WHERE id_usuario = rec.id_usuario;
            
            -- Atualiza o saldo da carteira, creditando o pagamento
            UPDATE Carteira
               SET saldo = v_saldo + v_payout
             WHERE id_carteira = v_id_carteira;
            
            -- Registra a transação de pagamento (id_tipo_transacao = 1 para PAGAMENTO)
            INSERT INTO Transacao (id_carteira, id_tipo_transacao, valor, descricao)
            VALUES (v_id_carteira, 1, v_payout, 'Pagamento de aposta vencedora para partida ' || p_id_partida);
            
            -- Registra o resultado da aposta como GANHO (id_status_resultado_aposta = 1 para GANHO)
            INSERT INTO Resultado_Aposta (id_aposta, valor_recebido, id_status_resultado_aposta)
            VALUES (rec.id_aposta, v_payout, 1);
            
            -- Envia notificação ao usuário informando que ganhou a aposta (usando id_tipo_notificacao = 4 para VOCE_GANHOU)
            INSERT INTO Notificacao (id_usuario, id_tipo_notificacao, titulo, conteudo)
            VALUES (rec.id_usuario, 4, 'Pagamento de Aposta Vencedora',
                    'Sua aposta na partida ' || p_id_partida || ' foi paga. Valor recebido: ' || v_payout);
        ELSE
            -- Aposta perdedora: registra o resultado como PERDA (id_status_resultado_aposta = 2)
            INSERT INTO Resultado_Aposta (id_aposta, valor_recebido, id_status_resultado_aposta)
            VALUES (rec.id_aposta, 0, 2);
            
            -- Notifica o usuário que a aposta não foi bem-sucedida (usando id_tipo_notificacao = 5 para VOCE_PERDEU)
            INSERT INTO Notificacao (id_usuario, id_tipo_notificacao, titulo, conteudo)
            VALUES (rec.id_usuario, 5, 'Aposta Perdida',
                    'Sua aposta na partida ' || p_id_partida || ' não foi bem-sucedida.');
        END IF;
        
        -- Atualiza o status da aposta para inativa
        UPDATE Aposta
           SET status = 'inativa'
         WHERE id_aposta = rec.id_aposta;
    END LOOP;
    
END;
$$;

CREATE OR REPLACE PROCEDURE cadastrar_usuario_completo(
    p_nome            VARCHAR,
    p_cpf             VARCHAR,
    p_email           VARCHAR,
    p_senha           VARCHAR,
    p_id_tipo_usuario INTEGER,
    p_dt_nascimento   DATE,
    p_foto            BYTEA,
    p_foto_nome       VARCHAR,
    p_foto_mime       VARCHAR,
    p_foto_size_mb    DECIMAL
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_id_usuario  INTEGER;
    v_id_carteira INTEGER;
BEGIN
    -- 1. Inserir o usuário na tabela Usuario
    INSERT INTO Usuario (nome, cpf, email, senha, id_tipo_usuario, status, dt_nascimento)
    VALUES (p_nome, p_cpf, p_email, p_senha, p_id_tipo_usuario, 'ativo', p_dt_nascimento)
    RETURNING id_usuario INTO v_id_usuario;
    
    -- 2. Inserir a foto do usuário na tabela Arquivo (se fornecida)
    IF p_foto IS NOT NULL THEN
        INSERT INTO Arquivo (
            id_usuario, nome, descricao, mime_type, size_mb, binary_data, dt_hora_upload
        )
        VALUES (
            v_id_usuario, p_foto_nome, 'Foto de perfil cadastrada', p_foto_mime, p_foto_size_mb, p_foto, CURRENT_TIMESTAMP
        );
    END IF;
    
    -- 3. Inserir notificação de Bem-vindo (assumindo id_tipo_notificacao = 7 para BEM_VINDO)
    INSERT INTO Notificacao (id_tipo_notificacao, titulo, conteudo, dt_hora_envio, id_usuario)
    VALUES (7, 'Bem-vindo!', 'Seja bem-vindo ao sistema!', CURRENT_TIMESTAMP, v_id_usuario);
    
    -- 4. Criar carteira para o usuário na tabela Carteira (assumindo id_status_carteira = 1 para ativo)
    INSERT INTO Carteira (id_usuario, tipo, saldo, id_status_carteira, dt_hora_registro, dt_hora_atualizacao)
    VALUES (v_id_usuario, 'principal', 0.00, 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
    RETURNING id_carteira INTO v_id_carteira;
    
    -- 5. Inserir transação de bônus na tabela Transacao (assumindo id_tipo_transacao = 4 para bônus)
    INSERT INTO Transacao (id_carteira, id_tipo_transacao, valor, descricao, dt_hora)
    VALUES (v_id_carteira, 4, 500.00, 'Bônus de cadastro', CURRENT_TIMESTAMP);
    
    -- 6. Atualizar o saldo da carteira para incluir o bônus
    UPDATE Carteira
       SET saldo = saldo + 500.00,
           dt_hora_atualizacao = CURRENT_TIMESTAMP
     WHERE id_carteira = v_id_carteira;
    
    -- 7. Inserir notificação informando que o usuário recebeu bônus (assumindo id_tipo_notificacao = 8 para VOCE_RECEBEU_BONUS)
    INSERT INTO Notificacao (id_tipo_notificacao, titulo, conteudo, dt_hora_envio, id_usuario)
    VALUES (8, 'Você recebeu bônus!', 'Um bônus de 500 foi creditado em sua carteira.', CURRENT_TIMESTAMP, v_id_usuario);
    
END;
$$;