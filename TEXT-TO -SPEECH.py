import pyttsx3
import PySimpleGUI as sg

# initialize the engine
engine = pyttsx3.init()

# get available voices
voices = engine.getProperty('voices')

# set male and female voices
male_voice = voices[0].id
female_voice = voices[1].id

# define the layout of the GUI
layout = [
[sg.Text("Enter text to speak:")],
[sg.InputText(key="-INPUT-")],
[sg.Text("Select voice:")],
[sg.Radio("Male", "RADIO1", default=True, key="-MALE-"), sg.Radio("Female", "RADIO1", key="-FEMALE-")],
[sg.Text("Pitch:"), sg.Slider(range=(0, 500), default_value=250, orientation="h", key="-PITCH-"),sg.Text("Volume:"), sg.Slider(range=(0, 100), resolution=50, default_value=50, orientation="h", key="-VOLUME-")],
[sg.Text("Rate:"), sg.Slider(range=(0, 300), default_value=200, orientation="h", key="-RATE-")],
[sg.Button("Speak"), sg.Button("Exit")]
]


# create the window
window = sg.Window("Text-to-Speech App", layout, background_color="CYAN")


# main event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    text = values["-INPUT-"]
    if values["-MALE-"]:
        voice = male_voice
    else:
        voice = female_voice
    engine.setProperty('voice', voice)
    engine.say(text)
    engine.runAndWait()

# close the window and the engine
window.close()
engine.stop()