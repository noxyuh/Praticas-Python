'''
1 - Ler um número e se for maior que 20 imprimir a metade desse número.
num = int(input('Digite um numero: '))
if num > 20:
    calculo = num /2
    print(calculo)
'''
'''
2 - Ler a idade de uma pessoa e informar a sua classe eleitoral:
● Não-eleitor (abaixo de 16 anos)
● Eleitor obrigatório (entre 18 e 65 anos)
● Eleitor facultativo (entre 16 e 18 aos ou maior de 65 anos)
idade = int(input('Digite sua idade: '))
if idade < 16:
    print('Não-eleitor')
elif idade >= 18 and idade <= 65:
    print('Eleitor obrigatório')
elif idade >= 16 and idade <= 18 or idade > 65:
    print('Eleitor facultativo')
'''
'''
4- Desenvolva um algoritmo que solicite ao usuário dois números e também a operação matemática
que deseja realizar, após utilizando o comando switch execute a operação selecionada.

num1 = int(input('\033[32m Digite um numero: \033[m'))
num2 = int(input('\033[32m Digite um numero: \033[m'))
print(' \033[31m Escolha uma das opçoes: \033[m')
operacao = int(input('\033[36m 1- matematica, 2- subttraçao, 3- multiplicaçao, 4- divisao: \033[m'))
if operacao == 1:
    soma = num1 + num2
    print('A soma é', soma)
elif operacao == 2:
    sub = num1 + num2
    print('A subtraçao é', sub)
elif operacao == 3:
    mult = num1 * num2
    print('A multiplicaçao é', mult)
elif operacao == 2:
    div = num1 / num2
    print('A divisao é', div)
'''

