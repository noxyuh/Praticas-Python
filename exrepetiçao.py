
'''
1. Leia 20 valores reais e escreva o seu somatório.
soma = 0
for i in range(20):
    n = int(input('Digite um numero: '))
    soma += n
print(soma)

soma = 0
cont = 0
while cont < 20:
    n = int(input('Digite um numero: '))
    soma += n
    cont += 1
print(soma)

soma = 0
while True:
    n = int(input('Digite um numero: '))
    para = str(input('S/N ')).upper()
    soma += n
    if para == 'N':
        break
    elif para == 'S':
        continue
    else:
        print('opcao invalida!')
print(f'A soma encontrada foi de {soma}')
'''
'''
2. Escrever um algoritmo que imprima a tabuada de um número informado pelo usuário;
num = int(input('Escolha um numero para a tabuada: '))
mult = 0
for i in range(10):
    mult = num * i
    print(f'{num} X {i} = {mult}')
'''
'''
3. Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 2000;

cont = 0
while cont < 2000:
    if cont % 2 == 1:
        print(cont)
    cont += 1
    
for i in range(2000):
    if i % 2 == 1:
        print(i)
'''
'''
4. Escrever um programa de computador que leia 10 números positivos e, ao final, apresente a soma de todos
os números lidos. Você deve testar se o numero é positivo.

soma = 0
for i in range(10):
    num = int(input('Digite um numero: '))
    if num > 0:
        soma += num
    else:
        print('Escolha um numero posivito!')
        break
print(soma)


soma = 0
cont = 0
while cont < 10:
    num = int(input('Digite um numero: '))
    cont += 1
    if num > 0:
        soma += num
    else:
        print('Escolha um numero posivito!')
        break
print(soma)

'''
'''
Faça um algoritmo para ler e escrever o Nome de 20 pessoas.
for i in range(20):
    nome = str(input('Digite seu nome: '))

'''
'''
5. Faça um algoritmo para ler e escrever o Nome de inúmeras pessoas. Só irá parar de informar o nome
quando o usuário digitar sair. 
  
while True: 
    nome = str(input('Digite seu nome [SAIR]: ')).upper()
    if nome == 'SAIR':
        break
        
from itertools import count

for i in count(start=0):
    nome=input(f"Digite {i+1} nome: ") 
    if nome == "sair":
        break
    else:
        continue
'''
'''
6. Faça um algoritmo para ler um valor X e calcular Y = X+2X+3X+4X+5X+...+20X

soma = 0
mult = 0
cont = 1
x = int(input('Digite um numero: '))
while cont <= 20:
    y = x * cont
    soma += y
    
    cont += 1
   
print('O resultado foi', soma)
'''
'''
7. Escreva um algoritmo que calcule a média dos números digitados pelo usuário, se eles forem pares.
Termine a leitura se o usuário digitar zero (0);

soma = 0
cont = 0
while True:
    num = int(input('Digite um numero [0 para sair]: '))
    if num == 0:
        print('Voce finalizou o programa!')
        break
    soma += num
    cont += 1
    resul = soma / cont
    
print('A media encontrada foi de', resul)

'''
'''
8. Escreva um algoritmo que leia valores inteiros entre -1000 e 1000 e encontre o maior e o menor deles.
Termine a leitura se o usuário digitar zero (0);

valores = []
while True:
    num = int(input('Digite um numero [0 para sair]: '))
    if num == 0:
        print('Voce finalizou o programa!')
        break
    if num >= -1000 and num <= 1000:
        valores.append(num)
        continue
    else:
        print('Digite outro valor')
    
    
print(f"o valor maior: {max(valores)}")
print(f"o valor menor: {min(valores)}")
'''
'''
9. Escreva um programa que leia dois valores reais. Ambos valores deverão ser lidos até que o usuário digite
um número no intervalo de 1 a 50. Apresentar a soma dos dois valores lidos.

soma = 0
while True:
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite outro numero: '))
    if num1 > 1 and num2 < 51 and num2 > 1 and num2 < 51:
        soma = num1 + num2
        print(f'{num1} + {num2} = {soma}')
    else:
        print('digite um valor entre 1 e 50')
'''
'''
10. Uma turma possui N alunos, e para cada aluno tem-se uma média para cada disciplina. O professor de
Matemática Led gostaria de saber a média geral de sua disciplina em uma turma. Faça um algoritmo para
auxiliar a encontrar este valor.

soma = 0
cont = 0
while True:
    alunos = str(input('Digite o nome do aluno: '))
    nota1_math = float(input('Digite a primeira nota do aluno em matematica: '))
    nota2_math = float(input('Digite a segunda nota do aluno em matematica: '))
    soma +=  nota1_math + nota2_math
    cont += 2
    continua = str(input('Deseja Continuar [S/N]? ')).upper()
    if continua == 'S':
        continue
    elif continua == 'N':
        break
    else:
        print('Opcao invalida!')
        
media = soma / cont  
print(f'A media geral da disciplina é: {media:2f}')   
'''
'''
11. Uma empresa com X funcionários precisa saber a média de seus salários. Faça um algoritmo para ler a
quantidade de funcionários e o salário de cada um e escrever a média dos salários.

soma = 0
funcionarios = int(input('Digite a quantidade de funcionarios: '))  
for i in range(funcionarios):
    salario = int(input('Digite o salario do funcionario: '))
    soma += salario
media = soma / funcionarios
print('A media salarial da empresa é', media)
'''
'''
12. Escreva um programa que leia um valor correspondente ao número de jogadores de um time de vôlei. O
programa deverá ler uma altura para cada um dos jogadores e, ao final, informar a altura média do time.

soma = 0
jogadores = int(input('Informe o numero de jogadores do time: '))
for i in range(jogadores):
     altura = float(input('Informe a altura do jogador: '))
     soma += altura
media = soma / altura
print('A media de altura dos jogadores é', media)
'''
'''
13. Faça um algoritmo para ler e escrever o Nome, idade e sexo de um número indeterminado de alunos. Ao
final escreva o total de alunos lidos, o total do sexo masculino, o total do sexo feminino, a media de idade, a
maior idade e a menor idade. O algoritmo só irá parar quando o usuário digitar sair.

lista = []
soma = 0
total_mulheres = 0
total_homens = 0
total_alunos = 0
while True:
    nome = str(input('Digite o nome do aluno: '))
    idade = int(input('Digite a idade do aluno: '))
    genero = str(input('Digite o genero do aluno [M/F]: ')).upper()
    
    total_alunos += 1
    soma += idade
    lista.append(idade)
    if genero == 'M':
        total_homens += 1
    elif genero == 'F':
        total_mulheres += 1
    else:
        print('Opcao invalida!')
        
    continuar = str(input('Quer continuar[S/N]? ')).upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue
    else:
        print('Opcao invalida!')
media = soma / total_alunos
print(f'O total de alunos foi {total_alunos}')
print(f'O total de alunos do genero masculino foi {total_homens}')
print(f'O total de alunos do genero feminino foi {total_mulheres}')
print(f'A media de idade dos alunos foi {media}')
print(f'O aluno mais velho tem {max(lista)}')
print(f'O aluno mais novo tem {min(lista)}')

'''
'''
1. Um algoritmo para imprimir 100 vezes na tela a palavra “Olá mundo”.
for i in range(100):
    print('Ola mundo!')    
'''
'''
2. Um algoritmo para imprimir n vezes na tela a palavra “Olá mundo”. O numero de vezes deve ser informado
pelo usuário.

vezes = int(input('Digite o numero de vezes: '))
for i in range(vezes):
    print('Ola mundo!')
''' 
'''
3. Um algoritmo para apresentar o total da soma obtida dos cem primeiros números inteiros
(1+2+3+4+5+6+7+...+97+98+ 99+100).

soma = 0
for i in range(100):
    soma += i
    print(soma)
'''
'''
4. Um algoritmo para imprimir os números de 1 a 10 em ordem crescente.
for i in range(1,11):
    print(i)
    
cont = 0
while cont < 11:
    print(cont)
    cont += 1
'''
'''
5. Um algoritmo para imprimir os números de 1 a 10 em ordem decrescente.
for i in range(11, 0, -1):
    print(i)

cont = 11
while True:
    cont -= 1
    print(cont)
    if cont <= 1:
        break
'''
'''
6. Um algoritmo para imprima todos os números ímpares de 1 até 303.
for i in range(1, 303, 2):
    print(i)
'''
'''
7. Um algoritmo para que leia um número N do usuário, some todos os números de 1 a N, e mostre o
resultado obtido.

soma = 0
n = int(input('Digite o numero: '))
for i in range(0, n+1):
    soma += i
print(soma)
'''
'''
8. Um algoritmo para imprimir na tela a soma dos números ímpares entre 1 e 30 e a multiplicação dos
números pares entre 1 e 30.

soma = 0
mult = 1
for i in range(1, 31):
    if i % 2 == 0:
        mult *= i
    else:
        soma += i
print(soma)
print(mult)
'''
'''
9. Um algoritmo que calcule e imprima a tabuada do 8 (1 a 10).

cont = 0
while cont < 10:
    cont += 1
    mult = 8 * cont
    
    print(f'{8} X {cont} = {mult}')
'''
'''
10. Um algoritmo que exibe uma pirâmide semelhante a abaixo, sendo que o maior valor N da pirâmide é
definido pelo usuário. Ex: n=9

num = int(input('Digite um numero: '))
for i in range(num, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()
'''
'''
11. Some os números de 1 a 100 e imprima o valor.

soma = 0
cont = 0
while cont < 100:
    soma += cont
    cont += 1
print(soma)

'''
'''
12. Construa um Algoritmo que, para um grupo de 50 valores inteiros, determine:
a) A soma dos números positivos;
b) A quantidade de valores negativos;

soma = 0
quant = 0
cont = 0
while cont < 10:
    num = int(input('Digite um numero: '))
    cont +=1
    if num < 0:
        quant += 1
    if num > 0:
        soma += num   
print('A soma dos números positivos é', soma) 
print('A quantidade de valores negativos é', quant)
'''
'''
13. Faça um algoritmo que imprima todos os números pares compreendidos entre 85 e 907. O algoritmo deve
também calcular a soma destes valores.

soma = 0
for i in range(84, 908, 2):
    soma += i
    print(i)
print('-='*10)    
print(soma)
'''
'''
14. Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números ímpares de 1
até N em ordem decrescente.

num = int(input('Digite um numero: '))
for i in range(num, -1, -1):
    print(i)
'''
'''
Terceira parte:
1. Escreva um programa em Python que imprima os números de 1 a 10 usando um laço "while".

cont = 0
while cont < 10:
    cont+= 1
    print(cont)
'''
'''
2. Escreva um programa em Python que imprima os números de 10 a 1 usando um laço "while".

cont = 10
while cont >= 1: 
    print(cont)
    cont -= 1
'''
'''
3. Escreva um programa em Python que calcule a soma dos números de 1 a 100 usando um laço "while".

soma = 0
cont = 0
while cont < 100:
    soma += cont
    cont += 1
print(soma)   
'''
'''
4. Escreva um programa em Python que imprima os números pares de 2 a 20 usando um laço "while".

cont = 2
while cont < 21:
    print(cont)
    cont += 2
'''
'''
5. Escreva um programa em Python que imprima os números ímpares de 1 a 19 usando um laço "while".

cont = 1
while cont < 20:
    print(cont)
    cont += 2
'''
'''
6. Escreva um programa em Python que peça ao usuário para digitar um número e imprima todos os números
de 1 até esse número usando um laço "while".

num = int(input('Digite um numero: '))
cont = 1
while cont < num+1:
    print(cont)
    cont += 1
'''
'''
7. Escreva um programa em Python que peça ao usuário para digitar um número e calcule a soma dos
números de 1 até esse número usando um laço "while".

num = int(input('Digite um numero: '))
cont = 0
soma = 0
while cont < num+1:
    soma += cont
    cont+=1
print(soma)
'''
'''
8. Escreva um programa em Python que peça ao usuário para digitar um número e imprima todos os números
pares de 2 até esse número usando um laço "while".

num = int(input('Digite um numero: '))
cont = 2
while cont < num:
    print(cont)
    cont += 2
'''
'''
9. Escreva um programa em Python que peça ao usuário para digitar um número e imprima todos os números
ímpares de 1 até esse número usando um laço "while".

num = int(input('Digite um numero: '))
cont = 1
while cont < num:
    print(cont)
    cont += 2
'''
'''
10. Escreva um programa em Python que peça ao usuário para digitar um número e imprima todos os números
primos de 2 até esse número usando um laço "while".

num = int(input('Digite um numero: '))
cont = 2
while cont <= num:
    i = 2
    primo = True
    while i < cont:
        if cont % i == 0:
            primo = False
            break
        i += 1
    if primo:
        print(cont)
    cont += 1
'''
'''
11. Escreva um programa em Python que peça ao usuário para digitar um número e verifique se esse número é
primo usando um laço "while".

num = int(input('Digite um numero: '))
cont = 2
primo = True
while cont < num:
    if num % cont == 0:
        primo = False
        break
    cont += 1
if primo and num != 1:
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} não é primo.')

'''
'''
16. Escreva um programa em Python que peça ao usuário para digitar um número e imprima a soma dos
números pares e ímpares menores ou iguais a esse número usando um laço "while".

num = int(input('Digite um numero: '))
cont = 0
soma_pares = soma_impares = 0
while cont < num:
    cont += 1
    if cont % 2 == 0:
        soma_pares += cont
    elif cont % 2 == 1:
        soma_impares += cont
print('A soma dos numeros pares é', soma_pares)
print('A soma dos numeros impares é', soma_impares)
'''
'''
20. Escreva um programa em Python que peça ao usuário para digitar um número e imprima a soma dos
números perfeitos menores ou iguais a esse número usando um laço "while".

'''









