# ---------- Innlevering 2: Del 2 ----------
# ----- Storyline: Interaktiv historie -----
#=============================================

#¤¤¤¤¤¤-Kommandoer-¤¤¤¤¤¤

# scorevariabel
score = 0

#-Trykk enter for å fortsette-
def trykk_enter():
    input("\nFor å fortsette trykk 'enter'...")
    print("")

# Enklere å forholde seg til, istedet for å skrive flere ganger.
    #-Valg alternativene for del 1- 
valg_1_1 = "Individuelle samtaler for å dempe temperaturen."
valg_2_1 = "Ta det opp i plenum."
valg_3_1 = "Unngå avgjørelse enn så lenge."

    #-Valg alternativene for del 2- 
valg_1_2 = "La dem være og løse de sin konflikten selv."
valg_2_2 = "Ta en sjefsavgjørelse for dem."
valg_3_2 = "Ha demokrati valg i gruppen."

    #-Valg alternativene for del 3- 
valg_1_3 = "Hold en motiverende tale."
valg_2_3 = "Styr prosjektet med en jernhånd."
valg_3_3 = "Team-building og pizzaa."

#¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤

# ~~~~~~ Introduskjon ~~~~~~
print("-------------------------------------------------")
print("\nDu er Erling, prosjektleder for et team.\n\nDin oppgave er å løse konflikter som oppstår under prosjektet." \
"\nGjennom denne storylinen, hvert valg du tar opptjener poeng. På slutten får du vite hvordan du klarte deg som prosjektleder.")
trykk_enter()

# ~~~~~~ Bakgrunn: Konflikt mellom Silje og Sivert ~~~~~~
print("-------------------------------------------------")
print("\33[1mKonflikt 1: \nSilje og Sivert\33[0m") # \33[1m = Starter bold text || \33[0m = Avslutter bold text
print("\n*Konflikt kommer..*") #Tar ikke med konflikt tekst for nå, fokuserer på oppbyggingen av koden.
trykk_enter()

print("\n*Kort forklart hva konflikten er?*")
trykk_enter()

# ~~~~~~ Valg: Konflikt mellom Silje og Sivert ~~~~~~
print("-------------------------------------------------")
print("\nTiden er kommet for å ta et valg!"
    #"\n\t1. Individuelle samtaler for å dempe temperaturen."
    #"\n\t2. Ta det opp i plenum."
    #"\n\t3. Unngå avgjørelse enn så lenge.")
    f"\n  1. {valg_1_1}"
    f"\n  2. {valg_2_1}"
    f"\n  3. {valg_3_1}")

while True: # Uendelig løkke.
    avgjørelse1 = input("\nHvordan vil du løse konflikten mellom Silje og Sivert?"
"\nSkriv valget ditt (1, 2, eller 3): ") #Spør brukeren hvilket valg de vil ta.

    if avgjørelse1 == "1":
        print("\nDu velger å snakke indivudelt med Silje og Sivert.")
        print("*Resultat av avgjørelsen*")
        score += 2 # Legger til poeng for valget. (Valg 1 gir 2 poeng)
        break # Avslutter while-løkken (da input er gyldig)
    elif avgjørelse1 == "2":
        print(f"\nDu velger å {valg_2_1}")
        print("*Resultat av avgjørelsen*")
        score += 1 # Legger til poeng for valget. (Valg 2 gir 1 poeng)
        break # Avslutter while-løkken (da input er gyldig)
    elif avgjørelse1 == "3":
        print(f"\nDu velger å {valg_3_1}")
        print("*Resultat av avgjørelsen*")
        score += 0 # Legger til poeng for valget. (Valg 3 gir 0 poeng)
        break # Avslutter while-løkken (da input er gyldig)
    else:
        print("     \33[1mUgyldig input. Prøv på nytt: \33[0m") # While-løkken gjør mulig for bruker å prøve på nytt uten å starte koden på nytt.

trykk_enter()

# ~~~~~~ Bakgrunn: Konflikt mellom Hamdi og Jabir ~~~~~~
print("-------------------------------------------------")
print("\33[1mKonflikt 2: \nHamdi og Jabir\33[0m") # \33[1m = Starter bold text || \33[0m = Avslutter bold text
print("\n*Konflikt kommer..*") #Tar ikke med konflikt tekst for nå, fokuserer på oppbyggingen av koden.
trykk_enter()

print("\n*Kort forklart hva konflikten er?*")
trykk_enter()

# ~~~~~~ Valg: Konflikt mellom Hamdi og Jabir ~~~~~~
print("-------------------------------------------------")
print("\nTiden er kommet for å ta et valg!"
    f"\n  1. {valg_1_2}"
    f"\n  2. {valg_2_2}"
    f"\n  3. {valg_3_2}")

