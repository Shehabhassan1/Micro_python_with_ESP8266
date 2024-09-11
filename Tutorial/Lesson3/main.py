from machine import Pin,Signal
from time import sleep

pin = Pin(2,Pin.OUT)
LED = Signal(pin,invert =True)

button = Pin(4,Pin.IN)

def Blink_Led():
    LED.on()
    sleep(1)
    LED.off()
    sleep(1)


def callback(p):
    for i in range(2):
        Blink_Led()

button.irq(trigger=button.IRQ_FALLING,handler=callback)    



