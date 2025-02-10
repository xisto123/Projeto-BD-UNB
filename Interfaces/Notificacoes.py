import tkinter as tk
from tkinter import ttk, messagebox
from Services.Helper.window_size import set_window_size
import Services.global_data as global_data
from Models.notificacao import Notificacao

class NotificacoesScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Minhas Notificações")
        set_window_size(self, 0.8, 0.7)
        self.create_widgets()
        self.carregar_notificacoes()

    def create_widgets(self):
        # Container principal
        self.container = tk.Frame(self)
        self.container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Cria uma Treeview para exibir as notificações
        self.tree = ttk.Treeview(
            self.container,
            columns=("ID", "Título", "Conteudo", "Lida", "Data/Hora"),
            show="headings"
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Conteudo", text="Conteudo")
        self.tree.heading("Lida", text="Lida")
        self.tree.heading("Data/Hora", text="Data/Hora")
        
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Título", width=150)
        self.tree.column("Conteudo", width=300)
        self.tree.column("Lida", width=60, anchor="center")
        self.tree.column("Data/Hora", width=150, anchor="center")
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Botão para atualizar a lista
        self.btn_refresh = tk.Button(self.container, text="Atualizar", command=self.carregar_notificacoes)
        self.btn_refresh.pack(pady=10)

    def carregar_notificacoes(self):
        # Remove itens anteriores
        for item in self.tree.get_children():
            self.tree.delete(item)
        try:
            # Busca notificações do usuário logado
            notificacoes = Notificacao.get_by("id_usuario", global_data.usuario_id)
            for notif in notificacoes:
                self.tree.insert("", "end", values=(
                    notif[0],
                    notif[3],
                    notif[4],
                    notif[5],
                    notif[6]
                ))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar notificações: {e}")

if __name__ == "__main__":
    app = NotificacoesScreen()
    app.mainloop()
