import PySimpleGUI as sg
from PIL import Image
from main import img2text
import json

image = Image.open('image.jpg')
image.thumbnail((700, 700))
image.save('image.png')

column1 = [
    [
        sg.Image(filename='image.png', key='Image'),
        sg.VerticalSeparator(pad=None),
    ]
]
column2 = [
    [sg.Text('Паспорт выдан: ', size=(16, 1)), sg.Multiline('', size=(45, 4))],
    [sg.Text('', size=(16, 1))],
    [sg.HorizontalSeparator()],

    [sg.Text('Дата выдачи: ', size=(16, 1)), sg.InputText('', size=(12, 1))],
    [sg.Text('Код подразделения: ', size=(16, 1)), sg.InputText('', size=(8, 1))],
    [sg.Text('Серия: ', size=(16, 1)), sg.InputText('', size=(8, 1))],
    [sg.Text('Номер: ', size=(16, 1)), sg.InputText('', size=(8, 1))],
    [sg.Text('', size=(16, 1))],
    [sg.HorizontalSeparator()],

    [sg.Text('Фамилия: ', size=(16, 1)), sg.InputText('')],
    [sg.Text('Имя: ', size=(16, 1)), sg.InputText('')],
    [sg.Text('Отчество: ', size=(16, 1)), sg.InputText('')],
    [sg.Text('', size=(16, 1))],
    [sg.HorizontalSeparator()],

    [sg.Text('Пол: ', size=(16, 1)), sg.InputText('', size=(8, 1))],
    [sg.Text('Дата рождения: ', size=(16, 1)), sg.InputText('', size=(12, 1))],
    [sg.Text('', size=(16, 1))],
    [sg.HorizontalSeparator()],

    [sg.Text('Место рождения: ', size=(16, 1)), sg.Multiline('', size=(45, 4))],
    [sg.Text('', size=(16, 1))],
    [sg.Text('', size=(16, 1))],
    [sg.Text('', size=(16, 1))],
    [sg.Text('', size=(16, 1))],
    [sg.Text('', size=(16, 1))],
    [sg.Text('', size=(16, 1))],
    [sg.Text('', size=(16, 1))],
    [sg.Button('Подтвердить')],
]

layout = [
    [sg.Column(column1), sg.Column(column2)]
]

window = sg.Window('Распознавалочка', layout)

while True:  # The Event Loop
    fields = [
        'issued_by',
        'issues_date',
        'department_code',
        'series',
        'number',
        'surname',
        'name',
        'patronymic',
        'sex',
        'birth_date',
        'birth_place',
    ]

    event, values = window.read()
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break

    # text = img2text(image)

    # for field in fields:
    #     window[field].update(text[field])

    if event == 'Подтвердить':
        json.dump(dict(zip(fields, [i.strip() for i in values.values()])), open('test.json', 'w', encoding='cp1251'))
        break
