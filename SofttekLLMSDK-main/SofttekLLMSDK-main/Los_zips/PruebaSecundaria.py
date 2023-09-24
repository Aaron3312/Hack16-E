from tkinter import *

def nuevaVentana3():
    variable = StringVar()  
    ventana_nueva1 = Toplevel()
    ventana_nueva1.title("Busqueda de palabras claves")
    ventana_nueva1.iconbitmap("Logo.ico")
    miFrame2 = Frame(ventana_nueva1)
    #Frame 2

    miFrame2.pack(side="left", anchor="n")
    miFrame2.config(bg="#800080")

    miFrame2.config(width="350", height="650")
    miFrame2.config(bd=9)
    miFrame2.config(relief="groove")

    #Pregunta:
    miLabelp3 = Label(miFrame2, text="Inserte palabra clave",fg="#FFFFFF",bg = "#800080",font=("DejaVuSansMono-Bold",15))
    miLabelp3.grid(row = 0, column = 1, pady=10)
    #Entrada de texto
    EntradaDeText = Entry(miFrame2, width=10)
    EntradaDeText.grid(row=2, column=1, pady=10)
    #Boton
    def boton():
        TercerVentana = Toplevel()
        TercerVentana.geometry("400x200")
        variable= EntradaDeText.get()
        miLabelPrueba = Label(TercerVentana, text="Felicidades!, se han encontrado tus palabras").grid(row=0)

    Boton2_1 = Button(miFrame2, text="Enviar",command=boton, width=10)
    Boton2_1.grid(row=3, column=1, pady=10)

def nuevaVentana4():
    variable2 = StringVar()  
    ventana_nueva2 = Toplevel()
    ventana_nueva2.title("Busqueda de palabras claves")
    ventana_nueva2.iconbitmap("Logo.ico")
    miFrame3 = Frame(ventana_nueva2)
    #Frame 3

    miFrame3.pack(side="left", anchor="n")
    miFrame3.config(bg="#800080")

    miFrame3.config(width="350", height="650")
    miFrame3.config(bd=9)
    miFrame3.config(relief="groove")

    #Pregunta:
    miLabelp4 = Label(miFrame3, text="Cual es tu duda?",fg="#FFFFFF",bg = "#800080",font=("DejaVuSansMono-Bold",15))
    miLabelp4.grid(row = 0, column = 1, pady=10)
    #Entrada de texto
    EntradaDeText = Entry(miFrame3, width=10)
    EntradaDeText.grid(row=2, column=1, pady=10)
    #Boton
    def boton():
        CuartaVentana = Toplevel()
        CuartaVentana.geometry("400x200")
        variable2= EntradaDeText.get()
        miLabelPrueba2 = Label(CuartaVentana, text="Esperamos que se haya resuelto :)").grid(row=0)

    Boton2_1 = Button(miFrame3, text="Enviar",command=boton, width=10)
    Boton2_1.grid(row=3, column=1, pady=10)
    

#Ventana principal
raiz = Tk()
raiz.title("GobSnap")
raiz.iconbitmap("Logo.ico")

raiz.config(bg="#00BFBF")
EntradaDeText = StringVar()   
#Frame 1

miFrame = Frame()

miFrame.pack(side="left", anchor="n")
miFrame.config(bg="#800080")

miFrame.config(width="350", height="650")
miFrame.config(bd=9)
miFrame.config(relief="groove")

#Titulo de la aplicacion
miLabel = Label(miFrame, text="Hightlighter",fg="#FFFFFF",bg = "#800080",font=("DejaVuSansMono-Bold",20))
miLabel.grid(row = 0, column = 1, pady=10)

EspacioBl = Label(miFrame, text="Bienvenido al menu de inicio, presione la instruccion que desea ejecutar",fg="#FFFFFF",bg = "#800080",font=("DejaVuSansMono-Bold",12))
EspacioBl.grid(row = 1, column = 1, pady=40)
#Logo de Softtex
miLogo = PhotoImage(file="Softek1.png")
LogoLb = Label(miFrame, image=miLogo)
LogoLb.grid(row = 12, column = 1 , pady=10, padx=10, sticky="e")
#Texto de botones
BotonT1 = Label(miFrame, text="Resumir",fg="#FFFFFF",bg = "#800080",font=("DejaVuSansMono-Bold",10))
BotonT1.grid(row = 2, column = 1, pady=10)
BotonT2 = Label(miFrame, text="Busqueda de palabras claves",fg="#FFFFFF",bg = "#800080",font=("DejaVuSansMono-Bold",10))
BotonT2.grid(row = 4, column = 1, pady=10)
BotonT3 = Label(miFrame, text="Busqueda de una palabra especifica",fg="#FFFFFF",bg = "#800080",font=("DejaVuSansMono-Bold",10))
BotonT3.grid(row = 6, column = 1, pady=10)
BotonT4 = Label(miFrame, text="Dudas",fg="#FFFFFF",bg = "#800080",font=("DejaVuSansMono-Bold",10))
BotonT4.grid(row = 8, column = 1, pady=10)
BotonT5 = Label(miFrame, text=" ",fg="#FFFFFF",bg = "#800080",font=("DejaVuSansMono-Bold",10))
BotonT5.grid(row = 10, column = 1, pady=10)

#Botones
Boton1 = Button(miFrame, text="Enviar", width=10)
Boton1.grid(row=3, column=1, padx=10)
Boton2 = Button(miFrame, text="Enviar", width=10)
Boton2.grid(row=5, column=1, padx=10)
Boton3 = Button(miFrame, text="Enviar", width=10, command=nuevaVentana3)
Boton3.grid(row=7, column=1, padx=10)
Boton4 = Button(miFrame, text="Enviar", width=10, command = nuevaVentana4)
Boton4.grid(row=9, column=1, padx=10)
Boton5 = Button(miFrame, text="Salir", command=raiz.destroy)
Boton5.grid(row=11, column=1, padx=10)


raiz.mainloop()