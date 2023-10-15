import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout 
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView

Builder.load_file('table/table.kv')

class TableWindow(BoxLayout):
    def __init__(self, parent=None, **kwargs):
        super().__init__(**kwargs)

class TableApp(App):
    def build (self):
        return TableWindow()

if __name__=='__main__':
    TableApp().run()

