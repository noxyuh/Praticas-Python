def ficha(nome='desconhecido', gols=0):
    
   
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'
    
    
    
jogador = str(input('Nome do Jogador: '))
gols = int(input('Numero de Gols: '))
resultado = ficha(jogador, gols)
print(resultado)

    
    
    
    