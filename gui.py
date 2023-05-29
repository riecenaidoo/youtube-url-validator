from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App


class MyApp(App):

    def build(self):
        layout = FloatLayout()
        add_button = Button(text="Add", pos_hint={'right': .985, 'top': .5}, size_hint=(.1, .05))
        url_get = TextInput(text="Youtube url", size_hint=(.8, .05), pos_hint={'right': .85, 'top': .5})
        validate_button = Button(text="Validate", size_hint=(.4, .05), pos_hint={'right': .7, 'top': .43})
        add_button.on_release()
        layout.add_widget(url_get)
        layout.add_widget(add_button)
        layout.add_widget(validate_button)
        return layout


if __name__ == "__main__":
    MyApp().run()
