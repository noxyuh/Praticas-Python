import random
maquina = random.randint(0,10)
print('=-'*10)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*10)
cont = 0
while True:
    valor = int(input('Diga um valor: '))
    escolha = str(input('Par ou Impar? [P/I] ')).upper()
    if escolha == 'P':
        resultado = valor + maquina
        if resultado % 2 == 0:
            print('Parabens voce ganhou!')
            cont += 1
        else:
            print('Voce perdeu!')
            break
    elif escolha == 'I':
        resultado  = valor + maquina
        if resultado % 2 == 1:
            print('Parabens voce ganhou!')
            cont += 1
        else:
            print('Voce perdeu!')
            break
print(f'Parabens voce ganhou {cont} vezes')       
