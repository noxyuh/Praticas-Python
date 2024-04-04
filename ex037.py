num = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases:')
base = int(input('-1 para binario, -2 para octal, -3 para hexadecimal: '))

if base == 1:
    b = bin(num)
    print(f'O numero {num} em binario é {b}')
elif base == 2:
    o = oct(num)
    print(f'O numero {num} em octal é {o}')
elif base == 3:
    h = hex(num)    
    print(f'O numero {num} em hexadecimal é {h}')

