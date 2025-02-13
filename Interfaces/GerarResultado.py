import tkinter as tk
from tkinter import ttk, messagebox
from Services.Helper.window_size import set_window_size
import Models.partida as Partida
import Models.equipe as Equipe
import Services.encerrar_partida_service as encerrar_service

class GerarResultadoScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Encerrar Partida")
        set_window_size(self, 0.8, 0.7)
        self.current_match = None
        self.create_widgets()
        self.load_matches_in_progress()

    def create_widgets(self):
        # Container principal
        self.container = tk.Frame(self)
        self.container.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Linha 0: Combobox para selecionar partidas em andamento
        lbl_matches = tk.Label(self.container, text="Selecione uma Partida (Em Andamento):")
        lbl_matches.grid(row=0, column=0, columnspan=2, pady=5)
        self.combo_matches = ttk.Combobox(self.container, state="readonly")
        self.combo_matches.grid(row=0, column=2, columnspan=2, pady=5, sticky="we")
        self.combo_matches.bind("<<ComboboxSelected>>", self.on_match_select)
        
        # Linha 1: Painéis para os times (mandante e visitante)
        self.frame_home = tk.LabelFrame(self.container, text="Time Mandante", padx=10, pady=10)
        self.frame_home.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        self.frame_away = tk.LabelFrame(self.container, text="Time Visitante", padx=10, pady=10)
        self.frame_away.grid(row=1, column=2, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        # Configure grid para distribuição equitativa
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=1)
        self.container.grid_columnconfigure(2, weight=1)
        self.container.grid_columnconfigure(3, weight=1)
        
        # Adiciona um label para exibir o nome do time em cada painel (linha superior de cada frame)
        self.lbl_home_team = tk.Label(self.frame_home, text="", font=("Helvetica", 12, "bold"))
        self.lbl_home_team.grid(row=0, column=0, columnspan=2, pady=5)
        self.lbl_away_team = tk.Label(self.frame_away, text="", font=("Helvetica", 12, "bold"))
        self.lbl_away_team.grid(row=0, column=0, columnspan=2, pady=5)
        
        # Define os campos de resultado para cada time (a partir da linha 1 em cada frame)
        self.fields = ["Gols", "Cartões Amarelos", "Cartões Vermelhos", "Escanteios", "Impedimentos", "Faltas Cometidas"]
        self.home_entries = {}
        self.away_entries = {}
        for idx, field in enumerate(self.fields, start=1):
            # Para time mandante
            lbl_home = tk.Label(self.frame_home, text=field + ":")
            lbl_home.grid(row=idx, column=0, sticky="e", pady=2)
            entry_home = tk.Entry(self.frame_home, width=10)
            entry_home.grid(row=idx, column=1, pady=2, padx=5)
            self.home_entries[field] = entry_home

            # Para time visitante
            lbl_away = tk.Label(self.frame_away, text=field + ":")
            lbl_away.grid(row=idx, column=0, sticky="e", pady=2)
            entry_away = tk.Entry(self.frame_away, width=10)
            entry_away.grid(row=idx, column=1, pady=2, padx=5)
            self.away_entries[field] = entry_away
        
        # Linha 2: Botão para Salvar Resultado
        self.btn_salvar = tk.Button(self.container, text="Salvar Resultado", command=self.salvar_resultado)
        self.btn_salvar.grid(row=2, column=0, columnspan=4, pady=15)
    
    def load_matches_in_progress(self):
        try:
            # Retorna partidas com status 2 (em andamento)
            self.matches = Partida.Partida.get_by("id_status_partida", 2)
            match_ids = [str(match[0]) for match in self.matches]
            self.combo_matches['values'] = match_ids
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar partidas: {e}")
            self.matches = []
    
    def on_match_select(self, event):
        selected_id = self.combo_matches.get()
        self.current_match = next((match for match in self.matches if str(match[0]) == selected_id), None)
        if self.current_match:
            # Supondo que a partida possui id_time_mandante e id_time_visitante nos índices 2 e 3
            home_id = self.current_match[2]
            away_id = self.current_match[3]
            self.lbl_home_team.config(text=Equipe.Equipe.get_nome_by_id(home_id))
            self.lbl_away_team.config(text=Equipe.Equipe.get_nome_by_id(away_id))
        else:
            messagebox.showerror("Erro", "Partida não encontrada.")
    
    def salvar_resultado(self):
        if not self.current_match:
            messagebox.showerror("Erro", "Nenhuma partida selecionada.")
            return
        
        try:
            # Coleta os valores inseridos nos campos, convertendo para int
            home_data = { field: int(self.home_entries[field].get()) for field in self.fields }
            away_data = { field: int(self.away_entries[field].get()) for field in self.fields }
        except ValueError:
            messagebox.showerror("Erro", "Certifique-se de que os campos possuem valores numéricos.")
            return
        
        # Chama o serviço encerrar_partida passando a id_partida e os resultados para cada time
        try:
            sucesso = encerrar_service.encerrar_partida(
                p_id_partida = self.current_match[0],
                p_gols_mandante = int(home_data["Gols"]),
                p_gols_visitante = int(away_data["Gols"]),
                p_cartoes_amarelos_mandante = int(home_data["Cartões Amarelos"]),
                p_cartoes_amarelos_visitante = int(away_data["Cartões Amarelos"]),
                p_cartoes_vermelhos_mandante = int(home_data["Cartões Vermelhos"]),
                p_cartoes_vermelhos_visitante = int(away_data["Cartões Vermelhos"]),
                p_escanteios_mandante = int(home_data["Escanteios"]),
                p_escanteios_visitante = int(away_data["Escanteios"]),
                p_impedimentos_mandante = int(home_data["Impedimentos"]),
                p_impedimentos_visitante = int(away_data["Impedimentos"]),
                p_faltas_mandante = int(home_data["Faltas Cometidas"]),
                p_faltas_visitante = int(away_data["Faltas Cometidas"])
            )
            if sucesso:
                messagebox.showinfo("Sucesso", "Resultado salvo com sucesso!")
            else:
                messagebox.showerror("Erro", "Falha ao salvar resultado.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar resultado: {e}")

if __name__ == "__main__":
    app = GerarResultadoScreen()
    app.mainloop()
