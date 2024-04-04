import random

print('Voce deseja escolher qual das opcoes?')
escolhas = ['pedra','papel','tesoura']
computador = random.choice(escolhas)
jogador = str(input('Escolha papel, pedra e tesoura: '))

if jogador == computador:
    print('Empate!')
    print(computador)
elif (jogador == 'papel' and computador == 'pedra') or(jogador == 'papel' and computador == 'tesoura') or(jogador == 'pedra' and computador == 'tesoura') or (jogador == 'pedra' and computador == 'papel')or(jogador == 'tesoura' and computador == 'pedra')or(jogador == 'tesoura' and computador == 'papel'):
    print('Voce ganhou')
    print(computador)
