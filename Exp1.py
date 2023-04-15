#exemplo de sequencia de caracteres

texto = "Aprendendo Python na disciplina de linguagem de programação."
#a operação len() permite saber o tamahno da sequência.
print(f"Tamanho do texto = {len(texto)}")

#o operador IN permite saber se um determinado valor esta ou não na sequência retornando true ou false
print(f"Python in texto = {'Python' in texto}")

#o operador count permite contar a quantidade de uma ocorrencia de um valor.
print(f"Quantidade de y no texto = {texto.count('y')}")

#a anotação com colchetes permite fatiar a sequencia exibindo somente parte dela. Pedimos para exibir da posição 0 até 5, pois o valor 6 não é incluido.
print(f"As 5 primeiras letras são: {texto [0:6]}")
