import math

#chiedo l' inserimento la prima coppia di coordinate
x1=input('inserire x1: ')
y1=input('inserire y1: ')
#li mostro a video senza convertirli prima in str perchè non li ho trasformati in int prima
print('primo punto: ('+x1+', '+y1+')')
#ora faccio la stessa cosa ma con la seconda coppia
x2=input('inserire x2: ')
y2=input('inserire y2: ')
print('primo punto: ('+x2+', '+y2+')')
#li trasfromo tutti in float per poterli utilizzare nei calcoli
fx1=float(x1)
fy1=float(y1)
fx2=float(x2)
fy2=float(y2)
#calcolo la distanza euclidea tra i due punti:
#radice di (x2-x1) alla seconda + (y2-y1) alla seconda
#parto dal calcolare le due sottrazioni
s1=fx2-fx1
s2=fy2-fy1
#ora le elevo alla seconda grazie alla funzione pow, mettendo prima il numero da elevare e poi quello che dice per quanto elevarlo
ps1=pow(s1,2)
ps2=pow(s2,2)
#ora li sommo
somma=ps1+ps2
#infine metto la somma appena ottenuta sotto radice quadrata utilizzando la funzione math.sqrt
d=math.sqrt(somma)
#stampo quindi il risultato della distanza mettondolo str
print('distanza Euclidea: '+str(d))