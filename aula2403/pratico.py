from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from PIL import Image, ImageTk
tela = Tk()

tela.title("Radio Buttons")

# cor da tela
tela.configure(background='grey')
# tamanho da tela
tela.geometry("800x600")

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

def cadastrar():
    dados = (
        f"Código: {txt_codigo.get()}\n"
        f"Nome: {txt_nome.get()}\n"
        f"Idade: {txt_idade.get()}\n"
        f"Altura: {txt_altura.get()}\n"
        f"Peso: {txt_peso.get()}\n"
        f"Sexo: {var.get()}\n"
        f"Cidade: {combo.get()}\n"
        f"Data Nasc.: {txt_datanasc.get()}\n"
        f"Data Cad.: {txt_datacad.get()}\n"
        f"Data Atualiz.: {txt_dataatu.get()}\n"
        f"Descrição: {txt_desc.get()}"
    )
    lbl_retorno.config(text=dados)


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
btn_salvar.config(command=cadastrar)
btn_editar = Button(tela, text="Editar", image=foto_editar, compound=TOP)
btn_editar.place(x=200, y=310)
btn_delet = Button(tela, text="Deletar", image=foto_delet, compound=TOP)
btn_delet.place(x=270, y=310)
btn_search = Button(tela, text="Consultar", image=foto_search, compound=TOP)
btn_search.place(x=340, y=310)
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
lbl_altura.place(x=270, y=150)
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
lbl_retorno = Label(tela, text="", font=("Arial", 8), background="white")
lbl_retorno.place(x=50, y=420)

tela.mainloop()
