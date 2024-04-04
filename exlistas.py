'''
1 - Escreva um programa que solicite ao usuário que insira 5 números inteiros e,
em seguida, calcule e exiba a soma desses números.

soma = 0
for i in range(5):
    num = int(input('Insira um numero: '))
    soma += num
print('A soma dos numeros foi',soma)
'''
'''
2 - Crie um algoritmo que receba 7 valores e que imprima-os na tela na ordem
contrária a qual foi recebida.

lista = []
for i in range(7):
    lista.append(int(input('Insira um numero: ')))
lista.sort(reverse=True)
print(lista)

'''
'''
3 - Crie um algoritmo que receba 12 valores reais, sendo os 6 primeiros
designados a uma lista P e os 6 últimos a uma lista I Após isso, crie uma terceira
lista S que recebe S[i] = P[i] − I[i].

P = []
I = []
S = []
for i in range(6):
    P.append(int(input('Digite um valor: ')))
for i in range(6):
    I.append(int(input('Digite um valor: ')))
for i in range(6):
    S.append(P[i] - I[i])

print('Lista S:', S)
'''

'''
4 - Crie um algoritmo que receba 12 valores reais, sendo os 6 primeiros
designados a uma lista X e os 6 últimos a uma lista Y. Após isso, crie uma terceira
lista M que recebe M[i] = X[i] × Y [i].

P = []
I = []
S = []
for i in range(6):
    P.append(int(input('Digite um valor: ')))
for i in range(6):
    I.append(int(input('Digite um valor: ')))
for i in range(6):
    S.append(P[i] * I[i])

print('Lista S:', S)
'''   
'''
5 - Crie um algoritmo que receba 12 valores reais, sendo os 6 primeiros
designados a uma lista X e os 6 últimos a uma lista Y. Após isso, crie uma terceira
lista D que recebe D[i] = 

X = []
Y = []
D = []
for i in range(6):
    X.append(int(input('Digite um valor: ')))
for i in range(6):
    Y.append(int(input('Digite um valor: ')))
for i in range(6):
    D.append(X[i] / Y[i])

print('Lista M:', D)
'''
'''
6 - Faça um Programa que peça as duas notas de 10 alunos, calcule e armazene
numa lista a média de cada aluno, imprima o número de alunos com média maior
ou igual a 70.

medias = []
for i in range(3):
    nota1 = int(input('Digite a 1 nota: '))
    nota2 = int(input('Digite a 2 nota: '))
    media = (nota1 + nota2) / 2
    medias.append(media)
alunos_acima_70 = 0
for media in medias:
    if media >= 7:
        alunos_acima_70 += 1

print('Número de alunos com média maior ou igual a 7:', alunos_acima_70)
'''
'''
7 - Faça um Programa que leia uma lista A com 10 números inteiros, calcule e
mostre a soma dos quadrados dos elementos da lista.

soma = 0
A = {2, 2, 1, 1, 1, 1, 1, 1, 2, 1}
for p in A:
    soma += p **2
print(soma)
'''
'''
8 - Foram anotadas as idades e alturas de 10 alunos. Faça um Programa que
determine quantos alunos com mais de 13 anos possuem altura inferior à média
de altura desses alunos.

alunos = []
soma_alturas = 0
cont = 1
for i in range(5):
    dados = []
    dados.append(int(input('Idade: ')))
    dados.append(float(input('Altura: ')))
    alunos.append(dados[:])
    soma_alturas += dados[1]
media = soma_alturas / 5
for aluno in alunos:
    if aluno[0] > 13 and aluno[1] < media:
        cont += 1
print(cont)
'''
'''
10 - Faça um algoritmo que receba uma lista qualquer, após isso, receba x e y
posições da lista e realize a troca dos valores dessa lista.

lista_qualquer= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

trocar = int(input("numero que vai trocar: "))
valor = int(input("numero novo: "))
lista_qualquer[trocar] = valor
print(lista_qualquer)
'''
'''
11 - Faça um algoritmo que receba 2 listas s e n, e compare quantos elementos
iguais há entre elas.

s = [1,2,3,4,5,6,7,8]
n = [2,4,6,7,9]
cont = 0
for i in s:
    for j in n:
        if i == j:
            cont+=1

print(cont)
'''
'''
15 – Faça um programa que receba a temperatura média de cada mês do ano e
armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e
mostre todas as temperaturas acima da média anual, e em que mês elas
ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . .

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

temperaturas_mes = []
soma_temp = 0
for i in range(12):
    temp = int(input(f'Digite a temperatura do mês de {meses[i]}: ')) 
    temperaturas_mes.append(temp)
    soma_temp += temp
media = soma_temp / 12
for i, temp in enumerate(temperaturas_mes):
    if temp > media:
        print(f'A temperatura no mês de {meses[i]} foi {temp}, que é acima da média anual.')
'''
'''
18 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa
sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da
pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve
ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
"Assassino". Caso contrário, ele será classificado como "Inocente".

lista = []
cont = 0
a = input('Telefonou para a vítima? ').upper()
b = input('Esteve no local do crime? ').upper()
c = input('Mora perto da vítima? ').upper()
d = input('Devia para a vítima? ').upper()
e = input('Já trabalhou com a vítima? ').upper()
lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)
lista.append(e)
for p in lista:
    if p == 'SIM':
        cont+=1
if cont == 2:
    print('Suspeita')
elif cont == 3 or cont == 4:
    print('Cumplise')
elif cont == 5:
    print('Assassino')
else:
    print('Inocente')
'''
animais = [['Cachorro', 100], ['Gato',100], ['Papagaio',150] , ['Periquito australiano',175], 
           ['Iguana',200], ['Peixe beta', 50]]
compra = ' '
print('-='*20)
print('Bem vindo a Loja de animais')
print('Temos essa opçoes:')
print('Cachorro = R$100,00')
print('Gato = 100,00')
print('Papagaio = 150,00')
print('Periquito australiano = R$ 175,00')
print('Iguana = R$ 200,00')
print('Peixe Beta = R$ 50,00')
print('-='*20)
while compra != 'Sair':
   compra = input('Qual animal voce deseja comprar[Sair]? ').capitalize()
   if compra == 'Sair':
       break
   for animal in animais:
        if compra == animal[0]:
            print(f'Voce escolheu um {animal[0]}, no valor de R$ {animal[1]:.2f} va ao caixa pagar')
            break
   else:
       print('Animal nao encontrado!')
         
             
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            