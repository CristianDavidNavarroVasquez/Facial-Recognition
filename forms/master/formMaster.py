import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
from Recognition import reconocimiento_facial_en_carpeta
from Recognition import mostrar_lista

class MasterPanel:
 
                                      
    def __init__(self):   
        self.ventana = tk.Tk()                             
        self.ventana.title('MASTER PANEL')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 500)         

        logo =utl.leer_imagen("./imagenes/logo.png", (200, 200))
                        
        # label = tk.Label( self.ventana, image=logo,bg='#3a7ff6' )
        # label.place(x=0,y=0,relwidth=1, relheight=1)

        # #frameLogo
        frameLogo = tk.Frame(self.ventana, bd=0, width=400, relief=tk.SOLID, padx=10, pady=10, bg='#3a7ff6')
        frameLogo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frameLogo, image=logo, bg='#3a7ff6')
        label.place(x=0, y=0, relwidth=1, relheight=1)


        #frameForm
        frameForm = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frameForm.pack(side='right', expand=tk.YES, fill=tk.BOTH)

        #frameTop
        frameFormTop = tk.Frame(frameForm, height=50, bd=0, relief=tk.SOLID, bg='black')
        frameFormTop.pack(side="top", fill=tk.X)
        title = tk.Label(frameFormTop, text="BIENVENIDO", font=('Times', 30), fg="#666a88", bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #frameFormFill
        frameFormFill = tk.Frame(frameForm, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frameFormFill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        #Boton
        btn_tomar_lista  = tk.Button(frameFormFill, text="TOMAR LISTA", font=('Times', 15, BOLD), bg='#3a7ff6', bd=0, fg="#fff",command=reconocimiento_facial_en_carpeta )
        btn_tomar_lista.pack(fill=tk.X, padx=20, pady=20)
        # btn_tomar_lista.bind("<Button-1>", self.escuchar_tomar_lista)
        # inicio.bind("<Return>", (lambda event: self.verificar()))

        #Boton
        btn_administrar_lista = tk.Button(frameFormFill, text="ADMINISTRAR LISTA", font=('Times', 15, BOLD), bg='#3a7ff6', bd=0, fg="#fff",command=mostrar_lista)
        btn_administrar_lista.pack(fill=tk.X, padx=20, pady=20)
        # btn_administrar_lista.bind("<Button-1>", self.mostrar_lista)


        self.ventana.mainloop()
    def escuchar_tomar_lista( event):
        print("TOMAR LISTA ")
        reconocimiento_facial_en_carpeta()

    def mostrar_lista( event):
        print("ADMINISTRAR LISTA")
        mostrar_lista()
