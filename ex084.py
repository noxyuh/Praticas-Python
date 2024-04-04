dados1 = []

while True:
    dados = []
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    dados1.append(dados[:])
    
    continuar = str(input('Quer continuar [S/N]? ')).upper()
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
    else:
        print('Opcao invalida!')
        
maior_peso = dados1[0][1]
menor_peso = dados1[0][1]
nome_maior_peso = dados1[0][0]
nome_menor_peso = dados1[0][0]


for p in dados1:
    if p[1] > maior_peso:
        maior_peso = p[1]
        nome_maior_peso = p[0]
    if p[1] < menor_peso:
        menor_peso = p[1]
        nome_menor_peso = p[0]
        
print(f'Ao todo, voce cadastrou {len(dados1)} pessoas')  
print(f'O maior peso foi de {maior_peso} kg e pertence a {nome_maior_peso}')
print(f'O menor peso foi de {menor_peso} kg e pertence a {nome_menor_peso}')