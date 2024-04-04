
dados1 = []
cont = 0
while True:
    dados = []
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Primeira nota: ')))
    dados.append(float(input('Segunda nota: ')))
    media = (dados[1] + dados[2]) / 2
    dados.append(media)
    dados1.append(dados[:])
    continuar = str(input('Quer continuar [S/N]? ')).upper()
    cont += 1
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
    else:
        print('Opcao invalida!')
    
print('-='*30)
print('No.', 'Nome', 'Media')
for i in range(cont):
    print(i+1, dados1[i][0], dados1[i][3], sep=' ')

m = 0
while m != 999:
    m = int(input('Mostrar notas de qual aluno? (999 para interromper) '))
    if m < len(dados1):
        print(f'Notas de {dados1[m][0]} sao {dados1[m][1]} e {dados1[m][2]}')
    else:
        print('Aluno não encontrado.')

