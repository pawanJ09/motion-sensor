from machine import Pin
import utime

led = Pin(28, Pin.OUT)
pir = Pin(16, Pin.IN, Pin.PULL_UP)
led.low()
utime.sleep(3)

while True:
    # Ideally this should be checking for 0 but the sensor I had didnt give a good voltage
    if pir.value() == 1:
        print('Motion Detected!')
        led.high()
        utime.sleep(2)
    else:
        print('Waiting for movement...')
        led.low()
        utime.sleep(0.2)
