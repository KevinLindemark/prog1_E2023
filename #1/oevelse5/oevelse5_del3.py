from machine import Pin
from time import sleep
# Øvelse 5 - Knap og LED
# Del 3 - Prøv at lave en variabel som inkrementere med 1 hver gang knappen trykkes
    #og print variablens værdi. (prøv at udkommentere  linjen med sleep(0.1) og se hvad der sker når knappen trykkes)

pb1 = Pin(4, Pin.IN) # Instantierer et Pin objekt - til pin 4 som input

led1 = Pin(26, Pin.OUT) # Instantierer et Pin objekt - til pin 16 som output

inkrementer = 0 # variabel der skal inkrementeres 

while True:
    # pb1.value() returnere knappens nuværende værdi (0 eller 1)
    # hvis værdien er 0 så køres koden i den indrykkede kodeblok
    if pb1.value() == 0:
        inkrementer = inkrementer + 1 # inkrementér variablen værdi med 1
        print("Inkrementer værdi: ", inkrementer) #print den nuværerende værdi
    sleep(0.1) # Hvis der ikke laves et delay registreres for mange knap-tryk

