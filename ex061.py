primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite o valor da razao: '))

cont = 0
while cont < 10:
    termo = primeiro_termo + cont * razao
    cont += 1
    print(f'Termo {cont}: {termo}')