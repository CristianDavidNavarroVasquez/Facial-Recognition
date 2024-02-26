from PIL import ImageTk, Image

def leer_imagen( path, size): 
        return ImageTk.PhotoImage(Image.open(path).resize(size, Image.BILINEAR))





def centrar_ventana(ventana,aplicacion_ancho,aplicacion_largo):    
    pantallAncho = ventana.winfo_screenwidth()
    pantallLargo = ventana.winfo_screenheight()
    x = int((pantallAncho/2) - (aplicacion_ancho/2))
    y = int((pantallLargo/2) - (aplicacion_largo/2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")
