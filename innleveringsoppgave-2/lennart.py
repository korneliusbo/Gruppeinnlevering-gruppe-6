


print("Velkommen til den interaktive historien!")
print("Hjelp Erling å finne de beste løsningene.\n")


poeng = 0

def konflikt_1():
    print("VALG 1: Det har oppstått en konflikt mellom Silje og Sivert")
    print("1: Ta det opp i plenum")
    print("2: Individuell samtale med begge parter")
    print("3: Ta det direkte opp med HR")
    while True:
        global poeng
        valg1 = input("Hva velger Erling? (1/2/3): ")
        if valg1 == "1":
            poeng += 1
            break
        elif valg1 == "3":
            poeng += 2
            break
        elif valg1 == "2":
            poeng += 3
            break
        else:
            print("Ugyldig input")


# ------------------------------
# VALG 2
# ------------------------------
def konflikt_2():
    print("VALG 2: Det har oppstatt en konflikt mellom Hamdi og Jabir")
    print("1: La de finne ut av det selv")
    print("2: Hamdi har vært her lengst, så han får viljen sin")
    print("3: Spørre flere brukere")
    while True:
        global poeng
        valg2 = input("Hva velger Erling? (1/2/3): ")
        if valg2 == "2":
            poeng += 1
            break
        elif valg2 == "1":
            poeng += 2
            break
        elif valg2 == "3":
            poeng += 3
            break
        else:
            print("Ugyldig input")


# ------------------------------
# VALG 3
# ------------------------------
def konflikt_3():
    print("VALG 3: Motivasjonen på gruppa har fått en smell, hvordan ønsker du å løse det?")
    print("1: Holde en langt motivasjonstale ")
    print("2: Styr prosjektet med jernhånd")
    print("3: Invitere til pizza party")
    while True:
        global poeng
        valg3 = input("Hva velger Erling? (1/2/3): ")
        if valg3 == "1":
            poeng += 1
            break
        elif valg3 == "2":
            poeng += 2
            break
        elif valg3 == "3":
            poeng += 3
            break
        else:
            print("Ugyldig input")


# ------------------------------
# SLUTTRESULTAT – basert på poeng
# ------------------------------


def slutt():
    global poeng
    print("SLUTTRESULTAT:")
    if poeng <= 4:
        print("Prosjektet mister samhold og forsinkes")
    elif 5 <= poeng <= 7:
        print("SLUTT 2: Konflikten løses delvis, men relasjonene er fortsatt sårbare.")
    else:
        print("SLUTT 3: Teamet gjenoppretter tillit og går videre til norming-fasen.")

    print("Takk for at du spilte!")
konflikt_1()
konflikt_2()
konflikt_3()
slutt()