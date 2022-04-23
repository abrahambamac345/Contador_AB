#Uso de la libreria Tkinter
import tkinter
#ventana
ventanatk = tkinter.Tk()#abrimos nuestra ventana
ventanatk.title("CONTADOR")
ventanatk.resizable(False,False)
ventanatk.geometry("500x300")#definimos el tamaño de la ventana

#monitor
conta = tkinter.Label(ventanatk, text = "CONTADOR", font='Georgia 40',foreground="blue")
conta.place(x=100,y=20)
Contador = tkinter.Label(ventanatk, text = "0", font='Arial_Black 50')
Contador.place(x=220, y=100)
#contador
def sum(): 
    val = int(Contador["text"])
    Contador["text"] = f"{val + 1}"
    val = int(Contador["text"])
    Color(val)
SUMA=tkinter.Button(ventanatk, text = "SUMAR", font= "Arial", width=13, height=3, command=sum, foreground="green" )
SUMA.place(x=40, y=200)
def res(): 
    val = int(Contador["text"])
    Contador["text"] = f"{val - 1}"
    val = int(Contador["text"])
    Color(val)
RESTA=tkinter.Button(ventanatk, text = "RESTAR", font= "Arial", width=13, height=3, command= res, foreground="red" )
RESTA.place(x=185, y=200)
def reset(): 
    val = int(Contador["text"])
    Contador["text"] = f"{val * 0}"
    val = int(Contador["text"])
    Color(val)
RESET=tkinter.Button(ventanatk, text = "RESTAR", font= "Arial_Black", width=13, height=3, command= reset)
RESET.place(x=330, y=200)
#color de nuestro numero
def Color(val): 
    if int(val) ==0:
        Contador.config(foreground="black")
    elif int(val)>0:
        Contador.config(foreground="green")
    elif int(val)<0:
        Contador.config(foreground="red")
ventanatk.mainloop()#cerramos
