from tkinter import *

janela = Tk()

janela.title("Calculadora de Metas")

nome = input("Digite o nome do vendedor: ")
print (f"Seja bem vindo {nome}!")

Meta = float(input("Digite o valor da meta que deseja atingir esse mês: "))


Dias = int (input ("Digite total de dias que irá trabalhar esse mês: "))

cal = Meta/Dias
print (f"A meta diaria que você deve atingir para conquistar a meta mensal é de {cal}")

janela.mainloop()