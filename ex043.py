peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura **2)

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25.0:
    print('Peso ideal')
elif imc  >= 25.0 and imc < 30.0:
    print('Sobrepeso')
elif imc >= 20.0 and imc < 40.0:
    print('Obesidade')
else:
    print('Obesidade morbida')
print(imc)