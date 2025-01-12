from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import NumericProperty

class NightLightApp(MDApp):
    brightness = NumericProperty(50)

    def build(self):
        return Builder.load_file('helloworld.kv')

    def increase_brightness(self):
        if self.brightness < 100:
            self.brightness += 10

    def decrease_brightness(self):
        if self.brightness > 0:
            self.brightness -= 10

    def toggle_light(self, instance, value):
        if value:
            print("Light On")
        else:
            print("Light Off")

if __name__ == '__main__':
    NightLightApp().run()
