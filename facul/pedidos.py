from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def winpedidos():
    import psycopg2
    connection = ""

    pedidos = Tk()

    def mostrar():
        tabela.delete(*tabela.get_children())
        try:
            connection = psycopg2.connect(database='produtoslimpeza',
                                          user='postgres',
                                          password='sjf7286',
                                          host='localhost')
            cursor = connection.cursor()
            postgreSQL_select_Query = "select * from pedidos"
            cursor.execute(postgreSQL_select_Query)
            pedidoss = cursor.fetchall()
            for i in pedidoss:
                tabela.insert("", "end", values=i)
        except (Exception, psycopg2.Error) as error:
            print("Ocorreu uma falha: {} ".format(error))
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL conexão encerrada")

    def salvar():
        try:
            connection = ""
            connection = psycopg2.connect(database='produtoslimpeza',
                                          user='postgres',
                                          password='sjf7286',
                                          host='localhost')


            clienteidp = clienteid.get()
            codproduto = codprop.get()
            endereco = enderecop.get()
            bairro = bairrop.get()
            cidadeestado = cidestadop.get()
            valor = valorp.get()
            quantidade = quantidadep.get()
            diaentrega = diaentregap.get
            cursor = connection.cursor()

            query = """INSERT INTO pedidos(clienteid, codproduto, endereco, bairro, cidadeestado, valor, quantidade, diaentrega)
                    VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"""
            cursor.execute(query.format(clienteidp, codproduto, endereco, bairro, cidadeestado, valor, quantidade, diaentrega))
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Ocorreu uma falha: {} ".format(error))
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL conexão encerrada salvo")
            mostrar()
            clienteid.delete(0, END)
            codprop.delete(0, END)
            enderecop.delete(0, END)
            bairrop.delete(0, END)
            cidestadop.delete(0, END)
            valorp.delete(0, END)
            quantidadep.delete(0, END)
            diaentregap.delete(0, END)
            clienteid.focus()

    def pesquisa():
        tabela.delete(*tabela.get_children())
        pesqui = pesquisarp.get()
        try:
            connection = psycopg2.connect(database='produtoslimpeza',
                                          user='postgres',
                                          password='sjf7286',
                                          host='localhost')
            cursor = connection.cursor()
            Query = "SELECT * FROM pedidos WHERE diaentrega LIKE '%{}%'"
            cursor.execute(Query.format(pesqui))
            connection.commit()
            pedidoss = cursor.fetchall()
            for i in pedidoss:
                tabela.insert("", "end", values=i)
        except:
            messagebox.showinfo(title="ERRO", message="Deu erro")
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL conexão encerrada")

    def apagar():
        try:
            itemselect = tabela.selection()[0]
            valores = tabela.item(itemselect, "values")

            connection = psycopg2.connect(database='produtoslimpeza',
                                          user='postgres',
                                          password='sjf7286',
                                          host='localhost')
            cursor = connection.cursor()
            query = """DELETE FROM pedidos WHERE codpedido = {}"""
            cursor.execute(query.format(valores[0]))
            connection.commit()
            print("deletando registro")
        except:
            messagebox.showinfo(title="ERRO", message="Deu erro")
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL conexão encerrada")
        mostrar()

    def editar():
        print("pagina que faltou ser criada")

    # ------------------------//-------------------
    pedidos.title("Cadastro de produtos")

    Label(pedidos, text="", background="#CEE3F6").place(x=18, y=40, width=330, height=310)
    Label(pedidos, text="ClienteId:", background="#CEE3F6").place(x=20, y=50)
    clienteid = Entry(pedidos)
    clienteid.place(x=100, y=50, width=50, height=23)

    Label(pedidos, text="CodProduto:", background="#CEE3F6").place(x=20, y=80)
    codprop = Entry(pedidos)
    codprop.place(x=100, y=80, width=50, height=23)

    Label(pedidos, text="Endereco:", background="#CEE3F6").place(x=20, y=120)
    enderecop = Entry(pedidos, font=('Arial', '9'))
    enderecop.place(x=100, y=120, width=245, height=23)

    Label(pedidos, text="Bairro:", background="#CEE3F6").place(x=20, y=160)
    bairrop = Entry(pedidos, font=('Arial', '10'))
    bairrop.place(x=100, y=160, width=150, height=23)

    Label(pedidos, text="CidadeEstado:", background="#CEE3F6").place(x=20, y=200)
    cidestadop = Entry(pedidos, font=('Arial', '10'))
    cidestadop.place(x=100, y=200, width=150, height=23)

    Label(pedidos, text="Valor:", background="#CEE3F6").place(x=50, y=240)
    valorp = Entry(pedidos, font=('Arial', '10'))
    valorp.place(x=100, y=240, width=50, height=23)

    Label(pedidos, text="Quantidade:", background="#CEE3F6").place(x=20, y=280)
    quantidadep = Entry(pedidos, font=('Arial', '10'))
    quantidadep.place(x=100, y=280, width=50, height=23)

    Label(pedidos, text="DiaEntrega:", background="#CEE3F6").place(x=20, y=320)
    diaentregap = Entry(pedidos, font=('Arial', '10'))
    diaentregap.place(x=100, y=320, width=50, height=23)

    Label(pedidos, text="", background="#CEE3F6").place(x=18, y=440, width=330, height=230)
    Label(pedidos, text="Pesquisar Pelo Dia de Entrega", font=('Arial', '10'), background="#CEE3F6").place(x=100, y=440)
    pesquisarp = Entry(pedidos, font=('Arial', '10'))
    pesquisarp.place(x=100, y=465, width=200, height=23)

    # Botões
    Button(pedidos, text="Salvar", command=salvar).place(x=100, y=360)
    Button(pedidos, text="Editar", command=editar).place(x=270, y=380, width=50, height=50)
    Button(pedidos, text="Apagar", command=apagar).place(x=200, y=380, width=50, height=50)
    Button(pedidos, text="Pesquisar", command=pesquisa).place(x=100, y=500)
    Button(pedidos, text="Mostar Tudo", command=mostrar).place(x=200, y=500)

    # Tabela
    tabela = ttk.Treeview(pedidos, height=3, column=("codpedido", "clienteid", "codproduto", "endereco", "bairro", "cicadeestado",
                                                        "valor", "quantidade", "diaentrega"), show='headings')
    tabela.column("codpedido", minwidth=0, width=5)
    tabela.column("clienteid", minwidth=0, width=5)
    tabela.column("codproduto", minwidth=0, width=5)
    tabela.column("endereco", minwidth=0, width=100)
    tabela.column("bairro", minwidth=0, width=50)
    tabela.column("cicadeestado", minwidth=0, width=50)
    tabela.column("valor", minwidth=0, width=20)
    tabela.column("quantidade", minwidth=0, width=20)
    tabela.column("diaentrega", minwidth=0, width=20)

    tabela.heading("codpedido", text="CodPedido")
    tabela.heading("clienteid", text="ClienteId")
    tabela.heading("codproduto", text="CodProduto")
    tabela.heading("endereco", text="Endereço")
    tabela.heading("bairro", text="Bairro")
    tabela.heading("cicadeestado", text="Cidade e Estado")
    tabela.heading("valor", text="Valor")
    tabela.heading("quantidade", text="Quantidade")
    tabela.heading("diaentrega", text="Dia da Entrega")
    tabela.place(x=360, y=80, width=970, height=600)
    # barra de rolagem (não sei se funciona já que não tem muitos dados no banco)
    scrollv = Scrollbar(pedidos, orient='vertical')
    tabela.configure(yscroll=scrollv.set)
    scrollv.place(x=1332, y=80, width=20, height=600)

    mostrar()

    pedidos.geometry("1280x720")
    # E0ECF8 azul claro
    pedidos.configure(background="#E0ECF8")
    pedidos.mainloop()

#winpedidos()
