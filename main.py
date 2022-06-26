import random
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

x = random.randint(1,3)
if x == 1:
    text = 'Налево'
elif x == 2:
    text =' Прямо'
elif x == 3:
    text = 'Направо'

class MyApp(App):
    def build(self):
        return Label(text=text)
if __name__ == '__main__':
    MyApp().run()