import tkinter as tk
import webbrowser
from picamera import PiCamera
from time import sleep
import RPi.GPIO
from gpiozero import LED, CPUTemperature
import os

RPi.GPIO.setmode(RPi.GPIO.BCM)

#rotate camera
os.system("v4l2-ctl --set-ctrl=rotate=90")

# TP settings window
class TpSettings:
    def main():
        window = tk.Tk()
        def __init__(self, master):
            self.master = master
            pad = 3
            self.window.attributes("-fullscreen", True)
            self.configure(bg = "black")
            
        def changeBrightness(event):
            level = brightness.get()
            with open('/sys/class/backlight/rpi_backlight/brightness', 'w') as file:
                file.write(str(level))
                
        brightness = tk.Scale(window, from_=10, to = 200, orient = tk.HORIZONTAL, command = changeBrightness)
        brightness.pack()
    main()
    

# main TP window
class TpWindow:
    window = tk.Tk()
    
    def __init__(self, master):
        self.master = master
        pad = 3
        self.window.attributes("-fullscreen", True)
        self.configure(bg = "#363635")
    def main():
        def joinCall():
            # join call logic here
            webbrowser.open('http://meet.jit.si/OperationGrammy')
            
        def volumeUp():
            # volume up
            print("Volume Up")
            
        def volumeDown():
            # volume down
            print("Volume Down")
            
        def openSettings():
            settings = TpSettings()
            
        def close():
            master.close()
            self.destroy()

        # tk buttons'
        joinBtn = tk.Button(window,
                            text = "Join Room",
                            bg = "#61E786",
                            fg = "white",
                            relief = tk.FLAT,
                            command = joinCall,
                            height = 10,
                            font = "Helvetica 36 bold")
        joinBtn.pack(side = tk.LEFT)
        volUpBtn = tk.Button(window,
                             text = "Volume Up",
                             bg = "#A2C7E5",
                             relief = tk.FLAT,
                             command = volumeUp,
                             height = 2,
                             font = "Helvetica 36 bold")
        volUpBtn.pack(side = tk.RIGHT)
        volDownBtn = tk.Button(window,
                               text = "Volume Down",
                               bg = "#A2C7E5",
                               relief = tk.FLAT,
                               command = volumeDown,
                               height = 2,
                               font = "Helvetica 36 bold")
        volDownBtn.pack(side = tk.RIGHT)
        settingsBtn = tk.Button(window,
                                text = "Settings",
                                bg = "#9D8DF1",
                                relief = tk.FLAT,
                                command = openSettings,
                                height = 2,
                                font = "Helvetica 36 bold")
        settingsBtn.pack(side = tk.RIGHT)

        
        root = tk.Tk()
        tp = TpWindow(root)
        
    main()

def fanMonitor():
    fan = LED(4)
    cpu = CPUTemperature()
    while True:
        if cpu.temperature > 72:
            fan.on()
        elif cpu.temperature < 70:
            fan.off()
        sleep(10)
        
fanMonitor()