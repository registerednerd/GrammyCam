from gpiozero import LED, CPUTemperature
from time import sleep

fan = LED(4)
cpu = CPUTemperature()
while True:
    if cpu.temperature > 72:
        fan.on()
    elif cpu.temperature < 70:
        fan.off()
    sleep(10)