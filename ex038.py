num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))

if num1 > num2:
    print('O numero maior é', num1)
elif num2 > num1:
    print('O numero maior é', num2)
elif num1 == num2:
    print('Nao existe valor maior, os dois sao iguais.')