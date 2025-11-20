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

#================================Konflikt 1 introen=====================================
print("\n" * 60)
print("KONFLIKT 1: DESIGNER MOT IT-RÅDGIVER")
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
print("\n" * 60)

def valg_konflikt1():
    print("Løs konflikten!")
    print("1.Skal du ta det i plenum?")
    print("2.Skal du ha individuelle samtaler?")
    print("3.Skal du tilkalle en ekstern mekler?")
    print("=======================================")
        
    while True:
        valg = input("Skriv inn ditt valg (1, 2 eller 3): ")

        if valg == "1":
             print("\n" * 60)
             print("Du valgte å ta det i plenum.")
             print("Dette var kanskje ikke det smarteste valget...")
             trykk_enter()
             print(f"{erling}: Ok folkens, la oss sette oss ned og snakke om dette sammen...")
             trykk_enter()
             print(f"Konflikten ble ikke løst, og prosjektet ditt lider under det...  \n{hamdi} og {jabir} har blitt innblandet \nog konflikten er enda vanskeligere å løse...")
             return 1
        elif valg == "2":
            print("\n" * 60)
            print("Du valgte å ha individuelle samtaler med de.")
            print("Dette er ikke så dumt...")
            trykk_enter()
            print(f"{erling}: Ok {silje}, la oss snakke litt, kom hit så finner vi ut av dette...\nSå tar vi en prat også {sivert}, vi løser dette...")
            trykk_enter()
            print("Etter samtalene, forstår begge partene hverandre bedre og konflikten blir bedre løst. Bra valg!")
            return 3
        elif valg == "3":
            print("\n" * 60)
            print("Du valgte å tilkalle en ekstern mekler. Du er tøffing nå! Eller, er du det?")
            trykk_enter()
            print(f"{erling}: Jeg har tilkalt en mekler som kan hjelpe oss med dette...\nLa oss høre hva han har å si...")
            trykk_enter()
            print("Mekleren hjelper partene med å forstå hverandre bedre, og konflikten blir løst på en god måte. \nMen, hjelper dette for tilliten til Erling som prosjektleder? \nKanskje ikke helt... eller?")
            return 2
        else:
            print("\nUgyldig valg.")



poeng += valg_konflikt1()

print(f"\nDin score fra konflikten: {poeng} poeng")
trykk_enter()


#=====================================Konflikt nr 2 ========================================#

#Hamdi og Jabir

print("\n" * 60)
print("KONFLIKT 2: KULTURAVDELINGEN MOT INNBYGGERFORENINGEN")
print("#=============================================================================#")

print(f"Neste dag, så sitter {erling} med gruppen. De skal diskutere videre om designen.")
trykk_enter()

print(f"{hamdi}: Jeg mener at vi må inkludere flere kulturelle elementer i designen, \nsærlig med tanke på de mangfoldige brukerne i kommunen vår.")
trykk_enter()
print(f"{jabir}: Ja kanskje det, men jeg tenker det er bedre å ha bruker vennlighet først. \nikke for mange elementer som kan forvirre brukerne.")
trykk_enter()
print(f"{hamdi}: Joda men, mangfoldet er jo viktig. Så vi tar det. Jeg legger det til.")
trykk_enter()
print(f"{jabir}: Men hamdi nei, det er ikke helt målet... det...")
trykk_enter()
print(f"{hamdi}: Jo det er det! Vi må tenke på alle brukerne! Det er åpenbart siden er brukere som skal bruke systemet.")
trykk_enter()
print(f"{jabir}: Hamdi, det er ikke det som blir effektivt bruk for brukere... Hør på meg!...")

trykk_enter()
print("\n" * 60)


#===========================Etter Konflikt 2 introen=====================================


print("#=============================================================================#")
print(f"{hamdi} og {jabir} har nå en konflikt om hvordan brukerportalen skal være for innbyggerne.")
print(f"Begge medlemene står litt fast på sine meninger, med sine forskjellige synspunkter.")
print("#=============================================================================#")
trykk_enter()

print(f"Din oppgave som prosjektleder {erling}, er: \n1. Velge det som er best, for at konflikten ikke eskalerer seg\n2. Velge slik at du får mest mulig poeng!")
trykk_enter()
print("\n" * 60)



def valg_konflikt2():
    print("Løs konflikten!")
    print("1.Vil du la de være?")
    print("2.Vil du ta sjefavgjørelsen?")
    print("3.Vil du velge demokrati?")
    print("=======================================")
        
    while True:
        valg = input("Skriv inn ditt valg (1, 2 eller 3): ")

        if valg == "1":
             print("\n" * 60)
             print("Du valgte å la de være.")
             print("Dette var kanskje ikke det smarteste valget...")
             trykk_enter()
             print(f"{erling}: Dere fikser dette, jeg drar på kontoret en tur...")
             trykk_enter()
             print(f"Konflikten blir verre, Hamdi og Jabir forstår egentlig ikke målet med oppgaven. \nDe er ubevisst.")
             return 1
        elif valg == "2":
            print("\n" * 60)
            print("Du valgte å ta sjef avgjørelsen.")
            print("Dette fungerer så vidt...")
            trykk_enter()
            print(f"{erling}: Ok folkens, jeg har bestemt at vi skal gå for min løsning. Løsningen er følgende...")
            trykk_enter()
            print("Etter at Erling har tatt avgjørelsen, så føler Hamdi og Jabir ikke seg hørt. \nKonflikten blir løst for nå men, Kanskje ikke det beste valget for gruppen på lang sikt...")
            return 2
        elif valg == "3":
            print("\n" * 60)
            print("Du valgte å spørre de andre gruppe medlemmene om hjelp.")
            trykk_enter()
            print(f"{erling}: La oss høre hva de andre i gruppen tenker om dette...")
            trykk_enter()
            print("De andre gruppemedlemmene bidrar med nye perspektiver, og konflikten blir løst på en god måte. \nDette bidrar å styrke gruppen sin forståelse til prosjektet.\nBra valg!")
            return 3
        else:
            print("\nUgyldig valg.")

