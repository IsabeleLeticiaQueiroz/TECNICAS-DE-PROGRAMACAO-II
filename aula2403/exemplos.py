from tkinter import *
tela = Tk()

tela.title("Radio Buttons")

# cor da tela
tela.configure(background='#1e3743')
# tamanho da tela
tela.geometry("700x600")

# definindo checkbox ja assinalada de aconrdo com seu valor
# definindo que o crtiterio do valor pro checkbox ser assinalado é string e valor "m"
var = StringVar()
var.set("m")

# botoes
radio_buttonm = Radiobutton(tela,text="m", variable=var, value="m")
radio_buttonm.place(x=20, y=40)
radio_buttonf = Radiobutton(tela, text="f", variable=var, value="f")
radio_buttonf.place(x=20, y=60)

tela.mainloop()
