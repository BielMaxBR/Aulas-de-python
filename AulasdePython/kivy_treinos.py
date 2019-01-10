import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

kivy.require('1.10.1')


class HAHAHAHAHA(GridLayout):
    def __init__(self, **kwargs):
        super(HAHAHAHAHA, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='HAHAHAHA'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='HAHA'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class Myapple(App):
    def build(self):
        return HAHAHAHAHA()


if __name__ == '__main__':
    Myapple().run()


