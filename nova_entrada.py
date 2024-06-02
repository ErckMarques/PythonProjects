import customtkinter as ctk
from tkinter import StringVar
from datetime import datetime
from funcoes import limpar_widgets, pegar_data

class NovaEntrada(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Registrar Nova Entrada")
        self.geometry("600x300+900+90")
        self.configure(bg_color="#FFC458")

        self.setup_variables()
        self.setup_grid()
        self.create_widgets()

    def setup_variables(self):
        self.var_date = StringVar(self, name="var_date")
        self.var_date.set(datetime.now().strftime("%d/%m/%Y"))
        self.var_quem = StringVar(self, name="var_quem")
        self.var_quem.set("Erik")
        self.var_velue = StringVar(self, name="var_velue")
        self.var_velue.set("R$ ")
        self.var_obs = StringVar(self, name="var_obs")
        self.var_tipo = StringVar(self, name="var_tipo")
        self.var_formato = StringVar(self, name="var_formato")

    def setup_grid(self):
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)

    def create_widgets(self):
        options_label = {'padx': (10, 4), 'pady': (4, 5), 'sticky': "ew"}
        fonte_subtitle = ctk.CTkFont(family="Helvetica", size=14)

        # Data
        ctk.CTkLabel(self, text="Data", font=fonte_subtitle).grid(column=0, row=0, **options_label)
        ctk.CTkEntry(self, textvariable=self.var_date).grid(column=1, row=0, sticky="w")
        btn_cal = ctk.CTkButton(self, text="Calendário", command=lambda: pegar_data(self, self.var_date))
        btn_cal.grid(column=2, row=0, sticky="w")

        # Valor
        ctk.CTkLabel(self, text="Valor", font=fonte_subtitle).grid(column=0, row=1, **options_label)
        ctk.CTkEntry(self, textvariable=self.var_velue).grid(column=1, row=1, sticky="w")

        # Feito Por
        ctk.CTkLabel(self, text="Feito Por", font=fonte_subtitle).grid(column=0, row=2, **options_label)
        ctk.CTkEntry(self, textvariable=self.var_quem).grid(column=1, row=2, sticky="w")

        # Tipo da Movimentação
        lbf = ctk.CTkFrame(self)
        lbf.grid(column=3, row=0, rowspan=2)
        ctk.CTkLabel(lbf, text="Tipo da Movimentação", font=fonte_subtitle).grid(column=0, row=0, padx=(0,20))
        for idx, valor in enumerate(("Entrada", "Saída")):
            radio = ctk.CTkRadioButton(lbf, text=valor, variable=self.var_tipo, value=valor)
            radio.grid(column=0, row=idx + 1, ipadx=3, ipady=3, padx=3, pady=3, sticky="w")

        # Formato
        lbf_1 = ctk.CTkFrame(self)
        lbf_1.grid(column=3, row=2)
        ctk.CTkLabel(lbf_1, text="Formato", font=fonte_subtitle).grid(column=0, row=0)
        for idx, valor in enumerate(("Pix", "Dinheiro")):
            radio = ctk.CTkRadioButton(lbf_1, text=valor, variable=self.var_formato, value=valor)
            radio.grid(column=0, row=idx + 1, ipadx=3, ipady=3, padx=3, pady=3)

        # Descrição
        ctk.CTkLabel(self, text="Descrição", font=fonte_subtitle).grid(column=0, row=3, **options_label)
        self.txt = ctk.CTkTextbox(self, width=40, height=2.5, font=("Helvetica", 10))
        self.txt.grid(column=1, row=3, columnspan=2, padx=(0, 8), pady=(0, 8), sticky="news")

        # Link the StringVar to the Text widget
        self.var_obs.trace_add("write", self.update_text_widget)
        self.txt.bind("<Control-A>", lambda event: self.select_all_text())
        self.txt.bind("<<Modified>>", self.update_stringvar)

        # Botões
        ctk.CTkButton(self, text="Salvar", command=lambda: print("Salvando Dados")).grid(column=0, row=4)
        ctk.CTkButton(self, text="Limpar", command=self.clear_widgets).grid(column=1, row=4, sticky="e")

    def update_text_widget(self, *args):
        self.txt.delete("1.0", "end")
        self.txt.insert("1.0", self.var_obs.get())

    def update_stringvar(self, event=None):
        if self.txt.edit_modified():
            self.var_obs.set(self.txt.get("1.0", "end-1c"))
            self.txt.edit_modified(False)

    def select_all_text(self):
        self.txt.tag_add("sel", "1.0", "end")

    def clear_widgets(self):
        limpar_widgets(self.var_date, self.var_quem, self.var_velue, self.var_formato, self.var_tipo, self.var_obs)


if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("green")
    
    root = ctk.CTk()
    app = NovaEntrada(master=root)
    app.mainloop()
