num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite mais um numero: '))
num4 = int(input('Digite o ultimo numero: '))
tupla = (num1, num2, num3, num4)
print('O numero 9 apareceu', tupla.count(9))
print(tupla.index(3)+1)
for num in tupla:
    if num % 2 == 0:
        print(f'O número {num} é par.')
