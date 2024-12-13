import PySimpleGUI as sg
"""""
#how to make your own window theme
my_window_t={
BACKGROUND='#00ff0a',
}
sg.theme_add_new('yes', my_window_t)
sg.theme('yes')
"""
sg.theme('green')
parts=[
    [sg.Text('text is very long and text like')],
    [sg.Text('gimie your name'), sg.InputText()],
    [sg.Button('OK'), sg.Button('Close')] 
]       
#make the window
image='sv.ico'
window=sg.Window('The Window',parts,size=(420,180), icon=image)
# show the window
while True:
    things, value=window.read()
    if things==sg.WIN_CLOSED or things=='Close':
        break
# priint that name 
    print("my name is;",value[0])

window.close()