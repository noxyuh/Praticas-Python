n = int(input('Digite um numero: '))

seq1 = 1
seq2 = 1

cont = 2
while cont < n:
    s = (seq1 + seq2)
    print(s) 
    seq1 = seq2
    seq2 = s
    cont += 1