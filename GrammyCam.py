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
largeFont = "Oswald 36 bold"

# Initialize CEC
cec.init()

# Rotate Camera
subprocess.Popen("v4l2-ctl --set-ctrl=rotate=90", shell = True)
#=========================================
#             ERROR DISPLAY
#=========================================
def showError(error, callback):
    errorWindow = tk.Tk()
    errorLabel = tk.Label(errorWindow,
                          text = error,
                          fg = red)
    errorLabel.pack(side = tk.TOP,
                    fill = tk.BOTH,
                    expand = 1)
    okButton = tk.Button(errorWindow,
                         text = "OK",
                         bg = red)
    okButton.pack(side = tk.BOTTOM)
    
#=========================================
#                PIN LOCK
#=========================================
# Button Commands
def setButtonCommands():
    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine
    global zero
    global cancel
    global backspace
    
    one["command"] = lambda: enterDigit('1')
    two["command"] = lambda: enterDigit('2')
    three["command"] = lambda: enterDigit('3')
    four["command"] = lambda: enterDigit('4')
    five["command"] = lambda: enterDigit('5')
    six["command"] = lambda: enterDigit('6')
    seven["command"] = lambda: enterDigit('7')
    eight["command"] = lambda: enterDigit('8')
    nine["command"] = lambda: enterDigit('9')
    zero["command"] = lambda: enterDigit('0')
    cancel["command"] = cancelPin
    backspace["command"] = backspace
    
def openPin():
    # PIN Window
    global pinWindow
    pinWindow = tk.Tk()
    pinWindow.configure(bg = "black")
    pinWindow.attributes("-fullscreen", True)
    
    # Frames
    display = tk.Frame(pinWindow,
                       bg = "black")
    display.pack(side = tk.TOP,
                 expand = 1,
                 fill = tk.BOTH)
    row1 = tk.Frame(pinWindow,
                    bg = "black")
    row1.pack(side = tk.TOP,
              expand = 1,
              fill = tk.BOTH)
    row2 = tk.Frame(pinWindow,
                    bg = "black")
    row2.pack(side = tk.TOP,
              expand = 1,
              fill = tk.BOTH)
    row3 = tk.Frame(pinWindow,
                    bg = "black")
    row3.pack(side = tk.TOP,
              expand = 1,
              fill = tk.BOTH)
    row4 = tk.Frame(pinWindow,
                    bg = "black")
    row4.pack(side = tk.TOP,
              expand = 1,
              fill = tk.BOTH)

    # Buttons
    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine
    global zero
    global cancel
    global backspace
    one = tk.Button(row1,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "1")
    one.pack(side = tk.LEFT,
             expand = 1,
             fill = tk.BOTH)
    two = tk.Button(row1,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "2")
    two.pack(side = tk.LEFT,
             expand = 1,
             fill = tk.BOTH)
    three = tk.Button(row1,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "3")
    three.pack(side = tk.LEFT,
               expand = 1,
               fill = tk.BOTH)
    four = tk.Button(row2,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "4")
    four.pack(side = tk.LEFT,
              expand = 1,
              fill = tk.BOTH)
    five = tk.Button(row2,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "5")
    five.pack(side = tk.LEFT,
              expand = 1,
              fill = tk.BOTH)
    six = tk.Button(row2,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "6")
    six.pack(side = tk.LEFT,
             expand = 1,
             fill = tk.BOTH)
    seven = tk.Button(row3,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "7")
    seven.pack(side = tk.LEFT,
               expand = 1,
               fill = tk.BOTH)
    eight = tk.Button(row3,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "8")
    eight.pack(side = tk.LEFT,
               expand = 1,
               fill = tk.BOTH)
    nine = tk.Button(row3,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "9")
    nine.pack(side = tk.LEFT,
              expand = 1,
              fill = tk.BOTH)
    cancel = tk.Button(row4,
                    bg = red,
                    fg = "white",
                    font = largeFont,
                    text = "Cancel")
    cancel.pack(side = tk.LEFT,
                expand = 1,
                fill = tk.BOTH)
    zero = tk.Button(row4,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "0")
    zero.pack(side = tk.LEFT,
              expand = 1,
              fill = tk.BOTH)
    backspace = tk.Button(row4,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "<")
    backspace.pack(side = tk.LEFT,
                   expand = 1,
                   fill = tk.BOTH)

    # Display Places
    global digit1
    global digit2
    global digit3
    global digit4
    
    digit1 = tk.Label(display,
                    bg = "grey",
                    fg = "white",
                    font = largeFont,
                    text = "")
    digit1.pack(side = tk.LEFT,
                expand = 1,
                fill = tk.BOTH)
    digit2 = tk.Label(display,
                    bg = "grey",
                    fg = "white",
                    font = largeFont,
                    text = "")
    digit2.pack(side = tk.LEFT,
                expand = 1,
                fill = tk.BOTH)
    digit3 = tk.Label(display,
                    bg = "grey",
                    fg = "white",
                    font = largeFont,
                    text = "")
    digit3.pack(side = tk.LEFT,
                expand = 1,
                fill = tk.BOTH)
    digit4 = tk.Label(display,
                    bg = "grey",
                    fg = "white",
                    font = largeFont,
                    text = "")
    digit4.pack(side = tk.LEFT,
                expand = 1,
                fill = tk.BOTH)
    
    setButtonCommands()

