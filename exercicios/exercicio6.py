'''6. Escreva uma função que remova todos os espaços em branco de uma string e retorne a string 
resultante.'''

def remove_espacos(frase):
    return frase.replace(' ', '')

frase = input('Frase: ')
print(remove_espacos(frase))
