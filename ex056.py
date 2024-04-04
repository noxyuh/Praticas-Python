
soma_idade = 0
mulher = 0
media = 0
maior_idade = 0
nome_maior = 0
for i in range(4):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    genero = str(input('Qual o seu sexo? '))
    media += idade /4 
    soma_idade += idade
    
    if genero == ('f' or genero == 'feminino' or genero == 'mulher') and idade < 20:
        mulher += 1
    elif genero == "m" or genero == "masculino" or genero == "homem":
            if idade > maior_idade:
                maior_idade = idade
                nome_maior = nome
               
print('A media entre as idades é de', media)
print(f'Tem {mulher} mulheres com menos de 20 anos ')    
print(f'O homem mais velho é {nome_maior} com {maior_idade} anos.')
    
    