from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App


class MyApp(App):

    layout = GridLayout(cols=1)

    def build(self):
        btn = Button(text="hello")
        self.layout.add_widget(btn)


if __name__ == "__main__":
    MyApp().run()
