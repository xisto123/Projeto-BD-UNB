from Database.connection import get_connection
from decimal import Decimal
from Enums.tipos_apoio import TipoTransacao
from Models.aposta import Aposta
from Models.carteira import Carteira
from Models.transacao import Transacao
import Services.global_data as global_data

def criar_aposta(**kwargs):
    """
    Cria uma aposta para o usuário, desconta o valor na carteira e registra a transação,
    agrupando todas as operações em uma única transação no banco de dados.
    
    Etapas:
      1. Salvar a aposta do usuário.
      2. Atualizar o saldo da carteira (descontando o valor apostado).
      3. Registrar a transação correspondente.
    
    Retorna a aposta criada.
    """
    try:
        local_tx = False
        # Verifica se já há uma conexão transacional definida globalmente
        conn = global_data.TRANSACTION_CONN
        if conn is None:
            conn = get_connection()
            global_data.TRANSACTION_CONN = conn
            local_tx = True

        usuarioId = global_data.usuario_id
        valor = Decimal(kwargs.get("valor"))
        
        # Etapa 1: Salvar a aposta do usuário (passando o objeto de conexão)
        aposta = Aposta.create(**kwargs, conn=conn)
        
        # Etapa 2: Recuperar a carteira do usuário usando a mesma conexão
        carteira = Carteira.get_by("id_usuario", usuarioId, conn=conn)
        if isinstance(carteira, list):
            if not carteira:
                raise Exception("Carteira do usuário não encontrada.")
            carteira = carteira[0]
        if not carteira:
            raise Exception("Carteira do usuário não encontrada.")
        
        # Supondo que a carteira seja uma tupla onde:
        # índice 0 -> id_carteira e índice 3 -> saldo
        novo_saldo = carteira[3] - valor
        dataCarteira = {
            "saldo": novo_saldo
        }
        # Atualiza a carteira utilizando o método update_by_pk que agora aceita o parâmetro conn
        carteira_atualizada = Carteira.update_by_pk(int(carteira[0]), **dataCarteira, conn=conn)
        if not carteira_atualizada:
            raise Exception("Erro ao atualizar a carteira.")
        
        # Etapa 3: Registrar a transação da aposta
        dataTransacao = {
            "id_carteira": carteira[0],
            "id_tipo_transacao": TipoTransacao.APOSTA.value,
            "valor": round(float(valor), 2),
            "descricao": "Valor de aposta"
        }
        if not Transacao.create(**dataTransacao, conn=conn):
            raise Exception("Erro ao salvar a transação.")
        
        if local_tx:
            conn.commit()
        return aposta

    except Exception as e:
        if local_tx and conn is not None:
            conn.rollback()
        raise e

    finally:
        if local_tx and conn is not None:
            conn.close()
            global_data.TRANSACTION_CONN = None
