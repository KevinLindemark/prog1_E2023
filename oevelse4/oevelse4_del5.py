# Øvelse 4 - Blinke LEDer

# Del 5 - Få den røde, gule og grønne LED til at blinke en efter den anden, med 1 sekunds interval.

from machine import Pin # importerer Pin klassen fra machine modulet
from time import sleep # importerer sleep funktionen fra time modulet

RED_LED_PIN = 26 # Opretter konstant variabel med integer værdien 26
led1 = Pin(RED_LED_PIN, Pin.OUT) # Instantierer et Pin objekt - til pin 26 som output

YELLOW_LED_PIN = 12 # Opretter konstant variabel med integer værdien 12
led2 = Pin(YELLOW_LED_PIN, Pin.OUT) # Instantierer et Pin objekt - til pin 12 som output

GREEN_LED_PIN = 13 # Opretter konstant variabel med integer værdien 13
led3 = Pin(GREEN_LED_PIN, Pin.OUT) # Instantierer et Pin objekt - til pin 13 som output

while True: # starter uendelig while løkke
    led1.on()
    sleep(1)
    led1.off()
    sleep(1)
    led2.off() # Aktiv lav LED
    sleep(1)
    led2.on()
    sleep(1)
    led3.on()
    sleep(1)
    led3.off()
    sleep(1)

