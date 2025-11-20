import sys

print("Hei, velkommen til konfliktløsningsguiden!")

#- - - - - - - - - - Silje og Sivert konflikt - - - - - - - - - -
print("Du skal nå løse første konflikt som handler om at Silje og Sivert er uenige.")
print("Du får nå tre hovedvalg, vennligst velg et hovedvalg ved å anngi 1, 2, eller 3:")
print("1. Løse konflikten internt mellom personene det gjelder for å dempe stemningen i prosjektgruppen.")
print("2. Løse konflikten i plenum for å skape åpenhet i prosjektgruppen.")
print("3. Skyve konflikten under teppet for å unngå uro i prosjektgruppen.")

valgt_hovedvalg = int(input("Anngi ditt valg: "))
if valgt_hovedvalg >= 1 and valgt_hovedvalg <= 3:
    print("Du har nå valgt alternativ " + str(valgt_hovedvalg) + " - Du vil nå få to alternativer, vennligs velg ett av dem: ")

if valgt_hovedvalg == 1: 
    print("a. Inviterer partene til et møte for å diskutere konflikten skalig og rolig.")
    print("b. Snakker med partene hver for seg for å forstå deres synspunkt.")

elif valgt_hovedvalg == 2:
    print("a. Innkaller til et gruppemøte for å diskutere konflikløsninger i fellesskap.")
    print("b. Sender ut et anonymt skjema der prosjektmedlemmene kan foreslå konfliktløsninger.")

elif valgt_hovedvalg == 3: 
    print("a. Unngå konflikten, og fortsette prosjektarbeidet som normalt.")
    print("b. Akseptere at konflikten eksisterer, og tenke at de er voksne nok til å løse den selv.")

else: 
    print("Beklager du har valgt et alernativ som ikke eksisterer. Programmet fortsetter til Del 2.")
    sys.exit()

valgt_alternativ = input("Anngi ditt alternativ: ")

if valgt_hovedvalg == 1 and (valgt_alternativ == "a" or valgt_alternativ == "b"):
    print("Konflikten løses effektivt, partene kommer overens, og prosjektet fortsetter som normalt.")

elif (valgt_hovedvalg == 2 or valgt_hovedvalg == 3) and valgt_alternativ == "a":
    print("Prosjektet forsinkes fordi det mistes mye tid på grunn av denne løsningen.")

elif (valgt_hovedvalg == 2 or valgt_hovedvalg == 3) and valgt_alternativ == "b":
    print("Konflikten løses delvis fordi gruppemedlemmene kan fortsette som normalt, men det er noe uoppgjort.")

else: 
    print("Du har valgt et ikke eksisterende alternativ. Programmet fortsetter til Del 2.")

#- - - - - - - - - - Hamdi og Jabir konflikt - - - - - - - - - -
print("Dette er del 2 av konfliktløsningsguiden. Du må forhindre at konflikten mellom Hamdi og Jabir blusser opp.")
print("Du får nå tre nye hovedvalg, vennligst velg et hovedvalg ved å anngi 1, 2, eller 3:")
print("1. La de være og fikse det selv.")
print("2. Velg en side og støtt dem.")
print("3. Spørr flere teammedlemmer om deres meninger.")

valgt_hovedvalg = int(input("Anngi ditt valg: "))
if valgt_hovedvalg >= 1 and valgt_hovedvalg <= 3:
    print("Du har nå valgt alternativ " + str(valgt_hovedvalg) + " - Du vil nå få to alternativer, vennligs velg ett av dem: ")

if valgt_hovedvalg == 1: 
    print("a. Du lar partene være, og tenker de klarer å fikse opp i det selv.")
    print("b. Du lar partene være, fordi du tenker at det ikke er verdt å bruket tid på.")

elif valgt_hovedvalg == 2:
    print("a. Du velger Hamdi sin side, og støtter den.")
    print("b. Du velger Jabir sin side, og støtter den.")

