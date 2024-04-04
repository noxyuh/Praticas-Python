# Inicializando uma matriz vazia
matriz = [[], [], []]
soma = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = None

# Preenchendo a matriz com valores do usuário
for l in range(3):
    for c in range(3):
        numero = int(input('Digite um valor para a posição [' + str(l) + '][' + str(c) + ']: '))
        matriz[l].append(numero)
        if numero % 2 == 0:
            soma+=numero
        if c == 2:  # terceira coluna
            soma_terceira_coluna += numero
        if l == 1:  # segunda linha
            if maior_valor_segunda_linha is None or numero > maior_valor_segunda_linha:
                maior_valor_segunda_linha = numero

# Imprimindo a matriz
for l in range(3):
    for c in range(3):
        print(matriz[l][c], end = ' ')
    print()

print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_valor_segunda_linha}')

