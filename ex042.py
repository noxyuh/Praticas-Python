lado1 = float(input('Digite o valor de um lado: '))
lado2 = float(input('Digite o valor de um lado: '))
lado3 = float(input('Digite o valor de um lado: '))
if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    print('Triangulo Equilatero')
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print('Triangulo Isoceles')
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print('Triangulo Escaleno')
  