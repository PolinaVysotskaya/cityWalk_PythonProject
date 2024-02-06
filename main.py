from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class CityWalkApp(MDApp):
    def build(self):
        return MDLabel(text="City Walk", halign="center")


CityWalkApp().run()