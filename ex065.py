
soma = 0
contador = 0
n = 0
maior = 0
menor = 1
cont = 'S'
while cont == 'S':
    n = int(input('Digite um numero: '))
    soma += n
    contador += 1
    
    if contador == 1:
        maior = menor = n
    else: 
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont = str(input('Deseja continuar? [S/N] ')).upper()
media = soma / contador
print(f'A média dos números digitados é {media}')
print(f'O maior número digitado foi {maior} ')
print(f'O menor número digitado foi {menor}')
    