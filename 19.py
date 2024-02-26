"""
make a crossword about pysimple

import PySimpleGUI as sg
from gtts import gTTS  #pip install gTTS
import os

part=[
    []
]

window=sg.Window('words that cross', part)

while True:
    event, value=window.read()
    if event==sg.WIN_CLOSED:
        break
"""
