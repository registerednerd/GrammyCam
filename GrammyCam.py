import tkinter as tk
import cec
import subprocess
from rpi_backlight import Backlight

# UI Colors
charcoal = "#363635"
red = "#BD9391"
blue = "#A2C7E5"
green = "#61E786"
purple = "#9D8DF1"

# Initialize CEC
cec.init()

# Rotate Camera
subprocess.Popen("v4l2-ctl --set-ctrl=rotate=90", shell = True)


#=========================================
#             MAIN TP WINDOW
#=========================================
tp = tk.Tk()
tp.attributes("-fullscreen", True)
tp.configure(bg = "black")
tp.title = "Main TP"

# Button Functions
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
    
def endCall():
    print("End Call")
    global callWindow
    callWindow.terminate()
    joinBtn["bg"] = green
    joinBtn["text"] = "Join\nRoom"
    joinBtn["command"] = joinCall
        
def volumeUp():
    subprocess.Popen("echo 'volup' | cec-client RPI -s -d 1", shell = True)

def volumeDown():
    subprocess.Popen("echo 'voldown' | cec-client RPI -s -d 1", shell = True)
    
# tk buttons
pad = 10
joinBtn = tk.Button(tp,
                    text = "Join\nRoom",
                    bg = green,
                    fg = "white",
                    relief = tk.FLAT,
                    font = "Helvetica 36 bold",
                    command = joinCall)
joinBtn.pack(side = tk.LEFT,
             fill = tk.BOTH,
             expand = 1,
             padx = pad,
             pady = pad)
sideFrame = tk.Frame(tp,bg = "black")
sideFrame.pack(side = tk.RIGHT,
               fill = tk.BOTH)
volUpBtn = tk.Button(sideFrame,
                     text = "Volume +",
                     bg = blue,
                     relief = tk.FLAT,
                     font = "Helvetica 36 bold",
                     command = volumeUp)
volUpBtn.pack(side = tk.TOP,
              fill = tk.BOTH,
              expand = 1,
              padx = pad,
              pady = pad)
volDownBtn = tk.Button(sideFrame,
                       text = "Volume -",
                       bg = blue,
                       relief = tk.FLAT,
                       font = "Helvetica 36 bold",
                       command = volumeDown)
volDownBtn.pack(side = tk.TOP,
                fill = tk.BOTH,
                expand = 1,
                padx = pad,
                pady = pad)
settingsBtn = tk.Button(sideFrame,
                        text = "Settings",
                        bg = purple,
                        relief = tk.FLAT,
                        font = "Helvetica 36 bold",)
settingsBtn.pack(side = tk.TOP,
                 fill = tk.BOTH,
                 padx = pad,
                 pady = pad)
    
    
    
    
#=========================================
#           SETTINGS WINDOW
#=========================================

def openSettings():
    global settingsWindow
    global brightnessSlider
    settingsWindow = tk.Tk()
    settingsWindow.attributes("-fullscreen", True)
    settingsWindow.configure(bg = "black")
    
    brightnessSlider = tk.Scale(settingsWindow,
                                from_=5,
                                to = 100,
                                orient = tk.HORIZONTAL,
                                command = changeBrightness)
    brightnessSlider.pack()
    brightnessSlider.set(Backlight().brightness)
settingsBtn["command"] = openSettings

def changeBrightness(event):
    brightness = brightnessSlider.get()
    Backlight().brightness = brightness
        
def close():
    settingsWindow.destroy()
    tpWindow.destroy()
