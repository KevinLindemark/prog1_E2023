# Øvelse 4 - Blinke LEDer
# Del 6 - Simuler nu et lyskryds, du bestemmer selv timing: 

from machine import Pin # importerer Pin klassen fra machine modulet
from time import sleep # importerer sleep funktionen fra time modulet

RED_LED_PIN = 26 # Opretter konstant variabel med integer værdien 26
led1 = Pin(RED_LED_PIN, Pin.OUT) # Instantierer et Pin objekt - til pin 26 som output

YELLOW_LED_PIN = 12 # Opretter konstant variabel med integer værdien 12
led2 = Pin(YELLOW_LED_PIN, Pin.OUT) # Instantierer et Pin objekt - til pin 12 som output

GREEN_LED_PIN = 13 # Opretter konstant variabel med integer værdien 13
led3 = Pin(GREEN_LED_PIN, Pin.OUT) # Instantierer et Pin objekt - til pin 13 som output

while True: # starter uendelig while løkke
    led1.on() # tænd rød
    sleep(4) # forbliv rød i 4 sekunder
    led2.off() # aktiv lav LED - Tænd gul
    sleep(2) # gul og rød forbliver tændt i 2 sekunder
    led1.off() # rød slukkes
    led2.on() # gul slukkes (Aktiv lav)
    led3.on() # grøn tændes
    sleep(6) # grøn forbliver tændt i 6 sekunder
    led3.off() # grøn slukkes
    led2.off() # gul tændes
    sleep(2) # gul forbliver tændt i 2 sekunder
    led2.on() # gul slukkes
    # koden går nu tilbage til linje 19 og starter forfra