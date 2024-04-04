
'''
Questao 1
a = 15*5-3*4
b = (28+384)/2
c = 8-30/6
d = 12-2/2+3
e = ((28+3)*4/2)
print(a,b,c,d,e)
'''
'''
Questao 2
A = 3
B = 4
C = 5

a = A*B-C
b = C/4*6
c = B/A+3
d = A*(B-C)

print(a,b,c,d)
'''
'''
Questao 4
Escreva um programa que leia um número, calcule seu dobro e escreva “O dobro do número é:”
num = int(input('Digite um numero: '))
cont = num *2 
print('O dobro do numero é:', cont)
'''
'''
 Faça um programa que leia e exiba um nome e a idade do aluno e notas
nome = str(input('Digite o nome do aluno: '))
idade = int(input('Digite a idade do aluno: '))
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota: '))
print('O nome do aluno é:', nome)
print('A idade do aluno é:', idade)
print('A primeira nota do aluno foi:', nota1)
print('A segunda nota do aluno foi:', nota2)
'''
'''
Questao 7
 Calcular e exibir a média ponderada de 2 notas dadas. (nota1= 10 e seu peso = 6 e nota2 = 7 e seu peso = 4).
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
peso1 = 6
peso2 = 7
soma = (nota1*peso1) + (nota2*peso2) / peso1 + peso2
print('A nota encontrada foi:', soma)
'''
'''
Questao 8
 Faça um algoritmo para “Calcular o estoque médio de uma peça”, sendo que ESTOQUEMÉDIO = (QUANTIDADE MÍNIMA + QUANTIDADE MÁXIMA) /2.
quantmin = int(input('Digite o estoque minino: '))
quantmax = int(input('Digite o estoque maximo: '))
estoquemedio = (quantmin + quantmax) /2
print('O estoque medio de peças é de:', estoquemedio)
'''
'''
Questao 9
 Calcular o salário líquido (SL) de um funcionário sabendo o seu salário bruno (SB) e o total dos descontos (D), sabendo que SL= SB-D.
SB = float(input('Digite o salario bruto: '))
D = int(input('Digite o total de descontos: '))
SL = SB - D
print('O salario liquido do funcionario é de:', SL)
'''
'''
Questao 10
 Faça um algoritmo que calcule o cumprimento de uma circunferência de raio R, dado C=2piR
R = float(input('Digite o valor de Raio: '))
C = 2*3.14*R
print('O comprimento é:', C)
'''
'''
Questao 11
# Faça um programa que leia dois números inteiros e mostre a soma deles.
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
soma = num1 + num2 
print(f'A soma entre {num1} + {num2} é igual a {soma}')
'''
'''
Questao 12
 Faça um programa que leia 3 nomes e mostre-os na ordem inversa de leitura
nome1 = str(input('Digite um nome: '))
nome2 = str(input('Digite um nome: '))
nome3 = str(input('Digite um nome: '))

print(nome3)
print(nome2)
print(nome1)
'''
'''
Questao 13
 Faça um programa para somar dois números e multiplicar o resultado pelo primeiro número.
n1 = int(input('Digite um numero: ')) 
n2 = int(input('Digite outro numero: '))
soma = n1 + n2 
mult = soma * n1
print('O resultado é:', mult)
'''
'''
Questao 14
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
n4 = int(input('Digite um numero: '))
resul = n1*2 + n2*2 + n3*2 + n4*2
print(resul)
'''
'''
Questao 15
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
soma = n1+n2+n3
sub = n1-n2-n3
mult = n1*n2*n3
div = n1/n2/n3
print(soma, sub, mult, div)
'''
'''
Questao 16
 Escreva um algoritmo para ler a temperatura dada na escala Celsius e exibir o equivalente em Fahrenheit. Para isto utilize a fórmula: F= 9/5 * C+32
temp = float(input('Digite a temperatura: '))
F = 9/5 * temp+32
print('A temperatura em Fahrenheit é: ', F)
'''
'''
Questao 17
  Escreva um algoritmo para calcular a distância média de um automóvel a partir da distância percorrida (S) e do tempo gasto para percorrer essa distância (T), sabendo que VM = S/T
S = float(input('Digite a distancia percorrida: '))
T = float(input('Digite o tempo gasto: '))
VM = S/T
print('A velocidade media percorrida é de', VM)
'''
''''
Questao 18
Faça um algoritmo para ler duas varáveis a e b inteiras e trocar o conteúdo lido de uma pela outra, ou seja, o valor da variável a ficará na variável b e o valor da variável b ficará na variável a
a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))

temp = a
a = b
b = temp

print(a, b)
'''
'''
Questao 19 
Calcule a média de quatro números inteiros dados.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) /4
print('A media obtida foi de:', media)
'''
'''
Questao 20
Leia uma quantidade de chuva dada em polegadas e imprima o equivalente em milímetros (25,4 mm = 1 polegada).
polegadas = float(input('Digite a quantidade de chuva em polegadas: '))
m = polegadas* 25.4
print('A chuva equivalente a milimetros é de', m)
'''
'''
Questao 21
O custo ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do
distribuidor e dos impostos, ambos aplicados ao custo de fábrica. Supondo que a porcentagem do
distribuidor seja de 12% e a dos impostos de 45%, prepare um algoritmo para ler o custo de fábrica do
carro e imprimir o custo ao consumidor
f = float(input('Digite o valor do custo de fabrica: '))
consumidor = f * 0.12
soma1 = consumidor + f
imposto = soma1 * 0.45
soma2 = imposto + f
print('O custo para o consumidor vai ser de:', soma2)
'''
'''
Questao 22
- Uma companhia de carros paga a seus empregados um salário de R$ 500,00 por mês mais uma
comissão de R$ 50,00 para cada carro vendido e mais 5% do valor da venda. Elabore um algoritmo para
calcular e imprimir o salário do vendedor num dado mês recebendo como dados de entrada o número de
carros vendidos e o valor total das vendas.
numero_de_carros_vendidos = float(input('Digite o numero de carros: '))
valor_total_das_vendas = float(input('Digite o total de vendas: '))
carro_vendido = 50 * numero_de_carros_vendidos
salario2 = 500 + carro_vendido
n = valor_total_das_vendas * 0.05
salario_final = salario2 + n 
print(f'O salario final é de {salario_final}')
'''
'''
 Faça um programa que receba o salário-base de um funcionário, calcule e mostre o salário a receber,
sabendo-se que esse funcionário tem gratificação de 5% sobre o salário-base e paga imposto de 7% sobre
salário-base.
'''
'''
Questao 23
salario = float(input('Digite o salario: '))
gratificacao = salario * 0.05
imposto = salario * 0.07
s = salario + gratificacao
n =  s - imposto
print('O salario final é de:', n)
'''
'''
Questao 24
Faça um programa que receba um número positivo e maior que zero, calcule e mostre
a) O número digitado ao quadrado.
b) O número digitado ao cubo.
c) A metade do número digitado.
d) O sucessor do número digitado.
num = 15
a = num * 2
b = num * 3
c = num / 2
d = num + 1

print(f'O numero {num} ao quadrado é {a}')
print(f'O numero {num} ao cubo é {b}')
print(f'A metade do numero {num} é {c}')
print(f'O sucessor do numero {num} é {d}')
'''
'''
Questao 25
 Codificar um programa que seja capaz de apresentar o valor em real (R$) de um valor lido em dólar
(US$) 4,92
dolar = float(input('Digite uma quantia em dolar: '))
dolar2 = dolar * 4.92
print(dolar2)
'''
'''
Questao 26
A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. Faça um
programa que receba um valor de uma compra e mostre o valor das prestações.
print('Bem vindo a Loja Mamão com Açúcar!')
valor_compra = float(input('Digite o valor da compra: '))
prestacao = valor_compra /5
print(f'O valor das prestações é de {prestacao}')
'''
'''
Questao 27
 Faça um programa para ler a idade de uma pessoa e exibir quantos dias de vida ela já viveu.
Considere sempre anos completos, e que um ano possui 365 dias. Ex: uma pessoa com 19 anos possui
6935 dias de vida. 

idade = int(input('Digite a sua idade: '))
ano = idade * 365
print(f'Essa pessoa possui {ano} dias de vida.')

'''
'''
Questao 28
x = 2
y = 5
conta = (25*x / 12*y) + ((y)**2 / x**2) - x/2*y
print(conta)
'''