elif valgt_hovedvalg == 3: 
    print("a. Du setter av tid til å innhente meninger fra flere teammedlemmene individuelt.")
    print("b. Du setter av tid til et gruppemøte, for å innhente flere meninger.")

else: 
    print("Beklager du har valgt et alernativ som ikke eksisterer. Programmet fortsetter til Del 3.")
    sys.exit()

valgt_alternativ = input("Anngi ditt alternativ: ")

if valgt_hovedvalg == 1 and (valgt_alternativ == "a" or valgt_alternativ == "b"):
    print("Du har latt partene være, og konflikten mellom dem blusser opp igjen.")

elif valgt_hovedvalg == 2 and (valgt_alternativ == "a" or valgt_alternativ == "b"):
    print("Du har valgt en side og støtter den, den andre parten er missfornøyd og konflikten blusser opp igjen.")

elif valgt_hovedvalg == 3 and (valgt_alternativ == "a" or valgt_alternativ == "b"):
    print("Du får innsyn fra flere teammedlemmer, som fører til at du klarer å løse konflikten.")

else: 
    print("Du har valgt et ikke eksisterende alternativ. Programmet fortsetter til Del 3.")

#- - - - - - - - - - Teamet begynner å miste motivasjon - - - - - - - - - -
print("Dette er del 3 av konfliktløsningsguiden. Teamet har begynt å miste motivasjon. Hva gjør du?")
print("Du får nå tre nye hovedvalg, vennligst velg et hovedvalg ved å anngi 1, 2, eller 3:")
print("1. Ha en fin samtale med hver enkelt.")
print("2. Styr prosjektet med en jernhånd.")
print("3. Pizzaparty og teambuilding aktiviteter.")

valgt_hovedvalg = int(input("Anngi ditt valg: "))
if valgt_hovedvalg >= 1 and valgt_hovedvalg <= 3:
    print("Du har nå valgt alternativ " + str(valgt_hovedvalg) + " - Du vil nå få to alternativer, vennligs velg ett av dem: ")

if valgt_hovedvalg == 1: 
    print("a. Ha en kortivarig samtale med hver enkelt.")
    print("b. Ha en langvarig samtale med hver enkelt.")

elif valgt_hovedvalg == 2:
    print("a. Du inntar en streng rolle som gruppeleder, og lar ikke de andre slippe til.")
    print("b. Du tydeligjør for de andre at du er sjefen, og styrer gruppen alene.")

elif valgt_hovedvalg == 3: 
    print("a. Du setter av tid til pizza og teambuildning for å løfte stemningen.")
    print("b. Du bruker tid på at teammedlemmene skal få opp motivasjonen gjennom sosialeaktiviteter.")

else: 
    print("Beklager du har valgt et alernativ som ikke eksisterer. Programmet avluttes, og du må starte på nytt.")
    sys.exit()

valgt_alternativ = input("Anngi ditt alternativ: ")

if valgt_hovedvalg == 1 and (valgt_alternativ == "a" or valgt_alternativ == "b"):
    print("Alle gruppemedlemmene har en samtale med deg, og de får økt motivasjon igjen.")

elif valgt_hovedvalg == 2 and (valgt_alternativ == "a" or valgt_alternativ == "b"):
    print("Du styrerer prosjektet med jernhånd, og gruppemedlemmene får mindre motivasjon.")

elif valgt_hovedvalg == 3 and (valgt_alternativ == "a" or valgt_alternativ == "b"):
    print("Teamet koser seg, og motivasjonen i teamet øker igjen.")

else: 
    print("Du har valgt et ikke eksisterende alternativ. Start programmet på nytt.")

# - - - - - - - - - - Avslutning - - - - - - - - - -
print("Du har nå vært igjennom konfliktløsningsguiden, og har endt opp med en avslutning til hver konflikt. Godt jobbet!")











