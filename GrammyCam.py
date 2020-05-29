#!/usr/bin/env python3

import tkinter as tk
import cec
import subprocess
import sys
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
                    activebackground = blue,
                    fg = "black",
                    font = largeFont,
                    text = "1")
    one.grid(row = 0,
             column = 0,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    two = tk.Button(keypad,
                    bg = blue,
                    activebackground = blue,
                    fg = "black",
                    font = largeFont,
                    text = "2")
    two.grid(row = 0,
             column = 1,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    three = tk.Button(keypad,
                    bg = blue,
                      activebackground = blue,
                    fg = "black",
                    font = largeFont,
                    text = "3")
    three.grid(row = 0,
             column = 2,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    four = tk.Button(keypad,
                    bg = blue,
                    activebackground = blue,
                    fg = "black",
                    font = largeFont,
                    text = "4")
    four.grid(row = 1,
             column = 0,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    five = tk.Button(keypad,
                    bg = blue,
                    activebackground = blue,
                    fg = "black",
                    font = largeFont,
                    text = "5")
    five.grid(row = 1,
             column = 1,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    six = tk.Button(keypad,
                    bg = blue,
                    activebackground = blue,
                    fg = "black",
                    font = largeFont,
                    text = "6")
    six.grid(row = 1,
             column = 2,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    seven = tk.Button(keypad,
                    bg = blue,
                    activebackground = blue,
                    fg = "black",
                    font = largeFont,
                    text = "7")
    seven.grid(row = 2,
             column = 0,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    eight = tk.Button(keypad,
                    bg = blue,
                    activebackground = blue,
                    fg = "black",
                    font = largeFont,
                    text = "8")
    eight.grid(row = 2,
             column = 1,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    nine = tk.Button(keypad,
                    bg = blue,
                    activebackground = blue,
                    fg = "black",
                    font = largeFont,
                    text = "9")
    nine.grid(row = 2,
             column = 2,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    cancel = tk.Button(keypad,
                    bg = red,
                    activebackground = red,
                    fg = "black",
                    font = largeFont,
                    text = "X",
                    command = cancelPin)
    cancel.grid(row = 3,
             column = 0,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    zero = tk.Button(keypad,
                    bg = blue,
                    activebackground = blue,
                    fg = "black",
                    font = largeFont,
                    text = "0")
    zero.grid(row = 3,
             column = 1,
             sticky = (tk.N, tk.S, tk.E, tk.W))
    backspace = tk.Button(keypad,
                    bg = purple,
                    activebackground = purple,
                    fg = "black",
                    font = largeFont,
                    text = "<",
                    command = backspace)
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
    
#=========================================
#           SETTINGS WINDOW
#=========================================

def openSettings():
    global settingsWindow
    global brightnessSlider
    global roomIdString
    global roomId
    global urlLabel
    settingsWindow = tk.Tk()
    settingsWindow.attributes("-fullscreen", True)
    settingsWindow.configure(bg = "black")
    settingsWindow.columnconfigure(0, weight = 3)
    settingsWindow.columnconfigure(1, weight = 9)
    settingsWindow.columnconfigure(2, weight = 4)
    settingsWindow.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight = 1)

    brightnessLabel = tk.Label(settingsWindow,
                               bg = "black",
                               fg = "white",
                               font = mediumFontBold,
                               text = "Brightness")
    brightnessLabel.grid(row = 2,
                         column = 0)
    brightnessSlider = tk.Scale(settingsWindow,
                                from_=5,
                                to = 100,
                                orient = tk.HORIZONTAL,
                                fg = blue,
                                bg = "black",
                                bd = 0,
                                highlightthickness = 0,
                                font = smallFont,
                                width = 40,
                                sliderrelief = tk.FLAT,
                                highlightcolor = blue,
                                command = changeBrightness)
    brightnessSlider.set(Backlight().brightness)
    brightnessSlider.grid(row = 2,
                          column = 1,
                          padx = 10,
                          sticky = "NSEW")
    
    roomLabel = tk.Label(settingsWindow,
                         font = mediumFontBold,
                         fg = "white",
                         bg = "black",
                         text = "Room ID")
    roomLabel.grid(row = 4,
                   column = 0)
    roomIdString = tk.StringVar()
    roomId = tk.Entry(settingsWindow,
                      font = mediumFontBold,
                      textvariable = roomIdString)
    roomId.grid(row = 4,
                column = 1,
                sticky = "EW",
                padx = 10)
    
    urlLabel = tk.Label(settingsWindow,
                        bg = "black",
                        fg = "white",
                        font = smallFont)
    urlLabel.grid(row = 6,
                  column = 0,
                  columnspan = 2)
    updateRoomId()
    
    setBtn = tk.Button(settingsWindow,
                          text = "Set",
                          bg = green,
                          activebackground = green,
                          fg = "black",
                          relief = tk.FLAT,
                          font = mediumFont,
                          command = setRoomId)
    setBtn.grid(row = 5,
                column = 1)
    
    backBtn = tk.Button(settingsWindow,
                        text = "Back",
                        bg = green,
                        activebackground = green,
                        relief = tk.FLAT,
                        font = mediumFont,
                        command = back)
    backBtn.grid(row = 0,
                 column = 0,
                 sticky = "NW")
    
    updateBtn = tk.Button(settingsWindow,
                          text = "Update",
                          bg = purple,
                          activebackground = purple,
                          relief = tk.FLAT,
                          font = largeFont,
                          command = update)
    updateBtn.grid(row = 0,
                   column = 2,
                   rowspan = 2,
                   sticky = "NSEW")
    rebootBtn = tk.Button(settingsWindow,
                          text = "Reboot",
                          bg = red,
                          activebackground = red,
                          relief = tk.FLAT,
                          font = largeFont,
                          command = reboot)
    rebootBtn.grid(row = 6,
                   column = 2,
                   rowspan = 2,
                   sticky = "NSEW")
    shutDownBtn = tk.Button(settingsWindow,
                            text = "Shut Down",
                            bg = red,
                            activebackground = red,
                            relief = tk.FLAT,
                            font = largeFont,
                            command = shutDown)
    shutDownBtn.grid(row = 4,
                     column = 2,
                     rowspan = 2,
                     sticky = "NSEW")
    quitBtn = tk.Button(settingsWindow,
                        text = "Quit",
                        bg = red,
                        activebackground = red,
                        relief = tk.FLAT,
                        font = largeFont,
                        command = close)
    quitBtn.grid(row = 2,
                 column = 2,
                 rowspan = 2,
                 sticky = "NSEW")
    
    settingsWindow.mainloop()

def changeBrightness(event):
    brightness = brightnessSlider.get()
    Backlight().brightness = brightness
    
    
def updateRoomId():
    global roomIdString
    global urlLabel
    roomFile = open("/home/pi/GrammyCam/roomId", "r")
    url = roomFile.readline()
    roomFile.close()
    roomName = url.lstrip("https://meet.jit.si/")
    print("Room Name: " + roomName)
    print("URL: " + url)
    roomIdString.set(roomName)
    urlLabel["text"] = ("Invite people to: " + url)
    
def setRoomId():
    global roomId
    roomFile = open("/home/pi/GrammyCam/roomId", "w")
    roomFile.write("https://meet.jit.si/" + roomId.get())
    roomFile.close()
    updateRoomId()
    
def update():
    subprocess.Popen("/home/pi/GrammyCam/Update", shell = True)
    close()
        
def close():
    settingsWindow.destroy()
    tp.destroy()
    sys.exit()

def back():
    settingsWindow.destroy()
    
def shutDown():
    subprocess.Popen("sudo poweroff", shell = True)
    
def reboot():
    subprocess.Popen("sudo reboot", shell = True)
    
#=========================================
#             MAIN TP WINDOW
#=========================================
tp = tk.Tk()
tp.attributes("-fullscreen", True)
tp.configure(bg = "black")
tp.title = "Main TP"
tp.columnconfigure(0, weight = 14)
tp.columnconfigure(1, weight = 3)
tp.rowconfigure((0, 1, 2), weight = 3)

# Button Functions
def joinCall():
    roomFile = open("/home/pi/GrammyCam/roomId", "r")
    url = roomFile.readline()
    roomFile.close()
    #subprocess.Popen("echo 'as' | cec-client RPI -s -d 1", shell = True)
    cec.set_active_source()
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
    cec.volume_up()

def volumeDown():
    cec.volume_down()
    
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
joinBtn.grid(row = 1,
             column = 0,
             rowspan = 2,
             sticky = "NSEW",
             padx = pad,
             pady = pad)

volUpImg = tk.PhotoImage(file = "/home/pi/GrammyCam/images/VolUp.png")
volDownImg = tk.PhotoImage(file = "/home/pi/GrammyCam/images/VolDown.png")
settingsImg = tk.PhotoImage(file = "/home/pi/GrammyCam/images/Settings.png")
logo = tk.PhotoImage(file = "/home/pi/GrammyCam/images/Wide.png").subsample(2, 2)

logoPane = tk.Label(tp,
                    image = logo,
                    bg = "black",
                    bd = 0,
                    highlightthickness = 0)
logoPane.grid(row = 0,
              column = 0,
              sticky = "NS")

volUpBtn = tk.Button(tp,
                     image = volUpImg,
                     bg = blue,
                     activebackground = blue,
                     activeforeground = "white",
                     fg = "white",
                     relief = tk.FLAT,
                     font = largeFont,
                     command = volumeUp)
volUpBtn.grid(row = 0,
              column = 1,
              sticky = "NSEW",
              padx = pad,
              pady = pad)

volDownBtn = tk.Button(tp,
                       image = volDownImg,
                       bg = blue,
                       activebackground = blue,
                       activeforeground = "white",
                       fg = "white",
                       relief = tk.FLAT,
                       font = largeFont,
                       command = volumeDown)
volDownBtn.grid(row = 1,
                column = 1,
                sticky = "NSEW",
                padx = pad,
                pady = pad)

settingsBtn = tk.Button(tp,
                        image = settingsImg,
                        bg = purple,
                        activebackground = purple,
                    activeforeground = "white",
                        fg = "white",
                        relief = tk.FLAT,
                        font = largeFont,
                        command = openPin)
settingsBtn.grid(row = 2,
                 column = 1,
                 sticky = "NSEW",
                 padx = pad,
                 pady = pad)

tp.mainloop()