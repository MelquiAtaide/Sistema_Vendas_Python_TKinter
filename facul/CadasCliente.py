from tkinter import *
from tkinter.ttk import *
import psycopg2
connection = ""

cadascliente = Tk()

def dados():
    try:
        connection = psycopg2.connect(database='produtoslimpeza',
                                      user='postgres',
                                      password='sjf7286',
                                      host='localhost')
        nome = nomec.get()
        cpfc = cpf.get()
        telefone = telefonec.get()
        endereco = enderecoc.get()
        bairro = bairroc.get()
        cidEstado = cidEstadoc.get()
        entrega = entregac.get()
        cursor = connection.cursor()

        query = """INSERT INTO clientes(nome, cpf, telefone, endereco, bairro, cidadeestado, diaentrega)
                VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')"""
        cursor.execute(query.format(nome, cpfc, telefone, endereco, bairro, cidEstado, entrega))
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Ocorreu uma falha, informe o erro {} ao suporte".format(error))
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL conexão encerrada")

cadascliente.title("Cadastro Cliente")

Label(cadascliente, text="Nome:", background = "#E0ECF8").place(x=50, y=80)
nomec=Entry(cadascliente)
nomec.place(x=100, y=80, width=250, height=23)

Label(cadascliente, text="CPF:", background = "#E0ECF8").place(x=50, y=120)
cpf=Entry(cadascliente, font=('Arial', '9'))
cpf.place(x=100, y=120, width=100, height=23)

Label(cadascliente, text="Telefone:", background = "#E0ECF8").place(x=42, y=160)
telefonec=Entry(cadascliente, font=('Arial', '10'))
telefonec.place(x=100, y=160, width=100, height=23)

Label(cadascliente, text="Endereço:", background = "#E0ECF8").place(x=42, y=200)
enderecoc=Entry(cadascliente, font=('Arial', '10'))
enderecoc.place(x=100, y=200, width=250, height=23)

Label(cadascliente, text="Bairro:", background = "#E0ECF8").place(x=18, y=240)
bairroc=Entry(cadascliente, font=('Arial', '10'))
bairroc.place(x=100, y=240, width=200, height=23)

Label(cadascliente, text="Cidade e Estado:", background = "#E0ECF8").place(x=8, y=280)
cidEstadoc=Entry(cadascliente, font=('Arial', '10'))
cidEstadoc.place(x=100, y=280, width=200, height=23)

Label(cadascliente, text="Dia da Entrega:", background = "#E0ECF8").place(x=18, y=320)
entregac=Entry(cadascliente, font=('Arial', '15'))
entregac.place(x=100, y=320, width=40, height=23)

Button(cadascliente, text="Salvar", command=dados).place(x=100, y=360)


cadascliente.geometry("1000x500")
#E0ECF8 azul claro
cadascliente.configure(background = "#E0ECF8")
cadascliente.mainloop()
