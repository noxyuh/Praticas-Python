# Inicializando uma matriz vazia
matriz = [[], [], []]

# Preenchendo a matriz com valores do usuário
for i in range(3):
    for j in range(3):
        numero = int(input('Digite um valor para a posição [' + str(i) + '][' + str(j) + ']: '))
        matriz[i].append(numero)

# Imprimindo a matriz
for i in range(3):
    for j in range(3):
        print(matriz[i][j], end = ' ')
    print()

    