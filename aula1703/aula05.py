from tkinter import *

tela = Tk()

tela.title("fatec de registro")
tela.configure(background='#aaaaaa')
tela.geometry("480x320")
tela.resizable(True, True)
tela.maxsize(width=760, height=480)
tela.minsize(width=300, height=200)

lbl_nome = Label(tela, text="Nome: ", font="Arial 18 bold").place(x=10, y=10)
lbl_telefone = Label(tela, text="Telefone: ").place(x=10, y=40)
lbl_endereco = Label(tela, text="Endereço: ").place(x=10, y=70)
lbl_cpf = Label(tela, text="CPF: ").place(x=10, y=100)

btn_botao = Button(tela, text="Clique aqui")
btn_botao.pack()

tela.mainloop()