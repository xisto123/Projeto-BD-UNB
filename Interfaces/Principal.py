import tkinter as tk
from Services.Helper.window_size import set_window_size
import Services.global_data as global_data
from Interfaces.Perfil import PerfilScreen

class PrincipalScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Principal")
        set_window_size(self, 0.8, 0.7)
        self.create_widgets()

    def create_widgets(self):
        # Frame superior para o título e a foto do usuário
        top_frame = tk.Frame(self)
        top_frame.pack(side=tk.TOP, fill=tk.X, padx=20, pady=10)

        # Título com o nome do usuário logado e "Menu Principal"
        titulo_texto = f"Bem vindo {global_data.usuario_nome} ao Menu Principal"
        self.lbl_titulo = tk.Label(top_frame, text=titulo_texto, font=("Helvetica", 24), justify=tk.LEFT)
        self.lbl_titulo.pack(side=tk.LEFT, anchor=tk.NW)

        # Exibição da foto do usuário no canto superior direito
        if global_data.usuario_foto is not None:
            # A foto já deve estar em um formato compatível (ex: PhotoImage)
            self.lbl_foto = tk.Label(top_frame, image=global_data.usuario_foto)
            self.lbl_foto.pack(side=tk.RIGHT, anchor=tk.NE)
        else:
            self.lbl_foto = tk.Label(top_frame, text="Foto não disponível", width=18, height=10, relief="solid")
            self.lbl_foto.pack(side=tk.RIGHT, anchor=tk.NE)

        # Frame central para os botões organizados em formato de quadrado (2x2)
        btn_frame = tk.Frame(self)
        btn_frame.pack(expand=True)

        # Configurando as linhas e colunas para que tenham peso igual e centralizem os botões
        for i in range(2):
            btn_frame.grid_rowconfigure(i, weight=1)
            btn_frame.grid_columnconfigure(i, weight=1)

        # Botões com tamanho quadrangular (os parâmetros width e height podem ser ajustados)
        btn_meu_perfil = tk.Button(btn_frame, text="Meu Perfil", width=20, height=5, bg="lightblue", command=self.abrir_tela_meuPerfil)
        btn_meu_perfil.grid(row=0, column=0, padx=10, pady=10)

        btn_notificacoes = tk.Button(btn_frame, text="Notificações", width=20, height=5, bg="lightcoral")
        btn_notificacoes.grid(row=0, column=1, padx=10, pady=10)

        btn_realizar_aposta = tk.Button(btn_frame, text="Apostas", width=20, height=5, bg="lightpink")
        btn_realizar_aposta.grid(row=1, column=0, padx=10, pady=10)

        btn_carteira = tk.Button(btn_frame, text="Carteira", width=20, height=5, bg="lightgreen")
        btn_carteira.grid(row=1, column=1, padx=10, pady=10)

        # Estilizando os botões para que tenham borda e sombra
        button_style = {
            "relief": tk.RAISED,
            "bd": 2
        }

        btn_meu_perfil.config(**button_style)
        btn_notificacoes.config(**button_style)
        btn_realizar_aposta.config(**button_style)
        btn_carteira.config(**button_style)

        # Adicionando sombra aos botões
        def add_shadow(widget):
            widget.bind("<Enter>", lambda e: widget.config(relief=tk.SUNKEN))
            widget.bind("<Leave>", lambda e: widget.config(relief=tk.RAISED))

        add_shadow(btn_meu_perfil)
        add_shadow(btn_notificacoes)
        add_shadow(btn_realizar_aposta)
        add_shadow(btn_carteira)

        # def abrir_tela_notificacoes(self):
        #     self.destroy()
        #     cadastro_window = PrincipalScreen()
        #     cadastro_window.mainloop()

        # def abrir_tela_apostas(self):
        #     self.destroy()
        #     cadastro_window = PrincipalScreen()
        #     cadastro_window.mainloop()

        # def abrir_tela_carteira(self):
        #     self.destroy()
        #     cadastro_window = PrincipalScreen()
        #     cadastro_window.mainloop()
    
    def abrir_tela_meuPerfil(self):
        self.destroy()
        cadastro_window = PerfilScreen()
        cadastro_window.mainloop()

if __name__ == "__main__":
    app = PrincipalScreen()
    app.mainloop()
