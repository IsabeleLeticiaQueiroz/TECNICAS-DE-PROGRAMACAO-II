import sqlite3
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
tela = Tk()

tela.title("Radio Buttons")

# cor da tela
tela.configure(background='grey')
# tamanho da tela
tela.geometry("800x600")

# criando banco
conn = sqlite3.connect("MyDB.db")

# criando cursor
cur = conn.cursor()

# criar tabela
cur.execute("""
CREATE TABLE IF NOT EXISTS pessoas (
    codigo INT PRIMARY KEY, 
    nome TEXT, 
    idade INTEGER, 
    sexo TEXT, 
    altura REAL, 
    peso REAL, 
    cidade TEXT, 
    datanasc TEXT, 
    dataAtual TEXT, 
    dataCadastro TEXT, 
    descricao TEXT
)
""")
conn.commit()
conn.close()

def insercao():
    conn = sqlite3.connect("MyDB.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO pessoas VALUES(:codigo,:nome,:idade,:sexo,:altura, :peso, :cidade,:dataNasc, :dataAtual,:dataCadastro,:descricao)",
                {'codigo': txt_codigo.get(), 'nome': txt_nome.get(), 'idade': txt_idade.get(), 'sexo': var.get(), 'altura': txt_altura.get(), 'peso': txt_peso.get(), 'cidade': combo.get(), 'dataNasc': txt_datanasc.get(),
                 'dataAtual': txt_dataatu.get(), 'dataCadastro': txt_datacad.get(), 'descricao': txt_desc.get()})
    conn.commit()
    conn.close()
    # clear text boxes
    txt_codigo.delete(0, END)
    txt_nome.delete(0, END)
    txt_idade.delete(0, END)
    txt_altura.delete(0, END)
    txt_peso.delete(0, END)
    txt_datanasc.delete(0, END)
    txt_datacad.delete(0, END)
    txt_dataatu.delete(0, END)
    txt_desc.delete(0, END)

def consulta():
    # Pegando o código fornecido no campo de entrada (txt_codigo)
    codigo = txt_codigo.get()

    # Verificando se o campo de código não está vazio
    if codigo == '':
        lbl_retorno.delete(1.0, END)  # Limpa o campo de texto
        return  # Sai da função sem fazer mais nada

    # Se o código não estiver vazio, faz a consulta
    conn = sqlite3.connect("MyDB.db")
    cur = conn.cursor()

    # Executar a consulta para buscar o código específico
    cur.execute("SELECT * FROM pessoas WHERE codigo = ?", (codigo,))
    records = cur.fetchall()

    # Se não encontrar registros
    if not records:
        lbl_retorno.delete(1.0, END)  # Limpa o campo de texto
        lbl_retorno.insert(END, f"Nenhum registro encontrado para o código {codigo}.")
    else:
        # Formatar os resultados para exibição
        print_records = ''
        for rec in records:
            print_records += (f"Código: {rec[0]}, Nome: {rec[1]}, Idade: {rec[2]}, Sexo: {rec[3]}, "
                              f"Altura: {rec[4]}, Peso: {rec[5]}, Cidade: {rec[6]}, Data Nasc: {rec[7]}, "
                              f"Data Atual: {rec[8]}, Data Cadastro: {rec[9]}, Descrição: {rec[10]}\n")
        
        lbl_retorno.delete(1.0, END)  # Limpa o campo de texto
        lbl_retorno.insert(END, print_records)  # Insere os resultados na label Text

    conn.close()



def delete():
    conn = sqlite3.connect("MyDB.db")
    cur = conn.cursor()
    cur.execute("DELETE from pessoas WHERE codigo = " + txt_codigo.get())
    conn.commit()
    conn.close()
    messagebox.showinfo("Excluindo...", "Registro deletado com sucesso")

def update():
    conn= sqlite3.connect("MyDB.db")
    cur = conn.cursor()
    record_id = txt_codigo.get()
    cur.execute("""UPDATE pessoas SET"
                nome = :nome,
                idade = :idade,
                sexo = :sexo,
                altura = :altura,
                peso = :peso,
                cidade = :cidade,
                datanasc = :datanasc,
                dataAtual = :dataAtual,
                dataCadastro = :dataCadastro,
                descricao = :descricao
                WHERE codigo = :codigo""",
                {'nome': txt_nome.get(),
                'idade': txt_idade.get(),
                'sexo': var.get(),
                'altura': txt_altura.get(),
                'peso': txt_peso.get(),
                'cidade': combo.get(),
                'datanasc': txt_datanasc.get(),
                'dataAtual': txt_dataatu.get(),
                'dataCadastro': txt_datacad.get(),
                'descricao': txt_desc.get(),
                'codigo': record_id})
    conn.commit()
    conn.close()
def escolher_img():
    caminho_img = filedialog.askopenfilename(initialdir=pasta_inicial, title="Escolha uma imagem", filetypes=(("Arquivos de imagem", "*.jpg;*.jpeg;*.png"),("Todos os arquivos", "*.*")))
    img_pil = Image.open(caminho_img)
    largura, altura = img_pil.size
    if largura > 150:
        proporcao = largura/ 150
        nova_altura = int(altura/proporcao)
        img_pil = img_pil.resize((110, nova_altura))
    img_tk = ImageTk.PhotoImage(img_pil)
    lbl_img = Label(tela, image=img_tk)
    lbl_img.image = img_tk
    lbl_img.place(x=10, y=50)

