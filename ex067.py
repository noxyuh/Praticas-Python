cont = mult = 0
while True:
    num = int(input('Escolha um numero para a tabuada: '))
    if num < 0:
        print("PROGRAMA ENCERRADO. NÚMERO INVÁLIDO")
        break    
    cont  = 1 
    while cont  <= 10:
        resultado = num * cont
        print(f"{num} x {cont} = {resultado}")

        cont  += 1
        