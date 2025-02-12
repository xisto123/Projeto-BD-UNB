import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Services.Helper.window_size import set_window_size
from Enums.tipos_apoio import TipoCompeticao, TipoPartida, StatusPartida
import Models.equipe as Equipe
import Models.partida as Partida

class PartidaScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Partida")
        set_window_size(self, 0.8, 0.8)
        teams = self.carrega_times()
        self.times = [team.nome for team in teams]
        self.teams = {team.id_equipe: team.nome for team in teams}
        self.teams_inv = {nome: id_equipe for id_equipe, nome in self.teams.items()}
        self.match_ids = []
        self.current_match_id = None
        self.create_widgets()
        self.get_all_ids_partida() 

    def create_widgets(self):
        # Rótulo do cabeçalho
        header_label = tk.Label(self, text="Partida", font=("Helvetica", 16, "bold"))
        header_label.pack(pady=10)
        
        # Frame para seleção de ID da partida
        frame_selection = tk.Frame(self)
        frame_selection.pack(pady=5)
        lbl_select = tk.Label(frame_selection, text="Selecionar Partida ID:")
        lbl_select.pack(side=tk.LEFT, padx=5)
        self.combo_partida_id = ttk.Combobox(frame_selection, state="readonly")
        self.combo_partida_id.pack(side=tk.LEFT, padx=5)
        self.combo_partida_id.bind("<<ComboboxSelected>>", self.on_match_select)
        
        # Container principal para os campos de entrada
        self.container = tk.Frame(self)
        self.container.pack(pady=10)
        
        # Linha 0: Tipo de Competição, Time Mandante e Time Visitante
        lbl_tipo_competicao = tk.Label(self.container, text="Tipo de Competição:")
        lbl_tipo_competicao.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.combo_tipo_competicao = ttk.Combobox(
            self.container,
            values=[tc.name for tc in TipoCompeticao],
            state="disabled"
        )
        self.combo_tipo_competicao.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        lbl_time_mandante = tk.Label(self.container, text="Time Mandante:")
        lbl_time_mandante.grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.combo_time_mandante = ttk.Combobox(
            self.container,
            values=self.times,
            state="disabled"
        )
        self.combo_time_mandante.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        self.combo_time_mandante.bind("<<ComboboxSelected>>", self.update_combo_time_visitante)
        
        lbl_time_visitante = tk.Label(self.container, text="Time Visitante:")
        lbl_time_visitante.grid(row=0, column=4, padx=5, pady=5, sticky="e")
        self.combo_time_visitante = ttk.Combobox(
            self.container,
            values=self.times,
            state="disabled"
        )
        self.combo_time_visitante.grid(row=0, column=5, padx=5, pady=5, sticky="w")
        self.combo_time_visitante.bind("<<ComboboxSelected>>", self.update_combo_time_mandante)
        
        # Linha 1: Tipo de Partida e Status da Partida
        lbl_tipo_partida = tk.Label(self.container, text="Tipo de Partida:")
        lbl_tipo_partida.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.combo_tipo_partida = ttk.Combobox(
            self.container,
            values=[tp.name for tp in TipoPartida],
            state="disabled"
        )
        self.combo_tipo_partida.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        lbl_status_partida = tk.Label(self.container, text="Status da Partida:")
        lbl_status_partida.grid(row=1, column=2, padx=5, pady=5, sticky="e")
        self.combo_status_partida = ttk.Combobox(
            self.container,
            values=[sp.name for sp in StatusPartida],
            state="disabled"
        )
        self.combo_status_partida.grid(row=1, column=3, padx=5, pady=5, sticky="w")
        
        # Linha 2: Estádio e Data e Horário de Início
        lbl_estadio = tk.Label(self.container, text="Estádio:")
        lbl_estadio.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_estadio = tk.Entry(self.container, state="disabled")
        self.entry_estadio.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        lbl_horario_inicio = tk.Label(self.container, text="Data e Horário de Início (DD/MM/YYYY HH:MM):")
        lbl_horario_inicio.grid(row=2, column=2, padx=5, pady=5, sticky="e")
        self.entry_horario_inicio = tk.Entry(self.container, state="disabled")
        self.entry_horario_inicio.grid(row=2, column=3, padx=5, pady=5, sticky="w")
        
        # Linha 3: Botões - Editar, Salvar e Excluir
        self.btn_editar = tk.Button(self.container, text="Editar", command=self.enable_edit, state="disabled")
        self.btn_editar.grid(row=3, column=1, padx=5, pady=20)
        
        self.btn_salvar = tk.Button(self.container, text="Salvar", command=self.save_partida, state="disabled")
        self.btn_salvar.grid(row=3, column=2, padx=5, pady=20)
        
        self.btn_excluir = tk.Button(self.container, text="Excluir", command=self.delete_partida, state="disabled")
        self.btn_excluir.grid(row=3, column=3, padx=5, pady=20)
    
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
    
    def carrega_times(self):
        rows = Equipe.Equipe.get_all()
        return [Equipe.Equipe(*row) for row in rows]
    
    def get_all_ids_partida(self):
        matches = Partida.Partida.get_all()
        self.match_ids = []
        for match in matches:
            if isinstance(match, tuple):
                match_id = match[0]
            elif hasattr(match, 'id'):
                match_id = match.id
            else:
                match_id = None
            if match_id is not None:
                self.match_ids.append(match_id)
        self.combo_partida_id['values'] = self.match_ids

    def on_match_select(self, event):
        selected_id = self.combo_partida_id.get()
        if not selected_id:
            return
        match = Partida.Partida.get(selected_id)
        # Converte a tupla em objeto, se necessário
        if match and isinstance(match, tuple):
            match = Partida.Partida(*match)
        if match:
            self.current_match_id = selected_id
            self.combo_tipo_competicao.set(
                self.get_enum_name_from_id(TipoCompeticao, match.id_competicao)
            )
            self.combo_time_mandante.set(
                self.teams.get(match.id_time_mandante, "")
            )
            self.combo_time_visitante.set(
                self.teams.get(match.id_time_visitante, "")
            )
            self.combo_tipo_partida.set(
                self.get_enum_name_from_id(TipoPartida, match.id_tipo_partida)
            )
            self.combo_status_partida.set(
                self.get_enum_name_from_id(StatusPartida, match.id_status_partida)
            )
            self.entry_estadio.config(state="normal")
            self.entry_estadio.delete(0, tk.END)
            self.entry_estadio.insert(0, match.estadio)
            self.entry_estadio.config(state="disabled")
            self.entry_horario_inicio.config(state="normal")
            self.entry_horario_inicio.delete(0, tk.END)
            if match.dt_hora_inicio:
                self.entry_horario_inicio.insert(0, match.dt_hora_inicio.strftime("%d/%m/%Y %H:%M"))
            else:
                self.entry_horario_inicio.insert(0, "")
            self.entry_horario_inicio.config(state="disabled")
            self.set_fields_state("disabled")
            self.btn_editar.config(state="normal")
            self.btn_excluir.config(state="normal")
            self.btn_salvar.config(state="disabled")
        else:
            messagebox.showerror("Erro", "Partida não encontrada.")
    
    def set_fields_state(self, state):
        self.combo_tipo_competicao.config(state=state)
        self.combo_time_mandante.config(state=state)
        self.combo_time_visitante.config(state=state)
        self.combo_tipo_partida.config(state=state)
        self.combo_status_partida.config(state=state)
        self.entry_estadio.config(state=state)
        self.entry_horario_inicio.config(state=state)
    
    def enable_edit(self):
        if not self.current_match_id:
            return
        self.set_fields_state("normal")
        self.btn_salvar.config(state="normal")
        self.btn_editar.config(state="disabled")
    
    def get_enum_id_from_name(self, enum_class, name):
        for member in enum_class:
            if member.name == name:
                return member.value
        return None
    
    def get_enum_name_from_id(self, enum_class, id_val):
        for member in enum_class:
            if member.value == id_val:
                return member.name
        return ""

    def save_partida(self):
        if not self.current_match_id:
            return
        # Obtenção dos valores exibidos
        tipo_competicao_name = self.combo_tipo_competicao.get()
        time_mandante_name = self.combo_time_mandante.get()
        time_visitante_name = self.combo_time_visitante.get()
        tipo_partida_name = self.combo_tipo_partida.get()
        status_partida_name = self.combo_status_partida.get()
        estadio = self.entry_estadio.get()
        dt_horario_inicio = self.entry_horario_inicio.get()
        
        # Verifica se todos os campos foram preenchidos
        if not (
            tipo_competicao_name and time_mandante_name and time_visitante_name and
            tipo_partida_name and status_partida_name and estadio and dt_horario_inicio
        ):
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        # Conversão dos valores para os IDs esperados no banco (usando os métodos de mapeamento dos enums e dos times)
        id_tipo_competicao = self.get_enum_id_from_name(TipoCompeticao, tipo_competicao_name)
        id_tipo_partida = self.get_enum_id_from_name(TipoPartida, tipo_partida_name)
        id_status_partida = self.get_enum_id_from_name(StatusPartida, status_partida_name)
        id_time_mandante = self.teams_inv.get(time_mandante_name)
        id_time_visitante = self.teams_inv.get(time_visitante_name)

        # Monta um dicionário com os dados a atualizar
        data = {
            "id_competicao": id_tipo_competicao,
            "id_time_mandante": id_time_mandante,
            "id_time_visitante": id_time_visitante,
            "estadio": estadio,
            "dt_hora_inicio": dt_horario_inicio,
            "id_tipo_partida": id_tipo_partida,
            "id_status_partida": id_status_partida,
        }

        updated = Partida.Partida.update_by_pk(int(self.current_match_id), **data)
        if updated:
            messagebox.showinfo("Sucesso", "Partida atualizada com sucesso.")
            self.set_fields_state("disabled")
            self.btn_salvar.config(state="disabled")
            self.btn_editar.config(state="normal")
            self.get_all_ids_partida()
        else:
            messagebox.showerror("Erro", "Falha ao atualizar a partida.")

    def delete_partida(self):
        if not self.current_match_id:
            return
        try:
            deleted = Partida.Partida.delete_by_pk(int(self.current_match_id))
            if deleted:
                messagebox.showinfo("Sucesso", "Partida excluída com sucesso.")
                self.current_match_id = None
                self.clear_fields()
                self.get_all_ids_partida()
                self.btn_editar.config(state="disabled")
                self.btn_salvar.config(state="disabled")
                self.btn_excluir.config(state="disabled")
            else:
                messagebox.showerror("Erro", "Erro ao excluir partida.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir partida: {e}")
    
    def clear_fields(self):
        self.combo_tipo_competicao.set("")
        self.combo_time_mandante.set("")
        self.combo_time_visitante.set("")
        self.combo_tipo_partida.set("")
        self.combo_status_partida.set("")
        self.entry_estadio.delete(0, tk.END)
        self.entry_horario_inicio.delete(0, tk.END)

if __name__ == "__main__":
    app = PartidaScreen()
    app.mainloop()