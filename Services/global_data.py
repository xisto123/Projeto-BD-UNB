# global_data.py
# Variáveis globais para armazenar informações do usuário logado.
usuario_id = None
usuario_nome = None
usuario_tipo = None
usuario_foto = None

# Se TRANSACTION_CONN for None, as funções da repository usarão get_connection() normalmente.
# Caso contrário, usarão essa conexão compartilhada.
TRANSACTION_CONN = None