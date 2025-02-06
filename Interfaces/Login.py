
import tkinter as tk
from tkinter import messagebox
from Interfaces.Cadastro import CadastroScreen
from Services.Helper.window_size import set_window_size

class LoginScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        set_window_size(self, 0.8, 0.7)
        self.create_widgets()

    def create_widgets(self):
        # Container principal
        self.container = tk.Frame(self)
        self.container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Título de bem-vindo
        self.label_welcome = tk.Label(self.container, text="Bem-vindo ao Sistema de Apostas!", font=("Arial", 28))
        self.label_welcome.pack(pady=10)

        # Label e entrada para o usuário
        self.label_cpf = tk.Label(self.container, text="Digite seu CPF:")
        self.label_cpf.pack(pady=10)

        self.entry_cpf = tk.Entry(self.container)
        self.entry_cpf.pack(pady=5)

        # Label e entrada para a senha
        self.label_password = tk.Label(self.container, text="Digite a sua Senha:")
        self.label_password.pack(pady=10)

        self.entry_password = tk.Entry(self.container, show="*")
        self.entry_password.pack(pady=5)

        # Frame para os botões
        self.button_frame = tk.Frame(self.container)
        self.button_frame.pack(pady=20)

        # Botão para login
        self.btn_login = tk.Button(self.button_frame, text="Login", command=self.validate_login, borderwidth=10)
        self.btn_login.pack(side=tk.LEFT, padx=5)

        # Botão para cadastrar-se
        self.btn_register = tk.Button(self.button_frame, text="Cadastrar-se", command=self.abrir_cadastro, borderwidth=10)
        self.btn_register.pack(side=tk.LEFT, padx=5)

    def validate_login(self):
        cpf = self.entry_cpf.get()
        password = self.entry_password.get()
        
        # Aqui você pode integrar com a camada de services para validar o login
        # Exemplo simples de validação:
        if cpf == "admin" and password == "admin":
            messagebox.showinfo("Login", "Login realizado com sucesso!")
            # Aqui você pode chamar a próxima tela ou função da aplicação
        else:
            messagebox.showerror("Login", "Usuário ou senha incorretos.")

    def abrir_cadastro(self):
        self.destroy()
        cadastro_window = CadastroScreen()
        cadastro_window.mainloop()
    
if __name__ == "__main__":
    app = LoginScreen()
    app.mainloop()
