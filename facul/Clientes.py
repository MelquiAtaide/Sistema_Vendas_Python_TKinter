from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def wincliente():
    import psycopg2
    connection = ""

    clientes = Tk()

    def mostrar():
        tabela.delete(*tabela.get_children())
        try:
            connection = psycopg2.connect(database='produtoslimpeza',
                                          user='postgres',
                                          password='sjf7286',
                                          host='localhost')
            cursor = connection.cursor()
            Query = "select * from clientes"
            cursor.execute(Query)
            print("Selecionando os registros")
            clientes = cursor.fetchall()
            print("Imprimindo cada linha e coluna")
            for i in clientes:
                tabela.insert("", "end", values=i)
        except (Exception, psycopg2.Error) as error:
            print("Ocorreu uma falha: {} ".format(error))
        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL conexão encerrada")

    def salvar():
        try:
            connection = psycopg2.connect(database='produtoslimpeza',
                                          user='postgres',
                                          password='sjf7286',
                                          host='localhost')
            nome = nomec.get()
            cpfc = cpf.get()
            telefone = telefonec.get()
            cursor = connection.cursor()

            query = """INSERT INTO clientes(nome, cpf, telefone)
                    VALUES ('{}', '{}', '{}')"""
            cursor.execute(query.format(nome, cpfc, telefone))
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Ocorreu uma falha, informe o erro {} ao suporte".format(error))
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL conexão encerrada salvo")
            mostrar()
            nomec.delete(0, END)
            cpf.delete(0, END)
            telefonec.delete(0, END)
            nomec.focus()

    def pesquisa():
        tabela.delete(*tabela.get_children())
        pesqui = pesquisarc.get()
        try:
            connection = psycopg2.connect(database='produtoslimpeza',
                                          user='postgres',
                                          password='sjf7286',
                                          host='localhost')
            cursor = connection.cursor()

            Query = "SELECT * FROM clientes WHERE nome LIKE '%{}%'"
            cursor.execute(Query.format(pesqui))
            connection.commit()
            clientess = cursor.fetchall()
            for i in clientess:
                tabela.insert("", "end", values=i)
        except (Exception, psycopg2.Error) as error:
            print("Ocorreu uma falha, informe o erro {} ao suporte".format(error))
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL conexão encerrada")

    def apagar():

        itemselect = tabela.selection()[0]
        valores = tabela.item(itemselect, "values")

        try:
            connection = psycopg2.connect(database='produtoslimpeza',
                                          user='postgres',
                                          password='sjf7286',
                                          host='localhost')
            cursor = connection.cursor()
            query = """DELETE FROM clientes WHERE clienteid = {}"""
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
            janelaedit.geometry("500x200")
            janelaedit.resizable(False, False)
            janelaedit.transient(clientes)
            janelaedit.focus_force()
            janelaedit.grab_set()

            itemselecionado = tabela.selection()[0]
            valor = tabela.item(itemselecionado, "values")

            def nomeedit():
                janelaedit.destroy()
                janelanome = Toplevel()
                janelanome.title("Editar Nome")
                janelanome.configure(background="#E0ECF8")
                janelanome.geometry("300x150")
                janelanome.resizable(False, False)
                janelanome.focus_force()
                janelanome.grab_set()

                def editnome():
                    try:
                        connection = psycopg2.connect(database='produtoslimpeza',
                                                      user='postgres',
                                                      password='sjf7286',
                                                      host='localhost')
                        nomen = novonome.get()
                        cursor = connection.cursor()
                        query = """UPDATE clientes 
                                       SET nome = '{}'
                                       WHERE clienteid = {}"""

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
                Button(janelanome, text="Editar", command=editnome).place(x=100, y=80)

            def cpfedit():
                janelaedit.destroy()
                janelacpf = Toplevel()
                janelacpf.title("Editar CPF")
                janelacpf.configure(background="#E0ECF8")
                janelacpf.geometry("300x150")
                janelacpf.resizable(False, False)
                janelacpf.focus_force()
                janelacpf.grab_set()

                def editcpf():
                    try:
                        connection = psycopg2.connect(database='produtoslimpeza',
                                                      user='postgres',
                                                      password='sjf7286',
                                                      host='localhost')
                        cpfn = novocpf.get()
                        cursor = connection.cursor()
                        query = """UPDATE clientes 
                                                   SET cpf = '{}'
                                                   WHERE clienteid = {}"""

                        cursor.execute(query.format(cpfn, valor[0]))
                        connection.commit()
                    except:
                        messagebox.showinfo(title="ERRO", message="Deu erro")
                    finally:
                        if (connection):
                            cursor.close()
                            connection.close()
                            print("PostgreSQL conexão encerrada")
                    janelacpf.destroy()
                    mostrar()

                Label(janelacpf, text="Digite o novo CPF", background="#E0ECF8").place(x=100, y=30)
                novocpf = Entry(janelacpf)
                novocpf.place(x=100, y=50, width=150, height=23)
                Button(janelacpf, text="Editar", command=editcpf).place(x=100, y=80)

            def teleedit():
                janelaedit.destroy()
                janelatele = Toplevel()
                janelatele.title("Editar Telefone")
                janelatele.configure(background="#E0ECF8")
                janelatele.geometry("300x150")
                janelatele.resizable(False, False)
                janelatele.focus_force()
                janelatele.grab_set()

                def edittele():
                    try:
                        connection = psycopg2.connect(database='produtoslimpeza',
                                                      user='postgres',
                                                      password='sjf7286',
                                                      host='localhost')
                        telen = novotele.get()
                        cursor = connection.cursor()
                        query = """UPDATE clientes 
                                    SET telefone = '{}'
                                    WHERE clienteid = {}"""

                        cursor.execute(query.format(telen, valor[0]))
                        connection.commit()
                    except:
                        messagebox.showinfo(title="ERRO", message="Deu erro")
                    finally:
                        if (connection):
                            cursor.close()
                            connection.close()
                            print("PostgreSQL conexão encerrada")
                    janelatele.destroy()
                    mostrar()

                Label(janelatele, text="Digite o novo telefone", background="#E0ECF8").place(x=100, y=30)
                novotele = Entry(janelatele)
                novotele.place(x=100, y=50, width=150, height=23)
                Button(janelatele, text="Editar", command=edittele).place(x=100, y=80)

            Label(janelaedit, text="Escolha o que deseja editar", background="#E0ECF8", font=('Arial', '15')).place(
                x=140, y=20)
            Button(janelaedit, text="Nome", command=nomeedit).place(x=70, y=60, width=100, height=60)
            Button(janelaedit, text="CPF", command=cpfedit).place(x=220, y=60, width=100, height=60)
            Button(janelaedit, text="Telefone", command=teleedit).place(x=370, y=60, width=100, height=60)
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um item na tabela para ser editado")

    # ------------------------//-------------------
    clientes.title("Cadastro Cliente")

    Label(clientes, text="", background="#CEE3F6").place(x=18, y=40, width=330, height=230)
    Label(clientes, text="Nome:", background="#CEE3F6").place(x=50, y=80)
    nomec = Entry(clientes)
    nomec.place(x=100, y=80, width=245, height=23)

    Label(clientes, text="CPF:", background="#CEE3F6").place(x=50, y=120)
    cpf = Entry(clientes, font=('Arial', '9'))
    cpf.place(x=100, y=120, width=100, height=23)

    Label(clientes, text="Telefone:", background="#CEE3F6").place(x=42, y=160)
    telefonec = Entry(clientes, font=('Arial', '10'))
    telefonec.place(x=100, y=160, width=100, height=23)

    Label(clientes, text="", background="#CEE3F6").place(x=18, y=440, width=330, height=230)
    Label(clientes, text="Pesquisar:", background="#CEE3F6").place(x=35, y=500)
    pesquisarc = Entry(clientes, font=('Arial', '10'))
    pesquisarc.place(x=100, y=500, width=200, height=23)
    # Botões
    Button(clientes, text="Salvar", command=salvar).place(x=100, y=190)
    Button(clientes, text="Editar", command=editar).place(x=200, y=380, width=50, height=50)
    Button(clientes, text="Apagar", command=apagar).place(x=200, y=300, width=50, height=50)
    Button(clientes, text="Pesquisar", command=pesquisa).place(x=100, y=540)
    Button(clientes, text="Mostar Tudo", command=mostrar).place(x=200, y=540)

    # Tabela
    tabela = ttk.Treeview(clientes, height=3, column=("id", "nome", "cpf", "fone"), show='headings')
    tabela.column("id", minwidth=0, width=2)
    tabela.column("nome", minwidth=0, width=200)
    tabela.column("cpf", minwidth=0, width=50)
    tabela.column("fone", minwidth=0, width=50)

    tabela.heading("id", text="Código")
    tabela.heading("nome", text="Nome")
    tabela.heading("cpf", text="CPF")
    tabela.heading("fone", text="Telefone")
    tabela.place(x=360, y=80, width=970, height=600)
    # barra de rolagem
    scrollv = Scrollbar(clientes, orient='vertical')
    tabela.configure(yscroll=scrollv.set)
    scrollv.place(x=1332, y=80, width=20, height=600)

    mostrar()

    clientes.geometry("1280x720")
    # E0ECF8 azul claro
    clientes.configure(background="#E0ECF8")
    clientes.mainloop()

#wincliente()