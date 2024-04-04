
numeros_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro',
                       'cinco', 'seis', 'sete', 'oito',
                       'nove', 'dez', 'onze', 'doze', 'treze',
                       'quatorze', 'quinze', 'dezesseis',
                       'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    num = int(input('Digite um número entre 0 e 20: '))
    
    if 0 <= num <= 20:
        
        print(f'Você digitou o número {numeros_por_extenso[num]}')
        continua = str(input('Deseja continuar[S/N]? ')).upper()
        if continua == 'S':
            continue
        elif continua == 'N':
            break
        else:
            print('Opcao invalida')


