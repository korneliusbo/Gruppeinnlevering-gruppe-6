# ====================================
# KONFLIKTHÅNDTERING - PROSJEKTARBEID
# ====================================
# Få mest mulig poeng ved å løse konflikter i et prosjektteam!


def trykk_enter():
    input("Trykk enter for å fortsette...")
    print("")



# Projektleder
erling = "Erling"

# === KONFLIKT 1: Design mot IT ===

silje = "Silje" #UX/UI designer
sivert = "Sivert" #IT-rådgiver fra kommunens IT-avdeling

# === KONFLIKT 2: Kulturavdelingen mot Innbyggerforeningen ===

hamdi = "Hamdi" #Representant fra kulturavdelingen
jabir = "Jabir" #Brukerrepresentant fra innbyggerforeningen

poeng = 0
#LET KONFLIKTENE BEGYNNE!

#=============================================================================#
print("\n\n\n\n\n\n")
print("KONFLIKT 1: DESIGN MOT IT-RÅDGIVER")
print("#=============================================================================#")
print(f"{erling} er i telefonen, å hører rasling med papirer...")
trykk_enter()

print(f"{erling}: Ja, vi høres Kristoffer!...")
trykk_enter()

print(f"Utenfor grupperommet, hører {erling} støy i bakgrunnen...")
trykk_enter()

print(f"{sivert}: Ja men {silje}, det blir ikke å skje!... Det er kostbart, kan du ikke skjønne det?")
trykk_enter()

print(f"{silje}: Jeg skjønner det {sivert}, men vi må finne en løsning som fungerer for brukere. \nDe trenger frihet i denne designen! Forstår du ikke det!?")
trykk_enter()

print(f"{silje}: Han Hamdi er enig med meg, sant Hamdi?")
trykk_enter()

print(f"{hamdi}: Ja, absolutt Silje! Vi må tenke på brukerne og deres behov først og fremst.")
trykk_enter()

print(f"{sivert}: Jeg forstår det, men sikkerheten er viktigst!... Vi kan ikke ha åpne systemer i kommunen, det er for risikabelt! Forstår du ikke det!?")
trykk_enter()

print(f"{erling} legger på telefonen og sukker dypt... går inn i grupperommet.")
trykk_enter()


#===========================Etter Konflikt 1 introen=====================================



print("#=============================================================================#")
print("Som du forstår, er det en konflikt mellom designeren og IT-rådgiveren i prosjektet ditt.")
print("#=============================================================================#")

trykk_enter()

print(f"Din oppgave som prosjektleder {erling}, er følgende: \n1. Velg den beste måten å løse konflikten \n2. Velg slik at du får mest mulig poeng!")
trykk_enter()

def valg_konflikt2():
    print("Løs konflikten!")
    print("1.Skal du ta det i plenum?")
    print("2.Skal du ha individuelle samtaler?")
    print("3.Skal du tilkalle en ekstern mekler?")
    print("=======================================")
        
    while True:
        valg = input("Skriv inn ditt valg (1, 2 eller 3): ")

        if valg == "1":
             print("")
             print("Du valgte å ta det i plenum.")
             print("Dette var kanskje ikke det smarteste valget...")
             trykk_enter()
             print(f"{erling}: Ok folkens, la oss sette oss ned og snakke om dette sammen...")
             trykk_enter()
             print(f"Konflikten ble ikke løst, og prosjektet ditt lider under det...  \n{hamdi} og {jabir} har blitt innblandet \nog konflikten er enda vanskeligere å løse...")
             return "2"
        elif valg == "2":
            print("")
            print("Du valgte å ha individuelle samtaler med de.")
            print("Dette er ikke så dumt...")
            trykk_enter()
            print(f"{erling}: Ok {silje}, la oss snakke litt, kom hit så finner vi ut av dette...\nSå tar vi en prat også {sivert}, vi løser dette...")
            trykk_enter()
            print("Etter samtalene, forstår begge partene hverandre bedre og konflikten blir bedre løst.")
            return "15"
        elif valg == "3":
            print("")
            print("Du valgte å tilkalle en ekstern mekler. Du er tøffing nå! Eller, er du det?")
            print(f"{erling}: Jeg har tilkalt en mekler som kan hjelpe oss med dette...\nLa oss høre hva hen har å si...")
            trykk_enter()
            print("Mekleren hjelper partene med å forstå hverandre bedre, og konflikten blir løst på en god måte. Men, hjelper dette for tilliten til Erling som prosjektleder? \nKanskje ikke helt... eller?")
            return "10"
        else:
            print("\nUgyldig valg.")



print(f"\nDin score fra konflikten: {poeng} poeng")
trykk_enter()




print("Konflikt nr 2")

#=====================================Konflikt nr 2 ========================================#

#Hamdi og Jabir

print("\n\n\n\n\n\n")
print("KONFLIKT 2: KULTURAVDELINGEN MOT INNBYGGERFORENINGEN")
print("#=============================================================================#")

print(f"Neste dag, så sitter {erling} med gruppen. De skal diskutere videre om designen.")


def valg_konflikt2():
    print("Løs konflikten!")
    print("1.La de være")
    print("2.Hamdi eller Jabir får viljen sin")
    print("3.Spørre andre gruppe medlemer")
    print("=======================================")
        
    while True:
        valg = input("Skriv inn ditt valg (1, 2 eller 3): ")

        if valg == "1":
             print("")
             print("Du valgte å la de være.")
             print("Dette var kanskje ikke det smarteste valget...")
             trykk_enter()
             print(f"{erling}: Dere fikser dette, jeg drar på kontoret en tur...")
             trykk_enter()
             print(f"Konflikten ble verre, Hamdi og Jabir forstår ikke målet med oppgaven. De er ubevisst.")
             return "2"
        elif valg == "2":
            print("")
            print("Du valgte å enten gi Hamdi eller Jabir få viljen sin \n Du valgte Hamdi")
            print("Dette fungerte greit, men kunne vært bedre...")
            trykk_enter()
            print(f"{erling}: Ok {hamdi}, la oss snakke litt, kom hit så finner vi ut av dette...\nSå tar vi en prat også {sivert}, vi løser dette...")
            trykk_enter()
            print("Etter samtalene, forstår begge partene hverandre bedre og konflikten blir bedre løst.")
            return "15"
        elif valg == "3":
            print("")
            print("Du valgte å spørre de andre gruppe medlemmene om hjelp.")
            print(f"{erling}: La oss høre hva de andre i gruppen tenker om dette...")
            trykk_enter()
            print("De andre gruppemedlemmene bidrar med nye perspektiver, og konflikten blir løst på en god måte. \n Dette bidrar å styrke gruppen sin forståelse til prosjektet.")
            return "10"
        else:
            print("\nUgyldig valg.")




