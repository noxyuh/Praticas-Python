numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    
    
    continuar = str(input('Quer continuar [S/N]? ')).upper()
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
    else:
        print('Opcao invalida!')
if 5 in numeros:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
    
print(f'Voce digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print('Os valores em ordem decrescente são ', numeros)
        
    