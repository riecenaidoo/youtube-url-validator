from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App
import re

import main


class MyApp(App):

    ids_to_check = set()

    def validate_then_add_to_list(self, text):
        """Uses a regex pattern to check if the link is in a valid format for a YouTube link
        takes a string as a parameter which is what will be checked if it is a valid link"""
        pattern = re.compile("(v=[_0-9A-Za-z]{11})")
        m = re.search(pattern, text)
        print(m)
        if m:
            self.ids_to_check.add(m.group(1)[2:])
        print(self.ids_to_check)

    def run_validation(self):
        main.final_validation(self.ids_to_check)

    def build(self):
        layout = FloatLayout()
        # creates a button to add ids to a list size/position are relative to layout size
        add_button = Button(text="Add", pos_hint={'right': .985, 'top': .5}, size_hint=(.1, .05))
        # creates a text box for url to pasted into
        url_get = TextInput(text="Youtube url", size_hint=(.8, .05), pos_hint={'right': .85, 'top': .5})
        # creates a validate button which takes the list of ids and checks if they are valid using final_validation
        validate_button = Button(text="Validate", size_hint=(.4, .05), pos_hint={'right': .7, 'top': .43})
        # binds the buttons to respective function
        add_button.bind(on_release=lambda x: self.validate_then_add_to_list(url_get.text))
        validate_button.bind(on_release=lambda x: self.run_validation())
        layout.add_widget(url_get)
        layout.add_widget(add_button)
        layout.add_widget(validate_button)
        return layout


if __name__ == "__main__":
    MyApp().run()
