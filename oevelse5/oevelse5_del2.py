# Øvelse 5 - Knap og LED
# Del 2 -Prøv at ændre koden så at tryk på knappen skifter tilstanden på en LED
# så den forbliver tændt eller slukket (efter  knappen er sluppet).

from machine import Pin # importerer Pin klassen fra machine modulet
from time import sleep # importerer sleep funktionen fra time modulet

pb1 = Pin(4, Pin.IN) # Instantierer et Pin objekt - til pin 4 som input

led1 = Pin(26, Pin.OUT) # Instantierer et Pin objekt - til pin 16 som output

while True: # starter uendelig while løkke
    # if sætning med betinget udtryk
    # hvis pb1.value() metoden returnere 0
    # køres den indrykkede kodeblok
    if pb1.value() == 0:
        # Toggler led1 ved at sætte værdien
        # til en inverterede værdi af den nuværende værdi
        led1.value(not led1.value())
        print("Tænder/slukker LED")
    # kalder sleep funktionen med argumentet 0.2
    # (som laver et delay i programmet på 0.2 sekund)
    sleep(0.2)
