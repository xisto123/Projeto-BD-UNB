import tkinter as tk
import Models.aposta as Aposta
import Models.odd as Odd

from tkinter import ttk, messagebox
from Services.Helper.window_size import set_window_size
from Services import global_data

class ApostaScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tela de Aposta")
        set_window_size(self, 0.8, 0.7)
        self.current_bet_id = None
        self.create_widgets()
        self.load_user_bets()

    def create_widgets(self):
        # Container centralizado
        self.container = tk.Frame(self)
        self.container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Row 0: Combobox com as apostas do usuário
        lbl_user_bets = tk.Label(self.container, text="Minhas Apostas:")
        lbl_user_bets.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.combo_user_bets = ttk.Combobox(self.container, state="readonly")
        self.combo_user_bets.grid(row=0, column=1, padx=10, pady=5, columnspan=2, sticky="w")
        self.combo_user_bets.bind("<<ComboboxSelected>>", self.on_user_bet_select)
        
        # Row 1: Combobox para Odds (disponíveis para a aposta)
        lbl_odds = tk.Label(self.container, text="Odd:")
        lbl_odds.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.combo_odds = ttk.Combobox(self.container, state="disable")
        self.combo_odds.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.combo_odds.bind("<<ComboboxSelected>>", self.on_odds_select)
        
        # Row 2: Campos readonly para Odd Descrição e ID da Partida
        lbl_odd_desc = tk.Label(self.container, text="Descrição da Odd:",)
        lbl_odd_desc.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_odd_desc = tk.Entry(self.container, state="readonly", width=50)
        self.entry_odd_desc.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        
        lbl_match_id = tk.Label(self.container, text="ID da Partida:")
        lbl_match_id.grid(row=2, column=2, padx=10, pady=5, sticky="e")
        self.entry_match_id = tk.Entry(self.container, state="readonly")
        self.entry_match_id.grid(row=2, column=3, padx=10, pady=5, sticky="w")
        
        # Row 3: Campos readonly para Valor da Aposta e Resultado Esperado
        lbl_bet_amount = tk.Label(self.container, text="Valor da Aposta:")
        lbl_bet_amount.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_bet_amount = tk.Entry(self.container, state="readonly")
        self.entry_bet_amount.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        
        lbl_desired_result = tk.Label(self.container, text="Resultado Esperado:")
        lbl_desired_result.grid(row=3, column=2, padx=10, pady=5, sticky="e")
        self.entry_desired_result = tk.Entry(self.container, state="readonly")
        self.entry_desired_result.grid(row=3, column=3, padx=10, pady=5, sticky="w")
        
        # Row 4: Botões Editar, Salvar e Excluir na mesma linha, com espaçamento
        self.btn_edit = tk.Button(self.container, text="Editar", command=self.edit_bet, state="normal")
        self.btn_edit.grid(row=4, column=0, padx=15, pady=10)
        self.btn_save = tk.Button(self.container, text="Salvar", command=self.save_bet, state="disabled")
        self.btn_save.grid(row=4, column=1, padx=15, pady=10)
        self.btn_delete = tk.Button(self.container, text="Excluir", command=self.delete_bet, state="disabled")
        self.btn_delete.grid(row=4, column=2, padx=15, pady=10)
    
    def load_user_bets(self):
        # Carrega as apostas do usuário e preenche a combobox
        user_bets = Aposta.Aposta.get_by("id_usuario", global_data.usuario_id)
        self.user_bets = user_bets
        bet_ids = [bet[0] for bet in user_bets]
        self.combo_user_bets['values'] = bet_ids

    def on_user_bet_select(self, event):
        # Converte o valor selecionado para inteiro para comparação
        try:
            selected_id = int(self.combo_user_bets.get())
        except ValueError:
            selected_id = None
        selected_bet = next((bet for bet in self.user_bets if int(bet[0]) == selected_id), None)
        if selected_bet:
            self.current_bet_id = selected_bet[0]
            self.btn_edit.config(state="normal")
            self.btn_delete.config(state="normal")

            self.combo_odds.config(state="normal")
            self.combo_odds.set(selected_bet[2])  # id_odd na posição 2
            self.combo_odds.config(state="disable")

            odd = Odd.Odd.get(selected_bet[2])
            self.entry_odd_desc.config(state="normal")
            self.entry_odd_desc.delete(0, tk.END)
            self.entry_odd_desc.insert(0, odd[4])   #descricao da odd
            self.entry_odd_desc.config(state="readonly")

            self.entry_match_id.config(state="normal")
            self.entry_match_id.delete(0, tk.END)
            self.entry_match_id.insert(0, odd[1])   #id_partida da odd
            self.entry_match_id.config(state="readonly")

            self.entry_bet_amount.config(state="normal")
            self.entry_bet_amount.delete(0, tk.END)
            self.entry_bet_amount.insert(0, selected_bet[3])  # valor na posição 3
            self.entry_bet_amount.config(state="readonly")
            
            self.entry_desired_result.config(state="normal")
            self.entry_desired_result.delete(0, tk.END)
            self.entry_desired_result.insert(0, selected_bet[4])  # resultado na posição 4
            self.entry_desired_result.config(state="readonly")
            
    def edit_bet(self):
        # Permite que o usuário edite os campos de aposta
        self.entry_bet_amount.config(state="normal")
        self.entry_desired_result.config(state="normal")
        # Permite alterar a odd via combobox
        self.combo_odds.config(state="normal")
        odds = Odd.Odd.get_by("id_partida", int(self.entry_match_id.get()))
        # Armazena um dicionário: key = id da odd e value = descrição da odd
        self.odds_data = {str(odd[0]): odd[4] for odd in odds}
        
        # Atualiza a combobox com os ids disponíveis
        self.combo_odds['values'] = list(self.odds_data.keys())

        self.btn_save.config(state="normal")
        self.btn_edit.config(state="disabled")
        self.btn_delete.config(state="disabled")
        
    def on_odds_select(self, event):
        # Quando o usuário seleciona uma odd, atualiza o campo de descrição da odd
        selected_id = self.combo_odds.get()
        if selected_id in self.odds_data:
            self.entry_odd_desc.config(state="normal")
            self.entry_odd_desc.delete(0, tk.END)
            self.entry_odd_desc.insert(0, self.odds_data[selected_id])
            self.entry_odd_desc.config(state="readonly")

    def save_bet(self):
        bet_amount = self.entry_bet_amount.get()
        desired_result = self.entry_desired_result.get()
        selected_odds = self.combo_odds.get()
        
        if not (bet_amount and desired_result and selected_odds):
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return
        
        if hasattr(self, "current_bet_id"):
            data = {
                "id_odd": selected_odds,
                "valor": bet_amount,
                "resultado": desired_result,
            }
    
            updated = Aposta.Aposta.update_by_pk(int(self.current_bet_id), **data)
            if updated:
                messagebox.showinfo("Sucesso", "Aposta atualizada com sucesso!")
                del self.current_bet_id
            else:
                messagebox.showerror("Erro", "Falha ao atualizar a aposta.")
        else:
            messagebox.showerror("Erro", "Nenhuma aposta selecionada para atualização.")
        self.clear_fields()
    
    def delete_bet(self):
        if not hasattr(self, "current_bet_id"):
            messagebox.showerror("Erro", "Nenhuma aposta selecionada para exclusão.")
            return
        
        deleted = Aposta.Aposta.delete_by_pk(int(self.current_bet_id))
        if deleted:
            messagebox.showinfo("Sucesso", "Aposta excluída com sucesso!")
            del self.current_bet_id
        else:
            messagebox.showerror("Erro", "Erro ao excluir aposta.")
        self.clear_fields()
    
    def clear_fields(self):
        self.combo_user_bets.set("")
        self.combo_odds.set("")
        self.entry_odd_desc.config(state="normal")
        self.entry_odd_desc.delete(0, tk.END)
        self.entry_odd_desc.config(state="readonly")
        self.entry_match_id.config(state="normal")
        self.entry_match_id.delete(0, tk.END)
        self.entry_match_id.config(state="readonly")
        self.entry_bet_amount.config(state="normal")
        self.entry_bet_amount.delete(0, tk.END)
        self.entry_bet_amount.config(state="readonly")
        self.entry_desired_result.config(state="normal")
        self.entry_desired_result.delete(0, tk.END)
        self.btn_edit.config(state="disabled")
        self.btn_delete.config(state="disabled")

if __name__ == "__main__":
    app = ApostaScreen()
    app.mainloop()
