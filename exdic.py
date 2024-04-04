'''
1- Com base em seu conhecimento define os dicionários. Crie um algoritmo que
solicite ao usuário informar os dados do registro e imprima os mesmos na tela:
a) conta de banco; b) livro; c) aluno; d) casa;
e) pessoa; e) animal f) veículo g) professor

lista = []

while True:
    dicionario = {}
    dicionario['conta de banco'] = int(input('Digite sua conta do banco: '))
    dicionario['livro'] = str(input('Digite um nome de livro: '))
    dicionario['aluno'] = str(input('Digite o nome do aluno: '))
    dicionario['casa'] = str(input('Digite o endereço da sua casa: '))
    dicionario['pessoa'] = str(input('Digite o nome de uma pessoa: '))
    dicionario['animal'] = str(input('Digite o nome de um animal: '))
    dicionario['veiculo'] = str(input('Digite o nome de um veiculo: '))
    dicionario['professor'] = str(input('Digite o nome de um professor: '))
    lista.append(dicionario)
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper()
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break
for dicionario in lista:
    for k, v in dicionario.items():
        print(f'Em {k} temos {v}') 

'''

'''
2 – Altere a questão anterior para solicitar do usuário 10 cadastros para cada
dicionário criado, ou seja, um lista para cada lista . Depois de listar todos eles e no
final solicitar do usuário um nome para pesquisar se existe ou não dentro de cada
dicionário na lista. ATENÇÃO: Esse exercício é um exercício de fixação, você não
poderá copiar e colar, tente fazer todas as dicionários para cada lista criada da letra
a até a letra g.

lista = []
cont = 0
while cont < 2:

    dicionario = {}
    dicionario['key'] = str(input('Digite seu nome: '))
    dicionario['conta de banco'] = int(input('Digite sua conta do banco: '))
    dicionario['livro'] = str(input('Digite um nome de livro: '))
    dicionario['aluno'] = str(input('Digite o nome do aluno: '))
    dicionario['casa'] = str(input('Digite o endereço da sua casa: '))
    dicionario['pessoa'] = str(input('Digite o nome de uma pessoa: '))
    dicionario['animal'] = str(input('Digite o nome de um animal: '))
    dicionario['veiculo'] = str(input('Digite o nome de um veiculo: '))
    dicionario['professor'] = str(input('Digite o nome de um professor: '))
    lista.append(dicionario)
    cont += 1
    
    
for dicionario in lista:
    for k, v in dicionario.items():
        if k == 'key': # quebra a linha a cada nova key
            print()
        print(f'{k}: {v}')
        
pesquisa_nome = str(input('Pesquise um nome: '))
existe = False
for dicionario in lista:
    if pesquisa_nome in dicionario.values():
        existe = True
        break
if existe:
    print('Existe!')
else:
    print('Nao existe!')
print('<< ENCERRADO >>')
'''
'''
3 - Escreva um programa para cadastrar dois clientes de uma loja. As informações
necessárias são: nome, endereço e telefone. Deve ser usada uma estrutura de
registro para a construção deste cadastro.

dados1 = []

for i in range(2):
    dados = {}
    dados['nome'] = str(input('Digite seu nome: '))
    dados['endereco'] = str(input('Digite seu endereço: '))
    dados['telefone'] = int(input('Digite o numero do seu telefone: '))
    dados1.append(dados)
print(dados1)  
'''
'''
4 – Altere o programa anterior para suportar até 50 clientes. Ao final do cadastro de
cada cliente deverá ser perguntado: "Novo Cliente (S/N)?". Deve-se utilizar um
listado tipo declarado como um registro para a solução deste programa.

dados1 = []

for i in range(50):
    dados = {}
    dados['nome'] = str(input('Digite seu nome: '))
    dados['endereco'] = str(input('Digite seu endereço: '))
    dados['telefone'] = int(input('Digite o numero do seu telefone: '))
    dados1.append(dados)
    continuacao = str(input('Deseja continuar? [S/N] ')).upper()
    if continuacao == 'S':
        continue
    elif continuacao == 'N':
        break
    else:
        print('Erro! Digite novamente.')
print(dados1)  
'''
'''
5- Fazer um programa que tenha um registro com os campos nome, endereco,
telefone, email, salário, leia os dados de entrada e processe o total dos salários e
imprima o valor do maior salário, e a quem pertence (nome). Faça isso usando uma
lista de 50 posições.

'''
dados1 = []

maior_salario = 0

for i in range(50):
    dados = {}
    dados['nome'] = str(input('Digite seu nome: '))
    dados['endereco'] = str(input('Digite seu endereço: '))
    dados['telefone'] = int(input('Digite o numero do seu telefone: '))
    dados['email'] = str(input('Digite seu email: '))
    dados['salario'] = float(input('Digite seu salario: '))
    dados1.append(dados)
    continuacao = str(input('Deseja continuar? [S/N] ')).upper()
    if continuacao == 'S':
        continue
    elif continuacao == 'N':
        break
    else:
        print('Erro! Digite novamente.')
        
total_salarios = sum(funcionario['salario'] for funcionario in dados1)

salarios = [funcionario['salario'] for funcionario in dados1]
 
maior_salario = max(salarios)



pessoa = [i['nome'] for i in dados1 if i['salario'] == maior_salario]



print(f'A pessoa {pessoa} tem o maior salario em {maior_salario}')
