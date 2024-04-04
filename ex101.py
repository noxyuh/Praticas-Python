def voto(ano):
    idade =  2024 - ano
    print(idade)
    if idade < 15:
        return 'Voto NEGADO!'
    elif idade >= 16 and idade < 18:
        return 'Voto OPCIONAL!'
    elif idade > 18 and idade <= 70:
        return 'Voto OBRIGATORIO!'
    else:
        return 'Voto OPCIONAL!'
    
        
        


ano_nascimento = int(input('Digite seu ano de nascimento: '))
resultado = voto(ano_nascimento)
print(resultado)
