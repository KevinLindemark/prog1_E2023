# Øvelse 6 - Debounce håndtering med software
# Del 2 - Toggle (skift tændt/slukket) status på en LED når knappen trykkes på.

from machine import Pin # importerer Pin klassen fra machine modulet
from time import sleep # importerer sleep funktionen fra time modulet

pb1 = Pin(4, Pin.IN) # Instantierer et Pin objekt - til pin 4 som input

led1 = Pin(26, Pin.OUT) # Instantierer et Pin objekt - til pin 16 som output

while True: # starter uendelig while løkke
    # gemmer returværdien fra pin objektets value() metode
    # i variablen som er navngivet first
    first = pb1.value()
    sleep(0.01) # pause i 10 millisekunder
    # gemmer returværdien fra pin objektets value() metode
    # i variablen som er navngivet second
    second = pb1.value()
    # sammensat betinget udtryk med and
    # tjekker hvis knappen pb1 går fra at have værdien 1 (ikke trykket)
    # til at have værdien 0 (trykket)
    if first == 1 and second == 0:
        # Toggler led1 ved at sætte værdien
        # til en inverterede værdi af den nuværende værdi
        led1.value(not led1.value())