from datetime import datetime
dados = {}
dados['Nome'] = str(input('Nome: '))
dados['AnoNascimento'] = int(input('Ano de nascimento: '))
dados['CarteiraDeTrabalho'] = int(input('Carteira de Trabalho(0 nao tem): '))


if dados['CarteiraDeTrabalho'] > 0:
    dados['AnoContratacao'] = int(input('Ano de Contrataçao: '))
    dados['Salario'] = int(input('Salario: R$'))
    dados['idade'] = datetime.now().year - dados['AnoNascimento'] 
    dados['Aposentadoria'] =  dados['AnoContratacao'] + 35 - datetime.now().year # pega o ano atual do computador
    print('-='*20)
    print(f'- nome tem o valor {dados["Nome"]}')
    print(f'- idade tem o valor {dados["idade"]}')
    print(f'- ctps tem o valor {dados["CarteiraDeTrabalho"]}')
    print(f'- contrataçao tem o valor {dados["AnoContratacao"]}')
    print(f'- salario tem o valor {dados["Salario"]}')
    print(f'- aposentadoria tem o valor {dados["Aposentadoria"]}')
else:
    print('-='*20)
    print(f'- nome tem o valor {dados["Nome"]}')
    print(f'- idade tem o valor {dados["AnoNascimento"]}')
    print(f'- ctps tem o valor {dados["CarteiraDeTrabalho"]}')
    
