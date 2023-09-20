# Øvelse 4 - Blinke LEDer
# Del 3 - Gradvist reducer intervallet, indtil du lige præcist ikke længere
# kan se at den grønne LED blinker længere. Hvilken interval endte du med?
from machine import Pin # importerer Pin klassen fra machine modulet
from time import sleep # importerer sleep funktionen fra time modulet

GREEN_LED_PIN = 13 # Opretter konstant variabel med integer værdien 13
led3 = Pin(GREEN_LED_PIN, Pin.OUT) # Instantierer et Pin objekt - til pin 13 som output

while True: # starter uendelig while løkke
    # Toggler led3 ved at sætte værdien
    # til en inverterede værdi af den nuværende værdi
    led3.value(not led3.value()) 
    sleep(0.014) # interval på 14 millisekunder

