ano_nascimento = int(input('Digite seu ano de nascimento: '))
idade =  2023 - ano_nascimento 
if idade <18 :
    tempo_que_falta = (idade - 18) *12
    print('Voce ainda vai se alistar!')
    print(f'Falta {tempo_que_falta} para voce se alistar!')
elif idade == 18:
    print('É hora de se alistar!')
elif idade > 18:
    print('Já passou do tempo de se alistar!')