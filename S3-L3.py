import math

def perimetro_quadrato(lato):
    return lato * 4

def perimetro_cerchio(raggio):
    return 2 * math.pi * raggio

def perimetro_rettangolo(base, altezza):
    return base * 2 + altezza * 2

scelta = input("Scegli una figura tra: quadrato, cerchio, rettangolo): ")

if scelta == "quadrato":
    lato = float(input("Inserisci il lato del quadrato: "))
    perimetro = perimetro_quadrato(lato)
    print(f"Il perimetro del quadrato è: {perimetro}")
elif scelta == "cerchio":
    raggio = float(input("Inserisci il raggio del cerchio: "))
    perimetro = perimetro_cerchio(raggio)
    print(f"La circonferenza del cerchio è: {perimetro}")
elif scelta == "rettangolo":
    base = float(input("Inserisci la base del rettangolo: "))
    altezza = float(input("Inserisci l'altezza del rettangolo: "))
    perimetro = perimetro_rettangolo(base, altezza)
    print(f"Il perimetro del rettangolo è: {perimetro}")
else:
    print("Scelta errata")