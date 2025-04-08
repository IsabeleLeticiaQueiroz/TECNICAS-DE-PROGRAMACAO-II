from tkinter import *
# esses outros imports do tkinter precisam ser importados separados pois nao vem inclusos no tkinter
from tkinter import ttk 
import tkinter as tk
#  esse import é para fazer a conexão com o banco de dados mongo
import pymongo

tela=Tk()
tela.title("Aula 07 - exemplo no MongoDB")
tela.geometry("800x600")
tela.resizable(width=True, height=True)
tela.configure(background="white")

exemplo = pymongo.MongoClient("mongodb://localhost:27017/")
db = exemplo["exemplo"]
colecao = db["clientes"]

lbl_codigo = Label(tela, text="Código:", bg="white")
lbl_codigo.place(x=130,y=140)
txt_codigo = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_codigo.place(x=190, y=140)

lbl_nome = Label(tela, text="Nome:", bg="white")
lbl_nome.place(x=130,y=170)
txt_nome = Entry(tela, width=40, borderwidth=2, fg="black", bg="white")
txt_nome.place(x=190, y=170)
txt_nome.insert(0,"")

lbl_cpf = Label(tela, text="CPF:", bg="white")
lbl_cpf.place(x=450,y=170)
txt_cpf = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_cpf.place(x=480, y=170)
txt_cpf.insert(0,"")

lbl_idade = Label(tela, text="Idade:", bg="white")
lbl_idade.place(x=130,y=200)
txt_idade = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_idade.place(x=190, y=200)
txt_idade.insert(0,"")

lbl_end = Label(tela, text="Rua:", bg="white")
lbl_end.place(x=450,y=200)
txt_end = Entry(tela, width=25, borderwidth=2, fg="black", bg="white")
txt_end.place(x=480, y=200)
txt_end.insert(0,"")

lbl_bairro = Label(tela, text="Bairro:", bg="white")
lbl_bairro.place(x=130,y=230)
txt_bairro = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_bairro.place(x=190, y=230)
txt_bairro.insert(0,"")

lbl_estado = Label(tela, text="Estado:", bg="white")
lbl_estado.place(x=330,y=230)
combo_estado = ttk.Combobox(tela, values=[
    "SP", "RJ", "MG", "BA", "PR", 
    "RS", "SC", "PA", "PB", 
    "PE", "PI", "RN", "RO", "AC"
    "RR", "AM", "GO", "ES", "MA",
    "MT", "MS", "AL", "CE", "SE",
    "TO", "AP"
    ],)
combo_estado.place(x=370, y=230)
# combo_estado.grid(column=0, row=1)

lbl_cidade = Label(tela, text="Cidade:", bg="white")
lbl_cidade.place(x=520,y=230)
txt_cidade = Entry(tela, width=20, borderwidth=2, fg="black", bg="white")
txt_cidade.place(x=570, y=230)
txt_cidade.insert(0,"")

def salvar():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    idade = int(txt_idade.get())
    end = txt_end.get()
    cpf = txt_cpf.get()
    bairro = txt_bairro.get()
    estado = combo_estado.get()
    cidade = txt_cidade.get()
    # apaga os campos
    txt_codigo.delete(0, tk.END)
    txt_nome.delete(0, tk.END)
    txt_idade.delete(0, tk.END)
    txt_end.delete(0, tk.END)
    txt_cpf.delete(0, tk.END)
    txt_bairro.delete(0, tk.END)
    txt_cidade.delete(0, tk.END)
    combo_estado.delete(0, tk.END)
    # inserir no banco de dados
    cliente = {
        "codigo": codigo,
        "nome": nome,
        "idade": idade,
        "end": end,
        "bairro": bairro,
        "estado": estado,
        "cidade": cidade,
        "cpf": cpf
    }
    colecao.insert_one(cliente)

def atualizar():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    idade = int(txt_idade.get())
    end = txt_end.get()
    cpf = txt_cpf.get()
    bairro = txt_bairro.get()
    estado = combo_estado.get()
    cidade = txt_cidade.get()

    colecao.update_one({"codigo": codigo}, {"$set": {
        "codigo": codigo,
        "nome": nome,
        "idade": idade,
        "end": end,
        "bairro": bairro,
        "estado": estado,
        "cidade": cidade,
        "cpf": cpf
    }})

def apagar():
    codigo = txt_codigo.get()
    colecao.delete_one({"codigo": codigo})
    # apaga os campos
    txt_codigo.delete(0, tk.END)
    txt_nome.delete(0, tk.END)
    txt_idade.delete(0, tk.END)
    txt_end.delete(0, tk.END)
    txt_cpf.delete(0, tk.END)
    txt_bairro.delete(0, tk.END)
    txt_cidade.delete(0, tk.END)
    combo_estado.delete(0, tk.END)

def consultar():
    codigo = txt_codigo.get()
    resultado = colecao.find_one({"codigo": codigo})
    if resultado:
        txt_nome.insert(END,f"{resultado['nome']}\n")
        txt_idade.insert(END,f"{resultado['idade']}\n")
        txt_end.insert(END,f"{resultado['end']}\n")
        txt_cpf.insert(END,f"{resultado['cpf']}\n")
        txt_bairro.insert(END,f"{resultado['bairro']}\n")
        txt_cidade.insert(END,f"{resultado['cidade']}\n")
        combo_estado.insert(END,f"{resultado['estado']}\n")
    else:
        lbl_resultado.config(text="Código não encontrado", bg="red")

lbl_resultado = Label(tela, text="", bg="white")
lbl_resultado.place(x=490,y=310)

btn_salvar = Button(tela, text="Salvar", width=10, command=salvar)
btn_salvar.place(x=130, y=280)
btn_alterar = Button(tela, text="Alterar", width=10, command=atualizar)
btn_alterar.place(x=220, y=280)
btn_excluir = Button(tela, text="Excluir", width=10, command=apagar)
btn_excluir.place(x=310, y=280)
btn_sair = Button(tela, text="Sair", width=10, command=tela.quit)
btn_sair.place(x=400, y=280)


tela.mainloop()