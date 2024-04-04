nome = str(input('\033[4;35mDigite seu nome completo: \033[m '))
print('\033[1;31mAnalisando seu nome...\033[m')
print('Seu nome em maiúsculas é', nome.upper())
print('Seu nome me minúsculas é', nome.lower())
nome1 = len(nome)-nome.count(" ")
print('Seu nome tem ao todo tem', nome1)
nome2 = nome.split()
nome3 = nome2[0]
print('Seu primeiro nome é', nome3)


