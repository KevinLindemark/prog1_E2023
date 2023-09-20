# Øvelse 4 - Blinke LEDer
# Del 2 - Få din ESP32 til at blinke den røde LED med 0.5 seconds interval

from machine import Pin # importerer Pin klassen fra machine modulet
from time import sleep # importerer sleep funktionen fra time modulet

RED_LED_PIN = 26 # Opretter konstant variabel med integer værdien 26
led1 = Pin(RED_LED_PIN, Pin.OUT) # Instantierer et Pin objekt - til pin 26 som output

while True: # starter uendelig while løkke
    # Toggler led1 ved at sætte værdien
    # til en inverterede værdi af den nuværende værdi
    led1.value(not led1.value())
    # kalder sleep funktionen med argumentet 0.5
    # (som laver et delay i programmet på 0.5 sekund)
    sleep(0.5)
