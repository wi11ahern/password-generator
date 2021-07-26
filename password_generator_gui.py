import PySimpleGUI as sg

from pasword_generator import PasswordGenerator


class PasswordGeneratorGui:

    def create_gui(self) -> None:
        password_options_frame_layout = [
            [sg.Text(text='Password Length', justification='left')],
            [sg.Slider(key='-PASSWORD_LENGTH-', range=(6, 100), default_value=6, orientation='horizontal')],
            [sg.Checkbox(key='-DIGITS-', text='Include Digits', default=True)],
            [sg.Checkbox(key='-SPECIAL_CHARS-', text='Include Special Characters', default=True)],
            [sg.Text(text='Keywords\n(Separate keywords with a space.', justification='left')],
            [sg.Input(key='-KEYWORDS-', justification='left', size=(30, 1))],
        ]

        output_frame_layout = [
            [sg.Output(key='-OUTPUT-', size=(35, 14))]
        ]

        button_frame_layout = [
            [
                sg.Button('Generate', key='-GENERATE-'),
                sg.Button('Reset', key='-RESET-'),
                sg.Button('Clear Output', key='-CLEAR-'),
                sg.Button('Exit', key='-EXIT-'),
            ]
        ]

        layout = [
            [
                sg.Frame('Password Options', password_options_frame_layout, element_justification='l'),
                sg.Frame('Generated Passwords', output_frame_layout, element_justification='c')
            ],
            [
                sg.Frame('', button_frame_layout, element_justification='c')
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

            if event == '-GENERATE-':
                password_generator = PasswordGenerator(
                    password_length=int(values['-PASSWORD_LENGTH-']),
                    include_numbers=values['-DIGITS-'],
                    include_special_chars=values['-SPECIAL_CHARS-'],
                    keywords=values['-KEYWORDS-'].split(' ')
                )
                password = password_generator.generate_password()
                print(password)
                print('\n')

            if event == '-RESET-':
                window.FindElement('-DIGITS-').Update(True)
                window.FindElement('-SPECIAL_CHARS-').Update(True)
                window.FindElement('-PASSWORD_LENGTH-').Update(0)
                window.FindElement('-KEYWORDS-').Update('')

            if event == '-CLEAR-':
                window.FindElement('-OUTPUT-').Update('')

            if event == '-EXIT-' or event == sg.WIN_CLOSED:
                break

        window.close()

