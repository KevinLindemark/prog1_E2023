# Øvelse 5 - Knap og LED
# Del 1 - Prøv at skrive programmet så at knappens værdi printes i Thonny’s shell.

from machine import Pin # importerer Pin klassen fra machine modulet
from time import sleep # importerer sleep funktionen fra time modulet

pb1 = Pin(4, Pin.IN) # Instantierer et Pin objekt - til pin 4 som input

while True: # starter uendelig while løkke
    # Kalder print funktionen med pb1.value() som argument
    # pb1.value() returnere knappens nuværende værdi (0 eller 1)
    print(pb1.value())
    # kalder sleep funktionen med argumentet 0.01
    # (som laver et delay i programmet på 0.01 sekund)
    sleep(0.01)