import PySimpleGUI as sg
from gtts import gTTS  #pip install gTTS
import os

menu_def=['help',['Help',['Help?',['HELP?',['HELP!']]]]]

parts=[
    [sg.Menu(menu_def)],
    [sg.Text("name:"), sg.InputText(key='-butter-')],
    [sg.Text("lastname:"), sg.InputText(key='-butter?-')],
    [sg.Multiline(size=(50,10), key='-the_buttering-', disabled=True)],
    [sg.Button('Print'), sg.Button('Leave')],
    [sg.Combo(['Bob','Bill','Joe','Dave'], key='-c-', enable_events=True)],
    [sg.Button('you choose')],
    [sg.Text('', key='-p-')]
]



window=sg.Window('placeholder name', parts)

while True:
    event, value=window.read()
    if event==sg.WIN_CLOSED:
        sg.popup_auto_close("or just do that", auto_close_duration=1)
        break
    if  event=='Leave':
        sg.popup_annoying("You realy thought that would work you cant leave you are trapped forever")
    if event=='Print':
        stuff= 'your name is ' + value['-butter-'] + ' ' + value['-butter?-']
        window['-the_buttering-'].update(stuff)
    elif event=='you choose':
        mine_pick=value['-c-']
        window['-p-'].update(f'you chose: {mine_pick}')
    if event=='HELP!':
        sg.popup_annoying('looser')
        break