import random
from time import sleep
x = random.randint(0,10)
print(x)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-')
print('Vou pensar em um numero entre 0 a 10. Tente adivinhar...')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=')
cont = 0
comparar = x
palpite = 0
while cont < comparar:
    num = int(input('Em que numero eu pensei? '))
    palpite += 1
    print('Processando...')
    sleep(3)
    if num == x:
        print('Parabens! Voce conseguiu me vencer')
        print(f'Voce acertou com {palpite} tentativas.')
    else:
        print(f'Ganhei! Eu pensei no numero {x} e nao no {num}')