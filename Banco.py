#importacion de la libreria tkinterf
from tkinter import *
from tkinter import messagebox

#definimos la ventana principal
root = Tk()
root.geometry('300x480')
root.title("Banco Ujapista")
root.iconbitmap('C:/Users/gonza/OneDrive/Imágenes/ujap.ico')

#funcion para validar si se esta ingresando un numero
def validate_entry(text):
    return text.isdecimal()

#creacion del frame 1
cuadro1 = LabelFrame(root, text="Datos",  padx=20, pady = 20).grid(row=0, column=0, padx=5, pady= 10)

#variable del pady en los label
padAltura = 20
padAncho = 20

#items del frame 1
#id
label1 = Label(cuadro1, text="ID:", padx=padAncho, pady=padAltura).grid(row=0, column=0)
eId = Entry(cuadro1, width=20,validate="key",validatecommand=(root.register(validate_entry), "%S"))
eId.grid(row=0, column=1)

#Nombre y apellido
label2 = Label(cuadro1, text="Nombre y apellido:", padx=padAncho,pady=padAltura, justify="left").grid(row=1, column=0)
eNombre = Entry(cuadro1, width=20)
eNombre.grid(row=1, column=1)

#Direccion
label3 = Label(cuadro1, text="Tipo de cuenta:", padx=padAncho,pady=padAltura, justify="left").grid(row=2, column=0)
eTipoCuenta = Entry(cuadro1, width=20)
eTipoCuenta.grid(row=2, column=1)

#Cedula de identidad
label4 = Label(cuadro1, text="Telefono", padx=padAncho, pady=padAltura).grid(row=3, column=0)
eCedula = Entry(cuadro1, width= 20, validate="key",validatecommand=(root.register(validate_entry), "%S"))
eCedula.grid(row=3, column=1)

#Monto inicial
label5 = Label(cuadro1, text="Monto Incial:", padx=padAncho, pady=padAltura).grid(row=4, column=0)
eMontoI = Entry(cuadro1, width=20,validate="key", validatecommand=(root.register(validate_entry), "%S"))
eMontoI.grid(row=4, column=1)

clientes = {"ID" : [],
                "Nombre" : [],
                "TipoCuenta" : [],
                "Telefono" : [],
                "Monto" : []
    };


#funciones de botones ventana principal

def registrar():
    band = 1
    for x in range(len(clientes["ID"])):
        if clientes["ID"][x] == eId.get():
            band = 0
    #agregado de variables de entrada al diccionario
    if band == 1:
        clientes["ID"].append(eId.get())
        clientes["Nombre"].append(eNombre.get())       
        clientes["TipoCuenta"].append(eTipoCuenta.get())       
        clientes["Telefono"].append(eCedula.get())       
        clientes["Monto"].append(eMontoI.get())
        print(clientes)
    else:
        messagebox.showerror('mensaje error', "el ID ingresado ya fue asignado a otro cliente, por favor ingrese otro")

def abrirConsulta():
    #ventana de consulta
    consultar = Toplevel(padx=20, pady=20)
    consultar.title('Consulta de usuario')
    consultar.iconbitmap('C:/Users/gonza/OneDrive/Imágenes/ujap.ico')
    
    #variables globales
    global eConId
    
    #items de la ventana consulta
    labelCon = Label(consultar, text="ID a consultar:", padx=20, pady=10)
    eConId = Entry(consultar, validate="key",validatecommand=(root.register(validate_entry), "%S"))
    bConsulta = Button(consultar, text="consultar", padx=20, pady=9, command=consultarCliente)
    #pack de los items de la ventana consulta
    labelCon.pack()
    eConId.pack()
    bConsulta.pack()
    
def abrirTransferencia():
    #ventana de transferir
    transferencia = Toplevel()
    transferencia.title('Transferencia a otros usuarios')
    transferencia.iconbitmap('C:/Users/gonza/OneDrive/Imágenes/ujap.ico')
    
    #variables globales
    global eTransId
    global eTransId2
    global eTransMonto
    
    #items de la ventana Transferir
    labelTrans = Label(transferencia, text="ID a debitar:", padx=20, pady=10)
    eTransId = Entry(transferencia, validate="key",validatecommand=(root.register(validate_entry), "%S"))
    labelTrans2 = Label(transferencia, text="ID a abonar:", padx=20, pady=10)
    eTransId2 = Entry(transferencia, validate="key",validatecommand=(root.register(validate_entry), "%S"))
    labelTransMonto = Label(transferencia, text="Monto a abonar:", padx=20, pady=10)
    eTransMonto = Entry(transferencia, validate="key", validatecommand=(root.register(validate_entry), "%S"))
    bTransferencia = Button(transferencia, text="Transferir", padx=20, pady=9, command=transferir)
    #pack de los items de la ventana Transferir
    labelTrans.pack()
    eTransId.pack()
    labelTrans2.pack()
    eTransId2.pack()
    labelTransMonto.pack()
    eTransMonto.pack()
    bTransferencia.pack()
    
