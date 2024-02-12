from kivy.app import App
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivy.uix.screenmanager import Screen


class HomeScreen(Screen):
    pass


class CardsScreen(Screen):
    pass


GUI = Builder.load_file("main.kv")


class CityWalkApp(App):
    def build(self):
        return GUI

    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        # screen_manager.transition
        screen_manager.current = screen_name


CityWalkApp().run()
