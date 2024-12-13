import PySimpleGUI as sg

part=[
[sg.Text('What is the designation of a panther tank?')],
[sg.Radio('Panzer 4', 'radio1',default=False, key='-good1-'), sg.Radio('Panzer 5', 'radio1',default=False, key='-good3-'), sg.Radio('Panzer 6', 'radio1',default=False, key='-good1-'), sg.Text('', key='-answer-')],
[sg.Text('What is the length of a football field?')],
[sg.Radio('90m', 'radio2',default=False, key='-1-'), sg.Radio('100m', 'radio2',default=False, key='-1-'), sg.Radio('110m', 'radio2',default=False, key='-3-'), sg.Text('', key='-answer2-')],
[sg.Text('What was the first jet airplane?')],
[sg.Radio('He 178', 'radio3',default=False, key='-4-'), sg.Radio('Ar 234', 'radio3',default=False, key='-1-'), sg.Radio('Me 262', 'radio3',default=False, key='-1-'), sg.Text('', key='-answer3-')],
[sg.Text('How large is a minecraft world?')],
[sg.Radio('60mil x 60mil', 'radio4',default=False, key='-5-'), sg.Radio('80mil x 80mil', 'radio4',default=False, key='-1-'), sg.Radio('100mil x 100mil', 'radio4',default=False, key='-1-'), sg.Text('', key='-answer4-')],
[sg.Text('How many times have i made a leave button that does not work?')],
[sg.Radio('4 times', 'radio5',default=False, key='-1-'), sg.Radio('5 times', 'radio5',default=False, key='-1-'), sg.Radio('6 times', 'radio5',default=False, key='-6-'), sg.Text('', key='-answer5-')],
[sg.Text('What year was constantinople conquered by the Ottomans?')],
[sg.Radio('1444', 'radio6',default=False, key='-1-'), sg.Radio('1453', 'radio6',default=False, key='-7-'), sg.Radio('1462', 'radio6',default=False, key='-1-'), sg.Text('', key='-answer6-')],
[sg.Text('Wich shotgun ammo is the best for home defence?')],
[sg.Radio('Slugs', 'radio7',default=False, key='-1-'), sg.Radio('Birdshot', 'radio7',default=False, key='-1-'), sg.Radio('Buckshot', 'radio7',default=False, key='-8-'), sg.Text('', key='-answer7-')],
[sg.Text('When did the western Roman empire collapse')],
[sg.Radio('476', 'radio8',default=False, key='-9-'), sg.Radio('486', 'radio8',default=False, key='-1-'), sg.Radio('496', 'radio8',default=False, key='-1-'), sg.Text('', key='-answer8-')],
[sg.Button('Check'), sg.Button('Save')]
]

window=sg.Window('test', part)

while True:
    event, value=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=='Check' and value['-good3-']==True:
        window['-answer-'].update('correct')
    if event=='Check' and value['-good3-']==False:
        window['-answer-'].update('incorrect')
    if event=='Check' and value['-3-']==True:
        window['-answer2-'].update('correct')
    if event=='Check' and value['-3-']==False:
        window['-answer2-'].update('incorrect')
    if event=='Check' and value['-4-']==True:
        window['-answer3-'].update('correct')
    if event=='Check' and value['-4-']==False:
        window['-answer3-'].update('incorrect')
    if event=='Check' and value['-5-']==True:
        window['-answer4-'].update('correct')
    if event=='Check' and value['-5-']==False:
        window['-answer4-'].update('incorrect')
    if event=='Check' and value['-6-']==True:
        window['-answer5-'].update('correct')
    if event=='Check' and value['-6-']==False:
        window['-answer5-'].update('incorrect')
    if event=='Check' and value['-7-']==True:
        window['-answer6-'].update('correct')
    if event=='Check' and value['-7-']==False:
        window['-answer6-'].update('incorrect')
    if event=='Check' and value['-8-']==True:
        window['-answer7-'].update('correct')
    if event=='Check' and value['-8-']==False:
        window['-answer7-'].update('incorrect')
    if event=='Check' and value['-9-']==True:
        window['-answer8-'].update('correct')
    if event=='Check' and value['-9-']==False:
        window['-answer8-'].update('incorrect')
    if event=='Save':
        sg.popup_annoying('Take a screenshot with "windows + shift + s"')
