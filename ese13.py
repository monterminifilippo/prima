#richiedo la base e la trasformo in float
b=input('Inserire la base: ')
fB=float(b)
#faccio lo stesso con l'esponente
e=input("Inserire l'esponente: ")
fE=float(e)
#calcolo la potenza grazie alla funzione pow(),dove metto come primo numero la base e come secondo l'esponente
ris=pow(fB,fE)
#infine stampo il risultato trasformando il risultato in str
print('b^e: '+str(ris))