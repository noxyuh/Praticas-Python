import random
import time
from operator import itemgetter # faz parte do comando importante
jogo = {}
jogo['jogador1'] = random.randint(1,6)
jogo['jogador2']  = random.randint(1,6)
jogo['jogador3'] = random.randint(1,6)
jogo['jogador4'] = random.randint(1,6)
print('Valores sorteados:')
for jogador, valor in jogo.items():
    print(f'{jogador} tirou {valor} no dado')
    time.sleep(1)
ranking = []
print('-='*20)
print('== RANKING DOS JOGADORES ==')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # comando importante
for i, item in enumerate(ranking):
    print(f'{i+1}º lugar: {item[0]} com {item[1]}')
    time.sleep(1)