'''
Questao 29
 Calcular o IMC. Recebe o valor do peso. Recebe o valor da altura. Calcule o IMC. Mostre o IMC.
 
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura '))
imc = peso / altura **2
print('Seu imc é de', imc)
'''
'''
Questao 30
Calcule o consumo médio do seu carro. Recebe a quantidade de quilômetros rodados. Recebe a
quantidade de litros gastos. Calcule e mostre o consumo médio.

quilometros = float(input('Digite a quantidade de quilometros rodados: '))
litros = float(input('Digite a quantidade de litros gastos: '))
media = quilometros / litros
print('O consumo medio foi de:', media)
'''
'''
Questao 31
 Escreva um algoritmo que calcula a extensão total de uma ponte, em metros, na qual um trem de
200m de comprimento, com velocidade escalar constante de x km/h, gasta um tempo t em segundos para
atravessar completamente essa ponte. O usuário deverá informar os valores do tempo e da velocidade.
tempo = float(input('Digite o tempo em segundos: '))
velocidade = float(input('Digite a velocidade do trem: '))
a = velocidade * (tempo/36000)
v = a + 200 
print(v)
'''
'''
Questao 32
 Crie um algoritmo para calcular a velocidade média de um automóvel. A distância percorrida e o
intervalo de tempo serão informados pelo usuário.

distancia = float(input('Digite a distancia: '))
tempo = float(input('Digite o tempo: '))
vm = distancia / tempo
print('A velocidade média do automóvel é', vm)
'''
'''
Questao 33
 Crie um algoritmo para calcular a aceleração média. A variação da velocidade e o intervalo de tempo
serão informados pelo usuário.
distancia = float(input('Digite a distancia: '))
tempo = float(input('Digite o tempo: '))
a = distancia / tempo
print('A aceleraçao média é', a)
'''
'''
34 - Crie um algoritmo para calcular a função horária do deslocamento. A posição inicial, a velocidade e o
intervalo de tempo serão informados pelo usuário. s = s0**2 + v . At
velocidade = float(input('Digite a velocidade: '))
intervalo_de_tempo = float(input('Digite o intervalo de tempo: '))
so = 5
s = 0**2 + velocidade * intervalo_de_tempo
print('A função horária do deslocamento: ', s)
'''
'''
35 - Crie um algoritmo para calcular a equação de Torricelli. A velocidade inicial, a aceleração e a distância
percorrida serão informados pelo usuário
velocidade_inicial = float(input('Digite a velocidae inicial: '))
aceleracao = float(input('Digite a aceleraçao inicial: '))
distancia = float(input('Digite a distancia inicial: '))
v = velocidade_inicial**2 + 2*aceleracao*distancia
print('O resultado é ', v)
'''
'''
1. Armazene o seu nome em uma variável e imprima na tela.
nome = 'Rafael'
print(nome)
'''
'''
2. Armazene um número inteiro em uma variável e imprima na tela.
num = 3
print(num)
'''
'''
3. Armazene dois números inteiros em variáveis diferentes e imprima a soma
desses números na tela.
num1 = 34
num2 = 89
soma = num1 + num2
print(soma)
'''
'''
4. Armazene uma frase em uma variável e imprima na tela.
frase = 'Ola pessoal, bem vindo ao python!'
print(frase)
'''
'''
5. Armazene seu nome e idade em variáveis diferentes e imprima na tela usando
o comando print.
nome = 'Rafael'
idade = 19

print(nome, idade)
'''
'''
6. Peça ao usuário para digitar o ano atual e o ano de nascimento e imprima a
idade desta pessoa.
ano_de_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = int(input('Digite o ano que estamos: '))

idade = ano_de_nascimento - ano_atual
print(idade)
'''
'''
7. Crie três variáveis com os valores dos lados de um triângulo e imprima o valor
da área deste triângulo.
lado1 = int(input('Digite um lado do triangulo: '))
lado2 = int(input('Digite um lado do triangulo: '))
lado3 = int(input('Digite um lado do triangulo: '))
b = (lado1+lado2+lado3) /2
c = (b-lado1)*(b-lado2)*(b-lado3)
a = b*c
d = (a **0.5)
print(d)
'''
'''
8. Peça ao usuário para digitar o raio de um círculo e imprima o valor da área
deste círculo(pi * r2).
r = float(input('Digite o valor do raio: '))
area = 3.14 * r**2
print('A area do circulo é', area)
'''
'''
9. Use o comando input para ler uma frase do usuário e armazene-a em uma
variável. Em seguida, imprima a frase na tela.
frase = str(input('Digite uma frase: '))
print(frase)
'''
'''
10. Use o comando input para ler um número inteiro do usuário e armazene-o
em uma variável. Em seguida, imprima o número na tela.
numero = int(input('Digite um numero: '))
print(numero)
'''
'''
11. Peça ao usuário para digitar três notas de um aluno e calcule a média
destas notas.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media = (nota1+nota2+nota3) /3
print('A media obtida foi de', media)
'''
'''
12. Peça ao usuário para digitar três notas de um aluno e os pesos
correspondentes, e calcule a média ponderada.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
peso1 = float(input('Digite o peso da primeira nota: '))
peso2 = float(input('Digite o peso da segunda nota: '))
peso3= float(input('Digite o peso da terceira nota: '))

media = (nota1 * peso1 + nota2 * peso2+ nota3 * peso3) /(peso1+peso2+peso3)
print('A media ponderada obtida foi de', media)
'''
'''
15. Escreva um programa que peça ao usuário que insira uma palavra e, em
seguida, imprima essa palavra na tela, mas com todas as letras em
maiúsculas.
palavra = str(input('Digite uma frase: '))
print(palavra.lower())
'''
'''
16. Escreva um programa que peça ao usuário que insira dois números inteiros
e imprima a divisão do primeiro pelo segundo.
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
div = num1/num2
print(div)
'''
'''
17. Peça ao usuário para digitar a quantidade de horas trabalhadas e o valor da
hora trabalhada, e calcule o salário bruto.
horas_trabalhadas = float(input('Digite as horas trabalhadas: '))
valor_horas_trabalhadas = float(input('Digite o valor das horas trabalhadas: '))
sl = horas_trabalhadas * valor_horas_trabalhadas
print('O salario bruto é de', sl)
'''

 


