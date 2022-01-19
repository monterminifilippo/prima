#importo il modulo os per poter utilizzare la funzione os._exit
import os

#chiedo l' inserimento del valore del mese
n1=input('Inserire mese (valore tra 1 e 12): ')
#ora controllo che il valore del mese sia un numero intero, in caso contrario chiudo il programma 
try:
    in1=int(n1)
except:
    print("Non e' un intero!")
    os._exit(1)
    
#ora controllo che sia compreso nell' intervallo [1,12]
if(in1<1 or in1>12):
    print('Valore non valido!')
    os._exit(1)
#chiedo l' inserimento del valore del giorno
n2=input('Inserire giorno del mese: ')
#ora controllo che il valore del giorno sia un numero intero, in caso contrario chiudo il programma 
try:
    in2=int(n2)
except:
    print("Non e' un intero!")
    os._exit(1)
#ora controllo che quel giorno di quel mese esista effettivamente
if((in1==2 and in1>29) or 
  ((in1==11 or in1==4 or in1==6 or in1==9) and in2>30) or 
  ((in1!=2 or in1!=11 or in1!=4 or in1!=6 or in1!=9) and in2>31)):
   print('Valore non valido!')
   os._exit(1)
    
    
#ora controllo il resto dei mesi per dire di che stagione si tratta
if(in1>=1 and in1<=2):
    print('Inverno')
if in1==3:
    if in2<21:
        print('Inverno')
    else:
        print('Primavera')
if(in1>=4 and in1<=5):
    print('Primavera')
if in1==6:
    if in2<21:
        print('Primavera')
    else:
        print('Estate')
if(in1>=7 and in1<=8):
    print('Estate')
if in1==9:
    if in2<23:
        print('Estate')
    else:
        print('Autunno')
if(in1>=10 and in1<=11):
    print('Autunno')
if in1==12:
    if in2<21:
        print('Autunno')
    else:
        print('Inverno')
        
        
        
        


