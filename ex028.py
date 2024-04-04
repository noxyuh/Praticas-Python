import random
from time import sleep
x = random.randint(0,5)
print(x)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-==-=-')
print('Vou pensar em um numero entre 0 a 5. Tente adivinhar...')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=')
num = int(input('Em que numero eu pensei? '))
print('Processando...')
sleep(3)
if num == x:
    print('Parabens! Voce conseguiu me vencer')
else:
    print(f'Ganhei! Eu pensei no numero {x} e nao no {num}')
    
    