#richiedo l' inserimento del primo numero facendolo inserire sotto con lo \n
v1=input('Inserire primo valore (reale): \n')
#trasformo il valore appena inserito in float
f1=float(v1)
#faccio lo stesso ma con il secondo valore
v2=input('Inserire secondo valore (reale): \n')
f2=float(v2)
#calcolo l' operazione richiesta
ris=(f1+f2)/(f1-f2)
#ora stampo l' operazione con il risultato calcolato prima alla fine trasfromando tutti i valori in str per poterli far cmparire a video
print('('+str(f1)+'+'+str(f2)+') / ('+str(f1)+'-'+str(f2)+') = '+str(ris))