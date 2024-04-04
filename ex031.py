distancia = float(input('Qual a distancia da viagem? '))
passagem = distancia *0.50
passagem2 = distancia *0.45
if distancia <= 200:
    print(f'O valor da passagem ate 200km é de R${passagem}')
else:
    print(f'O valor da passagem acima de 200km é de R${passagem2}')
