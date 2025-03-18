from tkinter import *
tela = Tk()

tela.title("Calculo Soma")
tela.configure(background="blue")
tela.geometry("800x600")

#labels 
lbl_titulo = Label(tela, text="Calculo de Soma", font="Arial 20 bold", bg="blue", fg="white")
lbl_titulo.place(x=250, y=10)

lbl_num1 = Label(tela, text="Digite o primeiro numero: ", font="Arial 12 bold", bg="blue", fg="white")
lbl_num1.place(x=10, y=50)

lbl_num2 = Label(tela, text="Digite o segundo numero: ", font="Arial 12 bold", bg="blue", fg="white")
lbl_num2.place(x=10, y=80)

lbl_resultado = Label(tela, text="Resultado: ", font="Arial 12 bold", bg="blue", fg="white")
lbl_resultado.place(x=10, y=120)

# txt areas
txt_num1 = Entry(tela, width=50, fg="black", bg="white")
txt_num1.place(x=300, y=50)
txt_num1.insert(0, "numero")

txt_num2 = Entry(tela, width=50, fg="black", bg="white")
txt_num2.place(x=300, y=80)
txt_num2.insert(0, "numero")

# acao do botao
def clicar():
    lbl_resultado = Label(tela, text=""+ str(int(txt_num1.get()) + int(txt_num2.get())), font="Arial 12", bg="blue", fg="white")
    lbl_resultado.place(x=100, y=120)

# acao de sumir as palavras
def sumir(event):
    if txt_num1.get() == "numero":
        txt_num1.delete(0, END)
    if txt_num2.get() == "numero":
        txt_num2.delete(0, END)
txt_num1.bind("<FocusIn>", sumir)
txt_num2.bind("<FocusIn>", sumir)

# btn
btn_botao = Button(tela, text="Calcular", command=clicar)
btn_botao.place(x=10, y=150)

tela.mainloop()