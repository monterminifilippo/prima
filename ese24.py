import os

while True:
    h=input('Altezza: ') 
    flag=True
    try:
        ih=int(h)
    except ValueError:
        print(h+" non e' un intero!")
        flag=False
        continue
    if(ih<=0 or ih>9):
        print(h+" non e' compreso tra 1 e 9!")
        flag=False
    
    if flag:
            break
            
i=0
for riga in range(1,ih+1):
    for colonna in range(1,ih-riga+1):
        print(' ',end='')
    i=1
    for j in range(ih-riga+1,ih+1):
        print(str(i),end='')
        i=i+1
    i=riga-1
    for j in range(ih-riga+2,ih+1):
        print(str(i),end='')
        i=i-1
    print('\n',end='')

            






