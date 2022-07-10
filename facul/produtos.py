from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def winprodutos():
    import psycopg2
    connection = ""

    produtos = Tk()

    def mostrar():
        tabela.delete(*tabela.get_children())
        try:
            connection = psycopg2.connect(database='produtoslimpeza',
                                          user='postgres',
                                          password='sjf7286',
                                          host='localhost')
            cursor = connection.cursor()
            Query = "select * from produtos"
            cursor.execute(Query)
            fornecedor = cursor.fetchall()
            for i in fornecedor:
                tabela.insert("", "end", values=i)
        except (Exception, psycopg2.Error) as error:
            print("Ocorreu uma falha: {}".format(error))
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL conexão encerrada")

    def salvarp():
        try:
            connection = ""
            connection = psycopg2.connect(database='produtoslimpeza',
                                          user='postgres',
                                          password='sjf7286',
                                          host='localhost')
            cod = codproduto.get()
            fornecedorp = fornecedorid.get()
            nome = nomep.get()
            descri = descricao.get()
            valor = valorp.get()
            quantidade = quantidadep.get()
            cursor = connection.cursor()

            query = """INSERT INTO produtos(codproduto, fornecedorid, nome, descricao, valor, quantidade)
                    VALUES ('{}', '{}', '{}', '{}', '{}', '{}')"""
            cursor.execute(query.format(cod, fornecedorp, nome, descri, valor, quantidade))
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Ocorreu uma falha: {}".format(error))
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL conexão encerrada salvo")
            mostrar()
            fornecedorid.delete(0, END)
            nomep.delete(0, END)
            descricao.delete(0, END)
            valorp.delete(0, END)
            quantidadep.delete(0, END)
            fornecedorid.focus()

    def pesquisa():
        tabela.delete(*tabela.get_children())
        pesqui = pesquisarp.get()
        try:
            connection = psycopg2.connect(database='produtoslimpeza',
                                          user='postgres',
                                          password='sjf7286',
                                          host='localhost')
            cursor = connection.cursor()
            Query = "SELECT * FROM produtos WHERE nome LIKE '%{}%'"
            cursor.execute(Query.format(pesqui))
            connection.commit()
            produtoss = cursor.fetchall()
            for i in produtoss:
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
            query = """DELETE FROM produtos WHERE codproduto = {}"""
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
        try:
            janelaedit = Toplevel()
            janelaedit.title("Editar")
            janelaedit.configure(background="#E0ECF8")
            janelaedit.geometry("500x300")
            janelaedit.resizable(False, False)
            janelaedit.transient(produtos)
            janelaedit.focus_force()
            janelaedit.grab_set()

            itemselecionado = tabela.selection()[0]
            valor = tabela.item(itemselecionado, "values")

            def forneedit():
                janelaedit.destroy()
                janelaforne = Toplevel()
                janelaforne.title("Editar fornecedor")
                janelaforne.configure(background="#E0ECF8")
                janelaforne.geometry("300x150")
                janelaforne.resizable(False, False)
                janelaforne.focus_force()
                janelaforne.grab_set()

                def forneedit():

                    try:
                        connection = psycopg2.connect(database='produtoslimpeza',
                                                      user='postgres',
                                                      password='sjf7286',
                                                      host='localhost')
                        forneid = novoforne.get()
                        cursor = connection.cursor()
                        query = """UPDATE produtos SET fornecedorid = '{}' WHERE codproduto = {}"""

                        cursor.execute(query.format(forneid, valor[0]))
                        connection.commit()
                    except:
                        messagebox.showinfo(title="ERRO", message="Deu erro")
                    finally:
                        if (connection):
                            cursor.close()
                            connection.close()
                            print("PostgreSQL conexão encerrada")
                    janelaforne.destroy()
                    mostrar()

                Label(janelaforne, text="Digite o novo fornecedor", background="#E0ECF8").place(x=100, y=30)
                novoforne = Entry(janelaforne)
                novoforne.place(x=100, y=50, width=150, height=23)
                Button(janelaforne, text="Editar", command=forneedit).place(x=100, y=80)

            def nomeeditp():
                janelaedit.destroy()
                janelanome = Toplevel()
                janelanome.title("Editar Nome")
                janelanome.configure(background="#E0ECF8")
                janelanome.geometry("300x150")
                janelanome.resizable(False, False)
                janelanome.focus_force()
                janelanome.grab_set()

                def editnomep():
                    try:
                        connection = psycopg2.connect(database='produtoslimpeza',
                                                      user='postgres',
                                                      password='sjf7286',
                                                      host='localhost')
                        nomen = novonome.get()
                        cursor = connection.cursor()
                        query = """UPDATE produtos 
                                       SET nome = '{}'
                                       WHERE codproduto = {}"""

                        cursor.execute(query.format(nomen, valor[0]))
                        connection.commit()
                    except:
                        messagebox.showinfo(title="ERRO", message="Deu erro")
                    finally:
                        if (connection):
                            cursor.close()
                            connection.close()
                            print("PostgreSQL conexão encerrada")
                    janelanome.destroy()
                    mostrar()

                Label(janelanome, text="Digite o novo nome", background="#E0ECF8").place(x=100, y=30)
                novonome = Entry(janelanome)
                novonome.place(x=100, y=50, width=150, height=23)
                Button(janelanome, text="Editar", command=editnomep).place(x=100, y=80)

            def descricaoedit():
                janelaedit.destroy()
                janeladescri = Toplevel()
                janeladescri.title("Editar Descrição")
                janeladescri.configure(background="#E0ECF8")
                janeladescri.geometry("300x150")
                janeladescri.resizable(False, False)
                janeladescri.focus_force()
                janeladescri.grab_set()

                def editdes():
                    try:
                        connection = psycopg2.connect(database='produtoslimpeza',
                                                      user='postgres',
                                                      password='sjf7286',
                                                      host='localhost')
                        descricaop = novades.get()
                        cursor = connection.cursor()
                        query = """UPDATE produtos 
                                                   SET descricao = '{}'
                                                   WHERE codproduto = {}"""

                        cursor.execute(query.format(descricaop, valor[0]))
                        connection.commit()
                    except:
                        messagebox.showinfo(title="ERRO", message="Deu erro")
                    finally:
                        if (connection):
                            cursor.close()
                            connection.close()
                            print("PostgreSQL conexão encerrada")
                    janeladescri.destroy()
                    mostrar()

                Label(janeladescri, text="Digite a nova descrição", background="#E0ECF8").place(x=100, y=30)
                novades = Entry(janeladescri)
                novades.place(x=100, y=50, width=150, height=23)
                Button(janeladescri, text="Editar", command=editdes).place(x=100, y=80)

            def valoredit():
                janelaedit.destroy()
                janelavalor = Toplevel()
                janelavalor.title("Editar o Valor")
                janelavalor.configure(background="#E0ECF8")
                janelavalor.geometry("300x150")
                janelavalor.resizable(False, False)
                janelavalor.focus_force()
                janelavalor.grab_set()

                def editvalor():
                    try:
                        connection = psycopg2.connect(database='produtoslimpeza',
                                                      user='postgres',
                                                      password='sjf7286',
                                                      host='localhost')
                        valorp = novovalor.get()
                        cursor = connection.cursor()
                        query = """UPDATE produtos 
                                    SET valor = '{}'
                                    WHERE codproduto = {}"""

                        cursor.execute(query.format(valorp, valor[0]))
                        connection.commit()
                    except:
                        messagebox.showinfo(title="ERRO", message="Deu erro")
                    finally:
                        if (connection):
                            cursor.close()
                            connection.close()
                            print("PostgreSQL conexão encerrada")
                    janelavalor.destroy()
                    mostrar()

                Label(janelavalor, text="Digite o novo Valor", background="#E0ECF8").place(x=100, y=30)
                novovalor = Entry(janelavalor)
                novovalor.place(x=100, y=50, width=150, height=23)
                Button(janelavalor, text="Editar", command=editvalor).place(x=100, y=80)

            def quantidadeedit():
                janelaedit.destroy()
                janelaquanti = Toplevel()
                janelaquanti.title("Editar Quantidade")
                janelaquanti.configure(background="#E0ECF8")
                janelaquanti.geometry("300x150")
                janelaquanti.resizable(False, False)
                janelaquanti.focus_force()
                janelaquanti.grab_set()

                def editquanti():
                    try:
                        connection = psycopg2.connect(database='produtoslimpeza',
                                                      user='postgres',
                                                      password='sjf7286',
                                                      host='localhost')
                        quanti = novoquan.get()
                        cursor = connection.cursor()
                        query = """UPDATE produtos 
                                   SET quantidade = '{}'
                                   WHERE codproduto = {}"""

                        cursor.execute(query.format(quanti, valor[0]))
                        connection.commit()
                    except:
                        messagebox.showinfo(title="ERRO", message="Deu erro")
                    finally:
                        if (connection):
                            cursor.close()
                            connection.close()
                            print("PostgreSQL conexão encerrada")
                    janelaquanti.destroy()
                    mostrar()

                Label(janelaquanti, text="Digite a quantidade", background="#E0ECF8").place(x=100, y=30)
                novoquan = Entry(janelaquanti)
                novoquan.place(x=100, y=50, width=150, height=23)
                Button(janelaquanti, text="Editar", command=editquanti).place(x=100, y=80)

            Label(janelaedit, text="Escolha o que deseja editar", background="#E0ECF8", font=('Arial', '15')).place(
                x=140, y=20)
            Button(janelaedit, text="FornecedorId", command=forneedit).place(x=70, y=60, width=100, height=60)
            Button(janelaedit, text="Nome", command=nomeeditp).place(x=220, y=60, width=100, height=60)
            Button(janelaedit, text="Descrição", command=descricaoedit).place(x=370, y=60, width=100, height=60)
            Button(janelaedit, text="Valor", command=valoredit).place(x=70, y=150, width=100, height=60)
            Button(janelaedit, text="Quantidade", command=quantidadeedit).place(x=220, y=150, width=100, height=60)
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um item na tabela para ser editado")

    # ------------------------//-------------------
    produtos.title("Cadastro de produtos")

    Label(produtos, text="", background="#CEE3F6").place(x=18, y=40, width=330, height=310)
    Label(produtos, text="CodProduto:", background="#CEE3F6").place(x=20, y=50)
    codproduto = Entry(produtos)
    codproduto.place(x=100, y=50, width=100, height=23)

    Label(produtos, text="FornecedorId:", background="#CEE3F6").place(x=20, y=80)
    fornecedorid = Entry(produtos)
    fornecedorid.place(x=100, y=80, width=100, height=23)

    Label(produtos, text="Nome:", background="#CEE3F6").place(x=50, y=120)
    nomep = Entry(produtos, font=('Arial', '9'))
    nomep.place(x=100, y=120, width=245, height=23)

    Label(produtos, text="Descrição:", background="#CEE3F6").place(x=42, y=160)
    descricao = Entry(produtos, font=('Arial', '10'))
    descricao.place(x=100, y=160, width=245, height=70)

    Label(produtos, text="Valor:", background="#CEE3F6").place(x=42, y=240)
    valorp = Entry(produtos, font=('Arial', '10'))
    valorp.place(x=100, y=240, width=50, height=23)

    Label(produtos, text="Quantidade:", background="#CEE3F6").place(x=20, y=280)
    quantidadep = Entry(produtos, font=('Arial', '10'))
    quantidadep.place(x=100, y=280, width=50, height=23)

    Label(produtos, text="", background="#CEE3F6").place(x=18, y=440, width=330, height=230)
    Label(produtos, text="Pesquisar:", background="#CEE3F6").place(x=35, y=500)
    pesquisarp = Entry(produtos, font=('Arial', '10'))
    pesquisarp.place(x=100, y=500, width=200, height=23)
    # Botões
    Button(produtos, text="Salvar", command=salvarp).place(x=100, y=320)
    Button(produtos, text="Editar", command=editar).place(x=100, y=380, width=50, height=50)
    Button(produtos, text="Apagar", command=apagar).place(x=200, y=380, width=50, height=50)
    Button(produtos, text="Pesquisar", command=pesquisa).place(x=100, y=540)
    Button(produtos, text="Mostar Tudo", command=mostrar).place(x=200, y=540)

    # Tabela
    tabela = ttk.Treeview(produtos, height=3, column=("codproduto", "fornecedorid", "nome", "descri", "valor",
                                                        "quantidade"), show='headings')
    tabela.column("codproduto", minwidth=0, width=5)
    tabela.column("fornecedorid", minwidth=0, width=5)
    tabela.column("nome", minwidth=0, width=100)
    tabela.column("descri", minwidth=0, width=400)
    tabela.column("valor", minwidth=0, width=5)
    tabela.column("quantidade", minwidth=0, width=20)

    tabela.heading("codproduto", text="CodProduto")
    tabela.heading("fornecedorid", text="FornecedorId")
    tabela.heading("nome", text="Nome")
    tabela.heading("descri", text="Descrição")
    tabela.heading("valor", text="Valor")
    tabela.heading("quantidade", text="Quantidade")
    tabela.place(x=360, y=80, width=970, height=600)
    # barra de rolagem
    scrollv = Scrollbar(produtos, orient='vertical')
    tabela.configure(yscroll=scrollv.set)
    scrollv.place(x=1332, y=80, width=20, height=600)

    mostrar()

    produtos.geometry("1280x720")
    # E0ECF8 azul claro
    produtos.configure(background="#E0ECF8")
    produtos.mainloop()

#winprodutos()
