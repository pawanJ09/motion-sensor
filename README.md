# PIR Motion Sensor

This is a small DIY project for creating a Motion Sensor LED using Raspberry Pi Pico and 
Micropython.


## Requirements

- [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/)
- Breadboard
- PIR Motion Sensor
- Jumper cables with M-F connectors
- LED
- 330 ohms resistor


## Pin Diagram

<img src="motion-sensor-pin-diagram.png">


## Running the application locally

Follow the pin diagram and complete the setup. After completing your setup connect your 
Raspberry Pi Pico to your laptop/computer using a USB-C cable and run the main.py program.


## Shutdown constantly running program

When you plugin your Raspberry Pi Pico to a power source main.py will start running. To stop 
this program from continuously running press the BOOTSEL button and plugin the USB-C so that the 
Raspberry Pi Pico appears as a drive. Now go to the drive and copy the flash_nuke.uf2 file to 
clear old contents.

[Flash Nuke UF2 File](https://datasheets.raspberrypi.com/soft/flash_nuke.uf2)





