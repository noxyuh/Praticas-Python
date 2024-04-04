def area(larg, comp):
    a = largura * comprimento
    print(f'A area de um terreno {larg} X {comp} é de {a}m2')
    
    
# programa principal
print(' Controle de Terrenos')
print('-' *20)
largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
area(largura, comprimento)
