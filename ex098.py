
def contador(i, f , p):
    for l in range(i, f , p):
        print(l)

print('Contagem de 1 ate 10 de 1 em 1')
for i in range(1, 11, 1):
    print(i, end=' ')
print()
print('Contagem de 10 ate 0 de 2 em 2')
for j in range(10, -1, -2):
    print(j, end=' ',)
print()
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))  
contador(inicio, fim, passo)   

