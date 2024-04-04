
'''largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura
print(area)
resul = area / 2
print(resul)

produto = float(input('Digite o valor de um produto: '))
des = produto * 5 /100
resul = produto - des
print(f'O valor do produto foi {produto}, o desconto aplicado de 5% foi de {des}, gerando um valor final de {resul}.')

salario = float(input('Digite o salaro de um funcionario: '))
aumento = salario * 0.15
novosalario = salario + aumento
print(novosalario)


n = float(input('Digite um numero em metros: '))
dm = n * 10
cm = n * 100
mm = n * 1000
dam = n / 10
hm = n / 100
km =  n / 1000

print(f'O valor de {n}m em decimetro é {dm}')
print(f'O valor de {n}m em centrimetro é {cm}')
print(f'O valor de {n}m em minimetro é {mm}')
print(f'O valor de {n}m em dam é {dam}')
print(f'O valor de {n}m em hm é {hm}')
print(f'O valor de {n}m em km é {km}')
'''
'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
'''
def contador (i,f,p):
    """
    
    
    
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c+=p
    print('Fim!')
help(contador)
 
