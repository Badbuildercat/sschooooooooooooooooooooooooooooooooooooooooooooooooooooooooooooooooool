#make a almost usless calculator that only + and x
import PySimpleGUI as sg
pc={'size':(7,2), 'font':('Calibri',18 ), 'button_color':("black", "#34fe03")}
stuff=[
    [sg.Text('Placeholder Text')],
    [sg.Button('7', **pc), sg.Button('8', **pc), sg.Button('9', **pc)],
    [sg.Button('4', **pc), sg.Button('5', **pc), sg.Button('6', **pc)],
    [sg.Button('1', **pc), sg.Button('2', **pc), sg.Button('3', **pc)],
    [sg.Button('0', **pc), sg.Button('.', **pc), sg.Button('=', **pc), sg.Button('+', **pc), sg.Button('x', **pc)]
]

window=sg.Window('The Window',stuff,size=(520,400))
while True:
    things, value=window.read()
    if things==sg.WIN_CLOSED:
        break

window.close()
