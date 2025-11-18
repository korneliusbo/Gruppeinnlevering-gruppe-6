#Introduksjonstekst
print("Du har fått oppgaven å lede et prosjekt for å utvikle en medborgerportal.")
      
# Lagre valgene i en tidslinje
valg_tidslinje = {}

# Funksjon for å vise tidslinjen
def vis_tidslinje():
    if not valg_tidslinje:
        print("\nIngen valg tatt enda.")
        return
    print("\nDin prosjekt tidslinje så langt:")
    for uke, valg in valg_tidslinje.items():
        print(f"{uke}: {valg}")

# Funksjon for første valg
def valg_1():
    print("Du står overfor to valg:")
    print(" 1. Komme i gang så fort som mulig")
    print(" 2. Fokusere på å skape sosiale bånd mellom gruppemedlemmene\n")
   
    while True:
        valg = input("Velg '1', eller '2', eller 3 for å åpne tidslinje: ")
        if valg == '1':
            valg_tidslinje['Uke 1'] = "Komme i gang så fort som mulig"
            print("Du har valgt å komme i gang så fort som mulig. \n")
            break
        elif valg == '2':
            valg_tidslinje['Uke 1'] = "Fokusere på å skape sosiale bånd mellom gruppemedlemmene"
            print("Du har valgt å fokusere på å skape sosiale bånd mellom gruppemedlemmene. \n")
            break
        elif valg == '3':
            vis_tidslinje()
        else:
            print("Ugyldig valg. Vennligst velg '1' eller '2'. \n")

# Funksjon for andre valg
def valg_2():
    print("Nå må du bestemme hvordan dere skal fordele arbeidsoppgaver:")
    print(" 1. Fordele oppgaver basert på individuelle styrker")
    print(" 2. La alle prøve seg på forskjellige oppgaver\n")
   
    while True:
        valg = input("Velg '1', eller '2', eller 3 for å åpne tidslinje: ")
        if valg == '1':
            valg_tidslinje['Uke 2'] = "Fordele oppgaver basert på individuelle styrker"
            print("Du har valgt å fordele oppgaver basert på individuelle styrker.")
            break
        elif valg == '2':
            valg_tidslinje['Uke 2'] = "La alle prøve seg på forskjellige oppgaver"
            print("Du har valgt å la alle prøve seg på forskjellige oppgaver.")
            break
        elif valg == '3':
            vis_tidslinje()
        else:
            print("Ugyldig valg. Vennligst velg '1' eller '2'.")


# start interaktiv historie
print("Velkommen til prosjektleder-simulatoren! \n Du vil ha mulighet til å ta valg som påvirker utfallet av prosjektet ditt, \nog kan åpne tidslinjen når som helst for å se dine tidligere valg.\n")
input("Trykk Enter for å starte...")
valg_1()
valg_2()
vis_tidslinje()