futebol = {}
futebol['Jogador'] = str(input('Nome do Jogador: '))

partida = int(input(f'Quantas partidas {futebol['Jogador']} jogou? '))
futebol['Partida'] = []
soma = 0

for i in range(partida):
    gols = int(input(f'Quantos gols na partida {i}? '))
    soma += gols
    
    futebol['Partida'].append(gols)
    
futebol['Total'] = soma
print('-='*20)
print(futebol.items())
print('-='*20)
for k, v in futebol.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)
print(f'O jogador {futebol['Jogador']} jogou {futebol['Total']} partidas')
for i, gols in enumerate(futebol["Partida"]):
    print(f'Na partida {i}, fez {gols} gols.')