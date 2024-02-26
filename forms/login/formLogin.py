import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.master.formMaster import MasterPanel


class App:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('INICIO DE SESION')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 500)

       

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200)) 

        # #frameLogo
        frameLogo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#3a7ff6')
        frameLogo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frameLogo, image=logo, bg='#3a7ff6')
        label.place(x=0, y=0, relwidth=1, relheight=1)


        #frameForm
        frameForm = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frameForm.pack(side='right', expand=tk.YES, fill=tk.BOTH)

        #frameTop
        frameFormTop = tk.Frame(frameForm, height=50, bd=0, relief=tk.SOLID, bg='black')
        frameFormTop.pack(side="top", fill=tk.X)
        title = tk.Label(frameFormTop, text="INICIO DE SESION", font=('Times', 30), fg="#666a88", bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #frameFormFill
        frameFormFill = tk.Frame(frameForm, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frameFormFill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        #EtiquetaUsuario
        etiquetaUsuario = tk.Label(frameFormFill, text="USUARIO", font=('Times', 14), fg="#666a88", bg='#fcfcfc',anchor="w")
        etiquetaUsuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frameFormFill, font=("Times", 14))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)

        #EtiquetaPassword
        etiquetaPassword = tk.Label(frameFormFill, text="CONTRASEÑA", font=('Times', 14), fg="#666a88", bg='#fcfcfc',anchor="w")
        etiquetaPassword.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frameFormFill, font=("Times", 14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")

        #Boton
        inicio = tk.Button(frameFormFill, text="INICIAR SESION", font=('Times', 15, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.verificar)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.verificar()))

        self.ventana.mainloop()
    
    def verificar(self):
        usuario = self.usuario.get()
        password = self.password.get()
        if(usuario == "root" and password == "1234"):
            self.ventana.destroy()
            MasterPanel()
        elif(usuario == "" and password == ""):
            messagebox.showerror(message="Ingrese datos", title="Mensaje")
        else:
            messagebox.showerror(message="La contraseña es incorrecta", title="Mensaje")
            