btn_escolher = Button(tela, text="Escolher imagem", command=escolher_img)
btn_escolher.place(x=10, y=140)


# definindo checkbox ja assinalada de aconrdo com seu valor
# definindo que o crtiterio do valor pro checkbox ser assinalado é string e valor "m"
var = StringVar()
var.set("m")

# CHECKBOXES
radio_buttonm = Radiobutton(tela,text="M", variable=var, value="m")
radio_buttonm.place(x=170, y=150)
radio_buttonf = Radiobutton(tela, text="F", variable=var, value="f")
radio_buttonf.place(x=220, y=150)
# combobox
combo = Combobox(tela)
combo['values']=("Iguape", "Ilha Comprida", "Registro", "Juquia", "Miracatu", "Cajati")
combo.current(1)
combo.place(x=550, y=150)
# cadastro de imagem
pasta_inicial = ""

# Fotos dos botões com resize para 30x30
foto_salvar = Image.open(r"icones\salvar.png").resize((30, 30))
foto_editar = Image.open(r"icones\pencil.png").resize((30, 30))
foto_delet = Image.open(r"icones\delete.png").resize((30, 30))
foto_search = Image.open(r"icones\search.png").resize((30, 30))
foto_sair = Image.open(r"icones\logout.png").resize((30, 30))

# Convertendo as imagens redimensionadas para o formato compatível com o tkinter
foto_salvar = ImageTk.PhotoImage(foto_salvar)
foto_editar = ImageTk.PhotoImage(foto_editar)
foto_delet = ImageTk.PhotoImage(foto_delet)
foto_search = ImageTk.PhotoImage(foto_search)
foto_sair = ImageTk.PhotoImage(foto_sair)

# Botões inferiores
btn_salvar = Button(tela, text="Salvar", image=foto_salvar, compound=TOP)
btn_salvar.place(x=130, y=310)
btn_salvar.config(command=insercao)
btn_editar = Button(tela, text="Editar", image=foto_editar, compound=TOP)
btn_editar.place(x=200, y=310)
btn_editar.config(command=update)
btn_delet = Button(tela, text="Deletar", image=foto_delet, compound=TOP)
btn_delet.place(x=270, y=310)
btn_delet.config(command=delete)
btn_search = Button(tela, text="Consultar", image=foto_search, compound=TOP)
btn_search.place(x=340, y=310)
btn_search.config(command=consulta)
btn_sair = Button(tela, text="Sair", image=foto_sair, compound=RIGHT)
btn_sair.place(x=620, y=310)

# Labels
# labels da esquerda
lbl_codigo = Label(tela, text="Código:", font=("Arial", 8), foreground="black")
lbl_codigo.place(x=130, y=50)
lbl_nome = Label(tela, text="Nome:", font=("Arial", 8), foreground="black")
lbl_nome.place(x=130, y=100)
lbl_sexo = Label(tela, text="Sexo:", font=("Arial", 8), foreground="black")
lbl_sexo.place(x=130, y=150)
lbl_datanasc = Label(tela, text="Data Nascimento:", font=("Arial", 8), foreground="black")
lbl_datanasc.place(x=130, y=200)
lbl_dataatu = Label(tela, text="Data Atualização:", font=("Arial", 8), foreground="black")
lbl_dataatu.place(x=130, y=250)
lbl_desc = Label(tela, text="Descrição:", font=("Arial", 8), foreground="black")
lbl_desc.place(x=130, y=280)
# labels da direita
lbl_idade = Label(tela, text="Idade:", font=("Arial", 8), foreground="black")
lbl_idade.place(x=500, y=100)
lbl_altura = Label(tela, text="Altura:", font=("Arial", 8), foreground="black")
lbl_altura.place(x=260, y=150)
lbl_peso = Label(tela, text="Peso:", font=("Arial", 8), foreground="black")
lbl_peso.place(x=370, y=150)
lbl_cidade = Label(tela, text="Cidade:", font=("Arial", 8), foreground="black")
lbl_cidade.place(x=500, y=150)
lbl_datacad = Label(tela, text="Data Cadastro:", font=("Arial", 8), foreground="black")
lbl_datacad.place(x=320, y=200)

# campos de digitação
txt_codigo = Entry(tela, width=10, background="white")
txt_codigo.place(x=200, y=50)
txt_nome = Entry(tela, width=40, background="white")
txt_nome.place(x=200, y=100)
txt_idade = Entry(tela, width=10, background="white")
txt_idade.place(x=550, y=100)
txt_altura = Entry(tela, width=10, background="white")
txt_altura.place(x=300, y=150)
txt_peso = Entry(tela, width=10, background="white")
txt_peso.place(x=415, y=150)
txt_datanasc = Entry(tela, width=10, background="white")
txt_datanasc.place(x=220, y=200)
txt_datacad = Entry(tela, width=10, background="white")
txt_datacad.place(x=420, y=200)
txt_dataatu = Entry(tela, width=10, background="white")
txt_dataatu.place(x=220, y=250)
txt_desc = Entry(tela, width=50, background="white")
txt_desc.place(x=200, y=280)

#retorno do cadastro
lbl_retorno = Text(tela, width=80, height=5, font=("Arial", 8))
lbl_retorno.place(x=50, y=420)  # Ajuste a posição conforme necessário


tela.mainloop()
