# Øvelse 6 - Debounce håndtering med software
# Del 1 - Indskriv eksemplet med med debounce håndtering af knappen  

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
        print("Knap trykket") # printer streng
    # sammensat betinget udtryk med and
    # tjekker hvis knappen pb1 går fra at have værdien 0 (trykket)
    # til at have værdien 1 (trykket)
    elif first == 0 and second == 1:
        print("Knap sluppet") # printer streng

    


