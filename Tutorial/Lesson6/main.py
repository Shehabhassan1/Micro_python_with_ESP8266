from machine import Pin,PWM,ADC
from time import sleep

# configure GPIO Pin for POT & Green LED  
pot_p 		= 0
green_pin	= 5
Green_led = PWM(green_pin)
Green_led.freq(1000)
# duty cycle from 0 to 1023 
# green led off 
Green_led.duty(0)
POT = ADC(pot_p)

while True:
    pot_value = POT.read()
    if pot_value == 5:
        print(0)
    else:    
        print(pot_value)
    Green_led.duty(pot_value)   
    sleep(0.5)
    
    