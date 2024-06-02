from customtkinter import CTk, CTkButton, CTkEntry, CTkLabel, CTkToplevel, StringVar, CTkSwitch

class Login(CTkToplevel):
    def __init__(self, master: CTk):
        super().__init__(master)
        
        self.title("Login")
        self.geometry("300x110")

        self.user = StringVar(name="var_user")
        self.senha = StringVar(name="var_senha")
        self.mode = StringVar(value="off", name="var_mode")

        self.configure_grid()
        self.widgets()
        
    def configure_grid(self):
        for i in range(3):
            self.rowconfigure(i)
        for j in range(2):
            self.columnconfigure(j)
    
    def widgets(self):
        # usuario
        CTkLabel(self, text="Usuário", ).grid(column=0, row=0, padx=(2,5), pady=(0,5))
        CTkEntry(self, textvariable=self.user).grid(column=1, row=0)
        # senha
        CTkLabel(self, text="Senha", ).grid(column=0, row=1, padx=(0,5), pady=(0,5))
        CTkEntry(self, show="*",textvariable=self.senha).grid(column=1, row=1)
        # login
        CTkButton(self, text="Login", command=lambda: print(self.geometry())).grid(column=1, row=2, pady=(5,0))
        # dark/light mode
        CTkSwitch(self, text="Dark",
                  command=self._appearence,
                  textvariable=self.mode,
                  onvalue="on", offvalue="off"
                  ).grid(column=0, row=2, padx=(20,0), sticky="e")
        
    def _appearence(self):
        self._set_appearance_mode("dark") if self.mode.get() == "on" else self._set_appearance_mode("light")

if __name__ == "__main__":
    root = CTk()
    login = Login(root)
    root.mainloop()