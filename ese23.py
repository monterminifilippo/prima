import os

#chiedo l'inserimento dei due lati controllando sempre se è intero
a=input('Lato a: ')
try:
    ia=int(a)
except ValueError:
    print("Non e' un intero!")
    os._exit(1)
b=input('Lato b: ')
try:
    ib=int(b)
except ValueError:
    print("Non e' un intero!")
    os._exit(1)
    
#finchè la riga in cui siamo è tra 0 e b il ciclo verrà ripetuto
for riga in range(0,ib):
    #se siamoin riga 0 o a b-1
    if(riga==0 or riga==(ib-1)):
        #stampo tutta la colonna  è tra 0 e a
        for colonna in range(0,ia):
            # non andando a capo ogni volta
            print('* ',end='')
        #tranne alla fine
        print('\n',end='')
    #altrimenti 
    else:
        #quando la colonna è tra e a
        for colonna in range(0,ia):
            #ed è la numero 0 o a-1 
            if (colonna==0 or colonna==(ia-1)):
                #scrivo un asterisco
                print('* ',end='')
            else:
                #altrimenti uno spazio vuoto
                print('  ',end='')
        print('\n',end='')         