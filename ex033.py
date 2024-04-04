num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))

if num1 > num2 and num1 > num3:
    print('O maior numero é', num1)
elif num2 > num1 and num2 > num3:
    print('O maior numero é', num2)
elif num3 > num1 and num3 > num2:
    print('O maior numero é', num3)
if num1 < num2 and num1 < num3:
    print('O menor numero é', num1)
elif num2 < num1 and num2 < num3:
    print('O maior numero é', num2)
elif num3 < num1 and num3 < num2:
    print('O maior numero é', num3)