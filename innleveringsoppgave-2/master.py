# ---------- Innlevering 2: Del 2 ----------
# ----- Storyline: Interaktiv historie -----
#=============================================


# Liste for tidslinje
valg_tidslinje = {}

# Poeng variabel
poeng = 0


# Funksjon for å vise tidslinje over tidligere valg
def vis_tidslinje():
    if not valg_tidslinje:
        print("\nIngen valg er registrert enda.")
        return
    print("\nProsjektets tidslinje:")
    for uke, valg in valg_tidslinje.items():
        print(f"{uke}: {valg}")


# ~~~~~~ Introduskjon ~~~~~~

print("-------------------------------------------------")

#Introduksjon
print("\33[1mVelkommen til Prosjektleder-simulatoren!\33[0m\n" # \33[1m = Starter bold text || \33[0m = Avslutter bold text
      "\nDu har fått oppgaven å lede et prosjekt for å utvikle en ny medborgerportal."
      "Her tar du valg som påvirker prosjektets fremgang og sluttresultat.\n"
      "Du kan når som helst vise tidslinjen for å se dine tidligere valg.\n")

# Starten
input("Trykk Enter for å starte...")


# ~~~~~~ Valg: Konflikt mellom Silje og Sivert ~~~~~~
# Konflikt 1: Silje vs. Sivert
def konflikt_silje_sivert():
    global poeng
    #Skriv introduksjon til dilemma her
    print("-------------------------------------------------")
    print("\33[1m\nKonflikt 1: \n Silje vs. Sivert\33[0m")
    print(" 1. Holde et felles møte for å diskutere konflikten")
    print(" 2. Ha individuelle samtaler")
    print(" 3. Ignorere situasjonen og håpe den løser seg selv")

    while True: # Uendelig løkke.
        valg = input("Velg 1, 2 eller 3 (eller 4 for å vise tidslinjen): ")
        if valg == '1':
            valg_tidslinje['Uke 1'] = "Felles møte for å løse konflikten"
            print("Du valgte å holde et felles møte.")
            poeng += 2
            break # Avslutter while-løkken (da input er gyldig)
        elif valg == '2':
            valg_tidslinje['Uke 1'] = "Individuelle samtaler for å håndtere konflikten"
            print("Du valgte å ha individuelle samtaler.")
            poeng += 3
            break # Avslutter while-løkken (da input er gyldig)
        elif valg == '3':
            valg_tidslinje['Uke 1'] = "Valgte å overse konflikten"
            print("Du valgte å ikke gripe inn i konflikten.")
            poeng += 1
            break # Avslutter while-løkken (da input er gyldig)
        elif valg == '4':
            vis_tidslinje()
        else:
            print("     \33[1m\nUgyldig valg. Prøv på nytt: \33[0m") # While-løkken gjør mulig for bruker å prøve på nytt uten å starte koden på nytt.


# ~~~~~~ Valg: Motivasjonsproblemer ~~~~~~

# Konflikt 2: Hamdi vs. Jabir
def konflikt_hamdi_jabir():
    global poeng
    #Introduksjon til dilemma her
    print("-------------------------------------------------")
    print("\33[1m\nKonflikt 2:\n Hamdi vs. Jabir\33[0m")
    print(" 1. La dem ordne opp selv")
    print(" 2. Ta en tydelig lederavgjørelse")
    print(" 3. Innhente tilbakemeldinger og ta en demokratisk avgjørelse")

    while True: # Uendelig løkke.
        valg = input("Velg 1, 2 eller 3 (eller 4 for å vise tidslinjen): ")
        if valg == '1':
            valg_tidslinje['Uke 2'] = "Lot konflikten utvikle seg på egenhånd"
            print("Du valgte å ikke gripe inn.")
            poeng += 1
            break # Avslutter while-løkken (da input er gyldig)
        elif valg == '2':
            valg_tidslinje['Uke 2'] = "Tok en tydelig lederavgjørelse"
            print("Du valgte å ta styringen i situasjonen.")
            poeng += 2
            break # Avslutter while-løkken (da input er gyldig)
        elif valg == '3':
            valg_tidslinje['Uke 2'] = "Tok en demokratisk avgjørelse basert på tilbakemeldinger"
            print("Du valgte å involvere flere og la gruppen bestemme.")
            poeng += 3
            break # Avslutter while-løkken (da input er gyldig)
        elif valg == '4':
            vis_tidslinje()
        else:
            print("     \33[1m\nUgyldig valg. Prøv på nytt: \33[0m") # While-løkken gjør mulig for bruker å prøve på nytt uten å starte koden på nytt.



