import PySimpleGUI as sg
from gtts import gTTS  #pip install gTTS
import os

parts=[
    [sg.Text('pick an image or dont does is look like i care'), sg.InputText(key='-file-'), sg.FileBrowse()],
    [sg.Image(key='-image-')],
    [sg.Button('show me thy image'), sg.Button('leave')]
]

window=sg.Window('window library',parts,resizable=True)

while True:
    event, value=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=='leave':
        sg.popup_annoying('you can try as much as you want but i will never make this button work')
    if event=='show me thy image':
        file_file=value['-file-']
        if file_file:
            window['-image-'].update(filename=file_file)
