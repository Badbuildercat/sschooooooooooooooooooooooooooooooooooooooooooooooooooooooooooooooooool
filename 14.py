"""
___________________________________________
|data format |  reading form               |
|____________|_____________________________|
|txt         |read() readline() readlines()|
|____________|_____________________________| 
|csv         |csv.reader()                 |
|____________|_____________________________|
|json        |json.load()                  |
|____________|_____________________________|

pysimplegui window stuff

___________________________________________________
|place definition   |say all the parts             | 
|window definiton   |win=sg.Window('name', part)   |
|main stuff         |event, value=window.read()    |
|close stuff        |if event==sg.WIN_CLOSED: break|
|__________________________________________________| 

      
"""
import PySimpleGUI as sg
from gtts import gTTS  #pip install gTTS
import os

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            stuff=file.read()
            return stuff
    except Exception as e:
        return f"problem has happend good luck | {e}"
def TTS(stuff):
    read=gTTS(stuff, lang='lv', slow=False)
    read.save('buttering.mp3')
    os.system('start buttering.mp3')

parts=[
    [sg.Text("pick a file to read:")],
    [sg.InputText(key='-butter?-'), sg.FileBrowse()],
    [sg.Button('Read'), sg.Button('Leave'), sg.Button('speakup'), sg.Button('Accept Deal')],
    [sg.Multiline(size=(50,10), key='-the_buttering-', disabled=True)]
]


window=sg.Window('placeholder name', parts)

while True:
    event, value=window.read()
    if event==sg.WIN_CLOSED:
        sg.popup_annoying("or just do that")
        break
    if  event=='Leave':
        sg.popup_annoying("You realy thought that would work you cant leave you are trapped forever")
    if event=="Read":
        filename=value['-butter?-']
        if filename:
            stuff=read_file(filename)
            window['-the_buttering-'].update(stuff)   
    if event=='Accept Deal':
        sg.popup_error('You Accepted and paid 400$ now you have Butter?')
    if event=='speakup':
        filename=value['-butter?-']
        stuff=TTS("Do you like butter well i sure hope you do becasue i have immensely large qauntitys of butter and i need to sell it soon so i will sell you 200kg of butter for the reasonable price of 2$ per kilo but you have to figure out how to transport the butter because once i sell it its not my  problem. So do we have a deal?")
            
