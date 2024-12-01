reddito = -1
while reddito < 0:
    reddito = float(input("Inserisci il tuo reddito: "))
imposta = 0
a1 = 0.12
a2 = 0.18
a3 = 0.27
a4 = 0.48
a5 = 0.60
if reddito > 100000:
    imposta = (reddito - 100000) * a5
    print("Imposta totale di:")
    print (imposta)
elif 60000 < reddito <= 100000:
    imposta = (reddito - 60000) * a4
    print("Imposta totale di:")
    print (imposta)
elif 35000 < reddito <= 60000:
    imposta = (reddito - 35000) * a3
    print("Imposta totale di:")
    print (imposta)
elif 20000 < reddito <= 35000:
    imposta = (reddito - 20000) * a2
    print("Imposta totale di:")
    print (imposta)
elif 10000 < reddito <= 20000:
    imposta = (reddito - 10000) * a1
    print("Imposta totale di:")
    print (imposta)