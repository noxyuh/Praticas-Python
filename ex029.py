velocidade = float(input('Qual é a velociade atual do carro: '))
a = velocidade - 80
multa = a * 7
if velocidade <= 80:
    print('Tenha um bom dia! Diriga com segurança!')
else:
    print(f'Voce foi multado em R${multa}')



