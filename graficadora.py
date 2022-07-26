import tkinter as tk
from tkinter import ANCHOR, BOTH, PhotoImage, Tk, Frame, Canvas, Label, messagebox, IntVar

BASE = 480
ALTURA = 450

def pendiente():
    messagebox.showinfo("Graficacion" , "La pendiente es...")
    m = (y2.get() - y1.get())/(x2.get() - x1.get())
    messagebox.showinfo("Pendiente" , str(m))

def graficar():
    messagebox.showinfo("Graficacion" , "Se esta graficando su recta")
    graf = C.create_line(x1.get() + 240 , (y2.get() + 225) - (y2.get()*2) , x2.get() + 240 , (y2.get() + 225)- (y2.get()*2) , fill="red")

def salir():
    messagebox.showinfo("Graficacion" , "La app se cerrará")
    ventana_principal.destroy()

#-------------------------
# VENTANA PRINCIPAL
#-------------------------

ventana_principal = Tk()
ventana_principal.title("Graficas 2D - Texto")
ventana_principal.geometry("500x600")
ventana_principal.resizable(False , False)
ventana_principal.config(bg = "green")


x1 = tk.IntVar()
y1 = tk.IntVar()
x2 = tk.IntVar()
y2 = tk.IntVar()

#-----------------------
# Frames
#-----------------------

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg = "white", width=480 , height=450)
frame_graficacion.place(x=10 , y=10)


frame_opciones = Frame(ventana_principal)
frame_opciones.config(bg= "gray" , width=460 , height= 120)
frame_opciones.place(x=10 , y= 470)


#etiqueta X1
label_x = tk.Label(frame_opciones, text="X1 =")
label_x.config(bg="grey" ,fg="blue" , font=("Arial" , 14))
label_x.place(x=10 , y=10)

# caja de texto para X1
entry_x = tk.Entry(frame_opciones , width= 5 ,textvariable= x1)
entry_x.config(font=("Arial" , 12) , )
entry_x.place(x= 60 , y=10)

#etiqueta Y1
label_y = tk.Label(frame_opciones, text="Y1 =")
label_y.config(bg="grey" ,fg="blue" , font=("Arial" , 14))
label_y.place(x=10 , y=60)

# caja de texto para Y1
entry_y = tk.Entry(frame_opciones , width= 5 , textvariable= y1)
entry_y.config(font=("Arial" , 12))
entry_y.place(x= 60 , y=60)

#-----------------------------------------------------

#etiqueta X2
label_x = tk.Label(frame_opciones, text="X2 =")
label_x.config(bg="grey" ,fg="blue" , font=("Arial" , 14))
label_x.place(x=120 , y=10)

# caja de texto para X2
entry_x = tk.Entry(frame_opciones , width= 5 , textvariable= x2)
entry_x.config(font=("Arial" , 12))
entry_x.place(x= 170 , y=10)

#etiqueta Y2
label_y = tk.Label(frame_opciones, text="Y2 =")
label_y.config(bg="grey" ,fg="blue" , font=("Arial" , 14))
label_y.place(x=120 , y=60)

# caja de texto para Y2
entry_y = tk.Entry(frame_opciones , width= 5 , textvariable= y2)
entry_y.config(font=("Arial" , 12))
entry_y.place(x= 170 , y=60)

#----------------------
# Creacion del canvas
#----------------------

C = Canvas(frame_graficacion, width=BASE , height= ALTURA)
C.place(x=0 , y=0)

texty = C.create_text(250 , 10 , text="Y" , fill="black")
textx = C.create_text(470 , 240 , text="X" , fill="black")

ejey = C.create_line( BASE/2 , 0 , BASE/2 , ALTURA , fill="black" )
ejex = C.create_line( 0 , ALTURA/2 , BASE , ALTURA/2 , fill="black" )

#----
# Botones
#----

boton_graficar = tk.Button(frame_opciones , text= "Graficar" , command=graficar)
boton_graficar.config(width=15)
boton_graficar.place(x=320 , y= 10)

boton_pendiente = tk.Button(frame_opciones , text= "Pendiente" , command=pendiente)
boton_pendiente.config(width=15)
boton_pendiente.place(x=320 , y= 50)

boton_salir = tk.Button(frame_opciones , text="Salir" , command= salir)
boton_salir.config(width=15)
boton_salir.place(x=320, y=90)



ventana_principal.mainloop()