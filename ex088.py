import random 
import time


print('-'*30)
print('JOGO NA MEGA SENA')
print('-'*30)
vezes = int(input('Quantos jogos voce quer que eu sorteie? '))
print(f'-=-=- Sorteando {vezes} Jogos -=-=-')
cont = 0
for i in range(vezes):
    lista = []
    cont+=1
    for j in range(6):
        numero = random.randint(1,60)
        while numero in lista:  # Garante que o mesmo número não seja escolhido duas vezes
            numero = random.randint(1,60)
        lista.append(numero)
        
    print(f'Jogo {cont}: {lista}')
    time.sleep(1)
   