while True: # Uendelig løkke.
    avgjørelse2 = input("\nHvordan vil du løse konflikten mellom Silje og Sivert?"
"\nSkriv valget ditt (1, 2, eller 3): ") #Spør brukeren hvilket valg de vil ta.

    if avgjørelse2 == "1":
        print(f"\nDu velger å {valg_1_2}")
        print("*Resultat av avgjørelsen*")
        score += 0 # Legger til poeng for valget. (Valg 1 gir 0 poeng)
        break # Avslutter while-løkken (da input er gyldig)
    elif avgjørelse2 == "2":
        print(f"\nDu velger å {valg_2_2}")
        print("*Resultat av avgjørelsen*")
        score += 1 # Legger til poeng for valget. (Valg 2 gir 2 poeng)
        break # Avslutter while-løkken (da input er gyldig)
    elif avgjørelse2 == "3":
        print(f"\nDu velger å {valg_3_2}")
        print("*Resultat av avgjørelsen*")
        score += 2 # Legger til poeng for valget. (Valg 3 gir 2 poeng)
        break # Avslutter while-løkken (da input er gyldig)
    else:
        print("     \33[1mUgyldig input. Prøv på nytt: \33[0m") # While-løkken gjør mulig for bruker å prøve på nytt uten å starte koden på nytt.

trykk_enter()

# ~~~~~~ Bakgrunn: Motivasjonsproblemer ~~~~~~
print("-------------------------------------------------")
print("\33[1mKonflikt 3: \nMotivasjonsproblemer\33[0m") # \33[1m = Starter bold text || \33[0m = Avslutter bold text
print("\n*Konflikt kommer..*") #Tar ikke med konflikt tekst for nå, fokuserer på oppbyggingen av koden.
trykk_enter()

print("\n*Kort forklart hva motivasjonsproblemene er?*")
trykk_enter()

# ~~~~~~ Valg: Motivasjonsproblemer ~~~~~~
print("-------------------------------------------------")
print("\nTiden er kommet for å ta et valg!"
    f"\n  1. {valg_1_3}"
    f"\n  2. {valg_2_3}"
    f"\n  3. {valg_3_3}")

while True: # Uendelig løkke.
    avgjørelse2 = input("\nHvordan vil du løse konflikten mellom Silje og Sivert?"
"\nSkriv valget ditt (1, 2, eller 3): ") #Spør brukeren hvilket valg de vil ta.

    if avgjørelse2 == "1":
        print(f"\nDu velger å {valg_1_3}")
        print("*Resultat av avgjørelsen*")
        score += 1 # Legger til poeng for valget. (Valg 1 gir 1 poeng)
        break # Avslutter while-løkken (da input er gyldig)
    elif avgjørelse2 == "2":
        print(f"\nDu velger å {valg_2_3}")
        print("*Resultat av avgjørelsen*")
        score += 0 # Legger til poeng for valget. (Valg 2 gir 0 poeng)
        break # Avslutter while-løkken (da input er gyldig)
    elif avgjørelse2 == "3":
        print(f"\nDu velger å {valg_3_3}")
        print("*Resultat av avgjørelsen*")
        score += 2 # Legger til poeng for valget. (Valg 3 gir 2 poeng)
        break # Avslutter while-løkken (da input er gyldig)
    else:
        print("     \33[1mUgyldig input. Prøv på nytt: \33[0m") # While-løkken gjør mulig for bruker å prøve på nytt uten å starte koden på nytt.

trykk_enter()


# ~~~~~~ Resultat + Utfall ~~~~~~
print("-------------------------------------------------")
print("\33[1mResultat og Utfall\33[0m") # \33[1m = Starter bold text || \33[0m = Avslutter bold text
print("\n*Forklaring av resultat og utfall kommer*") #Tar ikke med konflikt tekst for nå, fokuserer på oppbyggingen av koden.
trykk_enter()

print(f"\n\33[1mDin totale poengsum er: {score}/6.\33[0m")
if score == 6: # Høyeste sum. '==' må ha 6 poeng for å få høyest utfall.
    print("Utfall: Du er en eksepsjonell prosjektleder! Ditt team trives og leverer over forventning.")
elif score >= 4: # Mellomliggende sum. '>=' må ha minst 4 poeng for å få middels utfall.
    print("Utfall: Du er en kompetent prosjektleder. Ditt team fungerer bra med rom for forbedring.")
else: # Laveste sum. Alt under 4 poeng får laveste utfall.

    print("Utfall: Du har utfordringer som prosjektleder. Vurder å utvikle dine lederegenskaper for bedre teamdynamikk.")
