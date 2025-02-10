import tkinter as tk
from tkinter import ttk
from Services.Helper.window_size import set_window_size
from Services.detalhes_times_service import DetalhesTimesService

class DetalhesTimesScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Detalhes Times")
        set_window_size(self, 0.8, 0.7)
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.service = DetalhesTimesService()
        self.create_widgets()
        self.populate_table()

    def create_widgets(self):
        columns = (
            "Time",
            "Partidas Jogadas",
            "Vitórias",
            "Empates",
            "Derrotas",
            "Gols Marcados",
            "Gols Sofridos",
            "Saldo de Gols",
            "Cartões Amarelos",
            "Cartões Vermelhos"
        )
        self.table = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=120, anchor="center")
        self.table.pack(fill="both", expand=True)

    def populate_table(self):
        # Recupera os dados via serviço
        rows = self.service.get_detalhes_times()
        for row in rows:
            self.table.insert("", "end", values=row)

    def on_close(self):
        self.destroy()

if __name__ == "__main__":
    app = DetalhesTimesScreen()
    app.mainloop()