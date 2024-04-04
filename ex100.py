import random
numeros = []
def sorteio(sort):
    for i in range(5):
        s = random.randint(1,10)
        numeros.append(s)
    print('Sorteando 5 valores da lista: ', end='')
    for valor in numeros:
         print(f'{valor} ', end='')
    print('Pronto!')
sorteio(numeros)

def somar():
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'Somandos os valores pares de {numeros}, temos {soma}')        
somar()

