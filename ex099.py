from time import sleep
def maior(*m):
    cont = maior = 0
    print('-=' *20)
    print('Analisando os valores passados...')
    print(f'{m} foram informados {len(m)} ao todos.')
    sleep(0.3)
    print(f'O maior valor informado foi {max(m)}')
    
    
maior(9, 7, 8, 2, 5, 3, 6)
maior(7,4,6)
maior(1,2)
maior(6)
maior(0)


