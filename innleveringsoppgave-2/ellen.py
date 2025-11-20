#Erlings beslutning

#-------------Bakgrunnshistorie ----------------

# Det har gått seks uker siden Erling, prosjektleder for utviklingen av kommunens nye
# digitale medborgerportal, samlet sitt prosjektteam for første gang. Etter en inspirerende
# oppstart med høy energi, begynner samarbeidet nå å møte sine første reelle prøver. Prosjektet har
# beveget seg inn mot storming fasen - der sterke meninger, personlige verdier og ulike prioriteringer
# kolliderer. Konflikter har oppstått mellom teammedlemmer, og motivasjonen begynner å dale. Erling
# må navigere gjennom disse utfordringene for å sikre at prosjektet forblir på rett spor og at teamet 
# forblir engasjert og produktivt.

# Variabler


#-------------Intro-----------------------------

print("Velkommen til Erlings konfliktløsnings guide!")
print("Du er Erling, prosjektleder for utviklingen av kommunens nye digitale medborgerportal.")
print("Etter en lovende start har teamet begynt å møte utfordringer som truer fremdriften.")
print("Ditt mål er å navigere gjennom disse utfordringene og sikre at prosjektet lykkes.")  

#------------- Silje og Sivert konflikt ----------------

print("Del 1: Hvordan håndterer du konflikten mellom Silje og Sivert?")
print("1 = Snakke med dem individuelt")
print("2 = Arrangere et møte for å diskutere problemet åpent")
print("3 = Kontakte HR for å megle i konflikten")

valg_1 = int(input("Velg 1,2 eller 3: "))
if valg_1 == 1:
    print("Erling snakker med Silje og Sivert individuelt, noe som hjelper dem å uttrykke sine bekymringer uten press fra den andre.")
    print("Konsekvens: Konflikten løses")
elif valg_1 == 2:
    print("Erling arrangerer et møte hvor Silje og Sivert kan diskutere problemet åpent.")
    print("Konsekvens: Møtet fører til en bedre forståelse mellom dem, men det tar tid å løse konflikten.") 
elif valg_1 == 3:
    print("Erling kontakter HR for å megle i konflikten.") 

# - ----------- Hamdi og Jabir konflikt ----------------
print("Del 2: Hvordan håndterer du uenigheten mellom Hamdi og Jabir?")
print("1 = La de være og fikse det selv")
print("2 = Velge en side og støtte dem")
print("3 = Spørre flere teammedlemmer om deres mening")
    
valg_2 = int(input("Velg 1,2 eller 3: "))
if valg_2 == 1:
    print("Erling lar Hamdi og Jabir prøve å løse konflikten selv.")
    print("Konsekvens: Konflikten eskalerer og påvirker teamets moral.")   
elif valg_2 == 2:
    print("Erling velger å støtte Hamdi, noe som skaper misnøye hos Jabir.")
    print("Konsekvens: Teamets dynamikk forverres.")  
elif valg_2 == 3:
    print("Erling spør flere teammedlemmer om deres mening for å få et bredere perspektiv.")
    print("Konsekvens: Dette hjelper med å finne en balansert løsning som alle kan akseptere.") 

# ------------Motivasjonsproblem ----------------

print("Del 3: Teamet begynner å miste motivasjonen. Hva gjør du?")
print("1 = Ha en fin samtale med hver enkelt")
print("2 = Styr prosjektet med en jernhånd")   
print("3 = Pizzaparty og teambuilding aktiviteter")

valg_3 = int(input("Velg 1,2 eller 3: "))
if valg_3 == 1:
    print("Erling har en fin samtale med hver enkelt teammedlem for å forstå deres bekymringer.")
    print("Konsekvens: Teamet føler seg hørt og motivasjonen øker.")   
elif valg_3 == 2:
    print("Erling styrer prosjektet med en jernhånd, noe som skaper frykt og misnøye.")
    print("Konsekvens: Teamets moral synker ytterligere.")
elif valg_3 == 3:
    print("Erling arrangerer et pizzaparty og teambuilding aktiviteter.")
    print("Konsekvens: Teamet blir mer sammensveiset og motivasjonen øker.")        
    
#-------------Avslutning--------------------------
print("Takk for at du spilte Erlings beslutning!")
