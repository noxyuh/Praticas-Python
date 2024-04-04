cont_prod = 0
soma = 0
produto_barato = ''
print('-'*30)
print('     LOJA SUPER BARATÃO')
print('-'*30)
primeiro_produto = True
while True:
    nome_produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    soma += preco
    if preco > 1000:
        cont_prod += 1
        
    if primeiro_produto:
        preco_min = preco
        produto_barato = nome_produto
        primeiro_produto = False
    elif preco < preco_min:
        preco_min = preco
        produto_barato = nome_produto
    
     
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue
    else:
        print('invalido')
print('--------------FIM DO PROGRAMA------------------')
print('O total da compra foi de R$', soma)        
print(f'Temos {cont_prod} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produto_barato} que custa R${preco_min:.2f}')
