# Øvelse 4 - Blinke LEDer

# Del 4 - Få din røde, gule og grønne til alle
# at blinke samtidigt med 1 seconds interval.
from machine import Pin # importerer Pin klassen fra machine modulet
from time import sleep # importerer sleep funktionen fra time modulet

RED_LED_PIN = 26 # Opretter konstant variabel med integer værdien 26
led1 = Pin(RED_LED_PIN, Pin.OUT) # Instantierer et Pin objekt - til pin 26 som output

YELLOW_LED_PIN = 12 # Opretter konstant variabel med integer værdien 12
led2 = Pin(YELLOW_LED_PIN, Pin.OUT) # Instantierer et Pin objekt - til pin 12 som output

GREEN_LED_PIN = 13 # Opretter konstant variabel med integer værdien 13
led3 = Pin(GREEN_LED_PIN, Pin.OUT) # Instantierer et Pin objekt - til pin 13 som output

while True: # starter uendelig while løkke
    # Tænd alle 3 LED'er i 1 sekund
    led1.on()
    led2.off() # Aktiv lav LED (Tænder når den er off)
    led3.on()
    sleep(1)
    # Sluk alle 3 LED'er i 1 sekund
    led1.off()
    led2.on() # Aktiv lav LED (slukker når den er on)
    led3.off()
    sleep(1)

