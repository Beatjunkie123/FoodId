from kivy.uix.screenmanager import ScreenManager, Screen

sm = ScreenManager()

# Screens are added here, perhaps turn this into a list or dict?
class MainScreen(Screen):
    pass
sm.add_widget(MainScreen(name = 'main screen'))
