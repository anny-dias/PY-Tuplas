'''7. Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
a) o maior número da lista
b) o menor número da lista
c) a média dos números contidos na lista'''

def preenche_lista():
    lista = []
    for i in range(10):
        numero = int(input('Numero: '))
        lista.append(numero)
    print(lista)

    maior = max(lista)
    menor = min(lista)
    media = sum(lista) / len(lista)

    return maior, menor, media      #retorna uma tupla

resultado = preenche_lista()
print(f'Maior: {resultado[0]}')
print(f'Menor: {resultado[1]}')
print(f'Média: {resultado[2]}')


    