import os
import mimetypes
import datetime
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from PIL import Image, ImageTk
from Services.cadastro_usuario_service import cadastrar_usuario_completo
from Services.Helper.window_size import set_window_size
from Enums.tipos_apoio import TipoUsuario
from Models.usuario import Usuario

class CadastroScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tela de Cadastro")
        set_window_size(self, 0.8, 0.7)
        self.foto_data = None
        self.create_widgets()

    def create_widgets(self):
        # Container principal centralizado
        self.container = tk.Frame(self)
        self.container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Linha 0: Botões para selecionar foto e gerar dados aleatórios e espaço para a foto
        self.btn_selecionar_foto = tk.Button(self.container, text="Selecionar Foto", command=self.selecionar_foto)
        self.btn_selecionar_foto.grid(row=0, column=0, padx=10, pady=10)
        
        self.btn_random = tk.Button(self.container, text="Random", command=self.user_random)
        self.btn_random.grid(row=0, column=1, padx=10, pady=10)
        
        self.label_foto = tk.Label(self.container, text="Foto não selecionada", relief="solid")
        self.label_foto.grid(row=0, column=2, padx=10, pady=10)
        
        # Configura as colunas para distribuir igualmente e centralizar os widgets
        for i in range(3):
            self.container.grid_columnconfigure(i, weight=1)
        
        # Linha 1: Nome e CPF
        self.label_nome = tk.Label(self.container, text="Digite seu Nome:")
        self.label_nome.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_nome = tk.Entry(self.container)
        self.entry_nome.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        
        self.label_cpf = tk.Label(self.container, text="Digite seu CPF:")
        self.label_cpf.grid(row=1, column=2, padx=10, pady=10, sticky="e")
        self.entry_cpf = tk.Entry(self.container)
        self.entry_cpf.grid(row=1, column=3, padx=10, pady=10, sticky="w")
        
        # Linha 2: Email e Senha
        self.label_email = tk.Label(self.container, text="Digite seu Email:")
        self.label_email.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_email = tk.Entry(self.container)
        self.entry_email.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        
        self.label_password = tk.Label(self.container, text="Digite sua Senha:")
        self.label_password.grid(row=2, column=2, padx=10, pady=10, sticky="e")
        self.entry_password = tk.Entry(self.container, show="*")
        self.entry_password.grid(row=2, column=3, padx=10, pady=10, sticky="w")
        
        # Linha 3: Tipo de Usuário e Data de Nascimento
        self.label_tipo_usuario = tk.Label(self.container, text="Tipo de Usuário:")
        self.label_tipo_usuario.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.combo_tipo_usuario = ttk.Combobox(
            self.container, 
            values=[tipo.name for tipo in TipoUsuario],
            state="readonly"
        )
        self.combo_tipo_usuario.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        
        self.label_data_nascimento = tk.Label(self.container, text="Data de Nascimento (YYYY-MM-DD):")
        self.label_data_nascimento.grid(row=3, column=2, padx=10, pady=10, sticky="e")
        self.entry_data_nascimento = tk.Entry(self.container)
        self.entry_data_nascimento.grid(row=3, column=3, padx=10, pady=10, sticky="w")
        
        # Linha 4: Botões de Fechar e Cadastrar
        self.button_frame = tk.Frame(self.container)
        self.button_frame.grid(row=4, column=0, columnspan=4, pady=20)
        
        self.btn_fechar = tk.Button(self.button_frame, text="Fechar", command=self.fechar, borderwidth=10)
        self.btn_fechar.pack(side=tk.LEFT, padx=5)
        
        self.btn_register = tk.Button(self.button_frame, text="Salvar informações", command=self.cadastrar_usuario, borderwidth=10)
        self.btn_register.pack(side=tk.LEFT, padx=5)

    def selecionar_foto(self):
        """
        Abre um diálogo para que o usuário selecione uma foto.
        Armazena os metadados e dados binários em self.foto_info.
        """
        filename = filedialog.askopenfilename(
            title="Selecione a foto",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp"), ("All Files", "*.*")]
        )
        if filename:
            file_name = os.path.basename(filename)
            mime_type, _ = mimetypes.guess_type(filename)
            file_size_bytes = os.path.getsize(filename)
            file_size_mb = file_size_bytes / (1024 * 1024)
            with open(filename, "rb") as f:
                binary_data = f.read()
            self.foto_info = {
                "file_name": file_name,
                "mime_type": mime_type or "application/octet-stream",
                "file_size_mb": file_size_mb,
                "binary_data": binary_data
            }
            # Carregar a imagem e ajustá-la para caber dentro da área de visualização mantendo a proporção
            image = Image.open(filename)
            max_size = (300, 300)
            image.thumbnail(max_size, Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(image)
            self.label_foto.config(image=self.photo, text="")
            messagebox.showinfo("Foto", "Foto selecionada com sucesso!")
        else:
            self.foto_info = None

    def validate_date_format(self, date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def cadastrar_usuario(self):
        # Coleta os dados dos campos
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        email = self.entry_email.get()
        senha = self.entry_password.get()
        data_nascimento = self.entry_data_nascimento.get()
        tipo_usuario_label = self.combo_tipo_usuario.get()
        
        # Validação básica
        if nome and cpf and email and senha and tipo_usuario_label and self.validate_date_format(data_nascimento):
            try:
                sucesso = cadastrar_usuario_completo(
                    nome,
                    cpf,
                    email,
                    senha,
                    tipo_usuario_label,
                    data_nascimento,
                    self.foto_info
                )
                if sucesso:
                    messagebox.showinfo("Cadastro", f"Usuário {nome} cadastrado com sucesso!")
                    self.destroy()
                else:
                    messagebox.showerror("Erro", "Falha ao cadastrar o usuário.")
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        else:
            messagebox.showerror("Erro", "Preencha todos os campos corretamente.")

    def user_random(self):
        randomUser = Usuario.generate_random()
        self.entry_nome.delete(0, tk.END)
        self.entry_nome.insert(0, randomUser.nome)
        self.entry_cpf.delete(0, tk.END)
        self.entry_cpf.insert(0, randomUser.cpf)
        self.entry_email.delete(0, tk.END)
        self.entry_email.insert(0, randomUser.email)
        self.entry_password.delete(0, tk.END)
        self.entry_password.insert(0, randomUser.senha)
        self.combo_tipo_usuario.set(TipoUsuario(randomUser.id_tipo_usuario).name)
        self.entry_data_nascimento.delete(0, tk.END)
        self.entry_data_nascimento.insert(0, randomUser.dt_nascimento.strftime('%Y-%m-%d'))

    def fechar(self):
        self.destroy()

if __name__ == "__main__":
    app = CadastroScreen()
    app.mainloop()
