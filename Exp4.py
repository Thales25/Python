#dado um texto sobre strings em python, queremos saber quantas vezes o autor menciona as palavras string e strings no texto.

texto = """Operadores de String
Python oferece operadores para processar texto (ou seja, valores de string).
Assim como os números, as strings podem ser comparadas usando operadores de comparação:
==, !=, <, > e assim por diante.
O operador ==, por exemplo, retorna True se as strings nos dois lados do operador tiverem o mesmo valor (Perkovic, p. 23, 2016).
"""
print (f"O texto tem {len(texto)} caracteres. ")
texto = texto.lower()
texto = texto.replace (",", "").replace(".","").replace("(","").replace(")","").replace("\n"," ")


palavras = texto.split()
print (f"O texto possui {len(palavras)} palavras.")

string =  palavras.count('string')
strings = palavras.count('strings')
string = int(string)
strings = int(strings)
total = string+strings


print (f"Foi identificado a palavra STRING {string} vezes")
print (f"Foi identificado a palavra STRINGS {strings} vezes ")
print (f"Totalizando a quantidades de  {total} vezes que as palavras 'string' e 'strings' foram mencionadas.")
