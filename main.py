#!/usr/bin/python3
import time

import PySimpleGUI as sg

from Logger import Logger
from LoggerWriterToFile import LoggerWriterToFile as Log_To_File


# Создаем список элементов для первой вкладки
tab1_layout = [
    [sg.Text('Input time:')],
    [sg.Input(key='-INPUT-')],
    [sg.Button('Convert')],
    [sg.Button('Reset', key='-RESET-')]
]
# Создаем список элементов для второй вкладки
tab2_layout = [
    [sg.Text('Choose convert to:')],
    [sg.Combo(['Seconds in minutes', 'Minutes in hours', 'Hours in days'], key='-OPTION-',
              default_value='Seconds in minutes')],
    [sg.Button('Choose')],
    [sg.Button('Reset', key='-RESET-')]
]
# Создаем список элементов для третьей вкладки
tab3_layout = [
    [sg.Text('Result:', size=(15, 1), justification='center')],
    [sg.Text(size=(40, 1), key='-RESULT-')]
]
# Создаем вкладки
tab_group_layout = [
    [sg.Tab('Time', tab1_layout, key='-TAB1-'), sg.Tab('Format', tab2_layout),
     sg.Tab('Result', tab3_layout, key='-TAB3-')]
]
# Создаем окно приложения
layout = [[sg.TabGroup(tab_group_layout)]]
window = sg.Window('Time Converter', layout)

# Initialize decorator and singleton
logger = Logger()
log_to_file = Log_To_File(logger)

if __name__ == '__main__':
    # Обработка событий
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Convert':
            try:
                result = int(values['-INPUT-'])
            except:
                log_to_file.log_error_to_file("errorLog", "The entered is not a number")
                continue

            if values['-OPTION-'] == 'Seconds in minutes':
                result = int(values['-INPUT-']) // 60
            elif values['-OPTION-'] == 'Minutes in hours':
                result = int(values['-INPUT-']) // 60
            elif values['-OPTION-'] == 'Hours in days':
                result = int(values['-INPUT-']) // 24

            try:
                window['-RESULT-'].update(f'Time: {result}')
            except:
                log_to_file.log_error_to_file("errorLog", "Result is not defined")

            window['-TAB3-'].select()
            log_to_file.log_info_to_file("infoLog", f'result = {result}')
        elif event == 'Choose':
            window['-TAB1-'].select()
        elif event == '-RESET-':
            window['-RESULT-'].update(value='')
            window.write_event_value('-INPUT-', '')
            window['-INPUT-'].update(value='')
            log_to_file.log_warning_to_file("warningFile", f'Result = {result} and Input = {values["-INPUT-"]} have been reset')
    window.close()
