def notas(*n, sit= False):
    dicionario = {}
    dicionario['total'] = len(n)
    dicionario['maior'] = max(n)
    dicionario['menor'] = min(n)
    dicionario['media'] = sum(n)/ len(n)
    if sit:
        if dicionario['media'] >= 7:
            dicionario['situaçao'] = 'BOA'
        elif dicionario['media'] >= 5:
            dicionario['situaçao'] = 'RAZOAVEL'
        else:
            dicionario['situaçao'] = 'RUIM'
        return dicionario
resp = notas(5.5, 4.6, 7.8, sit=True)
print(resp)
            
   
    

    


