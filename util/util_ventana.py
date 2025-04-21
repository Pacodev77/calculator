# Funccion para centrar la ventana de la app

def centrar_ventana(ventana,ancho_v,alto_v):
    ancho_p = ventana.winfo_screenwidth()
    alto_p = ventana.winfo_screenheight()
    x = (ancho_p-ancho_v) //2
    y = (alto_p-alto_v) //2
    ventana.geometry(f'{ancho_v}x{alto_v}+{x}+{y}')














