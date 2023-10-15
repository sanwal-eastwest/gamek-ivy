import kivy
from kivy.app import App
from kivy.lang import Builder   
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty

Builder.load_string("""


<ChoiceSelection@GridLayout+Button+ButtonBehavior>:
    rows:1
    size_hint_x:1
    size_hint_y:1
    size:self.size
    padding:3
    background_normal:''
    canvas.before:
        Color:
            rgba:(1,1,1,1)
        Rectangle:
            pos:self.pos
            size:self.size


<Location>
    size_hint:1,1
    padding:1
    spacing:1
    orientation:'vertical'
    canvas.before:
        Color:
            rgba:(0,0,0,1)
        Rectangle:
            pos:self.pos
            size:self.size
    BoxLayout:
        size_hint:1,.10
        orientation:'vertical'
        spacing:5
        padding:5
        Label:
            text:"Select Location for Nest"
            text_size:self.size
            halign:'center'
            valign:'center'
            font_size:18
    BoxLayout:
        size_hint:1,1
        orientation:'vertical'
        spacing:5
        padding:5
        canvas.before:
            Color:
                rgba:(1,1,1,1)
            Rectangle:
                pos:self.pos
                size:self.size

        
        ChoiceSelection:
            on_press:root.call_result()
            Image:
                source: 'forest.png'
                size: self.texture_size
                size:self.size
                allow_stretch: True
        ChoiceSelection:
            on_press:root.call_result()
            Image:
                source: 'Swamp.png'
                size: self.texture_size
                size:self.size
                allow_stretch: True
        ChoiceSelection:
            on_press:root.call_result()
            Image:
                source: 'Desert.png'
                size: self.texture_size
                size:self.size
                allow_stretch: True
        ChoiceSelection:
            on_press:root.call_result()
            Image:
                source: 'Beach.png'
                size: self.texture_size
                size:self.size
                allow_stretch: True
        
        

""")

class Location(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
       
        self._name = "Location Window"

    def call_result(self):
        self.parent.parent.current='scrn_result'
        
class LocationApp(App):
    def build(self):
        return Location()


if __name__=='__main__':

    LocationApp().run()