entry = ""
pin = "1234"

def updateDisplay():
    global entry
    global digit1
    global digit2
    global digit3
    global digit4
    digits = [digit1, digit2, digit3, digit4]
    enteredCount = len(entry)
    for digit in [0, 1, 2, 3]:
        if digit <= enteredCount - 1:
            digits[digit]["text"] = "*"
            digits[digit]["bg"] = purple
        else:
            digits[digit]["text"] = ""
            digits[digit]["bg"] = "grey"

def enterDigit(digit):
    global entry
    entry += digit
    updateDisplay()
    if len(entry) == 4:
        checkPin()

def backspace():
    global entry
    if len(entry) != 0:
        entry = entry.rstrip(entry[-1])
        updateDisplay()
    
def checkPin():
    global pinWindow
    global entry
    global pin
    if entry == pin:
        pinWindow.destroy()
        openSettings()
    else:
        cancelPin()
        
def cancelPin():
    global pinWindow
    global entry
    entry = ""
    pinWindow.destroy()

#=========================================
#             MAIN TP WINDOW
#=========================================
tp = tk.Tk()
tp.attributes("-fullscreen", True)
tp.configure(bg = "black")
tp.title = "Main TP"

# Button Functions
def joinCall():
    url = "http://meet.jit.si/GrammyCam"
    subprocess.Popen("echo 'as' | cec-client RPI -s -d 1",
                     shell = True)
    global callWindow
    callWindow = subprocess.Popen(["chromium-browser",
                                 "--kiosk",
                                 url])
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
    subprocess.Popen("echo 'volup' | cec-client RPI -s -d 1",
                     shell = True)

def volumeDown():
    subprocess.Popen("echo 'voldown' | cec-client RPI -s -d 1",
                     shell = True)
    
# tk buttons
pad = 10
joinBtn = tk.Button(tp,
                    text = "Join\nRoom",
                    bg = green,
                    fg = "white",
                    relief = tk.FLAT,
                    font = largeFont,
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
                     fg = "white",
                     relief = tk.FLAT,
                     font = largeFont,
                     command = volumeUp)
volUpBtn.pack(side = tk.TOP,
              fill = tk.BOTH,
              expand = 1,
              padx = pad,
              pady = pad)
volDownBtn = tk.Button(sideFrame,
                       text = "Volume -",
                       bg = blue,
                       fg = "white",
                       relief = tk.FLAT,
                       font = largeFont,
                       command = volumeDown)
volDownBtn.pack(side = tk.TOP,
                fill = tk.BOTH,
                expand = 1,
                padx = pad,
                pady = pad)
settingsBtn = tk.Button(sideFrame,
                        text = "Settings",
                        bg = purple,
                        fg = "white",
                        relief = tk.FLAT,
                        font = largeFont,
                        command = openPin)
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
                                fg = blue,
                                command = changeBrightness)
    brightnessSlider.pack()
    brightnessSlider.set(Backlight().brightness)
    
    powerFrame = tk.Frame(settingsWindow,
                          bg = "black")
    powerFrame.pack(side = tk.RIGHT,
                    fill = tk.BOTH)
    rebootBtn = tk.Button(powerFrame,
                          text = "Reboot",
                          bg = red,
                          relief = tk.FLAT,
                          font = largeFont,
                          command = reboot)
    rebootBtn.pack(side = tk.BOTTOM,
                   fill = tk.BOTH,
                   expand = 1)
    shutDownBtn = tk.Button(powerFrame,
                            text = "Shut Down",
                            bg = red,
                            relief = tk.FLAT,
                            font = largeFont,
                            command = shutDown)
    shutDownBtn.pack(side = tk.BOTTOM,
                     fill = tk.BOTH,
                     expand = 1)
    quitBtn = tk.Button(powerFrame,
                        text = "Quit",
                        bg = red,
                        relief = tk.FLAT,
                        font = largeFont,
                        command = close)
    quitBtn.pack(side = tk.BOTTOM,
                 fill = tk.BOTH,
                 expand = 1)

def changeBrightness(event):
    brightness = brightnessSlider.get()
    Backlight().brightness = brightness
        
def close():
    settingsWindow.destroy()
    tp.destroy()

def back():
    settingsWindow.desroy()
    
def shutDown():
    subprocess.Popen("sudo poweroff", shell = True)
    
def reboot():
    subprocess.Popen("sudo reboot", shell = True)