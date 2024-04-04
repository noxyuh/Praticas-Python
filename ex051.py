primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite o valor da razao: '))

for c in range(10):
    termo = primeiro_termo + c * razao
    print(f'Termo {c + 1}: {termo}')
