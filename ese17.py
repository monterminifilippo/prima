#importo il modulo os per poter utilizzare la funzione os._exit
import os
#importo il modulo math per utilizzare la funzione math.sqrt
import math
#chiedo l'inserimento dei 3 numeri interi
n1=input('Inserire primo numero intero: ')
n2=input('Inserire secondo numero intero: ')
n3=input('Inserire terzo numero intero: ') 
#controllo che tutti 3 siano interi con il try
try:
    in1=int(n1)
    in2=int(n2)
    in3=int(n3)
#con l'except scrivo che devono essere inseriti 3 numeri interi e interromp l' esecuzione
except ValueError:
    print('Devi inserire 3 numeri interi!')
    os._exit(1)
#controllo ora quale dei 3 numeri è il maggiore
#se il primo è maggiore del secondo
if(in1>in2):
    #ed è anche maggiore del terzo
    if(in1>in3):
        #allora scrivo che il primo è il maggiore
        print('maggiore: '+str(in1))    
    else:
        #altrimenti il maggiore è il terzo
        print('maggiore: '+str(in3))
#se invece il secondo è maggiore del primo
else:
    #ed è anche maggiore del terzo
    if(in2>in3):
        #il maggiore ora è il secondo
        print('maggiore: '+str(in2))
    #altrimenti è il terzo
    else:
        print('maggiore: '+str(in3))
#ora invece controllo il minore con lo stesso procedimento
if(in1<in2):
    if(in1<in3):
        print('minore: '+str(in1))
    else:
        print('minore: '+str(in3))
else:
    if(in2<in3):
        print('minore: '+str(in2))
    else:
        print('minore: '+str(in3))
#calcolo la somma dei 3 numeri per calcolare la media
somma=in1+in2+in3
#calcolo ora la media facendo la somma diviso 3
media=somma/3
#stampo il risultato trasformandolo in str
print('media aritmetica:\n'+str(media))
#calcolo la radice quadrata grazie alla funzione math.sqrt
radice=math.sqrt(somma)
#ed infine la stampo
print('radice della somma:\n'+str(radice))