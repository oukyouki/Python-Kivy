from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase

from time import strftime


class ClockApp(App):
    sw_started = False
    sw_seconds = 0

    def update_time(self, nap):
        self.root.ids.time.text = strftime("[b]%H[/b]:%M:%S")
        if self.sw_started:
            self.sw_seconds += nap

    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)

    def on_start(self):
         Clock.schedule_interval(self.update_time, 1)
   
if __name__ == "__main__":

    Window.clearcolor = get_color_from_hex("#123456")
    ClockApp().run()
