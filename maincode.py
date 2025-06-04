import requests
from tkinter import *
from tkinter import messagebox

def decimal_para_binario():
    try:
        numero_decimal = int(entrada.get())
        resultado = bin(numero_decimal)[2:]
        saida.delete(0, END)
        saida.insert(0, resultado)
    except ValueError:
        messagebox.showerror("Erro", "Insira um número decimal válido.")

def binario_para_decimal():
    try:
        numero_binario = entrada.get()
        if not set(numero_binario).issubset({'0', '1'}):
            raise ValueError
        resultado = int(numero_binario, 2)
        saida.delete(0, END)
        saida.insert(0, str(resultado))
    except ValueError:
        messagebox.showerror("Erro", "Insira apenas os números '0' e '1'")

def limpar():
    entrada.delete(0, END)
    saida.delete(0, END)

janela = Tk()
janela.title("Conversor Decimal para Binário")
janela.geometry("500x300")

texto = Label(janela, text="Insira o número", font=("Arial", 14)).pack(pady=5)
entrada = Entry(janela, font=("Arial", 14), justify="center")
entrada.pack(pady=5)

botao_bin_para_dec = Button(janela, text="Binário para decimal", command=binario_para_decimal, width=20 ,font=("Arial", 12)).pack(pady=5)
botao_dec_para_bin = Button(janela, text="Decimal para binário", command=decimal_para_binario, width=20, font=("Arial", 12)).pack(pady=5)

resultado = Label(janela, text="Resultado: ", font=("Arial", 14)).pack(pady=5)
saida = Entry(janela, font=("Arial", 14), justify="center")
saida.pack(pady=5)

botao_limpar = Button(janela, text="Limpar", command=limpar, width=20, font=("Arial", 12)).pack(pady=5)

janela.mainloop()
