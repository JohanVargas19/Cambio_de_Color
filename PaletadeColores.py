from tkinter import*
from tkinter import messagebox as MessageBox

root = Tk()
root.title("PALETA DE COLORES") #Titulo de la raiz
root.resizable(0,0)

#Metodo
def changeColor():
    cantidad = contador()
    if cantidad == 6:
        color = "#" + rojoColor.get() + verdeColor.get() + azulColor.get()
        #print(color)
        ventana.config(bg=color)
        titulo.config(bg=color)
        rojo.config(bg=color)
        verde.config(bg=color)
        azul.config(bg=color)
        mostrarInfo()
    
    elif cantidad < 6:
        error2()

    else:
        error1()


def contador():

    contar = rojoColor.get() + verdeColor.get() + azulColor.get()
    digitos = 0
    letras = 0

    for c in contar:
        if c.isdigit():
            digitos = digitos + 1
        elif c.isalpha():
            letras = letras + 1
        else:
            pass

    #print(digitos)
    #print(letras)

    return digitos+letras

def mostrarInfo():
    MessageBox.showinfo("Informacion", "Color cambiado correctamente")

def error1():
    MessageBox.showerror("Error", "Solo puede ingresar dos datos en cada espacio")

def error2():
    MessageBox.showerror("Error", "Ingresar dos datos en cada espacio")

#variables
rojoColor= StringVar()
verdeColor= StringVar()
azulColor= StringVar()

rojoColor.set("a0")
verdeColor.set("a0")
azulColor.set("a0")

ventana = Frame(root, bg="#a0a0a0")
ventana.pack(fill="both", expand=1)

#Titulo de la ventana
titulo = Label(ventana, text="Paleta de Colores", font=("Roboto",20,"bold"), bg="#a0a0a0")
titulo.grid(row=1, column=1, columnspan=2, padx=20, pady=20)

#Etiqueta 1
rojo = Label(ventana, text="Rojo", font=("Roboto",10,"bold"), bg="#a0a0a0")
rojo.grid(row=2, column=1)
textoRojo = Entry(ventana, font=("Roboto",10), textvariable=rojoColor).grid(row=2, column=2)

#Etiqueta 2
verde = Label(ventana, text="Verde", font=("Roboto",10,"bold"), bg="#a0a0a0")
verde.grid(row=3, column=1)
textoVerde = Entry(ventana, font=("Roboto",10), textvariable=verdeColor).grid(row=3, column=2)

#Etiqueta 3
azul = Label(ventana, text="Azul", font=("Roboto",10,"bold"), bg="#a0a0a0")
azul.grid(row=4, column=1)
textoAzul = Entry(ventana, font=("Roboto",10), textvariable=azulColor).grid(row=4, column=2)

#Boton Cambiar color
boton = Button(ventana, text="Change Color", font=("Roboto",10), command=changeColor).grid(row=5, column=1, columnspan=2, padx=20, pady=10)


root.mainloop()