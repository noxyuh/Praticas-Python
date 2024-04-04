numeros = []
pares = []
impares = []
while True:
    num = int(input('Digite um valor: '))
    numeros.append(num)
    if num %2 == 0:
        pares.append(num)
    else:
        impares.append(num)
        
    continuar = str(input('Quer continuar [S/N]? ')).upper()
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
    else:
        print('Opcao invalida!')

print(f'A lista completa é {numeros}')   
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')