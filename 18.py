import PySimpleGUI as sg
from gtts import gTTS  #pip install gTTS
import os

part=[
    [sg.Text('pick or suffer the consequences of your actions')],
    [sg.Combo(['chicken','log','turnip','round object','dave?','cat','leave','come','car','table','egg','sqaurical object','bus','donkey','whats a hole full of donkeys','train','siberia','sea','boat','germany','france','tree','road','water','bridge','carrot','goat','ball','questions','paint','roll','joe','Ukraine','butter','track','hole','round','large','summer'], key='-combo-')],
    [sg.Checkbox('there is fog or is there i cant realy tell its odd because it seems there should be but there isnt', key='-box-')],
    [sg.Text('name:'), sg.InputText(key='-input-')],
    [sg.Button('copy file'), sg.Button('clear'), sg.Button('leave')],
    [sg.Output(size=(50,10), key='-output-')],
    [sg.Image(filename='sv.png', key='-image-')]
]

window=sg.Window('large hole', part , size=(600,600))

while True:
    event, value=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=='leave':
        sg.popup_annoying('why do you keep trying to make me put a leave button is the x button not enough for you?')
    if event=='copy file':
        stuff=value['-combo-']
        yes=value['-box-']
        inputs=value['-input-']

        filename='file that was made with code.txt'
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(f'you chose {stuff}\n')
            file.write(f'you good there buddy do you got some fog?  {yes}\n')
            file.write(f'your name probly is: {inputs}\n')
        window['-output-'].update(value=f'it was put in the file {filename}')
        window['-combo-'].update(value='')
        window['-box-'].update(value=False)
        window['-input-'].update(value='')
    if event=='clear':
        window['-combo-'].update(value='')
        window['-box-'].update(value=False)
        window['-input-'].update(value='')
        window['-output-'].update(value='')
