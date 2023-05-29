from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App
import re


class MyApp(App):

    ids_to_check = set()

    def validate_then_add_to_list(self, text):
        """Uses a regex pattern to check if the link is in a valid format for a Youtube link
        takes a string as a parameter which is what will be checked if it is a valid link"""
        pattern = re.compile("(v=[_0-9A-Za-z]{11})")
        m = re.search(pattern, text)
        print(m)
        if m:
            self.ids_to_check.add(m.group(1)[2:])
        print(self.ids_to_check)

    def build(self):
        layout = FloatLayout()
        add_button = Button(text="Add", pos_hint={'right': .985, 'top': .5}, size_hint=(.1, .05))
        url_get = TextInput(text="Youtube url", size_hint=(.8, .05), pos_hint={'right': .85, 'top': .5})
        validate_button = Button(text="Validate", size_hint=(.4, .05), pos_hint={'right': .7, 'top': .43})
        add_button.bind(on_release=lambda x: self.validate_then_add_to_list(url_get.text))
        layout.add_widget(url_get)
        layout.add_widget(add_button)
        layout.add_widget(validate_button)
        return layout


if __name__ == "__main__":
    MyApp().run()
