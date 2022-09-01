from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from welcome import *

class HotPotatosApp(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.3, 0.4)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5 }
        self.window.add_widget(Image(source="dancing-potato.gif"))

        self.button = Button(
            text = "Verified Hot Potato",
            size_hint = (0.3, 0.4),
            background_color = (0, 0.7, 0.3, 1),
            on_press = welcomePage)
        self.window.add_widget(self.button)


        return self.window

if __name__ == "__main__":
    HotPotatosApp().run()

