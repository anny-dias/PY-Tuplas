# TUPLAS
# sequencia de itens

# Tuplas são Imutáveis (não podem ser modificadas)

# Tuplas são delimitadas por parênteses
tupla = (3, 1, 10, 5)

# Tuplas são heterogêneas (armazena diferentes tipos de dados)
tupla = (3 , 'abc', 3.5, 6.99, 'dfdf')

print(tupla[0])
print(tupla[1])

# index - retorna o indice de um determinado item
print(tupla.index(6.99))

# count - conta a quantidade de vezes que um item aparece na tupla
print(tupla.count(3))

# operador in - busca um item na tupla e retorna True e False
if 3 in tupla:
    print('Existe')
else:
    print('Não existe')

# contatenação de tuplas
tupla1 = (1, 2, 3)
tupla2 = (20, 30, 60)
tupla3 = tupla1 + tupla2 + tupla2
print(tupla3)

# contatenação de strings
a = 'paulo'
b = 'vieira'
c = a.title() + ' ' + b.title()
print(c)

def teste(a,b):
    soma = a + b
    subtracao = a - b
    return soma, subtracao

resultado = teste(30, 7)
print(resultado)
print(resultado[0])
print(resultado[1])

# tupla com um único item (tem virgula no final)
tupla = (10)    #número inteiro entre parênteses (int)
tupla = (10, )  #tupla
print(tupla)

# list - copia os itens de uma tupla para uma lista
tupla = (4, 5, 6)
lista = list(tupla)
print(lista)

# tuple - copia os itens de uma lista para uma tupla
lista = [10, 20, 30]
tupla = tuple(lista) 
print(tupla)
print(lista)

# está faltando !!! pegar no teams

# copia de lista ou de tupla
lista = [1, 2, 3]
lista2 = lista
lista2.append(100)
print(lista)
print(lista2)




