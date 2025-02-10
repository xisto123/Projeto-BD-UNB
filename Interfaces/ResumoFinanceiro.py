import tkinter as tk
from tkinter import ttk, messagebox
from Services.Helper.window_size import set_window_size
from Database.repository import get_connection

class AdminResumoFinanceiroScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Resumo Financeiro dos Usuários")
        set_window_size(self, 0.9, 0.8)
        self.create_widgets()
        self.carregar_dados()

    def create_widgets(self):
        # Container principal
        self.container = tk.Frame(self)
        self.container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Define as colunas da tabela (Treeview)
        columns = (
            "ID Usuário", "Nome do Usuário", "Saldo Atual", "Total de Transações",
            "Total de Pagamentos", "Total de Depósitos", "Total de Retiradas",
            "Total de Bonus", "Total de Reembolsos", "Fluxo Líquido", "Média Valor Transação"
        )
        self.tree = ttk.Treeview(self.container, columns=columns, show="headings")
        
        # Configura os cabeçalhos e as larguras
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Botão para atualizar os dados
        self.btn_refresh = tk.Button(self.container, text="Atualizar", command=self.carregar_dados)
        self.btn_refresh.pack(pady=10)

    def carregar_dados(self):
        # Remove itens existentes
        for item in self.tree.get_children():
            self.tree.delete(item)
        try:
            conn = get_connection()
            cursor = conn.cursor()
            # Consulta a view de resumo financeiro
            cursor.execute("SELECT * FROM vw_resumo_financeiro;")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=row)
            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar os dados: {e}")

if __name__ == "__main__":
    app = AdminResumoFinanceiroScreen()
    app.mainloop()
