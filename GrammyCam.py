import tkinter as tk
import os
import cec
import subprocess

print("Program started")
# Colors
charcoal = "#363635"
red = "#BD9391"
blue = "#A2C7E5"
green = "#61E786"
purple = "#9D8DF1"

cec.init()
print("CEC Initialized")

# rotate camera
os.system("v4l2-ctl --set-ctrl=rotate=90")
print("Camera rotated")

# TP settings 
class TpSettings:
    window = tk.Tk()
    window.attributes("-fullscreen", True)
    window.configure(bg = "black")
    brightness = 0
    brightnessSlider = tk.Scale(window, from_=1, to = 100, orient = tk.HORIZONTAL, variable = brightness)
    brightnessSlider.pack()

    def changeBrightness(self):
        with open("/sys/class/backlight/rpi_backlight/brightness", 'w') as file:
            level = self.brightness
            file.write(str(level))
    brightnessSlider["command"] = changeBrightness
        
            
    def close(self):
        self.window.destroy()
        self.master.close()

# main TP window

window = tk.Tk()
window.attributes("-fullscreen", True)
window.configure(bg = "black")
window.title = "Main TP"

# tk buttons'
pad = 10
joinBtn = tk.Button(window,
                    text = "Join\nRoom",
                    bg = green,
                    fg = "white",
                    relief = tk.FLAT,
                    font = "Helvetica 36 bold")
joinBtn.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1, padx = pad, pady = pad)
sideFrame = tk.Frame(window,
                     bg = "black")
sideFrame.pack(side = tk.RIGHT, fill = tk.BOTH)
volUpBtn = tk.Button(sideFrame,
                     text = "Volume +",
                     bg = blue,
                     relief = tk.FLAT,
                     font = "Helvetica 36 bold")
volUpBtn.pack(side = tk.TOP, fill = tk.BOTH, expand = 1, padx = pad, pady = pad)
volDownBtn = tk.Button(sideFrame,
                       text = "Volume -",
                       bg = blue,
                       relief = tk.FLAT,
                       font = "Helvetica 36 bold")
volDownBtn.pack(side = tk.TOP, fill = tk.BOTH, expand = 1, padx = pad, pady = pad)
settingsBtn = tk.Button(sideFrame,
                        text = "Settings",
                        bg = purple,
                        relief = tk.FLAT,
                        font = "Helvetica 36 bold")
settingsBtn.pack(side = tk.TOP, fill = tk.BOTH, padx = pad, pady = pad)

def joinCall():
    serviceUrl = "http://meet.jit.si/"
    roomId = "GrammyCam"
    subprocess.Popen("echo 'as' | cec-client RPI -s -d 1", shell = True)
    global callWindow
    callWindow = subprocess.Popen(["chromium-browser",
                                 "--start-fullscreen",
                                 "--disable-session-crashed-bubble",
                                 "--disable-infoboards",
                                 "--disable-restore-session-state",
                                 f"{serviceUrl}{roomId}]"])
    joinBtn["bg"] = red
    joinBtn["text"] = "Leave\nRoom"
    joinBtn["command"] = endCall
joinBtn["command"] = joinCall
    
def endCall():
    print("End Call")
    global callWindow
    callWindow.terminate()
    joinBtn["bg"] = green
    joinBtn["text"] = "Join\nRoom"
    joinBtn["command"] = joinCall
        
def volumeUp():
    subprocess.Popen("echo 'volup' | cec-client RPI -s -d 1", shell = True)
volUpBtn["command"] = volumeUp

def volumeDown():
    subprocess.Popen("echo 'voldown' | cec-client RPI -s -d 1", shell = True)
volDownBtn["command"] = volumeDown
    
def openSettings():
    #settings = TpSettings()
    print("Open Settings")
settingsBtn["command"] = openSettings