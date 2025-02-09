import tkinter as tk
from tkinter import messagebox, ttk
from Services.Helper.window_size import set_window_size
from Enums.tipos_apoio import TipoUsuario
from Models.usuario import Usuario
import Services.global_data as global_data

class EditarUsuarioScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editar Perfil de Usuário")
        set_window_size(self, 0.8, 0.7)
        self.create_widgets()
        self.carregar_dados_usuario()

    def create_widgets(self):
        # Título da página
        self.label_titulo = tk.Label(self, text="Edição de Usuário", font=("Helvetica", 16, "bold"))
        self.label_titulo.pack(pady=20)

        # Container principal centralizado
        self.container = tk.Frame(self)
        self.container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Linha 1: Nome e CPF
        self.label_nome = tk.Label(self.container, text="Nome:")
        self.label_nome.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_nome = tk.Entry(self.container, width=30)
        self.entry_nome.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        
        self.label_cpf = tk.Label(self.container, text="CPF:")
        self.label_cpf.grid(row=1, column=2, padx=10, pady=10, sticky="e")
        self.entry_cpf = tk.Entry(self.container, width=30)
        self.entry_cpf.grid(row=1, column=3, padx=10, pady=10, sticky="w")
        
        # Linha 2: Email e Senha
        self.label_email = tk.Label(self.container, text="Email:")
        self.label_email.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_email = tk.Entry(self.container, width=30)
        self.entry_email.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        
        self.label_password = tk.Label(self.container, text="Senha:")
        self.label_password.grid(row=2, column=2, padx=10, pady=10, sticky="e")
        self.entry_password = tk.Entry(self.container, show="*", width=30)
        self.entry_password.grid(row=2, column=3, padx=10, pady=10, sticky="w")
        
        # Linha 3: Tipo de Usuário (Combobox) e Data de Nascimento
        self.label_tipo_usuario = tk.Label(self.container, text="Tipo de Usuário:")
        self.label_tipo_usuario.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.combo_tipo_usuario = ttk.Combobox(
            self.container,
            values=[tipo.name for tipo in TipoUsuario],
            state="readonly",
            width=28
        )
        self.combo_tipo_usuario.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        
        self.label_data_nascimento = tk.Label(self.container, text="Data de Nascimento:")
        self.label_data_nascimento.grid(row=3, column=2, padx=10, pady=10, sticky="e")
        self.entry_data_nascimento = tk.Entry(self.container, width=30)
        self.entry_data_nascimento.grid(row=3, column=3, padx=10, pady=10, sticky="w")
        
        # Linha 4: Botão de Salvar a Edição
        self.button_frame = tk.Frame(self.container)
        self.button_frame.grid(row=4, column=0, columnspan=4, pady=20)
        
        self.btn_salvar = tk.Button(self.button_frame, text="Salvar Edição", command=self.salvar_edicao, borderwidth=10)
        self.btn_salvar.pack()

    def carregar_dados_usuario(self):
        usuario = Usuario.get_by_id(global_data.usuario_id)
        if usuario:
            self.entry_nome.insert(0, usuario.nome)
            self.entry_cpf.insert(0, usuario.cpf)
            self.entry_email.insert(0, usuario.email)
            self.entry_password.insert(0, usuario.senha)
            self.combo_tipo_usuario.set(TipoUsuario(usuario.id_tipo_usuario).name)
            self.entry_data_nascimento.insert(0, usuario.dt_nascimento)
        else:
            messagebox.showerror("Erro", "Usuário não encontrado.")

    def salvar_edicao(self):
        # Coleta os dados dos campos
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        email = self.entry_email.get()
        senha = self.entry_password.get()
        dt_nascimento = self.entry_data_nascimento.get()
        tipo_usuario_nome = self.combo_tipo_usuario.get()

        # Verifica se todos os campos foram preenchidos
        if not all([nome, cpf, email, senha, dt_nascimento, tipo_usuario_nome]):
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        # Converte o nome do tipo de usuário para o valor correspondente
        id_tipo_usuario = None
        for tipo in TipoUsuario:
            if tipo.name == tipo_usuario_nome:
                id_tipo_usuario = tipo.value
                break

        usuario_atualizado = Usuario.editar(
            global_data.usuario_id,
            nome=nome,
            cpf=cpf,
            email=email,
            senha=senha,
            id_tipo_usuario=id_tipo_usuario,
            dt_nascimento=dt_nascimento
        )

        if usuario_atualizado:
            messagebox.showinfo("Sucesso", "Dados atualizados com sucesso!")
            # self.destroy()
        else:
            messagebox.showerror("Erro", "Falha ao atualizar os dados.")

if __name__ == "__main__":
    app = EditarUsuarioScreen()
    app.mainloop()
