cont_idade = 0
homem = 0
mulheres = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    genero = str(input('Genero: [M/F] ')).upper()
    if idade > 18:
        cont_idade += 1
    if genero == 'M':
        homem += 1
    if genero == 'F' and idade < 20:
            mulheres += 1
    cont = str(input('Quer continuar? [S/N] ')).upper()
    if cont == 'N':
        break
    
print('Total de pessoas com mais de 18 anos:', cont_idade)
print(f'Ao todos temos {homem} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')