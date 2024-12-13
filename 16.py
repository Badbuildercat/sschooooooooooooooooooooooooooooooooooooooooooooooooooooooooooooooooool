"""
1) give me a checkbox - checkbox
2) i want the radial button - radio
3) how to picker belt - menu and other stuff
4) the list that falls - combobox
"""
import PySimpleGUI as sg
from gtts import gTTS  #pip install gTTS
import os

menu_def=[['File',['Leave']], ['Edit',['Save',['name',['Leave?',['LEAVE?',['LEAVE!']]]],['where',['why']]]]]

parts=[
    [sg.Menu(menu_def)],
    [sg.T("")],
    [sg.T("    "), sg.Button("The Button", size=(8,4)), sg.T(""), sg.Button("The button", size=(8,4))],
    [sg.T("")],
    [sg.T("    "),sg.Checkbox('Print', default=False, key='-check-')],
    [sg.T('    '), sg.Radio('Not Communist', 'radio1',default=False, key='-good-')],
    [sg.T('    '), sg.Radio('Communist', 'radio1',default=False, key='-bad-')],
    [sg.T('    '), sg.Radio('Not', 'radio1',default=False, key='-goo1d-')],
    [sg.Multiline(size=(60,10), key='-sentence-')],
    [sg.Button('leave')]
]

window=sg.Window('placeholder name', parts, size=(500,500))

while True:
    event, value=window.read()
    if event==sg.WIN_CLOSED:
        sg.popup_error("You can not leave i will not let you!")
    if event=='LEAVE!' and value['-good-']:
        break
    if event=='LEAVE!':
        sg.popup_annoying('You realy thought that would work')
    if event=='leave':
        sg.popup_annoying('its never that easy')
    if event=='why':
        sg.popup_annoying('Why not?')
    if event=='Leave':
        sg.popup_annoying('you are not going to escape me')
    if event=='The button':
        sg.popup_annoying('Why would you think that would work?')
    if event=="The Button":
        if value['-check-']==True and value['-good-']:
            window['-sentence-'].update("Good answer your free to go.")
        elif value['-check-']==True and value['-bad-']:
            window['-sentence-'].update("Wrong answer comrade off to the gulag with you!")
        elif value['-check-']==True and value['-goo1d-']:
            window['-sentence-'].update("I see no Answer well i wont be leting you past anytime soon")


