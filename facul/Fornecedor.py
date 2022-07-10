from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def winfornecedor():
    import psycopg2
    connection = ""

    fornecedor = Tk()

    def mostrar():
        tabela.delete(*tabela.get_children())
        try:
            connection = psycopg2.connect(database='produtoslimpeza',
                                          user='postgres',
                                          password='sjf7286',
                                          host='localhost')
            cursor = connection.cursor()
            Query = "select * from fornecedor"
            cursor.execute(Query)
            fornecedor = cursor.fetchall()
            for i in fornecedor:
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
            cnpj = cnpjf.get()
            nome = nomef.get()
            endereco = enderecof.get()
            bairro = bairrof.get()
            cidadeestado = cicadeestadof.get()
            telefone = telefonef.get()
            cursor = connection.cursor()

            query = """INSERT INTO fornecedor(cnpj, nome, endereco, bairro, cidadeestado, telefone)
                    VALUES ('{}', '{}', '{}', '{}', '{}', '{}')"""
            cursor.execute(query.format(cnpj, nome, endereco, bairro, cidadeestado, telefone))
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Ocorreu uma falha: {} ".format(error))
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL conexão encerrada salvo")
            mostrar()
            cnpjf.delete(0, END)
            nomef.delete(0, END)
            enderecof.delete(0, END)
            bairrof.delete(0, END)
            cicadeestadof.delete(0, END)
            telefonef.delete(0, END)
            cnpjf.focus()

    def pesquisa():
        tabela.delete(*tabela.get_children())
        pesqui = pesquisarf
        try:
            connection = psycopg2.connect(database='produtoslimpeza',
                                          user='postgres',
                                          password='sjf7286',
                                          host='localhost')
            cursor = connection.cursor()
            Query = "SELECT * FROM fornecedor WHERE nome LIKE '%" + pesqui.get() + "%'"
            cursor.execute(Query)
            connection.commit()
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

    def apagar():
        try:
            itemselect = tabela.selection()[0]
            valores = tabela.item(itemselect, "values")

            connection = psycopg2.connect(database='produtoslimpeza',
                                          user='postgres',
                                          password='sjf7286',
                                          host='localhost')
            cursor = connection.cursor()
            query = """DELETE FROM fornecedor WHERE fornecedorid = {}"""
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
            janelaedit.transient(fornecedor)
            janelaedit.focus_force()
            janelaedit.grab_set()

            itemselecionado = tabela.selection()[0]
            valor = tabela.item(itemselecionado, "values")

            def cnpjedit():
                janelaedit.destroy()
                janelacnpj = Toplevel()
                janelacnpj.title("Editar CNPJ")
                janelacnpj.configure(background="#E0ECF8")
                janelacnpj.geometry("300x150")
                janelacnpj.resizable(False, False)
                janelacnpj.focus_force()
                janelacnpj.grab_set()

                def editcnpj():

                    try:
                        connection = psycopg2.connect(database='produtoslimpeza',
                                                      user='postgres',
                                                      password='sjf7286',
                                                      host='localhost')
                        cnpj = novocnpj.get()
                        cursor = connection.cursor()
                        query = """UPDATE fornecedor SET cnpj = '{}' WHERE fornecedorid = {}"""

                        cursor.execute(query.format(cnpj, valor[0]))
                        connection.commit()
                    except:
                        messagebox.showinfo(title="ERRO", message="Deu erro")
                    finally:
                        if (connection):
                            cursor.close()
                            connection.close()
                            print("PostgreSQL conexão encerrada")
                    janelacnpj.destroy()
                    mostrar()

                Label(janelacnpj, text="Digite o novo CNPJ", background="#E0ECF8").place(x=100, y=30)
                novocnpj = Entry(janelacnpj)
                novocnpj.place(x=100, y=50, width=150, height=23)
                Button(janelacnpj, text="Editar", command=editcnpj).place(x=100, y=80)

            def nomeeditf():
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
                        query = """UPDATE fornecedor 
                                       SET nome = '{}'
                                       WHERE fornecedorid = {}"""

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

            def enderecoedit():
                janelaedit.destroy()
                janelaendereco = Toplevel()
                janelaendereco.title("Editar CPF")
                janelaendereco.configure(background="#E0ECF8")
                janelaendereco.geometry("300x150")
                janelaendereco.resizable(False, False)
                janelaendereco.focus_force()
                janelaendereco.grab_set()

                def editender():
                    try:
                        connection = psycopg2.connect(database='produtoslimpeza',
                                                      user='postgres',
                                                      password='sjf7286',
                                                      host='localhost')
                        enderf = novoender.get()
                        cursor = connection.cursor()
                        query = """UPDATE fornecedor 
                                                   SET endereco = '{}'
                                                   WHERE fornecedorid = {}"""

                        cursor.execute(query.format(enderf, valor[0]))
                        connection.commit()
                    except:
                        messagebox.showinfo(title="ERRO", message="Deu erro")
                    finally:
                        if (connection):
                            cursor.close()
                            connection.close()
                            print("PostgreSQL conexão encerrada")
                    janelaendereco.destroy()
                    mostrar()

                Label(janelaendereco, text="Digite o novo Endereço", background="#E0ECF8").place(x=100, y=30)
                novoender = Entry(janelaendereco)
                novoender.place(x=100, y=50, width=150, height=23)
                Button(janelaendereco, text="Editar", command=editender).place(x=100, y=80)

            def bairroedit():
                janelaedit.destroy()
                janelabairro = Toplevel()
                janelabairro.title("Editar o Bairro")
                janelabairro.configure(background="#E0ECF8")
                janelabairro.geometry("300x150")
                janelabairro.resizable(False, False)
                janelabairro.focus_force()
                janelabairro.grab_set()

                def editbairro():
                    try:
                        connection = psycopg2.connect(database='produtoslimpeza',
                                                      user='postgres',
                                                      password='sjf7286',
                                                      host='localhost')
                        bairro = novobairro.get()
                        cursor = connection.cursor()
                        query = """UPDATE fornecedor 
                                                                   SET bairro = '{}'
                                                                   WHERE fornecedorid = {}"""

                        cursor.execute(query.format(bairro, valor[0]))
                        connection.commit()
                    except:
                        messagebox.showinfo(title="ERRO", message="Deu erro")
                    finally:
                        if (connection):
                            cursor.close()
                            connection.close()
                            print("PostgreSQL conexão encerrada")
                    janelabairro.destroy()
                    mostrar()

                Label(janelabairro, text="Digite o novo Endereço", background="#E0ECF8").place(x=100, y=30)
                novobairro = Entry(janelabairro)
                novobairro.place(x=100, y=50, width=150, height=23)
                Button(janelabairro, text="Editar", command=editbairro).place(x=100, y=80)

            def ciestadoedit():
                janelaedit.destroy()
                janelauf = Toplevel()
                janelauf.title("Editar CIdade e Estado")
                janelauf.configure(background="#E0ECF8")
                janelauf.geometry("300x150")
                janelauf.resizable(False, False)
                janelauf.focus_force()
                janelauf.grab_set()

                def edituf():
                    try:
                        connection = psycopg2.connect(database='produtoslimpeza',
                                                      user='postgres',
                                                      password='sjf7286',
                                                      host='localhost')
                        uf = novouf.get()
                        cursor = connection.cursor()
                        query = """UPDATE fornecedor 
                                                                   SET cidadeestado = '{}'
                                                                   WHERE fornecedorid = {}"""

                        cursor.execute(query.format(uf, valor[0]))
                        connection.commit()
                    except:
                        messagebox.showinfo(title="ERRO", message="Deu erro")
                    finally:
                        if (connection):
                            cursor.close()
                            connection.close()
                            print("PostgreSQL conexão encerrada")
                    janelauf.destroy()
                    mostrar()

                Label(janelauf, text="Digite o novo Endereço", background="#E0ECF8").place(x=100, y=30)
                novouf = Entry(janelauf)
                novouf.place(x=100, y=50, width=150, height=23)
                Button(janelauf, text="Editar", command=edituf).place(x=100, y=80)

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
                        query = """UPDATE fornecedor 
                                    SET telefone = '{}'
                                    WHERE fornecedorid = {}"""

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
            Button(janelaedit, text="CNPJ", command=cnpjedit).place(x=70, y=60, width=100, height=60)
            Button(janelaedit, text="Nome", command=nomeeditf).place(x=220, y=60, width=100, height=60)
            Button(janelaedit, text="Endereço", command=enderecoedit).place(x=370, y=60, width=100, height=60)
            Button(janelaedit, text="Bairro", command=bairroedit).place(x=70, y=150, width=100, height=60)
            Button(janelaedit, text="CidadeEstado", command=ciestadoedit).place(x=220, y=150, width=100, height=60)
            Button(janelaedit, text="Telefone", command=teleedit).place(x=370, y=150, width=100, height=60)
        except:
            messagebox.showinfo(title="ERRO", message="Selecione um item na tabela para ser editado")

    # ------------------------//-------------------
    fornecedor.title("Cadastro de Fornecedor")

    Label(fornecedor, text="", background="#CEE3F6").place(x=18, y=40, width=330, height=310)
    Label(fornecedor, text="CNPJ:", background="#CEE3F6").place(x=50, y=80)
    cnpjf = Entry(fornecedor)
    cnpjf.place(x=100, y=80, width=100, height=23)

    Label(fornecedor, text="Nome:", background="#CEE3F6").place(x=50, y=120)
    nomef = Entry(fornecedor, font=('Arial', '9'))
    nomef.place(x=100, y=120, width=245, height=23)

    Label(fornecedor, text="Endereço:", background="#CEE3F6").place(x=42, y=160)
    enderecof = Entry(fornecedor, font=('Arial', '10'))
    enderecof.place(x=100, y=160, width=100, height=23)

    Label(fornecedor, text="Bairro:", background="#CEE3F6").place(x=42, y=200)
    bairrof = Entry(fornecedor, font=('Arial', '10'))
    bairrof.place(x=100, y=200, width=100, height=23)

    Label(fornecedor, text="CidadeEstado:", background="#CEE3F6").place(x=20, y=240)
    cicadeestadof = Entry(fornecedor, font=('Arial', '10'))
    cicadeestadof.place(x=100, y=240, width=100, height=23)

    Label(fornecedor, text="Telefone:", background="#CEE3F6").place(x=42, y=280)
    telefonef = Entry(fornecedor, font=('Arial', '10'))
    telefonef.place(x=100, y=280, width=100, height=23)

    Label(fornecedor, text="", background="#CEE3F6").place(x=18, y=440, width=330, height=230)
    Label(fornecedor, text="Pesquisar:", background="#CEE3F6").place(x=35, y=500)
    pesquisarf = Entry(fornecedor, font=('Arial', '10'))
    pesquisarf.place(x=100, y=500, width=200, height=23)
    # Botões
    Button(fornecedor, text="Salvar", command=salvar).place(x=100, y=320)
    Button(fornecedor, text="Editar", command=editar).place(x=100, y=380, width=50, height=50)
    Button(fornecedor, text="Apagar", command=apagar).place(x=200, y=380, width=50, height=50)
    Button(fornecedor, text="Pesquisar", command=pesquisa).place(x=100, y=540)
    Button(fornecedor, text="Mostar Tudo", command=mostrar).place(x=200, y=540)

    # Tabela
    tabela = ttk.Treeview(fornecedor, height=3, column=("id", "cnpj", "nome", "endereco", "bairro",
                                                        "cidadeestado", "telefone"), show='headings')
    tabela.column("id", minwidth=0, width=5)
    tabela.column("cnpj", minwidth=0, width=50)
    tabela.column("nome", minwidth=0, width=200)
    tabela.column("endereco", minwidth=0, width=50)
    tabela.column("bairro", minwidth=0, width=50)
    tabela.column("cidadeestado", minwidth=0, width=50)
    tabela.column("telefone", minwidth=0, width=50)

    tabela.heading("id", text="FornecedorId")
    tabela.heading("cnpj", text="CNPJ")
    tabela.heading("nome", text="Nome")
    tabela.heading("endereco", text="Endereço")
    tabela.heading("bairro", text="Bairro")
    tabela.heading("cidadeestado", text="CidadeEstado")
    tabela.heading("telefone", text="Telefone")
    tabela.place(x=360, y=80, width=970, height=600)
    # barra de rolagem
    scrollv = Scrollbar(fornecedor, orient='vertical')
    tabela.configure(yscroll=scrollv.set)
    scrollv.place(x=1332, y=80, width=20, height=600)

    mostrar()

    fornecedor.geometry("1280x720")
    # E0ECF8 azul claro
    fornecedor.configure(background="#E0ECF8")
    fornecedor.mainloop()

#winfornecedor()
