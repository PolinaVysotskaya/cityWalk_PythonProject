from kivy.core.text import LabelBase
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivy.uix.screenmanager import Screen
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout


class HomeScreen(Screen):
    pass


class CardsScreen(Screen):
    pass


class HistoryScreen(Screen):
    pass


class NewRouteScreen(Screen):
    pass


LabelBase.register(name='my_font', fn_regular='ABeeZee-Regular.ttf')


class CheckItem(MDBoxLayout):
    text = StringProperty()
    group = StringProperty()


class CityWalkApp(MDApp):
    def build(self):
        GUI = Builder.load_file("main.kv")
        self.theme_cls.primary_palette = "Green"
        return GUI

    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        # screen_manager.transition
        screen_manager.current = screen_name


CityWalkApp().run()
