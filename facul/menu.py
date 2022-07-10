from tkinter import *
from tkinter.ttk import *
import psycopg2
import Clientes
import Fornecedor
import produtos
import pedidos

def cli():
    Clientes.wincliente()

def pro():
    produtos.winprodutos()

def forn():
    Fornecedor.winfornecedor()

def ped():
    pedidos.winpedidos()

def sair():
    menu.destroy()

menu = Tk()
menu.title("Pagina Inicial")

Label(menu, text="", background = "#E0ECF8").place(x=20, y=80, width=970, height=500)
Label(menu, text="Pagina Inicial", background = "#CEE3F6", font=('Arial', '20')).place(x=430, y=10)
#width=400, height=200     #8181F7     #E0ECF8

Button(menu, text="Clientes", command=cli).place(x=160, y=160, width=190, height=110)
Button(menu, text="Produtos", command=pro).place(x=416, y=160, width=190, height=110)
Button(menu, text="Fornecedores", command=forn).place(x=660, y=160, width=190, height=110)
Button(menu, text="Pedidos", command=ped).place(x=285, y=290, width=190, height=110)
Button(menu, text="Sair", command=sair).place(x=540, y=290, width=190, height=110)

menu.geometry("1000x500")
menu.configure(background = "#CEE3F6")
menu.mainloop()