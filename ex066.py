soma = 0
cont = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Foi digitado {cont} numeros e a soma entre eles foi de {soma}')