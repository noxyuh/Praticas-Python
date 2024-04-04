
num = [[], []]
numero = 0
for i in range(1,8):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        num[0].append(numero)
        
    else:
        num[1].append(numero)
num[0].sort()
num[1].sort()
print(num[0])
print(num[1])

       
    
    