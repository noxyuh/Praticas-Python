tupla = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO',
         'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

print('-='*30)
print('Os 5 primeiros sao ', tupla[0:5])
print('-='*30)
print('Os 4 ultimos sao ', tupla[-4:])
print('-='*30)
print('Times em ordem alfabetica', sorted(tupla))
print('-='*30)
print('Chapecoense esta na posiçao', tupla.index('Chapecoense')+1 ,'posiçao' )
