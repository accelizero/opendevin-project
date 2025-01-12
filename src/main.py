from kivymd.app import MDApp
from kivy.lang import Builder

class HelloWorldApp(MDApp):
    def build(self):
        return Builder.load_file('helloworld.kv')

if __name__ == '__main__':
    HelloWorldApp().run()
