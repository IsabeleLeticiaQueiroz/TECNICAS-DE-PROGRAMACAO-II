from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from PIL import Image, ImageTk
tela = Tk()

tela.title("Radio Buttons")

# cor da tela
tela.configure(background='white')
# tamanho da tela
tela.geometry("700x600")

# definindo checkbox ja assinalada de aconrdo com seu valor
# definindo que o crtiterio do valor pro checkbox ser assinalado é string e valor "m"
var = StringVar()
var.set("m")

# CHECKBOXES
radio_buttonm = Radiobutton(tela,text="M", variable=var, value="m")
radio_buttonm.place(x=120, y=40)
radio_buttonf = Radiobutton(tela, text="F", variable=var, value="f")
radio_buttonf.place(x=160, y=40)
# combobox
combo = Combobox(tela)
combo['values']=("Iguape", "Ilha Comprida", "Registro", "Juquia", "Miracatu", "Cajati")
combo.current(1)
combo.place(x=400, y=40)
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
btn_editar = Button(tela, text="Editar", image=foto_editar, compound=TOP)
btn_editar.place(x=200, y=310)
btn_delet = Button(tela, text="Deletar", image=foto_delet, compound=TOP)
btn_delet.place(x=270, y=310)
btn_search = Button(tela, text="Consultar", image=foto_search, compound=TOP)
btn_search.place(x=340, y=310)
btn_sair = Button(tela, text="Sair", image=foto_sair, compound=RIGHT)
btn_sair.place(x=620, y=310)

# LABELS
lbl_codigo = Label(tela, text="Código:", font="Arial 20 bold", fg="black")
lbl_codigo.place(x=50, y=50)
tela.mainloop()
