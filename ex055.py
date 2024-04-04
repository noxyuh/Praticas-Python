maior_peso = 0
menor_peso = float('inf')

for i in range(1,6):
    peso = float(input('Digite seu peso: '))
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
print(f"O maior peso é {maior_peso} kg e o menor peso é {menor_peso} kg.")

'''
m=0
i= 0
for c in range(1,8):
  ano= int(input(f'Digite o ano de nascimento: '))
  soma=2023-ano
  if soma <18:
    i += 1
  elif soma>= 18 :
        m += 1
print(f'Você informou {i}  pessoas que nao atigiram a ideda de 18 ou maior que dezoito.')
print(f'Você informou {m}  pessoas que  atigiram a ideda de 18 ou maior que dezoito.')

'''