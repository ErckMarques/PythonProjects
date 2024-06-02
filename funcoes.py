import customtkinter as ctk
from customtkinter import StringVar, CTkToplevel, CTk
from tkcalendar import Calendar

def limpar_widgets(*string_vars: StringVar) -> None:
    for string_var in string_vars:
        if isinstance(string_var, StringVar): 
            string_var.set("") if string_var.__dict__["_name"] != "var_velue" else string_var.set("R$ ")

def pegar_data(master: CTk, string_var: StringVar) -> None:
    def selecionar_data():
        data_selecionada = cal.get_date()
        string_var.set(data_selecionada)
        sub.destroy()
    
    sub = CTkToplevel(master)
    sub.title("Selecionar Data")
    sub.grab_set()
    sub.geometry("271x251+953+116")
    sub.resizable(False, False)

    cal = Calendar(sub, selectmode="day", locale="pt_br.UTF-8")
    cal.pack(padx=10, pady=10)
    
    btn_selecionar = ctk.CTkButton(sub, text="Selecionar Data", command=selecionar_data)
    btn_selecionar.pack(pady=10)


if __name__ == "__main__":
    ...
