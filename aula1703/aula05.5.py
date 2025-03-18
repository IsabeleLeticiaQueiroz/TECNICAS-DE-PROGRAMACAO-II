from tkinter import *
tela = Tk()

txt_nome = Entry(tela, width=50, fg="black", bg="pink")
txt_nome.pack()
txt_nome.insert(0, "Digite seu nome:  ")

def clicar():
    lbl_nome = Label(tela, text="Bem vindo(a): " + txt_nome.get())
    lbl_nome.pack()

btn_botao = Button(tela, text="Clique aqui", command=clicar)
btn_botao.pack()

tela.mainloop()
