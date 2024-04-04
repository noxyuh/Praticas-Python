
dados = []
soma = 0
while True:
    cadastro = {}
    cadastro['Nome'] = str(input('Nome: '))
    cadastro['Genero'] = str(input('Genero: [M/F] ')).upper()
    cadastro['Idade'] = int(input('Idade: '))
    dados.append(cadastro)
    soma += 1
    soma_idades = 0
    tot_idades = 0
    for cadastro in dados:
        soma_idades += cadastro['Idade']
        tot_idades += 1
    media = soma_idades / tot_idades
    
    mulheres = 0
    nomes_mulheres = []
    for cadastro in dados:
        if cadastro['Genero'] == 'F':
            mulheres += 1
            nomes_mulheres.append(cadastro['Nome'])
     
    continuar = str(input('Quer continuar? [S/N] ')).upper()
   
    
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
    else: 
        print('ERRO! Responda apenas S ou N')
    
print(f'A) Ao todo temos {soma} pessoas cadastradas.')
print(f'B) A média de idade é de {media}')
print(f'C) As mulheres cadastradas foram {nomes_mulheres}')
print('D) Lista das pessoas que estao acima da media:')
for cadastro in dados:
    if cadastro['Idade'] > media:
        print(cadastro['Nome'], end=' ')
print()
print('<< ENCERRADO >>')