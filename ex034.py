salario = float(input('Digite o salario: '))
aumento = salario + (salario * 15/100)
aumento2 = salario + (salario * 10/100)
if salario <= 1250:
    print('O aumento é de: R$', aumento)
else:
    print('O aumento é de R$', aumento2)


