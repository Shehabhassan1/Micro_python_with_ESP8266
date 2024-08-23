from machine import Pin,Signal
import time
led = Pin(2,Pin.OUT)
led_Blue = Signal(led,invert = True)
Button = Pin(15,Pin.IN,Pin.PULL_UP)
led_Blue.value(0)
led_on = 0
#led_Blue.value(not led_Blue.value(0))
while True:
    but = Button.value()
    time.sleep_ms(5)
    prev_but = 0
    if but == 1 and prev_but == 0:
        led_on = not led_on
        led_Blue.value(led_on)
        but = prev_but