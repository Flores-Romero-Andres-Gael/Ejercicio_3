from tkinter import *
from tkinter import ttk
import tkinter as ttk

root = Tk()

#--------------------ROOT--------------------
root.geometry("1050x465")
root.config(background="gray6")

#--------------------MENU FRAME--------------------

MENUFrame = ttk.Frame(root, background="turquoise4")
MENUFrame.grid(column=0, row=0, sticky=(W))

imagMD = PhotoImage(file="DrawerMenu.png")
MenuDrawer= ttk.Label(MENUFrame, background="turquoise4")
MenuDrawer.grid(column=0, row=0, padx=5, sticky=(W,N))
MenuDrawer['image'] = imagMD

ttk.Label(MENUFrame, background="turquoise4",text="SPAI 4.0", foreground="white", font=("arial",12,"bold"), anchor="w",width=300).grid(column=1,row=0,sticky=(W))

#--------------------INICIO FRAME--------------------

Frameinicio = ttk.Frame(root, background="gray6")
Frameinicio.grid(column=0, row=1, sticky=(W))

#--------------------FRAMES IZQUIERDA--------------------

Izquierda = ttk.Frame(Frameinicio, background="gray6")
Izquierda.grid(column=0, row=0, sticky=(W))

IzquierdaArriba = ttk.Frame(Izquierda, background="gray6")
IzquierdaArriba.grid(column=0, row=0, padx=50, sticky=(W))

IzquierdaAbajo = ttk.Frame(Izquierda, background="gray6")
IzquierdaAbajo.grid(column=0, row=1, padx=50, sticky=(W))

#--------------------PRIMER FRAME IZQUIERDA ARRIBA--------------------

Frame1 = ttk.Frame(IzquierdaArriba, background="gray20")
Frame1.grid(column=0, row=0, padx=10 ,pady=5, sticky=(W,N))

ttk.Label(Frame1, background="gray20", foreground="cyan4", font=("arial",10), text="Indicadores Digitales").grid(column=0, row=0, padx=4, pady=2, sticky=(W,N))
ttk.Label(Frame1, background="gray20", foreground="white", text="Linea 1: ").grid(column=0, row=1, padx=4, pady= 8, sticky=(W,N))
ttk.Label(Frame1, background="gray20", foreground="white", text="Linea 2: ").grid(column=0, row=2, padx=4, pady= 8, sticky=(W,N))
ttk.Label(Frame1, background="gray20", foreground="white", text="Linea 3: ").grid(column=0, row=3, padx=4, pady= 8,sticky=(W,N))
ttk.Label(Frame1, background="gray20", foreground="white", text="Gabinete: Abierto").grid(column=0, row=4, padx=4,  pady= 8, sticky=(W,N),columnspan=1)
ttk.Label(Frame1, background="gray20", foreground="white", text="Alarma: ").grid(column=0, row=5, padx=4, pady= 8, sticky=(W,N))
ttk.Label(Frame1, background="gray20", foreground="white", text="Alarma 2: ").grid(column=0, row=6, padx=4, pady= 8, sticky=(W,N))

ttk.Label(Frame1, background="gray20", foreground="white", text="On").grid(column=1, row=1, padx=4, pady= 8, sticky=(W,N))
ttk.Label(Frame1, background="gray20", foreground="white", text="On").grid(column=1, row=2, padx=4, pady= 8, sticky=(W,N))
ttk.Label(Frame1, background="gray20", foreground="white", text="On").grid(column=1, row=3, padx=4, pady= 8, sticky=(W,N))
ttk.Label(Frame1, background="gray20", foreground="white", text="On").grid(column=1, row=5, padx=4, pady= 8, sticky=(W,N))
ttk.Label(Frame1, background="gray20", foreground="white", text="Off").grid(column=1, row=6, padx=4, pady= 8, sticky=(W,N))


imagBV = PhotoImage(file="BotonVerde.png")
BotonVerde1= ttk.Label(Frame1, background="gray20")
BotonVerde2= ttk.Label(Frame1, background="gray20")
BotonVerde3= ttk.Label(Frame1, background="gray20")
BotonVerde4= ttk.Label(Frame1, background="gray20")
BotonVerde1.grid(column=2, row=1, pady=2, sticky=(W))
BotonVerde2.grid(column=2, row=2, pady=2, sticky=(W))
BotonVerde3.grid(column=2, row=3, pady=2, sticky=(W))
BotonVerde4.grid(column=2, row=6, pady=2, sticky=(W))
BotonVerde1['image'] = imagBV
BotonVerde2['image'] = imagBV
BotonVerde3['image'] = imagBV
BotonVerde4['image'] = imagBV

