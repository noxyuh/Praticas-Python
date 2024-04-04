
valor_produto = float(input('Qual o valor do produto? '))
opcoes = int(input('Digite uma das opçoes, 1- para dinheiro/cheque, 2- á vista no cartao, 3- em ate 2x no cartao, 4- em 3x ou mais no cartao:'))

if opcoes == 1:
    desconto = valor_produto * 0.10
    valor = valor_produto - desconto
    print('O valor do produto a vista em dinheiro ou chegue vai ficar em', valor)
elif opcoes == 2:
    desconto2 = valor_produto * 0.05
    valor2 = valor_produto - desconto2
    print('O valor do produto no cartao a vista vai ficar em', valor2)
elif opcoes == 3:
    valor3 = valor_produto / 2
    print('O valor do produto parcelado em 2x vai ficar em', valor3)
elif opcoes == 4:
    juros = valor_produto * 0.20
    valor4 = (juros + valor_produto) /3
    print('O valor do produto parcelado em 3x vai ficar em', valor4)
    

