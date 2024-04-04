valor_da_casa = float(input('Digite o valor da casa que voce deseja comprar: '))
salario = float(input('Digite o valor do seu salario: '))
quantos_anos = int(input('Em quantos anos voce quer pagar a casa? '))
a = (quantos_anos *12)
prestacao_mensal = valor_da_casa / a

if prestacao_mensal > salario *0.30:
    print('Emprestimo negado!')
elif prestacao_mensal < salario *0.30:
    print('Emprestimo feito com sucesso!')
    print(f'As parcelas vao ser de {prestacao_mensal} por {a} mes')

                            



