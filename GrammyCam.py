#!/usr/bin/env python3

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
largeFont = "Oswald 36"
largeFontBold = "Oswald 36 bold"
mediumFont = "Oswald 20"
mediumFontBold = "Oswald 20 bold"
smallFont = "Lato 14"

print("UI Elements Established")

# Initialize CEC
cec.init()
print("CEC Initialized")

# Rotate Camera
subprocess.Popen("v4l2-ctl --set-ctrl=rotate=90", shell = True)
print("Camera Rotated")

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
    errorWindow.mainloop()
    
print("End of Error Display definition")
    
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
    keypad = tk.Frame(pinWindow,
                     bg = "black")
    keypad.pack(side = tk.TOP,
                expand = 1,
                fill = tk.BOTH)
    keypad.columnconfigure((0, 1, 2), weight = 1)
    keypad.rowconfigure((0, 1, 2, 3), weight = 1)

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
    one = tk.Button(keypad,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "1")
    one.grid(row = 0,
             column = 0,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    two = tk.Button(keypad,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "2")
    two.grid(row = 0,
             column = 1,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    three = tk.Button(keypad,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "3")
    three.grid(row = 0,
             column = 2,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    four = tk.Button(keypad,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "4")
    four.grid(row = 1,
             column = 0,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    five = tk.Button(keypad,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "5")
    five.grid(row = 1,
             column = 1,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    six = tk.Button(keypad,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "6")
    six.grid(row = 1,
             column = 2,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    seven = tk.Button(keypad,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "7")
    seven.grid(row = 2,
             column = 0,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    eight = tk.Button(keypad,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "8")
    eight.grid(row = 2,
             column = 1,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    nine = tk.Button(keypad,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "9")
    nine.grid(row = 2,
             column = 2,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    cancel = tk.Button(keypad,
                    bg = red,
                    fg = "white",
                    font = largeFont,
                    text = "Cancel")
    cancel.grid(row = 3,
             column = 0,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    zero = tk.Button(keypad,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "0")
    zero.grid(row = 3,
             column = 1,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    backspace = tk.Button(keypad,
                    bg = blue,
                    fg = "white",
                    font = largeFont,
                    text = "<")
    backspace.grid(row = 3,
             column = 2,
             sticky = (tk.N, tk.S, tk.E, tk.W))

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
    pinWindow.mainloop()

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
        entry = ""
        openSettings()
    else:
        cancelPin()
        
def cancelPin():
    global pinWindow
    global entry
    entry = ""
    pinWindow.destroy()

print("End of PIN Entry definition")
    
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
    
    settingsWindow.mainloop()

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
    
print("End of Settings Window definition")

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
    #subprocess.Popen("echo 'as' | cec-client RPI -s -d 1", shell = True)
    global callWindow
    callWindow = subprocess.Popen(["chromium-browser",
                                 "--kiosk",
                                 url])
    joinBtn["bg"] = red
    joinBtn["activebackground"] = red
    joinBtn["text"] = "Leave\nRoom"
    joinBtn["command"] = endCall
    
def endCall():
    print("End Call")
    global callWindow
    callWindow.terminate()
    joinBtn["bg"] = green
    joinBtn["activebackground"] = green
    joinBtn["text"] = "Join\nRoom"
    joinBtn["command"] = joinCall
        
def volumeUp():
    subprocess.Popen("echo 'volup' | cec-client RPI -s -d 1", shell = True)
    print("Volume Up")

def volumeDown():
    subprocess.Popen("echo 'voldown' | cec-client RPI -s -d 1", shell = True)
    print("Volume Down")
    
# tk buttons
pad = 10
joinBtn = tk.Button(tp,
                    text = "Join\nRoom",
                    bg = green,
                    activebackground = green,
                    activeforeground = "white",
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
                     activebackground = blue,
                     activeforeground = "white",
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
                       activebackground = blue,
                    activeforeground = "white",
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
                        activebackground = purple,
                    activeforeground = "white",
                        fg = "white",
                        relief = tk.FLAT,
                        font = largeFont,
                        command = openPin)
settingsBtn.pack(side = tk.TOP,
                 fill = tk.BOTH,
                 padx = pad,
                 pady = pad)

tp.mainloop()

print("End of Main Window definition")