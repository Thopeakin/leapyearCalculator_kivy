from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

class Frame(Widget):
    def calculate(self, *args):
        getter = self.ids['text']
        try:
            year = int(getter.text)
            ly = 2016
            if ly > year:
                diff = ly - year
            else:
                diff = year - ly
            if diff % 4 == 0:
                get = self.ids['label']
                get.color= 0, 1, 0 ,1
                get.text= '{} is a leap year'.format(year)
            else:
                get = self.ids['label']
                get.color= 1, 0, 1 ,.5
                get.text= '{} is not a leap year'.format(year)

        except Exception as e:
            get = self.ids['label']
            get.color= 1, 0, 0, 1
            get.text= 'Invalid Year'
            
Builder.load_file('leapyear.kv')

class App(App):
    def build(self):
        return Frame()

App().run()
