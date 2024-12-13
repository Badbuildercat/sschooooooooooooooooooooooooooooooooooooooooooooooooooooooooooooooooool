"""
pysimple GUI
goal - make an actaul calculator
result - a broken calculator that only remembers the second input
"""
import PySimpleGUI as sg

# time for functions
def calculate(num1, num2, operation):
    try:
        num1=float(num1)
        num2=float(num2)
        if operation == '+':
            resault=num1 + num2
        elif operation == 'x':
            resault=num1 * num2
        elif operation == '-':
            resault=num1 - num2
    except ValueError:
        return "Problems have hapened"
    return resault

#make the stuff save
current_input='' # 1234567890
current_operation='' # + x



#make the gui places

layout=[
    [sg.InputText(key='-DISPLAY-',size=(20,1), justification='right',readonly=True)],
    [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('+')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('x')],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('C')],
    [sg.Button('0'), sg.Button('='), sg.Button('Exit'), sg.Button('-')]
]

#make a window

window=sg.Window('calculator', layout, resizable=True)

#show the window with a cycle and break it when it closes

while True:
    event, value=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=='Exit':
        sg.popup_annoying("NO")
#if number is pressed then add it to the text box
    elif event in '1234567890':
        current_input += event
        window['-DISPLAY-'].update(current_input)
#if the + or x button is pressed than give the answer and clear  the input window
    elif event in '+x-':
        current_operation=event
        current_input=''
        window['-DISPLAY-'].update(current_input)
#if you click C it clears everything
    elif event == 'C':
        current_operation=''
        current_input=''
        window['-DISPLAY-'].update(current_input)
#if the = button is pressed make the calculation and put it in the text box
    elif event == '=':
        resault=calculate(current_input, value['-DISPLAY-'], current_operation)
        window['-DISPLAY-'].update(resault  if resault is not None else '') 
        current_input=str(resault) if resault is not None else ''






window.close