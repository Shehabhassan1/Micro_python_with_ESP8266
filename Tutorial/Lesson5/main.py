from machine import Pin,PWM
from time import sleep

# configure GPIO Pin for servo motor & Green LED  
servo_p 	= 14
green_pin	= 5

Green_led   = PWM(green_pin)
Servo_motor = PWM(servo_p)

Green_led.freq(1000)
Servo_motor.freq(50)
# duty cycle from 0 to 1023 
# green led off 
Green_led.duty(0)
# 0.39ms / 20ms = 0.0195 ms
# 1024 * 0.0195 = 20  > 0 degree  
Servo_motor.duty(20)
sleep(2)
# 1.36ms / 20ms =  0.068 ms
# 1024 * 0.068 = 70  > 90 degree  
Servo_motor.duty(70)
sleep(2)
# 2.34ms / 20ms = 0.117 ms
# 1024 * 0.117 = 120  > 180 degree  
Servo_motor.duty(120)
sleep(2)

