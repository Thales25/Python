# O mesmo resultado do Exp5.py 

vogais = [] #lista vazia
print (f"Tipo do objeto vogais: {type(vogais)}")

#append adiciona um novo valor ao final da lista
vogais.append('a')
vogais.append('e')
vogais.append('i')
vogais.append('o')
vogais.append('u')

# a função enumerate é usada para percorrer um objeto interável retornando a posição e o valor.
for p, x in enumerate(vogais):
    print(f'Posição: {p}, valor: {x}')

