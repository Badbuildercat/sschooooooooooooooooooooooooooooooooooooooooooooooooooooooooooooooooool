import PySimpleGUI as sg

layout=[
    [sg.Button('click')],
    [sg.Button('OK'), sg.InputText(key='-IN-', enable_events=True)],
    [sg.Text('name now'), sg.InputText(key='-INN-', enable_events=True)],
    [sg.Text('last name now'), sg.InputText(key='-INNN-', enable_events=True)],
    [sg.Button('the button is sus')],
    [sg.Text('', key='-SUS-')]
]
window=sg.Window('name', layout)
while True:
    event, value=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=='click':
        print("how dare you touch thy button")
    if event=='OK':
        print(value['-IN-'])
    if event=='the button is sus':
        print(f"Your a Communist {value['-INN-']} {value['-INNN-']}.")
    elif event=='the button is sus':
        if value['-INN-'] and value['-INNN-']:
            window['-SUS-'].update(f"Your a Communist {value['-INN-']} {value['-INNN-']}!")
        else:
            sg.popup_annoying('There was an Error no idea what it was tho')

window.close()