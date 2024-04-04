primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite o valor da razao: '))


cont = 0
while cont < 10:
    termo = primeiro_termo + cont * razao
    cont += 1
    print(f'Termo {cont}: {termo}')
    
termo1 = int(input("Quantos termos você quer mostrar a mais? "))    
cont = 0
while cont <= 10 + termo1:
    if termo1 > 0:
        termo = primeiro_termo + (cont - 1) * razao
        print(f'Termo {cont}: {termo}')
        cont += 1
    else:
        break
