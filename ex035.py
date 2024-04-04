a = float(input('Digite o valor de um lado: '))
b = float(input('Digite o valor de um lado: '))
c = float(input('Digite o valor de um lado: '))
if a < b + c and b < a + c and c < a + b :
    print('É um triangulo')
else:
    print('Nao é um triangulo')