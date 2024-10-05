from machine import Pin,Signal
from time import sleep

blue_pin 	= 2
green_pin	= 5
button 		= 4 

Button = Pin(button,Pin.IN,Pin.PULL_UP)

Green_led = Pin(green_pin,Pin.OUT)

Blue = Pin(blue_pin,Pin.OUT)

Blue_LED = Signal(Blue,invert =True)

    
    

##

from machine import Pin,PWM
from time import sleep

servo_p 	= 14
green_pin	= 5

#configure led pin  
Green_led = PWM(Pin(green_pin))
servo_pin = PWM(Pin(servo_p))
# set freq 1KHz --> 1 ms 
Green_led.freq(1000)
# Range of duty cycle from 0 to 1023
# Frequncy
servo_pin.freq(50) # 1/50 = 20ms

# 0.38ms / 20ms = 0.019 
# 1.36ms / 20ms = 0.068
# 2.34   / 20ms = 0.117

count = 0
while True:
    servo_pin.duty(20)
    sleep(1)
    servo_pin.duty(70)
    sleep(1)
    servo_pin.duty(120)
    sleep(1)
    count+=1
    if count == 2:
        break
