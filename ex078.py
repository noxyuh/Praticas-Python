numeros = []
for cont in range(0,5):
    numeros.append(int(input(f'Digite o numero na posiçao {cont}: ')))
print('=-'*30)
print('Voce digitou os valores', numeros)
print('O maior valor digitado foi', max(numeros))
print('O menor valor digitado foi', min(numeros))