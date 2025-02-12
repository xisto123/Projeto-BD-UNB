-- Remover as funções antigas, se existirem
DROP FUNCTION IF EXISTS fn_atualiza_valor_aposta();
DROP FUNCTION IF EXISTS fn_criar_odds_para_nova_partida();

-- Criar a função que será usada pelo trigger de atualização de apostas
CREATE OR REPLACE FUNCTION fn_atualiza_valor_aposta()
RETURNS trigger AS $$
DECLARE
    diff NUMERIC;
    v_id_carteira  INTEGER;
    v_saldo        NUMERIC;
BEGIN
    -- Calcula a diferença entre o novo e o antigo valor da aposta
    diff := NEW.valor - OLD.valor;
    
    -- Se não houve alteração no valor, não precisa fazer nada
    IF diff = 0 THEN
        RETURN NEW;
    END IF;
    
    -- Recupera a carteira do usuário
    SELECT id_carteira, saldo
      INTO v_id_carteira, v_saldo
      FROM Carteira
     WHERE id_usuario = NEW.id_usuario;
    
    IF v_id_carteira IS NULL THEN
        RAISE EXCEPTION 'Carteira não encontrada para o usuário %', NEW.id_usuario;
    END IF;
    
    IF diff > 0 THEN
        -- Se o valor da aposta aumentou, verifica se o saldo é suficiente
        IF v_saldo < diff THEN
            RAISE EXCEPTION 'Saldo insuficiente: Saldo atual: %, valor adicional requerido: %', v_saldo, diff;
        END IF;
        -- Atualiza a carteira subtraindo o valor adicional
        UPDATE Carteira
           SET saldo = saldo - diff,
               dt_hora_atualizacao = CURRENT_TIMESTAMP
         WHERE id_carteira = v_id_carteira;
         
        -- Registra a transação de AUMENTO DA APOSTA
        INSERT INTO Transacao (id_carteira, id_tipo_transacao, valor, descricao, dt_hora)
        VALUES (v_id_carteira, 7, diff, 'Aumento do valor da aposta', CURRENT_TIMESTAMP);
    ELSE
        -- Se o valor da aposta diminuiu, diff será negativo; recredita o valor (subtrair um valor negativo é somar)
        UPDATE Carteira
           SET saldo = saldo - diff,  
               dt_hora_atualizacao = CURRENT_TIMESTAMP
         WHERE id_carteira = v_id_carteira;
         
        -- Registra a transação de REDUÇÃO DA APOSTA
        INSERT INTO Transacao (id_carteira, id_tipo_transacao, valor, descricao, dt_hora)
        VALUES (v_id_carteira, 8, ABS(diff), 'Redução do valor da aposta', CURRENT_TIMESTAMP);
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Criar a função que será usada pelo trigger de criação de odds para novas partidas
CREATE OR REPLACE FUNCTION fn_criar_odds_para_nova_partida()
RETURNS trigger AS $$
DECLARE
    v_id_mercado  INTEGER;
    v_random_odd NUMERIC;
BEGIN
    -- Percorre todos os mercados disponíveis na tabela Mercado_Aposta
    FOR v_id_mercado IN (SELECT id_mercado FROM Mercado_Aposta) LOOP
        
        -- Gera um valor aleatório entre 1.0 e 10.0, arredondado para 2 casas decimais.
        v_random_odd := ROUND((1.0 + (random() * 9.0))::numeric, 2); 
        
        -- Insere uma nova odd associada à nova partida e ao mercado de aposta
        INSERT INTO Odd (id_partida, id_mercado, valor, descricao, dt_hora_criacao)
        VALUES (
            NEW.id_partida, 
            v_id_mercado, 
            v_random_odd, 
            CONCAT('Odd para ', (SELECT descricao FROM Mercado_Aposta WHERE id_mercado = v_id_mercado)),
            CURRENT_TIMESTAMP
        );
    END LOOP;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Criar o trigger que chama a função após a inserção de uma nova partida
CREATE TRIGGER trg_criar_odds_nova_partida
AFTER INSERT ON Partida
FOR EACH ROW
EXECUTE FUNCTION fn_criar_odds_para_nova_partida();

-- Criar o trigger que chama a função após a atualização do valor da aposta
CREATE TRIGGER trg_atualiza_valor_aposta
AFTER UPDATE OF valor ON Aposta
FOR EACH ROW
WHEN (OLD.valor IS DISTINCT FROM NEW.valor)
EXECUTE FUNCTION fn_atualiza_valor_aposta();
