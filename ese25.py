import math

while True:
    x=input('inserire un intero >0: ')
    flag=True
    try:
        ix=int(x)
    except ValueError:
        print(x+" non e' un intero!")
        flag=False
        continue
        
    if(in1<=0):
        print(x+" non e' > 0!")
        flag=False

    if flag:
            break

x=n 
c=0
while x>0:
    x=x//10
    c=c+1
acc=n
i=c 
while i>0:
    v=accx/math.pow(10.,i-1)
    print(str(int(v))+' ',end='')
    j=0
    while j<v:
        print('*',end='')
        j=j+1
    print('\n',end='')
    acc%=int(math.pow(10.,i-1)
    i=i-1