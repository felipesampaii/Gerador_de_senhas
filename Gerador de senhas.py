from random import *
from tkinter import *
import pyperclip

def senha():
    cMax = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cMin = 'abcdefghijklmnopqrstuvwxyz'
    num = '0123456789'
    cEsp = '!@#$%&'

    composicao = cMax + cMin + num + cEsp

    caracteres = quantide_caractere()

    senha = ''.join(sample(composicao, caracteres))

    texto = f'''{senha}'''
    texto_senha["text"] = texto



def quantide_caractere():
    caracteres_inseridos = caracteres.get()
    return int(caracteres_inseridos) if caracteres_inseridos.isdigit() else 15

def copair_senha():
    senha_copiada = texto_senha["text"]
    if senha_copiada:
        pyperclip.copy(senha_copiada)
        mensagem_copiada["text"] = "Copiado!"
        janela.after(1000, limpar_mensagem)

def limpar_mensagem():
    mensagem_copiada["text"] = ""

janela = Tk()
janela.title("Gerador de senhas")
janela.geometry("750x350+300+153")


fundo = PhotoImage(file="imagem\\layout.png")
gerar = PhotoImage(file="imagem\\Gerar.png")
encerrar = PhotoImage(file="imagem\\encerrar.png")
copiar = PhotoImage(file="imagem\\copiar.png")

lab_fundo = Label(janela, image=fundo)
lab_fundo.pack()

caracteres = Entry(janela, bd=2, font=("Calibri", 15), justify=CENTER)
caracteres.place(width=61, height=33, x=417, y=125)

texto_senha = Label(janela, bd=2, text="", font=("Calibri", 15), justify=CENTER)
texto_senha.place(width=376, height=41, x=170, y=163)

botao_gerar = Button(janela, bd=0, image=gerar, command=senha)
botao_gerar.place(width=98, height=41, x=224, y=221)

botao_copiar = Button(janela, bd=0, image=copiar, command=copair_senha)
botao_copiar.place(width=105, height=41, x=371, y=221)

botao_encerrar = Button(janela, bd=0, image=encerrar, command=janela.destroy)
botao_encerrar.place(width=151, height=40, x=273, y=275)

mensagem_copiada = Label(janela, bd=0, text="", font=("Calibri", 15), fg="green")
mensagem_copiada.place(width=95, height=33, x=224, y=125)

janela.mainloop()

