import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix import *

Builder.load_file('FoodId.kv')



from ScreenManager import sm as ScreenManager

class FoodIdApp(App):
    def build(self):
        return ScreenManager

if __name__ == '__main__':
    FoodIdApp().run()
