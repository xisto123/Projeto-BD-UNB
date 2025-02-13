import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Services.Helper.window_size import set_window_size
from Enums.tipos_apoio import TipoCompeticao, TipoPartida, StatusPartida
import Models.equipe as Equipe
import Models.partida as Partida

class CriarPartidaScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Criar Partida")
        set_window_size(self, 0.8, 0.7)
        # Cria a lista de times e um mapeamento do nome para o id da equipe
        times_obj = self.carrega_times()
        self.times = [t.nome for t in times_obj]
        self.times_mapping = {t.nome: t.id_equipe for t in times_obj}
        self.create_widgets()
    
    def create_widgets(self):
        # Header label at the top da página
        header_label = tk.Label(self, text="Criar Partida", font=("Helvetica", 16, "bold"))
        header_label.pack(pady=10)
        
        # Container principal centralizado
        self.container = tk.Frame(self)
        self.container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Linha 0: Tipo de Competição, Time Mandante e Time Visitante
        lbl_tipo_competicao = tk.Label(self.container, text="Tipo de Competição:")
        lbl_tipo_competicao.grid(row=0, column=0, padx=5, pady=20, sticky="e")
        self.combo_tipo_competicao = ttk.Combobox(
            self.container, 
            values=[tc.name for tc in TipoCompeticao],
            state="readonly")
        self.combo_tipo_competicao.grid(row=0, column=1, padx=5, pady=20, sticky="w")
        
        lbl_time_mandante = tk.Label(self.container, text="Time Mandante:")
        lbl_time_mandante.grid(row=0, column=2, padx=5, pady=20, sticky="e")
        self.combo_time_mandante = ttk.Combobox(
            self.container,
            values=self.times,
            state="readonly")
        self.combo_time_mandante.grid(row=0, column=3, padx=5, pady=20, sticky="w")
        self.combo_time_mandante.bind("<<ComboboxSelected>>", self.update_combo_time_visitante)
        
        lbl_time_visitante = tk.Label(self.container, text="Time Visitante:")
        lbl_time_visitante.grid(row=0, column=4, padx=5, pady=20, sticky="e")
        self.combo_time_visitante = ttk.Combobox(
            self.container,
            values=self.times,
            state="readonly")
        self.combo_time_visitante.grid(row=0, column=5, padx=5, pady=20, sticky="w")
        self.combo_time_visitante.bind("<<ComboboxSelected>>", self.update_combo_time_mandante)
        
        # Linha 1: Tipo de Partida e Status da Partida
        lbl_tipo_partida = tk.Label(self.container, text="Tipo de Partida:")
        lbl_tipo_partida.grid(row=1, column=0, padx=5, pady=20, sticky="e")
        self.combo_tipo_partida = ttk.Combobox(
            self.container,
            values=[tp.name for tp in TipoPartida],
            state="readonly")
        self.combo_tipo_partida.grid(row=1, column=1, padx=5, pady=20, sticky="w")
        
        lbl_status_partida = tk.Label(self.container, text="Status da Partida:")
        lbl_status_partida.grid(row=1, column=2, padx=5, pady=20, sticky="e")
        self.combo_status_partida = ttk.Combobox(
            self.container,
            values=[sp.name for sp in StatusPartida],
            state="readonly")
        self.combo_status_partida.grid(row=1, column=3, padx=5, pady=20, sticky="w")
        
        # Linha 2: Estádio e Data e Horário de Início
        lbl_estadio = tk.Label(self.container, text="Estádio:")
        lbl_estadio.grid(row=2, column=0, padx=5, pady=20, sticky="e")
        self.entry_estadio = tk.Entry(self.container)
        self.entry_estadio.grid(row=2, column=1, padx=5, pady=20, sticky="w")
        
        lbl_horario_inicio = tk.Label(self.container, text="Data e Horário de Início (YYYY-MM-DD HH:MM:SS):")
        lbl_horario_inicio.grid(row=2, column=2, padx=5, pady=20, sticky="e")
        self.entry_horario_inicio = tk.Entry(self.container)
        self.entry_horario_inicio.grid(row=2, column=3, padx=5, pady=20, sticky="w")
        
        # Linha 3: Botão para Criar Partida
        self.btn_criar = tk.Button(self.container, text="Criar Partida", command=self.criar_partida)
        self.btn_criar.grid(row=3, column=0, columnspan=6, pady=20)
    
    def update_combo_time_visitante(self, event):
        selected_mandante = self.combo_time_mandante.get()
        new_values = [team for team in self.times if team != selected_mandante]
        self.combo_time_visitante['values'] = new_values
        if self.combo_time_visitante.get() == selected_mandante:
            self.combo_time_visitante.set("")
    
    def update_combo_time_mandante(self, event):
        selected_visitante = self.combo_time_visitante.get()
        new_values = [team for team in self.times if team != selected_visitante]
        self.combo_time_mandante['values'] = new_values
        if self.combo_time_mandante.get() == selected_visitante:
            self.combo_time_mandante.set("")
    
    def criar_partida(self):
        tipo_competicao = self.combo_tipo_competicao.get()
        time_mandante = self.combo_time_mandante.get()
        time_visitante = self.combo_time_visitante.get()
        tipo_partida = self.combo_tipo_partida.get()
        status_partida = self.combo_status_partida.get()
        estadio = self.entry_estadio.get()
        horario_inicio = self.entry_horario_inicio.get()
        
        if not (tipo_competicao and time_mandante and time_visitante and tipo_partida and status_partida and estadio and horario_inicio):
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return
        
        data = {
            "id_competicao": TipoCompeticao[tipo_competicao].value,
            "id_time_mandante": self.times_mapping.get(time_mandante),
            "id_time_visitante": self.times_mapping.get(time_visitante),
            "estadio": estadio,
            "dt_hora_inicio": horario_inicio,
            "id_tipo_partida": TipoPartida[tipo_partida].value,
            "id_status_partida": StatusPartida[status_partida].value
        }

        if Partida.Partida.create(**data):
            messagebox.showinfo("Info", "Partida Criada com Sucesso.")
        else:
            messagebox.showerror("Erro", "Erro ao criar a partida.")
    
    def carrega_times(self):
        rows = Equipe.Equipe.get_all()
        return [Equipe.Equipe(*row) for row in rows]

if __name__ == "__main__":
    app = CriarPartidaScreen()
    app.mainloop()
