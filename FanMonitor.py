from gpiozero import LED, CPUTemperature
from time import sleep

fan = LED(4)
cpu = CPUTemperature()

# test/validate
fan.on()
sleep(3)
fan.off()
sleep(3)

while True:
    if cpu.temperature > 65:
        fan.on()
    elif cpu.temperature < 62:
        fan.off()
    sleep(10)