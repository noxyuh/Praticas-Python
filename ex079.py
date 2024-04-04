valores = []
while True:
    numero = int(input('Digite um numero: '))
    if numero not in valores:
        valores.append(numero)
    else:
        print('Numero ja existe na lista!')
    continuar = str(input('Deseja continuar[S/N]? ')).upper()
    
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
    else:
        print('Opçao invalida!')

valores.sort()
print(valores)