def abrirRetiro():
    #ventana de retiro
    retiro = Toplevel()
    retiro.title('Retiro de fondos')
    retiro.iconbitmap('C:/Users/gonza/OneDrive/Imágenes/ujap.ico')
    
    #variables globales
    global eRetId
    global eRetMonto
    
    #items de la ventana retiro
    labelRet = Label(retiro, text="ID a Retirar:", padx=20, pady=10)
    eRetId = Entry(retiro,validate="key",validatecommand=(root.register(validate_entry), "%S"))
    labelRetMonto = Label(retiro, text="Monto a Retirar:", padx=20, pady=10)
    eRetMonto = Entry(retiro,validate="key", validatecommand=(root.register(validate_entry), "%S"))
    bRetiro = Button(retiro, text="Retirar", padx=20, pady=9, command=retirar)
    
    #pack de los items de la ventana retiro
    labelRet.pack()
    eRetId.pack()
    labelRetMonto.pack()
    eRetMonto.pack()
    bRetiro.pack()
    
#funciones de botones Consultar
def consultarCliente():
    #busqueda del id
    index = -1
    for x in range(len(clientes["ID"])):
        if clientes["ID"][x] == eConId.get():
            index = x
    if index == -1:
        messagebox.showerror("ventana de error","El ID a debitar no se encuentra ingresado a ningun cliente, intentelo de nuevo")
    if index >= 0:
        for x in clientes:
            print(x +": " , clientes[x][index])
    


def transferir():
    index = -1
    index2 = -1
    
    #busqueda del primer id
    for x in range(len(clientes["ID"])):
        if clientes["ID"][x] == eTransId.get():
            index = x
    if index == -1:
        messagebox.showerror("ventana de error","El ID a debitar no se encuentra ingresado a ningun cliente, intentelo de nuevo")
                
    
    #descuento del monto al id 1
    if index != -1:
        if int(round(float(clientes["Monto"][index]),2)) < int(round(float(eTransMonto.get()),2)):
            messagebox.showerror("mensaje de error" ,"saldo menor al monto a transferir")
        else:
            clientes["Monto"][index] = str(round(float(clientes["Monto"][index]),2) - round(float(eTransMonto.get()),2))
    #busqueda del segundo id
    for x in range(len(clientes["ID"])):
        if clientes["ID"][x] == eTransId2.get():
            index2 = x
    if index2 == -1:
        messagebox.showerror("ventana de error","El ID a abonar no se encuentra ingresado a ningun cliente, intentelo de nuevo")
        
    #suma del monto al id 2
    if index2 != -1:
        if int(round(float(clientes["Monto"][index2]),2)) >= int(round(float(eTransMonto.get()),2)):
            clientes["Monto"][index2] = str(round(float(clientes["Monto"][index2]),2) + round(float(eTransMonto.get()),2))
            print(clientes["Monto"][index2], clientes["Monto"][index])
    
def retirar():
    #busqueda del id
    index = -1
    for x in range(len(clientes["ID"])):
        if clientes["ID"][x] == eRetId.get():
            index = x
    if index == -1:
        messagebox.showerror("ventana de error","El ID a debitar no se encuentra ingresado a ningun cliente, intentelo de nuevo")
        
    if index >= -1:
        if int(round(float(clientes["Monto"][index]),2)) < int(round(float(eRetMonto.get()),2)):
            messagebox.showerror("mensaje de error","saldo menor al monto a retirar")
        else:
            clientes["Monto"][index] = str(round(float(clientes["Monto"][index]),2) - round(float(eRetMonto.get()),2))
            print(clientes["Monto"][index])
    
    
#Botones
bRegistrar = Button(cuadro1, text="Registrar", width=15, padx=5, pady=padAltura, command=registrar).grid(row=5, column=0)
bConsultar = Button(cuadro1, text="Consultar", width=15, padx=5, pady=padAltura, command=abrirConsulta).grid(row=5, column=1)
bTransferir = Button(cuadro1, text="Transferir", width=15, padx=5, pady=padAltura, command=abrirTransferencia).grid(row=6, column=0)
bRetirar = Button(cuadro1, text="Retirar", width=15, padx=5, pady=padAltura, command=abrirRetiro).grid(row=6, column=1)


root.mainloop()