'''
5 - Fazer um programa para imprimir o conceito de um aluno, dada a sua nota (um valor real). O critério
para os conceitos é o seguinte:
● Notas inferiores a 3 - conceito E
● Notas maiores ou iguais a 3 e inferiores a 6 - conceito D
● Notas maiores ou iguais a 6 e inferiores a 8 - conceito C
● Notas maiores ou iguais a 8 e inferiores a 9 - conceito B
● Notas maiores ou iguais a 9 - conceito A

nota = int(input('Digite a nota do aluno: '))
if nota < 3:
    print('Conceito E')
elif nota >= 3 and nota < 6:
    print('Conceito D')
elif nota >= 6 and nota < 8:
    print('Conceito C')
elif nota >= 8 and nota < 9:
    print('Conceito B')
elif nota >= 9 :
    print('Conceito A')
'''
'''
6 - Dada a idade de um jogador de futebol classifique-o em uma das seguintes categorias: (a) infantil
A=5-7 anos; (b)infantil B = 8-10 anos; (c)juvenil A = 11-13 anos; (d)juvenil B = 14-17 anos; (e)adulto =
maiores de 18 anos.

idade=int(input("Digite sua idade: "))
if 5 <= idade <= 7:
    print("(a) Infantil A")
elif 8 <= idade <= 10:
     print("(b) Infantil B")
elif 11 <= idade <= 13:
    print("(c) Juvenil A")
elif 14 <= idade <= 17:
    print("(d) Juvenil B")
elif idade >= 18:
    print("(e) Adulto")
else:
    print("Idade inválida para categorização.")
'''
'''
7 - Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da compra
for menor que R$ 20,00; caso contrário, o lucro será de 30%. Elabore um algoritmo que leia o valor do
produto e imprima o valor de venda para o produto.

valor_produto = float(input('Digite o valor do produto: '))
if valor_produto < 20:
    lucro = valor_produto * 0.45
    lucro45 = lucro + valor_produto
    print(lucro45)
else:
    lucro2 = valor_produto * 0.30
    lucro30 = lucro2 + valor_produto
    print(lucro30)
'''
'''
8 - Faça um algoritmo para ler três notas e o número de faltas de um aluno e escrever qual a sua
situação final: Aprovado, Reprovado por Falta ou Reprovado por Média. A média para aprovação é 7,0 e
o limite de faltas é 25% do total de aulas. O número de aulas ministradas no semestre foi de 80. A
reprovação por falta sobrepõe a reprovação por Média.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
faltas = int(input('Digite as faltas do aluno: '))
media = (nota1 + nota2 + nota3) /3
aulas = 80 * 0.25

if media == 7:
    print('Aprovado!')
elif media < 7:
    print('Reprovado!')
elif faltas > aulas:
    print('Reprovado por falta!')
'''
'''
temperatura = float(input('Digite a temperatura atual: '))
if temperatura <= 15:
    print('Muito frio!')
elif 16 >= temperatura < 23:
    print('Frio!')
elif 23 >= temperatura < 26:
    print('Agradavel!')
elif 27 >= temperatura < 30:
    print('Calor!')
else:
    print('Muito quente!')
    
temp= float(input("Digite a temperatura: "))

if temp <=15:
    print("MUITO FRIO!!!!")
elif temp >= 16 and temp <23:
    print("FRIO!!")
elif temp >=23 and temp <26:
     print("AGRADÁVEL")
elif temp >= 26 and temp <30:
     print("CALOR")
else:
     print ("MUITO CALOR!!!!!!!!!!!!") 
'''
'''
10 - Faça um algoritmo para ler um número inteiro e informar se o número é par ou ímpar.
num = int(input('Digite um numero: '))
cal = num %2
if cal == 0:
    print('Par')
else:
    print('impar')
'''
'''
11 - Faça um algoritmo que leia os valores A, B e C. Mostre uma mensagem que informe se a soma de A
com B é menor, maior ou igual a C.
A = int(input('Digite um numero: '))
B = int(input('Digite um numero: '))
C = int(input('Digite um numero: '))
soma = A + B
if soma > C:
    print(f'A soma dos numeros {A} e {B} é maior q {C}')
elif soma == C:
    print(f'A soma dos numeros {A} e {B} é ou igual a {C}')
else:
    print(f'A soma dos numeros {A} e {B} é menor q {C}')
'''
'''
12 - Escreva um algoritmo que, para uma conta bancária, leia o seu número, o saldo, o tipo de operação
a ser realizada (depósito ou retirada) e o valor da operação. Após, determine e mostre o novo saldo. Se o

novo saldo ficar negativo, deve ser mostrada, também, a mensagem “conta estourada”
numero_da_conta = int(input('Digite o numero da sua conta: '))
if numero_da_conta == 12345:

    saldo = float(input('Digite o seu saldo da conta: '))
    tipo_de_operaçao = int(input('1- para deposito, 2- para retirada: '))

    if tipo_de_operaçao == 1:
        deposito = float(input('Qual o valor do deposito? '))
        valor = saldo + deposito
        print('Seu novo saldo é de', valor)
    elif tipo_de_operaçao == 2:
        print('Seu saldo atual é de', saldo )
        retirar = float(input('Qual o valor a ser retirado? '))
        valor2 = saldo - retirar
        print('Seu saldo no momento é de', valor2)
        if valor2 < 0:
            print('Conta estourada!!!!!!!')
        else:
            print('Valor atual', valor2)
else:
    print('Numero da conta invalido') 
'''
'''
13 - Suponha que o conceito de um aluno seja determinado em função da sua nota. Suponha, também,
que esta nota seja um valor inteiro na faixa de 0 a 100, conforme a seguinte faixa:
Nota Conceito
0 a 49 Insuficiente
50 a 64 Regular
65 a 84 Bom
85 a 100 Ótimo

 nota = int(input('Digite a nota do aluno: '))

if nota > 0 and nota <= 49:
    print('Insuficiente')
elif nota >= 50 and nota <= 64:
    print('Regular')
elif nota >= 65 and nota <= 84:
    print('bom')
elif nota >= 85 and nota <= 100:
    print('otimo')   
'''
'''
Q:1 - Escreva um programa que recebe a idade de uma pessoa e imprime "Maior de idade" se a idade
for maior ou igual a 18, ou "Menor de idade" caso contrário.

idade = int(input('Digite sua idade: '))
if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')
'''
'''
Q:2 - Crie um programa que solicita dois números ao usuário e exibe o maior deles.

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
if num1 > num2:
    print('O maior numero é', num1)
elif num2 > num1:
    print('O maior numero é', num2)
'''
'''
Q:3 - Elabore um programa que verifica se um número digitado é positivo, negativo ou zero.

num = int(input('Digite um numero: '))
if num > 0:
    print(f'O numero {num} é positivo')
elif num == 0:
    print(f'O numero {num} é igual a 0')
elif num < 0:
    print(f'O numero {num} é negativo')
'''
'''
Q:4 - Escreva um programa que calcule o preço a pagar por um produto, considerando um desconto de
10% caso o valor total seja maior que R$ 100,00.

preco_pagar = float(input('Digite o valor do produto a pagar: '))
if preco_pagar > 100:
    desconto = preco_pagar * 0.10
    preco_final = preco_pagar - desconto
    print('Por causa do desonto de 10% o valor do produto vai ser de', preco_final)
else:
    print('O valor do produto é de:', preco_pagar)
'''
'''
Q:7 - Escreva um programa que leia três números e os imprima em ordem crescente

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))

if num1 < num2 and num1 < num3:
    if num2 < num3:
        print(num1,num2, num3)
    else:
        print(num1,num3,num2)
elif num2 < num1 and num2 < num3:
    if num1 < num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
else:
    if num1 < num2:
        print(num3, num1 , num2)
    else:
        print(num3, num2, num1)
'''

