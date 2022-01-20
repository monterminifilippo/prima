#con questo while true dico che il ciclo viene ripetuto fino a quando
#è corretto,in questo caso che il valore sia giusto
while True:
    n1=input('valore intero: ')
    #inizializzo un flag che rimane true quand l' utente inserisce un
    #valore intero 
    flag=True
    #controllo se il valore inserito è intero 
    try:
        in1=int(n1)
    except ValueError:
        print(n1+" non e' un intero!")
        #se non è intero mette il flag false 
        flag=False
        continue
        
    if(in1<=0):
        print(str(in1)+"non e' > 0!")
        flag=False
    
    #fino a quando il flag resta false il ciclo continua, quando diventa
    #true uscirà interrompendolo con il break, in questo caso con if flag
    #e come se scrivessi if flag==true
    if flag:
            break

#grazie ad un ciclo while fino a quando il valore inserito è maggiore di 0
#stampo a video un asterisco, diminuendo di uno il valore ogni volta
while(in1>0):
    #grazie a quell' end=''evita di andare a capo ogni volta
    print('*',end='')
    in1=in1-1
#infine, andando a capo per interrompere l' uso dell' end, scrivo finito
print('\nfinito')