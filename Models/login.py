# Models/login.py

import socket
from Models.base_model import BaseModel

class Login(BaseModel):
    table_name = "Login"
    primary_key = "id_login"

    def __init__(self, id_login=None, id_usuario=None, dt_hora_login=None, endereco_ip=None, sucesso=None):
        self.id_login = id_login
        self.id_usuario = id_usuario
        self.dt_hora_login = dt_hora_login
        self.endereco_ip = endereco_ip
        self.sucesso = sucesso

    def __str__(self):
        return (f"Login(id_login={self.id_login}, id_usuario={self.id_usuario}, dt_hora_login={self.dt_hora_login},\n"
                f"endereco_ip={self.endereco_ip}, sucesso={self.sucesso})")
    
    def get_local_ip():
        return socket.gethostbyname(socket.gethostname())