'''
Q:10 - Desenvolva um programa que calcule o preço final de um produto com base em seu valor original
e um percentual de desconto fornecido pelo usuário.

preco_final = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o valor do desconto: '))
valor = preco_final * (desconto/100)
valor2 = preco_final - valor
print(valor2)
'''
'''
Q:11 - Faça um programa que determine se um número é positivo e par ao mesmo tempo

num = int(input('Digite um numero: '))
par = num % 2
if num > 0:
    print('É positivo')
    
elif num == 0:
    print('É par')
'''
'''
Q:12 - Escreva um programa que leia um número de 1 a 7 e imprima o dia da semana correspondente
(considerando 1 como domingo, 2 como segunda-feira, etc.).

num = int(input('Digite um numero entre 1 a 7: '))
if num == 1:
    print('Domingo!')
elif num == 2:
    print('Segunda!')
elif num == 3:
    print('Terça!')
elif num == 4:
    print('Quarta!')
elif num == 5:
    print('Quinta!')  
elif num == 6:
    print('Sexta!')
elif num == 7:
    print('Sabado!')
else:
    print('Voce escolheu errado, leia burro!') 
'''
'''
Q:13 - Desenvolva um programa que leia o ano de nascimento de uma pessoa e classifique-a em uma
das seguintes categorias: criança, adolescente, adulto ou idoso.

ano_de_nascimento = int(input('Digite seu ano de nascimento: '))
idade =  2023 - ano_de_nascimento 
if idade <= 13:
    print('Criança')
elif idade >= 14 and idade <= 21:
    print('Adolescente')
elif idade >= 22 and idade <= 61:
    print('Adulto')
else:
    print('Idoso')
'''
'''
Q:14 - Escreva um programa que determine se uma senha digitada pelo usuário é válida. A senha é
válida se tiver pelo menos 8 caracteres e conter letras maiúsculas, minúsculas e números.

senha = str(input('Digite sua senha: ')).strip()

quantidadade_caracteres = len(senha)
tem_maiuscula = any(letra.isupper() for letra in senha)
tem_minuscula = any(letra.islower() for letra in senha)
tem_numero = any(digito.isdigit() for digito in senha)

if quantidadade_caracteres < 8:
    print('Senha invalida. Escolha uma senha que tenha no mínimo 8 caracteres.')
else:
    if tem_maiuscula:
        if tem_minuscula:
            if tem_numero:
                print("Senha confirmada, CARREGANDO ...........")
            else:
                print("A senha não contém pelo menos um número.")
        else:
            print("A senha não contém letras minúsculas.")
    else:
        print("A senha não contém letras maiúsculas.")  
'''
'''
Q:16 - Desenvolva um programa que simule um sistema de login, onde o usuário deve digitar um nome
de usuário e uma senha. O programa deve permitir o acesso apenas se o nome de usuário for "cd2" e a
senha for "cd2_123". Mostra a mensagem informando usuário logado com sucesso ou login e/ou senha
invalido

import time
nome = str(input('Digite seu usuario: '))
senha = str(input('Digite sua senha: '))
if nome == 'cd2' and senha == 'cd2_123':
    print('Carregando...')
    time.sleep(2)
    print('Parabens! Logado com sucesso.')
else:
    print('Carregando...')
    time.sleep(2)
    print('Falha ao tentar logar!')
'''
'''
Q:17 - Elabore um programa que leia o valor de três produtos e informe qual deles é o mais barato.

produto1 = float(input('Digite o valor do primeiro produto: '))
produto2 = float(input('Digite o valor do segundo produto: '))
produto3 = float(input('Digite o valor do terceiro produto: '))
if produto1 < produto2 and produto1 < produto3:
    print('O mais barato é o primeiro produto')
elif produto2 < produto1 and produto2 < produto3:
    print('O mais barato é o segundo produto')
elif produto3 < produto1 and produto3 < produto2:
    print('O mais barato é o terceiro produto')
'''
'''
Q:18 - Escreva um programa que leia o nome de um mês e exiba o número correspondente
mes = str(input('Digite o nome do mes: ')).capitalize()
if mes == 'Janeiro':
    print(f'O mes {mes} corresponde ao mes 1')
elif mes == 'Fevereiro':
    print(f'O mes {mes} corresponde ao mes 2')
elif mes == 'Março':
    print(f'O mes {mes} corresponde ao mes 3')
elif mes == 'Abril':
    print(f'O mes {mes} corresponde ao mes 4')
elif mes == 'Maio':
    print(f'O mes {mes} corresponde ao mes 5')
elif mes == 'Junho':
    print(f'O mes {mes} corresponde ao mes 6')
elif mes == 'Julho':
    print(f'O mes {mes} corresponde ao mes 7')
elif mes == 'Agosto':
    print(f'O mes {mes} corresponde ao mes 8')
elif mes == 'Setembro':
    print(f'O mes {mes} corresponde ao mes 9')
elif mes == 'Outubro':
    print(f'O mes {mes} corresponde ao mes 10')    
elif mes == 'Novembro':
    print(f'O mes {mes} corresponde ao mes 11')
elif mes == 'Dezembro':
    print(f'O mes {mes} corresponde ao mes 12')
'''


