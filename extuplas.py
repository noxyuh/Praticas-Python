'''
1. Crie uma tupla com os números de 1 a 10 e imprima todos os elementos.
2. Crie uma tupla com quatro cidades do mundo. Em seguida, pergunte ao usuário para digitar o nome de uma cidade e verifique se a cidade está na sua tupla.
3. Crie uma tupla com três elementos e tente alterar o valor do segundo elemento para um novo valor. Observe o resultado e explique o que aconteceu.
4. Crie duas tuplas, cada uma com três elementos. Em seguida, crie uma terceira tupla que seja a concatenação das duas primeiras.
5. Crie uma tupla com vários números e imprima o maior e o menor número.
'''
'''
1-
numeros = (1, 2, 3, 4 , 5, 6 , 7 , 8 , 9 , 10)
for n in numeros:
    print(n)
'''
'''
2-
cidade = ('SAO PAULO', 'BARCELONA', 'TORONTO', 'TOKYO')
nome = str(input('Digite o nome de uma cidade: ')).upper()
for n in cidade:
    if n == nome:
        print(f'A cidade {nome} esta na tupla')
print('Fim do programa!')   
'''
'''
4-
t1 = ('SAO PAULO', 'BARCELONA', 'TORONTO')
t2 = ('ACRE', 'TOKYO', 'RIO DE JANEIRO')

t3 = (t1, t2)
print(t3)
'''