# ~~~~~~ Valg: Motivasjon i teamet ~~~~~~

# Konflikt 3: Motivasjon i teamet
def motivasjon_teamet():
    global poeng
    print("-------------------------------------------------")
    print("\33[1m\nKonflikt 3:\n Team-motivasjon:\33[0m")
    print(" 1. Holde en motiverende pep-talk")
    print(" 2. Innføre strengere styring og tydelige rammer")
    print(" 3. Arrangere teambuilding med pizza og sosialt opplegg")

    # Uendelig løkke.
    while True:
        valg = input("Velg 1, 2 eller 3 (eller 4 for å vise tidslinjen): ")
        if valg == '1':
            valg_tidslinje['Uke 3'] = "Motiverende pep-talk"
            print("Du valgte å motivere teamet med en pep-talk.")
            poeng += 2
            break # Avslutter while-løkken (da input er gyldig)
        elif valg == '2':
            valg_tidslinje['Uke 3'] = "Streng og strukturert ledelse"
            print("Du valgte å stramme inn og lede mer strukturert.")
            poeng += 1
            break # Avslutter while-løkken (da input er gyldig)
        elif valg == '3':
            valg_tidslinje['Uke 3'] = "Teambuilding med pizza"
            print("Du valgte å arrangere sosial teambuilding.")
            poeng += 3
            break # Avslutter while-løkken (da input er gyldig)
        elif valg == '4':
            vis_tidslinje()
        else:
            print("     \33[1m\nUgyldig valg. Prøv på nytt: \33[0m") # While-løkken gjør mulig for bruker å prøve på nytt uten å starte koden på nytt.



# ~~~~~~ Resultat + Utfall ~~~~~~

# Avsluttning og resultat
def sluttresultat():
    global poeng
    print("-------------------------------------------------")
    print("\n\33[1mSLUTTRESULTAT:\33[0m")
    if poeng <= 3:
        print("Prototypen ble ikke levert. Prosjektet endte i store utfordringer.")
        # print("Utfall: Du trenger å utvikle dine ferdigheter som prosjektleder.")
    elif 4 <= poeng <= 6:
        print("Prototypen ble levert, men teamet befinner seg fortsatt i storming-fasen.")
        # print("Utfall: Du er en kompetent prosjektleder. Ditt team fungerer bra med rom for forbedring.")
    else:
        print("Prototypen ble levert, og teamet har tatt steget inn i norming-fasen.")
        # print("Utfall: Du er en eksepsjonell prosjektleder! Ditt team trives og leverer over forventning.")

    print("\nTakk for at du spillte!")




# Rekkefølge på call til funksjoner (legg rundt en enkel loop for restart)
def reset_game():
    """Nullstill spilltilstand for å starte historien på nytt."""
    global valg_tidslinje, poeng
    valg_tidslinje.clear()
    poeng = 0


while True:
    konflikt_silje_sivert()
    konflikt_hamdi_jabir()
    motivasjon_teamet()

    vis_tidslinje()

    sluttresultat()

    # Spør brukeren om de vil prøve på nytt (vises etter sluttresultat)
    exit_program = False
    while True:
        igjen = input("Vil du spille på nytt? Skriv '987' for ja, eller 'nei' for å avslutte: ").strip().lower()
        if igjen == '987':
            reset_game()
            print("\nStarter på nytt...\n")
            input("Trykk Enter for å fortsette...")
            break
        elif igjen == 'nei':
            print("\nAvslutter. Ha en fin dag!\n")
            exit_program = True
            break
        else:
            print("Ugyldig svar. Skriv '987' for ja eller 'nei' for å avslutte.")

    if exit_program:
        break
    else:
        continue


