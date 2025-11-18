#----------------------------------------Intro-----------------------------------------------#


print("Erling skal lage en medborger portal for å hjelpe \n folk med å finne informasjon om offentlige tjenester." )
print("Han jobber i kommunen og er leder for ett lite team \n med uike typer utviklere som hver har fått tildelt sin egen oppgave")
print("Men, konflikter har oppstått i prosjektet med andre utviklere!" )
print("Nå må du hjelpe Erling med å fikse konfliktene i prosjektet så han rekker fristen!")

score = 0 

#---------------------------Scenario 1 silje og sivert sin konflikt--------------------------# 

print("Scenario 1 - Silje og Sivert sin konflikt")
print("Erling merker at stemningen i teamet begynner å bli dårlig, og at folk ikke samarbeider så godt som de burde." )
print("Han får senere vite at Sivert og Silje har hatt en konflikt om hvordan de skal løse en oppgave i prosjektet." )


print( "Hva bør Erling gjøre for å fikse konflikten?" )

print ("1. Erling tar opp temaet med Sivert og Silje, ")
print ("2. Erling ignorerer problemet og håper på at det ordner seg selv")
print ("3. Erling snakker med begge en til en")
valg1 = input("skriv inn ditt valg:")

while valg1 not in ["1", "2", "3"]:
    valg1 = input("Ugyldig valg. Vennligst velg 1, 2 eller 3: ")

if valg1 == "1":
    print("Riktig! Erling tar opp temaet med Sivert og Silje, og hjelper dem med å finne en løsning som begge er fornøyde med, dette løser problemet på en god måte.")
    score += 1
    

elif valg1 == "2": 
    print(" Erling ignorerer problemet og håper på at det ordner seg selv, det gjør det ikke og konflikten eskalerer videre. feil valg.")

elif valg1 == "3":
    print("Erling snakker med begge en til en,men dette fører ikke til en løsning på konflikten. feil valg.") 

#---------------------------Scenario 2 Hamdi og Jabar sin uenighet--------------------------#

print("Scenario 2- Hamdi og Jabar sin uenighet")
print("Erling får senere i tillegg vite at Hamdi og Jabbar har en uenighet som angår den løsningen som passer best")
print("Hamdi mener at det å bruke en trygg og kontrollert kommuneløsning er det riktige å gjøre")
print("Mens Jabar mener dette er feil og at en løsning der innbyggerne kan være mer interaktive å delta mer fritt er bedre") 


print("hvordan skal Erling håndtere dette på best mulig måte?")

print("1. Erling gjør ingenting, han regner med at de klarer å løse problemet selv.")
print("2. Erling samler de og diskuterer om hvilken løsning som passer best og hvorfor")

valg2= input("skriv inn ditt valg: ")

while valg2 not in ["1", "2"]: 
    valg2 = input("Ugyldig valg, prøv igjen!")

if valg2 == "1":
    print ("Feil valg, uenigheten blir bare større og eskalerer seg mer og mer")

elif valg2 == "2":
    print("Riktig valg, de kommer til en enighet og sier seg fornøyd med resultatet!")
    score += 1


#----------------------------Scenario 3 bevare motivasjon i teamet-------------------------#

print("Scenario 3, bevare motivasjon i teamet")
print("Etter litt tid med vanskeligheter er motivasjonen i teamet ikke helt der den skal være")
print("Han merker at folk er stresset og mindre engasjerte for ")

print("1. Erling arrangerer en teambuilding aktivitet for å styrke samholdet i teamet")
print("2. Erling presser teamet til å jobbe hardere for å nå fristen")
print("3. Erling ignorerer situasjonen og håper på det beste")

valg3= input("Skriv inn ditt valg:")
while valg3 not in ["1", "2", "3"]:
    valg3 = input("Ugyldig valg. Vennligst velg 1, 2 eller 3: ")

if valg3 == "1":
    print("Riktig! Erling arrangerer en teambuilding aktivitet for å styrke samholdet i teamet, noe som øker motivasjonen og engasjementet.")
    score += 1 

elif valg3 == "2":
    print ("Feil valg. Erling presser teamet til å jobbe hardere, noe som fører til økt stress og redusert motivasjon.")

elif valg3 == "3":
    print ("Feil valg. Erling ignorerer situasjonen, noe som fører til at motivasjonen i teamet fortsetter å synke.")



#----------------------------------Sluttpoeng og evaluering------------------------------------#

print("\n Spillet er over!")

if score == 3:
    print("Utmerket! Du har hjulpet Erling med å håndtere konflikter og bevare motivasjonen i teamet på en eksemplarisk måte.")

elif score == 2: 
    print("Bra jobbet! Du har gjort en god jobb med å hjelpe")
          
elif score == 1:
    print(" Du gjorde så godt du kunne, Erling prøvde og redde så mye han kunne av prosjektet.")

else: print(" Desverre klarte du ikke å hjelpe Erling, prosjektet mislyktes på grunn av dårlig konflikthåndtering og lav motivasjon i teamet."
            )