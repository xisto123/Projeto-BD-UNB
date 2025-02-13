import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import Models.odd as Odd
import Models.partida as Partida
import Services.global_data as global_data
from Models.carteira import Carteira
from Services.Helper.window_size import set_window_size
from Services.criar_aposta_service import criar_aposta

class CriarApostaScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Realizar Aposta")
        set_window_size(self, 0.8, 0.7)
        self.create_widgets()
 
    def create_widgets(self):
        # Header label
        header_label = tk.Label(self, text="Realizar Aposta", font=("Helvetica", 16, "bold"))
        header_label.pack(pady=10)
        
        # Container principal centralizado
        self.container = tk.Frame(self)
        self.container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Linha 0: Combobox para selecionar a partida (usando o id)
        lbl_partidas = tk.Label(self.container, text="Partida ID:")
        lbl_partidas.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.combo_partidas = ttk.Combobox(
            self.container, 
            values=[str(partida.id_partida) for partida in self.carrega_partidas()],
            state="readonly")
        self.combo_partidas.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.combo_partidas.bind("<<ComboboxSelected>>", self.on_partida_selected)
        
        # Linha 1: Campo para Odd com duas partes:
        # Combobox para selecionar a odd e campo readonly para exibir a descrição
        lbl_odd = tk.Label(self.container, text="Odd:")
        lbl_odd.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        
        # Combobox para seleção da odd (inicialmente desabilitada)
        self.combo_odds = ttk.Combobox(self.container, state="disabled")
        self.combo_odds.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.combo_odds.bind("<<ComboboxSelected>>", self.on_odd_selected)
        
        # Campo somente leitura para exibir a descrição da Odd
        self.entry_odd_desc = tk.Entry(self.container, state='disabled', width=50)
        self.entry_odd_desc.grid(row=1, column=2, padx=5, pady=5, sticky="w")
        
        # Linha 2: Campo para Valor da Aposta (inicialmente desabilitado)
        lbl_valor_aposta = tk.Label(self.container, text="Valor Aposta:")
        lbl_valor_aposta.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_valor_aposta = tk.Entry(self.container, state='disabled')
        self.entry_valor_aposta.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        # Linha 3: Campo para Resultado (inicialmente desabilitado)
        lbl_resultado = tk.Label(self.container, text="Resultado:")
        lbl_resultado.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_resultado = tk.Entry(self.container, state='disabled')
        self.entry_resultado.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        
        # Linha 4: Botão para criar a aposta (inicialmente desabilitado)
        self.btn_criar = tk.Button(self.container, text="Criar Aposta", state='disabled', command=self.criar_aposta)
        self.btn_criar.grid(row=4, column=0, columnspan=3, padx=5, pady=10)
    
    def on_partida_selected(self, event):
        selected_id = self.combo_partidas.get()
        if selected_id:
            self.id_partida = selected_id
            odds = self.carrega_odds()
            if odds:
                # Armazena a lista de odds para referência futura
                self.odds_list = odds
                # Habilita a combobox e atualiza seus valores (utilizando o id da odd no display)
                self.combo_odds.config(state="readonly")
                self.combo_odds['values'] = [str(odd.id_odd) for odd in odds]
                # Seleciona a primeira odd por padrão
                self.combo_odds.current(0)
                self.on_odd_selected(None)  # Atualiza o campo de descrição
                # Habilita os demais campos para preenchimento
                self.entry_valor_aposta.config(state='normal')
                self.entry_resultado.config(state='normal')
                self.btn_criar.config(state='normal')
            else:
                messagebox.showerror("Erro", "Nenhuma odd encontrada para a partida selecionada.")
    
    def on_odd_selected(self, event):
        index = self.combo_odds.current()
        if index >= 0:
            selected_odd = self.odds_list[index]
            self.odd = selected_odd
            # Atualiza o campo readonly com a descrição da odd selecionada
            self.entry_odd_desc.config(state='normal')
            self.entry_odd_desc.delete(0, tk.END)
            self.entry_odd_desc.insert(0, selected_odd.descricao)
            self.entry_odd_desc.config(state='readonly')
    
    def criar_aposta(self):
        id_usuario = global_data.usuario_id
        id_odd = self.odd.id_odd if hasattr(self, 'odd') else None
        valor = self.entry_valor_aposta.get().strip()
        resultado = self.entry_resultado.get().strip()
        
        # Validação simples: verificar se todos os campos foram preenchidos
        if not (id_usuario and id_odd and valor and resultado):
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return
        
        if not Carteira.verifica_saldo(global_data.usuario_id, valor):
            messagebox.showerror("Erro", "Usuario nao possui saldo suficiente.")
            return
        
        data = {
            "id_usuario": id_usuario,
            "id_odd": id_odd,
            "valor": valor,
            "resultado": resultado
        }

        if criar_aposta(**data):
            self.limpar_campos()
            messagebox.showinfo("Sucesso", "Aposta criada com sucesso!")
        else:
            messagebox.showerror("Erro", "Erro ao criar a aposta.")    

    def limpar_campos(self):
        self.combo_partidas.set('')
        self.combo_odds.set('')
        self.entry_odd_desc.config(state='normal')
        self.entry_odd_desc.delete(0, tk.END)
        self.entry_odd_desc.config(state='disabled')
        self.entry_valor_aposta.delete(0, tk.END)
        self.entry_valor_aposta.config(state='disabled')
        self.entry_resultado.delete(0, tk.END)
        self.entry_resultado.config(state='disabled')
        self.btn_criar.config(state='disabled')
    
    def carrega_partidas(self):
        rows = Partida.Partida.get_all()
        return [Partida.Partida(*row) for row in rows]
    
    def carrega_odds(self):
        rows = Odd.Odd.get_by("id_partida", self.id_partida)
        return [Odd.Odd(*row) for row in rows]

if __name__ == "__main__":
    app = CriarApostaScreen()
    app.mainloop()
