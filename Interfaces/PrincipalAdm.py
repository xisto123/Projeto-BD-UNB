import tkinter as tk
from Services.Helper.window_size import set_window_size
import Services.global_data as global_data
from Interfaces.Partida.CriarPartida import CriarPartidaScreen
from Interfaces.Partida.Partida import PartidaScreen
from Interfaces.DetalhesPartidas import DetalhesPartidasScreen
from Interfaces.DetalhesTimes import DetalhesTimesScreen
from Interfaces.GerarResultado import GerarResultadoScreen

class PrincipalAdmScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Principal")
        set_window_size(self, 0.8, 0.7)
        self.create_widgets()

    def create_widgets(self):
        # Frame superior para o título
        top_frame = tk.Frame(self)
        top_frame.pack(side=tk.TOP, fill=tk.X, padx=20, pady=10)

        # Título centralizado com o nome do usuário logado e "Menu Principal"
        titulo_texto = f"Bem vindo Adm {global_data.usuario_nome} ao Menu Principal"
        self.lbl_titulo = tk.Label(top_frame, text=titulo_texto, font=("Helvetica", 24), justify=tk.CENTER)
        self.lbl_titulo.pack(side=tk.TOP, anchor=tk.CENTER)

        # Frame central para os botões organizados em formato de grid
        btn_frame = tk.Frame(self)
        btn_frame.pack(expand=True)

        # Configurando as linhas e colunas para que tenham peso igual
        btn_frame.grid_rowconfigure(0, weight=1)
        for i in range(3):
            btn_frame.grid_columnconfigure(i, weight=1)

        # Botões da primeira linha
        btn_criar_partida = tk.Button(
            btn_frame,
            text="Criar Partida",
            width=20,
            height=5,
            bg="lightblue",
            command=self.open_criar_partida   # Agora abre CriarPartidaScreen
        )
        btn_criar_partida.grid(row=0, column=0, padx=10, pady=10)

        btn_partida = tk.Button(
            btn_frame,
            text="Partida",
            width=20,
            height=5,
            bg="orchid",
            command=self.open_partida
        )
        btn_partida.grid(row=0, column=1, padx=10, pady=10)

        btn_gerar_resultado = tk.Button(
            btn_frame,
            text="Gerar Resultado",
            width=20,
            height=5,
            bg="lightgreen",
            command=self.open_gerar_resultado
        )
        btn_gerar_resultado.grid(row=0, column=2, padx=10, pady=10)

        # Botões da segunda linha
        btn_detalhes_times = tk.Button(
            btn_frame,
            text="Detalhes Times",
            width=20,
            height=5,
            bg="lightpink",
            command=self.open_detalhes_times
        )
        btn_detalhes_times.grid(row=1, column=0, padx=10, pady=10)

        btn_detalhes_partidas = tk.Button(
            btn_frame,
            text="Detalhes Partidas",
            width=20,
            height=5,
            bg="lightyellow",
            command=self.open_detalhes_partidas
        )
        btn_detalhes_partidas.grid(row=1, column=1, padx=10, pady=10)

        # Estilizando os botões para que tenham borda e sombra
        button_style = {
            "relief": tk.RAISED,
            "bd": 2
        }
        btn_criar_partida.config(**button_style)
        btn_partida.config(**button_style)
        btn_gerar_resultado.config(**button_style)
        btn_detalhes_times.config(**button_style)
        btn_detalhes_partidas.config(**button_style)

        # Adicionando sombra aos botões
        def add_shadow(widget):
            widget.bind("<Enter>", lambda e: widget.config(relief=tk.SUNKEN))
            widget.bind("<Leave>", lambda e: widget.config(relief=tk.RAISED))

        add_shadow(btn_criar_partida)
        add_shadow(btn_partida)
        add_shadow(btn_gerar_resultado)
        add_shadow(btn_detalhes_times)
        add_shadow(btn_detalhes_partidas)

    def open_criar_partida(self):
        self.destroy() 
        tela_criar_partida = CriarPartidaScreen()
        tela_criar_partida.mainloop()

    def open_partida(self):
        self.destroy() 
        tela_partida = PartidaScreen()
        tela_partida.mainloop()

    def open_detalhes_times(self):
        self.destroy() 
        tela_detalhes_times = DetalhesTimesScreen()
        tela_detalhes_times.mainloop()

    def open_detalhes_partidas(self):
        self.destroy() 
        tela_detalhes_partida = DetalhesPartidasScreen()
        tela_detalhes_partida.mainloop()

    def open_gerar_resultado(self):
        self.destroy() 
        tela_gerar_resultado = GerarResultadoScreen()
        tela_gerar_resultado.mainloop()

if __name__ == "__main__":
    app = PrincipalAdmScreen()
    app.mainloop()
