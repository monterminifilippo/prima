#chiedo l' inserimento dell' eta'
eta=input("Inserire gli anni di eta': ")
#calcolo la sua eta' in ore moltiplicando il numero di ore in un giorno x365
#e trasfromando l' eta' inserita prima in int per usarla nel calcolo
etaOre=(24*365)*int(eta)
#stampo il risultato dell' operazione trasfromandolo prima in str
print("La tua eta' in ore e': "+str(etaOre))