import time
num = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

opcao = 0
while opcao < 5:
    print('=-'*10)    
    print('[1]somar')
    print('[2]multiplicar')
    print('[3]maior')
    print('[4]novos numeros')
    print('[5]sair do programa')
    opcao = int(input('Escolha uma opçao: '))
    if opcao == 1:
        soma = num + num2
        print('A soma entre os numeros é de', soma)
    elif opcao == 2:
        mult = num * num2
        print('A o resultado da multiplicaçao é', mult)
    elif opcao == 3:
        if num > num2:
            print('O maior numero é', num)
        else:
            print('O maior numero é', num2)
    elif opcao == 4:
        num = int(input('Digite um valor: '))
        num2 = int(input('Digite outro valor: '))
    elif opcao == 5:
        print('Voce escolheu sair do programa!')
        print('Saindo...')
        time.sleep(2)
        print('Obrigado! tenha um bom dia.')
    else:
        print('Opcao invalida! Tente novamente.')