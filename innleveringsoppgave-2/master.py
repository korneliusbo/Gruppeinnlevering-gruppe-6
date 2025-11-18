print("Du har fått oppgaven å lede et prosjekt for å utvikle en medborgerportal.")
      
valg_tidslinje = {}

poeng = 0;

def vis_tidslinje():
    if not valg_tidslinje:
        print("\nIngen valg tatt enda.")
        return
    print("\nDin prosjekt tidslinje så langt:")
    for uke, valg in valg_tidslinje.items():
        print(f"{uke}: {valg}")

def valg_1():
    global poeng;
    print("\nSilje vs Sivert:")
    print(" 1. Plenum møte for å diskutere konflikten")
    print(" 2. Individuel Samtale")
   
    while True:
        valg = input("Velg '1', eller '2', eller '3', eller 4 for å åpne tidslinje:")
        if valg == '1':
            valg_tidslinje['Uke 1'] = "Plenum møte for å diskutere konflikten"
            print("Du har valgt å ta Plenum møte for å diskutere konflikten")
            poeng+=2;
            break
        elif valg == '2':
            valg_tidslinje['Uke 1'] = "Individuel Samtale"
            print("Du har valgt å ta Individuel Samtale")
            poeng += 3;
            break
        elif valg == '3':
            valg_tidslinje['Uke 1'] = "Skyve det under teppet"
            print("Du har valgt å Skyve det under teppet")
            poeng+=1;
            break
        elif valg == '4':
            vis_tidslinje()
        else:
            print("Ugyldig valg. Vennligst velg '1' eller '2'. ")
def valg_2():
    global poeng;
    print("\nHamdi vs Jabir:")
    print(" 1. La de være")
    print(" 2. Ta en sjefsavgjørelse selv.")
    print(" 3. Spørre flerebrukere. Velg demokratisk.")

    while True:
        valg = input("Velg '1', eller '2', eller '3', eller 4 for å åpne tidslinje: ")
        if valg == '1':
            valg_tidslinje['Uke 2'] = "La de være"
            print("Du har valgt å La de være")
            poeng+=1;
            break
        elif valg == '2':
            valg_tidslinje['Uke 2'] = "Ta en sjefsavgjørelse selv."
            print("Du har valgt å Ta en sjefsavgjørelse selv.")
            poeng += 2;
            break
        elif valg == '3':
            valg_tidslinje['Uke 2'] = "Spørre flere brukere. Velg demokratisk."
            print("Du har valgt å Spørre flere brukere. Velg demokratisk.")
            poeng += 3;
            break
        elif valg == '4':
            vis_tidslinje()
        else:
            print("Ugyldig valg. Vennligst velg '1' eller '2' eller '3'.")

def valg_3():
    global poeng;
    print("\nTeam motivasjon:")
    print(" 1. Motivational speech")
    print(" 2. Styr prosjektet med en jernhånd")
    print(" 3. Pizza party / Teambuilding")

    while True:
        valg = input("Velg '1', eller '2', eller '3',  eller 4 for å åpne tidslinje: ")
        if valg == '1':
            valg_tidslinje['Uke 3'] = "Motivational speech"
            print("Du har valgt Motivational speech")
            poeng += 2;
            break
        elif valg == '2':
            valg_tidslinje['Uke 3'] = "Styr prosjektet med en jernhånd"
            print("Du har valgt å Styre prosjektet med en jernhånd")
            poeng += 1;
            break
        elif valg == '3':
            valg_tidslinje['Uke 3'] = "Pizza party / Teambuilding"
            print("Du har valgtPizza party / Teambuilding")
            poeng +=3;
            break
        elif valg == '4':
            vis_tidslinje()
        else:
            print("Ugyldig valg. Vennligst velg '1' eller '2'.")

def slutt():
    global poeng
    print("\nSLUTTRESULTAT:")
    if poeng <= 3:
        print("Prototypen ble ikke levert. Failet prosjekt")
    elif 4 <= poeng <= 6:
        print("Prototypen ble levert men gruppen er fremdeles i stormingfasen")
    else:
        print("Prototypen ble levert og gruppen gikk videre til normingfasen")

    print("Takk for at du spilte!")

print("Velkommen til prosjektleder-simulatoren! \n Du vil ha mulighet til å ta valg som påvirker utfallet av prosjektet ditt, \nog kan åpne tidslinjen når som helst for å se dine tidligere valg.\n")
input("Trykk Enter for å starte...")
valg_1()
valg_2()
valg_3()
slutt()

vis_tidslinje()