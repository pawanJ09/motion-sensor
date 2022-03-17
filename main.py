from machine import Pin
import utime

led = Pin(28, Pin.OUT)
pir = Pin(16, Pin.IN, Pin.PULL_DOWN)  # Default to low voltage
led.low()
utime.sleep(3)

while True:
    # Voltage is high when motion i.e. 1 is detected
    if pir.value() == 1:
        print('Motion Detected!')
        led.high()
        utime.sleep(2)
    else:
        led.low()
        utime.sleep(0.2)
