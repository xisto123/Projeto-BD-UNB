import os
import mimetypes
import datetime
import tkinter as tk
from tkinter import messagebox
from Services.Helper.window_size import set_window_size
from Enums.tipos_apoio import TipoUsuario
from Models.usuario import Usuario
import Services.global_data as global_data
import Models.arquivo as Arquivo
from PIL import Image, ImageTk
import io

class PerfilScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Perfil")
        set_window_size(self, 0.8, 0.7)
        self.create_widgets()
        self.buscar_usuario()

    def create_widgets(self):
        # Frame superior para exibir a foto do usuário centralizada horizontalmente
        top_frame = tk.Frame(self)
        top_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

        # Inicialmente, exibe mensagem caso a foto não esteja disponível
        self.lbl_foto = tk.Label(top_frame, text="Foto não disponível", width=200, height=200, relief="solid")
        self.lbl_foto.pack(anchor="center")

        # Container principal centralizado
        self.container = tk.Frame(self)
        self.container.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
        
        # Linha 1: Nome e CPF
        self.label_nome = tk.Label(self.container, text="Nome:")
        self.label_nome.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.lbl_nome_valor = tk.Label(self.container, text="", relief="sunken", width=30)
        self.lbl_nome_valor.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        
        self.label_cpf = tk.Label(self.container, text="CPF:")
        self.label_cpf.grid(row=1, column=2, padx=10, pady=10, sticky="e")
        self.lbl_cpf_valor = tk.Label(self.container, text="", relief="sunken", width=30)
        self.lbl_cpf_valor.grid(row=1, column=3, padx=10, pady=10, sticky="w")
        
        # Linha 2: Email e Senha
        self.label_email = tk.Label(self.container, text="Email:")
        self.label_email.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.lbl_email_valor = tk.Label(self.container, text="", relief="sunken", width=30)
        self.lbl_email_valor.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        
        self.label_password = tk.Label(self.container, text="Senha:")
        self.label_password.grid(row=2, column=2, padx=10, pady=10, sticky="e")
        self.lbl_password_valor = tk.Label(self.container, text="", relief="sunken", width=30)
        self.lbl_password_valor.grid(row=2, column=3, padx=10, pady=10, sticky="w")
        
        # Linha 3: Tipo de Usuário e Data de Nascimento
        self.label_tipo_usuario = tk.Label(self.container, text="Tipo de Usuário:")
        self.label_tipo_usuario.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.lbl_tipo_usuario_valor = tk.Label(self.container, text="", relief="sunken", width=30)
        self.lbl_tipo_usuario_valor.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        
        self.label_data_nascimento = tk.Label(self.container, text="Data de Nascimento:")
        self.label_data_nascimento.grid(row=3, column=2, padx=10, pady=10, sticky="e")
        self.lbl_data_nascimento_valor = tk.Label(self.container, text="", relief="sunken", width=30)
        self.lbl_data_nascimento_valor.grid(row=3, column=3, padx=10, pady=10, sticky="w")
        
        # Linha 4: Botões de Excluir e Editar
        self.button_frame = tk.Frame(self.container)
        self.button_frame.grid(row=4, column=0, columnspan=4, pady=20)
        
        self.btn_excluir = tk.Button(self.button_frame, text="Excluir", command=self.excluir_usuario, borderwidth=10)
        self.btn_excluir.pack(side=tk.LEFT, padx=5)
        
        self.btn_editar = tk.Button(self.button_frame, text="Editar", command=self.editar_usuario, borderwidth=10)
        self.btn_editar.pack(side=tk.LEFT, padx=5)

    def buscar_usuario(self):
        usuario = Usuario.get_by_id(global_data.usuario_id)
        if usuario:
            self.lbl_nome_valor.config(text=usuario.nome)
            self.lbl_cpf_valor.config(text=usuario.cpf)
            self.lbl_email_valor.config(text=usuario.email)
            self.lbl_password_valor.config(text=usuario.senha)
            self.lbl_tipo_usuario_valor.config(text=TipoUsuario(usuario.id_tipo_usuario).name)
            self.lbl_data_nascimento_valor.config(text=usuario.dt_nascimento)
            
            # Busca a foto do usuário na tabela Arquivo utilizando o método get_by
            arquivo_records = Arquivo.Arquivo.get_by("id_usuario", usuario.id_usuario)
            if arquivo_records and len(arquivo_records) > 0:
                # Supondo que a coluna na posição 6 contenha os dados binários da imagem
                arquivo = arquivo_records[0]
                foto_binary = arquivo[6]
                try:
                    # Converte os dados binários em imagem
                    image = Image.open(io.BytesIO(foto_binary))

                    # **FORÇA O TAMANHO EXATO DA IMAGEM** (400x400 pixels)
                    image = image.resize((350, 350), Image.LANCZOS)

                    # Converte para o formato Tkinter
                    photo = ImageTk.PhotoImage(image)

                    # Define a imagem na Label
                    self.lbl_foto.config(image=photo, text="", width=400, height=400)
                    self.lbl_foto.image = photo  # Mantém referência para evitar garbage collection
                except Exception as e:
                    self.lbl_foto.config(text="Erro ao carregar foto")
                    print("Erro ao converter foto:", e)
            else:
                self.lbl_foto.config(text="Foto não disponível")
        else:
            messagebox.showerror("Erro", "Usuário não encontrado.")

    def excluir_usuario(self):
        resposta = messagebox.askyesno("Confirmação", "Deseja excluir o usuário?")
        if resposta:
            if Usuario.excluir(global_data.usuario_id):
                messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!")
                self.destroy()
            else:
                messagebox.showerror("Erro", "Não foi possível excluir o usuário.")

    def editar_usuario(self):
        try:
            self.destroy()
            from Interfaces.Usuario.EditarUsuario import EditarUsuarioScreen
            tela_edicao = EditarUsuarioScreen()
            tela_edicao.mainloop()
        except ImportError:
            messagebox.showerror("Erro", "Tela de edição não encontrada.")

if __name__ == "__main__":
    app = PerfilScreen()
    app.mainloop()
