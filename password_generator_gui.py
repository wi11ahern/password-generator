import PySimpleGUI as sg

from pasword_generator import PasswordGenerator


class PasswordGeneratorGui:

    def create_gui(self) -> None:
        body_text_font = ('Aerial', 16)
        frame_title_font_size = ('Aerial', 20)

        password_options_frame_layout = [
            [sg.Text(text='Password Length', justification='left', font=body_text_font)],
            [sg.Slider(key='-PASSWORD_LENGTH-', range=(6, 100), default_value=6, size=(30, 10), orientation='horizontal', font=body_text_font)],
            [sg.Checkbox(key='-DIGITS-', text='Include Numbers', default=True, font=body_text_font)],
            [sg.Checkbox(key='-SPECIAL_CHARS-', text='Include Special Characters', default=True, font=body_text_font)],
            [sg.Text(text='Keywords\n(Separate keywords with a space.)', justification='left', font=body_text_font)],
            [sg.Input(key='-KEYWORDS-', justification='left', size=(30, 1), font=body_text_font)],
        ]

        output_frame_layout = [
            [sg.Output(key='-OUTPUT-', size=(35, 11), font=body_text_font)]
        ]

        button_frame_layout = [
            [
                sg.Button('Generate', key='-GENERATE-', font=body_text_font),
                sg.Button('Reset', key='-RESET-', font=body_text_font),
                sg.Button('Clear Output', key='-CLEAR-', font=body_text_font),
                sg.Button('Exit', key='-EXIT-', font=body_text_font),
            ]
        ]

        layout = [
            [
                sg.Frame('Password Options', password_options_frame_layout, element_justification='l', font=frame_title_font_size),
                sg.Frame('Generated Passwords', output_frame_layout, element_justification='c', font=frame_title_font_size)
            ],
            [
                sg.Frame('', button_frame_layout, element_justification='c', border_width=0)
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