imagBR = PhotoImage(file="BotonRojo.png")
BotonRojo1= ttk.Label(Frame1, background="gray20")
BotonRojo2= ttk.Label(Frame1, background="gray20")
BotonRojo1.grid(column=2, row=4, pady=2, sticky=(W))
BotonRojo2.grid(column=2, row=5, pady=2, sticky=(W))
BotonRojo1['image'] = imagBR
BotonRojo2['image'] = imagBR

#--------------------Segundo FRAME IZQUIERDA ARRIBA--------------------

Frame2 = ttk.Frame(IzquierdaArriba, background="gray20")
Frame2.grid(column=1, row=0,pady=5, sticky=(W,N)) 

ttk.Label(Frame2, background="gray20", foreground="cyan4", font=("arial",10), text="Temperaturas:").grid(column=0, row=0, sticky=(W, N))
ttk.Label(Frame2, background="gray20", foreground="white", text="Temperatura 1:").grid(column=0, row=1, padx=50, pady=20, sticky=(W))
ttk.Label(Frame2, background="gray20", foreground="white", text="Temperatura 2:").grid(column=1, row=1, padx=30, pady=20, sticky=(W))

imagGV = PhotoImage(file="GraficaVerde.png")
GraficaVerde= ttk.Label(Frame2, background="gray20")
GraficaVerde.grid(column=0, row=2, padx=28, sticky=(W,N))
GraficaVerde['image'] = imagGV

imagGA = PhotoImage(file="GraficaAmarilla.png")
GraficaAmarilla= ttk.Label(Frame2, background="gray20")
GraficaAmarilla.grid(column=1, row=2, sticky=(W,N))
GraficaAmarilla['image'] = imagGA

ttk.Label(Frame2, background="gray20", foreground="white", text="Temp. Agua: 58°C", anchor="center").grid(column=0, row=3, pady=8, columnspan=2)
ttk.Label(Frame2, background="gray20", foreground="white", text="Temp. Ambiente: 32°C", anchor="center").grid(column=0, row=4, pady=8, columnspan=2)


#--------------------PRIMER FRAME IZQUIERDA ABAJO--------------------

Frame3 = ttk.Frame(IzquierdaAbajo, background="gray20")
Frame3.grid(column=0, row=0, padx=8 ,sticky=(W,N))

ttk.Label(Frame3, background="gray20", foreground="white", text="Velocidad bomba:", width=35, anchor="w").grid(column=0, row=0, padx=20, pady=20, sticky=(W), columnspan=1)

imagGN = PhotoImage(file="GraficaNaranja.png")
GraficaNaranja= ttk.Label(Frame3, background="gray20")
GraficaNaranja.grid(column=0, row=1, sticky=(W,N), columnspan=1, padx=10)
GraficaNaranja['image'] = imagGN

#--------------------SEGUNDO FRAME IZQUIERDA ABAJO--------------------

Frame4 = ttk.Frame(IzquierdaAbajo, background="gray20")
Frame4.grid(column=1, row=0,sticky=(W,N))

ttk.Label(Frame4, background="gray20", foreground="cyan4", font=("arial",12), text="  Nivel del tanque: ",width=25, anchor="w").grid(column=0, row=0, sticky=(W), pady=2, padx=3)

imagGAZ = PhotoImage(file="GraficaAzul.png")
GraficaAzul= ttk.Label(Frame4, background="gray20")
GraficaAzul.grid(column=0, row=1, sticky=(W,N), columnspan=1, padx=10)
GraficaAzul['image'] = imagGAZ


#--------------------FRAMES DERECHA--------------------

Derecha = ttk.Frame(Frameinicio, background="gray6")
Derecha.grid(column=0, row=0, padx = 600 , pady=5, sticky=(W,N))

Frame5 = ttk.Frame(Derecha, background="gray20")
Frame5.grid(column=0,row=0,sticky=(W))

ttk.Label(Frame5, background="gray20", foreground="cyan4", font=("arial",12), text="Produccion: ").grid(column=0, row=0, sticky=(W))
ttk.Label(Frame5, background="gray20", foreground="white", text="Piezas producidas: 50").grid(column=0, row=2, columnspan=2, pady=10)
ttk.Label(Frame5, background="gray20", foreground="white", text="Piezas defectuosas: 12").grid(column=0, row=3, columnspan=2, pady=5)

imagDG = PhotoImage(file="DiagramaGrafica.png")
GraficaDG= ttk.Label(Frame5, background="gray20")
GraficaDG.grid(column=0, row=1, sticky=(W,N), columnspan=1, padx=10, pady=10)
GraficaDG['image'] = imagDG

root.mainloop()