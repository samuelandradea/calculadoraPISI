import requests
from tkinter import *
from tkinter import messagebox

def adicionar_caractere(caractere):
    entrada.insert(END, caractere)

def limpar():
    entrada.delete(0, END)
    resultado.delete(0, END)

def decimal_para_binario():
    try:
        numero = int(entrada.get())
        binario = bin(numero)[2:]
        resultado.delete(0, END)
        resultado.insert(0, binario)
    except ValueError:
        messagebox.showerror("Erro", "Digite um número decimal válido.")

def binario_para_decimal():
    try:
        binario = entrada.get()
        if not set(binario).issubset({'0', '1'}):
            raise ValueError
        decimal = int(binario, 2)
        resultado.delete(0, END)
        resultado.insert(0, str(decimal))
    except ValueError:
        messagebox.showerror("Erro", "Digite um número binário válido (apenas 0 e 1).")

# Janela principal
janela = Tk()
janela.title("Calculadora Conversora")
janela.geometry("300x400")

# Campo de entrada
entrada = Entry(janela, font=("Arial", 16), justify='right')
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Campo de resultado
resultado = Entry(janela, font=("Arial", 16), justify='right')
resultado.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

# Botões numéricos
botoes = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2),
    ('0', 5, 1)
]

for (texto, linha, coluna) in botoes:
    botao_adicionar = Button(janela, text=texto, font=("Arial", 14), width=5, command=lambda t=texto: adicionar_caractere(t)).grid(row=linha, column=coluna, padx=5, pady=5)

# Botões de conversão
botao_dec_to_bin = Button(janela, text="DEC → BIN", font=("Arial", 12), width=10, command=decimal_para_binario).grid(row=5, column=0, padx=5, pady=5)
botao_bin_to_dec = Button(janela, text="BIN → DEC", font=("Arial", 12), width=10, command=binario_para_decimal).grid(row=5, column=2, padx=5, pady=5)

# Botão limpar
botao_limpar = Button(janela, text="Limpar", font=("Arial", 12), width=22, bg="lightgray", command=limpar).grid(row=6, column=0, columnspan=3, padx=5, pady=10)

janela.mainloop()