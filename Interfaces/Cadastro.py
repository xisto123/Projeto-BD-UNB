import tkinter as tk
from tkinter import messagebox
from Services.Helper.window_size import set_window_size

class CadastroScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tela de Cadastro")
        set_window_size(self, 0.8, 0.7)
        # self.geometry("300x300")
        self.create_widgets()

    def create_widgets(self):
        self.label_nome = tk.Label(self, text="Nome:")
        self.label_nome.pack(pady=5)

        self.entry_nome = tk.Entry(self)
        self.entry_nome.pack(pady=5)

        self.label_email = tk.Label(self, text="Email:")
        self.label_email.pack(pady=5)

        self.entry_email = tk.Entry(self)
        self.entry_email.pack(pady=5)

        self.btn_cadastrar = tk.Button(self, text="Cadastrar", command=self.cadastrar_usuario)
        self.btn_cadastrar.pack(pady=20)

    def cadastrar_usuario(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        
        # Lógica para cadastro (integração futura com o banco)
        if nome and email:
            messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
            self.destroy()  # Fecha a tela de cadastro após o cadastro
        else:
            messagebox.showerror("Erro", "Preencha todos os campos.")

if __name__ == "__main__":
    app = CadastroScreen()
    app.mainloop()