poeng += valg_konflikt2()

print(f"\nDin totale score fra konfliktene: {poeng} poeng")
trykk_enter()



#===================================== Motivasjon =======================================#
print("\n" * 60)
print("MOTIVASJON: GRUPPEN SKAL SAMLES")
print("#=============================================================================#")

print(f"Torsdags morgen... klokka er 08:30. {erling} går inn i grupperommet. ")
trykk_enter()
print("Alle er heldigvis tilstede. Men, de ser litt slitne ut... litt stille i rommet.")
trykk_enter()
print("Heldigvis, ingen konflikter denne gangen. Eller? Er vi så heldige?")
trykk_enter()
print(f"{erling} stusser litt... han ser motivasjonen i gruppen ikke er helt på topp...")
trykk_enter()
print(f"Dette må vi finne ut av, tenker {erling}...")
trykk_enter()
print(f"{erling}: God morgen alle sammen. Hvordan går det med dere? Jeg tenker at...")
trykk_enter()
print("\n" * 60)




print("#=============================================================================#")
print(f"Etter de to konfliktene i prosjektgruppen som har vært i denne uka, \nså er gruppe medlemmene litt slitne og demotiverte.")
print("Noen føler kanskje at arbeidet ikke har mening lenger, eller at det er uklart og for mye press.")
print("#=============================================================================#")
trykk_enter()

print(f"Din oppgave som prosjektleder {erling}, er følgende: \n1. Velge det som gir best motivasjonen i gruppen for prosjektet videre. \n2. Velge slik at du får mest mulig poeng!")
trykk_enter()
print("\n" * 60)

def valg_motivasjon():
    print("Løs motivasjonsproblemet!")
    print("1. Ha en motiverende tale for dem")
    print("2. Styr prosjektet med jernhånd")
    print("3. Få dem med på team building aktivitet")

    while True:
        valg = input("Skriv inn ditt valg (1, 2 eller 3): ")
        if valg == "1":
             print("\n" * 60)
             print("Du valgte å ha en motiverende tale for gruppen.")
             print("Dette var et bra valg!")
             trykk_enter()
             print(f"{erling}: Jeg vet at vi har hatt noen utfordringer, men jeg har troen på oss! \nSammen...")
             print("Gruppen føler seg inspirert og motivert etter talen! \nDe er klare for å ta fatt på arbeidet igjen med ny energi. \nMen, er dette nok?")
             return 2
        elif valg == "2":
            print("\n" * 60)
            print("Du valgte å styre prosjektet med jernhånd.")
            print("Dette var kanskje ikke det smarteste valget...")
            trykk_enter()
            print(f"{erling}: Fra nå av, skal alt gå etter min plan! Ingen diskusjoner, ingen spørsmål! \nTidsfrister må overholdes! Dette skal vi klare folkens!")
            trykk_enter()
            print("Gruppen føler seg undertrykt og motivasjonen synker... Når Erling ikke er til stede, \nså slakker de av på arbeidet sitt...")
            return 1
        elif valg == "3":
            print("\n" * 60)
            print("Du valgte å arrangere en team building aktivitet med gruppen.")
            print("Dette var et bra valg!")
            trykk_enter()
            print(f"{erling}: La oss ta team building aktivitet folkens! \nSå får vi litt avbrekk fra arbeidet idag...")
            trykk_enter()
            print("Gruppen føler seg mer sammensveiset og motivasjonen øker! \nDe jobber bedre sammen etter og blitt bedre kjent med hverandre. \nBra valg!")
            return 3
        else:
            print("\nUgyldig valg.")
        



poeng += valg_motivasjon()
print(f"\nDin totale score fra konfliktene: {poeng} poeng")

trykk_enter()

def vis_sluttresultat(poeng):
    print("\n" * 60)
    print("SLUTTRESULTAT")
    if poeng <= 3:
        print(f"Dine {poeng} poeng score, gjør at prosjektet ditt sliter veldig... \nDet fører til prosjektet ikke blir fullført og Erling mister jobben sin!")
    elif poeng >= 4 and poeng <=6:
        print(f"Dine {poeng} poeng score, gjør at prosjektet ditt går greit... \nDet fører til prosjektet sliter litt, men fortsatt mulig for å komme seg til Norming fasen.")
    else:
        print(f"Dine {poeng} poeng score, gjør at gruppen går til Norming fasen! \nProsjektet går utmerket og gruppen begynne å fungere svært bra! Bra jobbet!")

vis_sluttresultat(poeng)