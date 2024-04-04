km = float(input('Digite o km rodado pelo carro alugado: '))
dia = int(input('Digite o numero de dias do carro alugado: '))
valordia = dia * 60
valorkm = km * 0.15
valortotal = valordia + valorkm
print('O valor total a pagar pelo aluguel do carro vai ser R$', valortotal)