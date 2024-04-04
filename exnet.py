'''
1-
for i in range(0,3):
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite outro numero: '))
    sub = num1 - num2
    print(f'{num1} - {num2} = {sub}')
    
num = int(input('Digite um numero: '))
print('Numeros impares de', num)
for i in range(1,num+1, 2):
    print(i, end=' ') #a funçao end deixa de lado os numeros
'''
'''
jogo = ["pedra","papel","tesoura"]
for item in jogo:
    print(item, end=' ')
'''
'''
cont = 1
soma = 0
while cont < 100:
    soma += cont
    cont += 1
print(soma)
'''
'''
cont = 'S'
while cont == 'S':
    palavra = str(input('Digite uma palavras: ')).upper()
    cont = str(input('Quer continuar? {S/N} ')).upper()
    
cont = 'S'
while cont == 'S':
    idade = int(input('Digite a idade do pessoal na fila: '))
    cont = str(input('Tem mais pessoas na fila? [S/N] ')).upper()

print('Fim')       
'''
'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:   
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
            
print(f'Voce digitou tantos {par} numeros pares e {impar} numeros impares')
'''


 
 
    
    