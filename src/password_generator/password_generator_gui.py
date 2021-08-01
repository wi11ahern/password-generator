import PySimpleGUI as sg

from src.password_generator.shuffled_password_generator import ShuffledPasswordGenerator
from src.password_generator.human_readable_password_generator import HumanReadablePasswordGenerator


class PasswordGeneratorGui:

    def create_gui(self) -> None:
        body_text_font = ('Aerial', 16)
        frame_title_font_size = ('Aerial', 20)

        password_options_column_one_layout = [
            [
                sg.Text(
                    text='Password Length',
                    justification='left',
                    font=body_text_font
                )
            ],
            [
                sg.Checkbox(
                    key='-DIGITS-',
                    text='Include Numbers',
                    default=True,
                    font=body_text_font
                )
            ],
            [
                sg.Checkbox(
                    key='-SPECIAL_CHARS-',
                    text='Include Special Characters',
                    default=True,
                    font=body_text_font
                )
            ],
            [
                sg.Slider(
                    key='-PASSWORD_LENGTH-',
                    range=(8, 100),
                    default_value=8,
                    size=(39, 10),
                    orientation='horizontal',
                    font=body_text_font
                )
            ]
        ]

        password_options_column_two_layout = [
            [
                sg.Checkbox(
                    key='-HR_UPPERCASE-',
                    text='Include Uppercase Words',
                    default=False,
                    font=body_text_font
                )
            ],
            [
                sg.Checkbox(
                    key='-HR_SPECIAL_CHARS-',
                    text='Include Special Characters',
                    default=False,
                    font=body_text_font
                )
            ],
            [
                sg.Checkbox(
                    key='-HR_NUMBERS-',
                    text='Include Numbers',
                    default=False,
                    font=body_text_font
                )
            ],
            [
                sg.Text(
                    text='Delimiter Type',
                    justification='left',
                    font=body_text_font
                )
            ],
            [
                sg.DropDown(
                    key='-HR_DELIMITER_TYPE-',
                    values=['Dash', 'Underscore', 'Space', 'Comma', 'Period'],
                    default_value='Dash',
                    enable_events=True,
                    font=body_text_font
                )
            ],
            [
                sg.Text(
                    text='Number of Words',
                    justification='left',
                    font=body_text_font
                )
            ],
            [
                sg.Slider(
                    key='-HR_NUM_OF_WORDS-',
                    range=(4, 20),
                    default_value=4,
                    size=(39, 10),
                    orientation='horizontal',
                    font=body_text_font
                )
            ],
        ]

        password_options_layout = [
            [
                sg.DropDown(
                    key='-OPTIONS_LIST-',
                    values=['Shuffled Passwords', 'Human-Readable Passwords'],
                    default_value='Shuffled Passwords',
                    enable_events=True,
                    pad=(0, 10),
                    font=body_text_font
                )
            ],
            [
                sg.Column(
                    key='-PO_COL_1-',
                    layout=password_options_column_one_layout,
                    size=(400, 150)
                ),
                sg.Column(
                    key='-PO_COL_2-',
                    layout=password_options_column_two_layout,
                    size=(400, 230),
                    visible=False
                )
            ],
        ]

        output_column_layout = [
            [
                sg.Output(
                    key='-OUTPUT-',
                    font=body_text_font,
                    echo_stdout_stderr=False,
                    pad=(4, 4),
                    size=(36, 1)
                )
            ]
        ]
        output_frame_layout = [
            [
                sg.Column(
                    key='-OUT_COL_1-',
                    layout=output_column_layout,
                    size=(400, 50),
                    visible=True
                )
            ]
        ]

        button_frame_layout = [
            [
                sg.Button(
                    button_text='Generate',
                    key='-GENERATE-',
                    font=body_text_font
                ),
                sg.Button(
                    button_text='Reset Options',
                    key='-RESET-',
                    font=body_text_font
                ),
                sg.Button(
                    button_text='Clear Output',
                    key='-CLEAR-',
                    font=body_text_font
                ),
                sg.Button(
                    button_text='Exit',
                    key='-EXIT-',
                    font=body_text_font
                ),
            ]
        ]

        layout = [
            [
                sg.Frame(
                    title='Password Options',
                    layout=password_options_layout,
                    element_justification='c',
                    font=frame_title_font_size
                )
            ],
            [
                sg.Frame(
                    title='Generated Password',
                    layout=output_frame_layout,
                    element_justification='c',
                    font=frame_title_font_size
                )
            ],
            [
                sg.Frame(
                    title='',
                    layout=button_frame_layout,
                    element_justification='c',
                    border_width=0
                )
            ]
        ]

        window = sg.Window(
            title='Password Generator',
            layout=layout,
            margins=(50, 50),
            auto_size_text=True,
            auto_size_buttons=True,
            resizable=True,
            element_justification='c',
        ).finalize()

        while True:
            event, values = window.read()

            if event == '-GENERATE-' and window['-PO_COL_1-'].visible:
                password_generator = ShuffledPasswordGenerator(
                    password_length=int(values['-PASSWORD_LENGTH-']),
                    include_numbers=values['-DIGITS-'],
                    include_special_chars=values['-SPECIAL_CHARS-'],
                )
                password = password_generator.generate_password()
                window['-OUTPUT-'].update(password)

            elif event == '-GENERATE-' and window['-PO_COL_2-'].visible:
                human_readable_password_generator = HumanReadablePasswordGenerator(
                    number_of_words=int(values['-HR_NUM_OF_WORDS-']),
                    word_delimiter=values['-HR_DELIMITER_TYPE-'],
                    include_uppercase_words=values['-HR_UPPERCASE-'],
                    include_special_chars=values['-HR_SPECIAL_CHARS-'],
                    include_numbers=values['-HR_NUMBERS-']
                )
                password = human_readable_password_generator.generate_password()
                window['-OUTPUT-'].update(password)

            if event == '-OPTIONS_LIST-':
                if values['-OPTIONS_LIST-'] == 'Shuffled Passwords':
                    window['-PO_COL_1-'].update(visible=True)
                    window['-PO_COL_2-'].update(visible=False)

                elif values['-OPTIONS_LIST-'] == 'Human-Readable Passwords':
                    window['-PO_COL_1-'].update(visible=False)
                    window['-PO_COL_2-'].update(visible=True)

            if event == '-RESET-':
                if '-DIGITS-' in values.keys():
                    window.FindElement('-DIGITS-').Update(True)

                if '-SPECIAL_CHARS-' in values.keys():
                    window.FindElement('-SPECIAL_CHARS-').Update(True)

                if '-PASSWORD_LENGTH-' in values.keys():
                    window.FindElement('-PASSWORD_LENGTH-').Update(0)

                if '-HR_UPPERCASE-' in values.keys():
                    window.FindElement('-HR_UPPERCASE-').Update(False)

                if '-HR_SPECIAL_CHARS-' in values.keys():
                    window.FindElement('-HR_SPECIAL_CHARS-').Update(False)

                if '-HR_NUMBERS-' in values.keys():
                    window.FindElement('-HR_NUMBERS-').Update(0)

                if '-HR_DELIMITER_TYPE-' in values.keys():
                    window.FindElement('-HR_DELIMITER_TYPE-').Update('Dash')

                if '-HR_NUM_OF_WORDS-' in values.keys():
                    window.FindElement('-HR_NUM_OF_WORDS-').Update(0)

            if event == '-CLEAR-':
                window.FindElement('-OUTPUT-').Update('')

            if event == '-EXIT-' or event == sg.WIN_CLOSED:
                break

        window.close()

