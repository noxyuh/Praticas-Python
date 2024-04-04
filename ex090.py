dados = {}
dados['Nome'] = str(input('Nome: '))
dados['Media'] = float(input(f'Média de {dados["Nome"]}: '))
print('-='*20)
print(f'- nome é igual a {dados["Nome"]}')
print(f'- media é igual a {dados["Media"]}')
if dados['Media'] > 7:
    print('- situaçao é igual a Aprovado')
else:
    print('- situaçao é igual a Reprovado')