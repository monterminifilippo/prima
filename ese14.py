#importo il modulo math per poter utilizzare la funzione math.sqrt
import math
#importo il modulo os per poter utilizzare la funzione os._exit
import os

#chiedo l'inserimento del numero
n1=input('Inserire un numero (>0): ')
#con il try provo a trasformare il numero da str a int, per verificare che sia effettivamente int
#se lo converte significa che è int
try:
    in1=int(n1)
#se al contrario non lo converte e trova un errore stampa il messaggio
#e grazie alla funzione os._exit arresta l' esecuzione del programma
except ValueError:
    print("Non e' un intero!")
    os._exit(1)
#ora che ho controllato se è intero posso procedere nel
#controllare che il numero sia >0
if in1>0:
#se è >0
#calcolo la radice quadrata del numero grazie alla funzione math.sqrt
    rfN1=math.sqrt(in1)
#e stampo il risultato appena ottenuto trasfromandolo prima in str 
    print('radice quadrata: '+str(rfN1))
#altrimenti, se non è >0
else:
#stampo che non lo è
    print("Non e' > 0!")
