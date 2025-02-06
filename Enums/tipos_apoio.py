# Enums/tipos_apoio.py

from enum import Enum

class TipoUsuario(Enum):
    ADMIN = 1
    USUARIO = 2
    FISCAL = 3
    VISITANTE = 4

class TipoNotificacao(Enum):
    PARTIDA_QUASE_INICIANDO = 1
    PARTIDA_INICIADA = 2
    PARTIDA_ENCERRADA = 3
    VOCE_GANHOU = 4
    VOCE_PERDEU = 5
    MUDANCA_ODDS = 6

class StatusCarteira(Enum):
    ATIVO = 1
    INATIVO = 2
    SUSPENSO = 3
    BLOQUEADO = 4
    PENDENTE = 5

class TipoTransacao(Enum):
    PAGAMENTO = 1
    DEPOSITO = 2
    RETIRADA = 3
    BONUS = 4
    REEMBOLSO = 5

class TipoCompeticao(Enum):
    CAMPEONATO = 1
    TORNEIO = 2
    COPA = 3
    LIGA = 4
    AMISTOSO = 5
    REGIONAL = 6

class FaseCompeticao(Enum):
    FASE_GRUPOS = 1
    ELIMINATORIA = 2
    SEMIFINAL = 3
    FINAL = 4

class StatusResultadoAposta(Enum):
    GANHO = 1
    PERDA = 2
    REEMBOLSADO = 3
    CANCELADO = 4
    AGUARDANDO_RESULTADO = 5
