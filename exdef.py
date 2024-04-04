'''
1. Escreva um programa que exiba uma mensagem de boas-vindas através de
uma função (procedimento).

def mensagem():
    print('Seja bem vindo a esse programa!')
    
mensagem() # Chama a funçao para ser executada
'''
'''
2. Escreva um programa que peça um número e retorne o seu antecessor através
de uma função.

def ante(n):
    antecessor = n - 1
    return antecessor


num = int(input('Digite um numero: ')) 
resultado = ante(num)
print(resultado)
'''
'''
3. Faça um procedimento que receba um número inteiro por parâmetro e informe
se ele é par, impar ou zero.

def funcao(n):
    if n == 0:
        return 'ZERO!'
    elif n % 2 == 0:
        return 'PAR!'
    elif n % 2 == 1:
        return 'IMPAR!'
    

num = int(input('Digite um numero: '))
resultado = funcao(num)
print(resultado)
'''
'''
4. Escreva um programa para ler as notas das três avaliações de um aluno no
bimestre. Também faça uma função que receba as notas por parâmetro e
calcule a média bimestral. Por fim, escreva a mensagem de Aprovado ou
Recuperação.

def media(n1, n2, n3):
    m = (n1 + n2 + n3) / 3
    return m 


aluno =  str(input('Nome do aluno: '))
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
media_bimestral = media(nota1, nota2, nota3)
if media_bimestral < 7:
    print('Reprovado!')
else: 
    print('Aprovado!')
'''
'''
5. Faça uma função que calcule o IMC (peso/altura2) de uma pessoa e conforme o
seu retorno classifique, no programa principal, conforme a tabela abaixo:

def imc(p, a):
    imc_pessoa = p / (a**2)
    return imc_pessoa

peso = float(input('Digite o peso: '))
altura = float(input('Digite o altura: '))
resultado_imc = imc(peso, altura)
if resultado_imc <= 18.5:
    print('Abaixo do Peso')
elif resultado_imc >= 18.5 and resultado_imc < 25:
    print('Peso normal')
elif resultado_imc >= 25.1 and resultado_imc < 30:
    print('Acima do Peso')
else:
    print('Obeso')
'''
'''
6. Faça um programa de calculadora com as operações básicas: adição,
subtração, multiplicação e divisão. O programa inicia apresentando um menu
de opções como mostrado abaixo. Posteriormente, o usuário deve digitar 2
valores. Deve ser criada uma função para cada operação matemática. A função
deverá receber os valores como parâmetros.

def adicao(n1, n2):
    soma = n1 + n2
    return soma

def subtracao(n1, n2):
    sub = n1 - n2
    return sub

def multiplicacao(n1, n2):
    mult = n1 * n2 
    return mult

def divisao(n1, n2):
    div = n1 / n2
    return div
    
print('=-' *20)
print('Calculadora')
print('=-' *20)
print('Opçoes:')
print('1- Soma')
print('2- Subtraçao')
print('3- Multiplicaçao')
print('4- Divisao')
opcao = int(input('Qual opçao? '))

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
if opcao == 1:
    soma_resul = adicao(num1, num2)
    print(f'{num1} + {num2} = {soma_resul}')
elif opcao == 2:
    sub_resul = subtracao(num1, num2)
    print(f'{num1} - {num2} = {sub_resul}')
elif opcao == 3: 
    mult_resul = multiplicacao(num1, num2)
    print(f'{num1} x {num2} = {mult_resul}')
elif opcao == 4:
    div_resul = divisao(num1, num2)
    print(f'{num1} / {num2} = {div_resul}')
'''
'''
8. Crie uma função que receba por parâmetro um número inteiro e verifique se o
número é positivo ou negativo. Retorne um valor lógico (verdadeiro ou falso)

def funcao(n):
    if n < 0:
        return False
    else:
        return True

num = int(input('Digite um numero: '))
resul = funcao(num)
if resul == True:
    print('Verdadeiro!')
elif resul == False:
    print('Falso!')
'''
'''
9. Crie uma função que verifique se um determinado número é par. Retorne um
valor lógico (verdadeiro ou falso)

def funcao(n):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um numero: '))
resul = funcao(num)
if resul == True:
    print('Verdadeiro!')
elif resul == False:
    print('Falso!')
'''
'''
10. Crie uma função que verifique se um determinado número é par ou ímpar.
Retorne um valor do tipo caractere que informe o resultado (par ou ímpar)

def verificacao(n):
    if n % 2 == 0:
        return f'{n} é par'
    else:
        return f'{n} é impar'


num = int(input('Digite um numero: '))
resul = verificacao(num)
print(resul)
'''
'''
11. Faça uma função que recebe, por parâmetro, a altura (alt) e o sexo de uma
pessoa e retorna o seu peso ideal. Para homens, calcular o peso ideal usando a
fórmula peso ideal = 72.7 * alt - 58 e, para mulheres, peso ideal = 62.1 * alt -
44.7.

def homens(alt):
    peso_ideal1 = 72.7 * alt - 58
    return peso_ideal1
def mulheres(alt):
    peso_ideal2 = 62.1 * alt - 44.7
    return peso_ideal2

altura = float(input('Altura: '))
genero = input('Genero: ').upper()
if genero == 'HOMEM':
    peso_homem = homens(altura)
    print(f'O peso ideal é {peso_homem}')
elif genero == 'MULHER':
    peso_mulher = mulheres(altura)
    print(f'O peso ideal é {peso_mulher}')
'''
'''
12. Faça uma função para calcular o maior e menor número entre três
números. Os números são passados por parâmetros.

def funcao(n1, n2, n3):
    maior = max(numeros)
    menor = min(numeros)
    return maior, menor

numeros = []
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))
numeros.append(num1)
numeros.append(num2)
numeros.append(num3)
maior, menor = funcao(num1, num2, num3)
print(f'O maior número é {maior} e o menor número é {menor}.')
'''
'''
13. Faça uma função para calcular o somatório dos elementos de uma lista com
50 números.

def soma(n):
    soma = 0
    for n in numeros:
        soma += n
    return soma


numeros = []
for i in range(50):
    numeros.append(i)
resultado = soma(numeros)
print(f'A soma dos numeros compotos na lista é {resultado}')
'''
'''
14. Faça uma função para verificar se um determinado caractere pertence a
uma lista de caracteres de 20 posições. O retorno da função é uma mensagem
indicando se o caractere pertence ou não.

def verificacao(lista, numero):
    if numero in lista:
        return 'Pertence'
    else:
        return 'Não Pertence'
    

lista = []
for i in range(1,21,2):
    lista.append(i)
num = int(input('Digite um numero: '))
resultado = verificacao(lista, num)
print(resultado)
'''
'''
15. Faça uma função que receba um vetor de 20 posições e retorne uma lista
com os elementos invertidos. Obs.: Inverter os números usando o for

'''
def inverter(vetor):
    vetor_invertido = []
    for i in range(len(vetor)-1, -1, -1):
        vetor_invertido.append(vetor[i])
    return vetor_invertido

# Testando a função
vetor = list(range(20))  # Cria uma lista de 0 a 19
resultado = inverter(vetor)
print(resultado)










