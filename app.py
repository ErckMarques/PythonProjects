from customtkinter import CTk, CTkButton, CTkEntry, CTkLabel, CTkToplevel, StringVar, CTkSwitch
from tela_login import Login
from nova_entrada import NovaEntrada

class App(CTk):
    def __init__(self,):
        super().__init__()
        
        self.title("Caixa - Mocidade El-Shadday")
        # self._set_appearance_mode("dark")
        self.geometry("500x450")
        
        self.configure_grid()
        self.widgets()

    def configure_grid(self):
        for i in range(4):
            self.columnconfigure(i, weight=1)
        for j in range(4):
            self.rowconfigure(j, weight=1)

    def widgets(self):
        # Adicionar um controle não abrir mais de 1 tela, em todas as telas.
        CTkButton(self, text="Login", command=lambda: Login(self)).grid(column=0, row=0,)
        CTkButton(self, text="Nova Entrada", command=lambda: NovaEntrada(self)).grid(column=3, row=3,)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()