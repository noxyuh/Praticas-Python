
def leiaInt(num="Erro. numero invalido"):
        print(num)

n = input("Número: ").strip()

if n.isnumeric():
    n = int(n)
    if n == 0:
        leiaInt("Erro. numero  invalido")
    else:
        leiaInt(n)
else:
    leiaInt()
    
    
    
        
    

