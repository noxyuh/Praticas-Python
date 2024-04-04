
cont = 'S'
while cont == 'S':
    genero = str(input('Digite M para masculino ou F para feminino: ')).lower().strip()
    if genero == 'f' or genero == 'm':
        print('Seu genero é', genero)
        break
    else:
        print('Digite novamente')