
num = int(input('Digite um numero: '))
    
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print('Nao é um numero primo!')
            break
    else:
        print('É um numero primo')
else:
    print('Nao é um numero primo')

