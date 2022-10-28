from  kivy.app import App
from kivy.lang import Builder

kv = '''
FloatLayout:
    Button:
        text:'Hello World!'
'''

class myApp(App):
    def build(self):
        return Builder.load_string(kv)

myApp().run()
