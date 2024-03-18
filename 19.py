"""
picture gallery

"""
import PySimpleGUI as sg
from gtts import gTTS  #pip install gTTS
import os
import io #input output operations
from PIL import Image # pip install Pillow

def get_image_file(directory):
    image_file=[f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpeg', '.jpg', '.gif'))]
    return image_file

def show_gallery(image_file, selected_index, window):
    if selected_index<len(image_file):
        filename=os.path.join(directory, image_file[selected_index])
        image=Image.open(filename)
        image.thumbnail((4000,4000))
        bio=io.BytesIO() 
        image.save(bio, format='PNG') #RAM moment?
        window['-image-'].update(data=bio.getvalue())
        window['-index-'].update(f'{selected_index +1} / {len(image_file)}')
    else:
        window['-image-'].update(filename='', size=(400,400))
        window['-index-'].update('0 / 0')

menu_def=[['File',['Close']],['Help',['Help']]]
part=[
    [sg.Menu(menu_def)],
    [sg.Text('pick the folder that has the images: '),sg.InputText(key='-file-', enable_events=True), sg.FileBrowse()],
    [sg.Image(key='-image-',size=(400,400))],
    [sg.Text('image:'), sg.Text('0 / 0',key='-index-')],
    [sg.Button('Leave'),sg.Button('Back'),sg.Button('Next')]
]

window=sg.Window('images that you can see', part, finalize=True)

while True:
    event, value=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=='Leave':
        sg.popup_annoying('Why do you keep trying it will never work just use the X button like a normal person')
    if event=='Close':
        sg.popup_annoying("This is no better than the leave button like i said use the X like a normal person")
    if event=='Help':
        sg.popup_annoying('all i can help you with is that you need to use the X button to leave')
    if event=='-file-':
        directory=value['-file-']
        image_file=get_image_file(directory)
        selected_index=0
        show_gallery(image_file, selected_index, window)
    if event=='Back':
        if selected_index>0:
            selected_index-=1
            show_gallery(image_file, selected_index, window)
    if event=='Next':
        if selected_index<len(image_file)-1:
            selected_index+=1
            show_gallery(image_file, selected_index, window)
       