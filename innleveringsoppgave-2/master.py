print("Du har fått oppgaven å lede et prosjekt for å utvikle en ny medborgerportal.")

valg_tidslinje = {}
poeng = 0

def vis_tidslinje():
    if not valg_tidslinje:
        print("\nIngen valg er registrert enda.")
        return
    print("\nProsjektets tidslinje:")
    for uke, valg in valg_tidslinje.items():
        print(f"{uke}: {valg}")

def konflikt_silje_sivert():
    global poeng
    print("\nKonflikt 1: Silje vs. Sivert")
    print(" 1. Holde et felles møte for å diskutere konflikten")
    print(" 2. Ha individuelle samtaler")
    print(" 3. Ignorere situasjonen og håpe den løser seg selv")

    while True:
        valg = input("Velg 1, 2 eller 3 (eller 4 for å vise tidslinjen): ")
        if valg == '1':
            valg_tidslinje['Uke 1'] = "Felles møte for å løse konflikten"
            print("Du valgte å holde et felles møte.")
            poeng += 2
            break
        elif valg == '2':
            valg_tidslinje['Uke 1'] = "Individuelle samtaler for å håndtere konflikten"
            print("Du valgte å ha individuelle samtaler.")
            poeng += 3
            break
        elif valg == '3':
            valg_tidslinje['Uke 1'] = "Valgte å overse konflikten"
            print("Du valgte å ikke gripe inn i konflikten.")
            poeng += 1
            break
        elif valg == '4':
            vis_tidslinje()
        else:
            print("Ugyldig valg. Velg 1, 2 eller 3.")

def konflikt_hamdi_jabir():
    global poeng
    print("\nKonflikt 2: Hamdi vs. Jabir")
    print(" 1. La dem ordne opp selv")
    print(" 2. Ta en tydelig lederavgjørelse")
    print(" 3. Innhente tilbakemeldinger og ta en demokratisk avgjørelse")

    while True:
        valg = input("Velg 1, 2 eller 3 (eller 4 for å vise tidslinjen): ")
        if valg == '1':
            valg_tidslinje['Uke 2'] = "Lot konflikten utvikle seg på egenhånd"
            print("Du valgte å ikke gripe inn.")
            poeng += 1
            break
        elif valg == '2':
            valg_tidslinje['Uke 2'] = "Tok en tydelig lederavgjørelse"
            print("Du valgte å ta styringen i situasjonen.")
            poeng += 2
            break
        elif valg == '3':
            valg_tidslinje['Uke 2'] = "Tok en demokratisk avgjørelse basert på tilbakemeldinger"
            print("Du valgte å involvere flere og la gruppen bestemme.")
            poeng += 3
            break
        elif valg == '4':
            vis_tidslinje()
        else:
            print("Ugyldig valg. Velg 1, 2 eller 3.")

def motivasjon_teamet():
    global poeng
    print("\nTeam-motivasjon:")
    print(" 1. Holde en motiverende pep-talk")
    print(" 2. Innføre strengere styring og tydelige rammer")
    print(" 3. Arrangere teambuilding med pizza og sosialt opplegg")

    while True:
        valg = input("Velg 1, 2 eller 3 (eller 4 for å vise tidslinjen): ")
        if valg == '1':
            valg_tidslinje['Uke 3'] = "Motiverende pep-talk"
            print("Du valgte å motivere teamet med en pep-talk.")
            poeng += 2
            break
        elif valg == '2':
            valg_tidslinje['Uke 3'] = "Streng og strukturert ledelse"
            print("Du valgte å stramme inn og lede mer strukturert.")
            poeng += 1
            break
        elif valg == '3':
            valg_tidslinje['Uke 3'] = "Teambuilding med pizza"
            print("Du valgte å arrangere sosial teambuilding.")
            poeng += 3
            break
        elif valg == '4':
            vis_tidslinje()
        else:
            print("Ugyldig valg. Velg 1, 2 eller 3.")

def sluttresultat():
    global poeng
    print("\nSLUTTRESULTAT:")
    if poeng <= 3:
        print("Prototypen ble ikke levert. Prosjektet endte i store utfordringer.")
    elif 4 <= poeng <= 6:
        print("Prototypen ble levert, men teamet befinner seg fortsatt i storming-fasen.")
    else:
        print("Prototypen ble levert, og teamet har tatt steget inn i norming-fasen.")

    print("Takk for at du spilte!")

print("Velkommen til Prosjektleder-simulatoren!\n"
      "Her tar du valg som påvirker prosjektets fremgang og sluttresultat.\n"
      "Du kan når som helst vise tidslinjen for å se dine tidligere valg.\n")

input("Trykk Enter for å starte...")

konflikt_silje_sivert()
konflikt_hamdi_jabir()
motivasjon_teamet()

vis_tidslinje()

sluttresultat()


