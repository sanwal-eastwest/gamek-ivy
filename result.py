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
<Result>
    size_hint:1,1
    padding:5
    spacing:5
    orientation:'vertical'
    canvas.before:
        Color:
            rgba:(0,0,0,1)
        Rectangle:
            pos:self.pos
            size:self.size
    BoxLayout:
        padding:20
        spacing:1
        orientation:'vertical'
        size_hint:1,.6
        Label:
            id:lbl_result1
            text:"The Queen Lived for 100 Days!"
            text_size:self.size
            halign:'left'
            valign:'center'
            size_hint:1,None
            height:30
        Label:
            id:lbl_result2
            text:"She laid 682"
            text_size:self.size
            halign:'left'
            valign:'center'
            size_hint:1,None
            height:30
        Label:
            id:lbl_result3
            text:"88 workers survived"
            text_size:self.size
            halign:'left'
            valign:'center'
            size_hint:1,None
            height:30
        Label:
            id:lbl_result4
            text:"1678 foods left for the next Queen"
            text_size:self.size
            halign:'left'
            valign:'center'
            size_hint:1,None
            height:30
        Widget:
    BoxLayout:
        padding:1
        spacing:1
        orientation:'vertical'
        size_hint:1,.4
        Button:
            id:btn_selectNewQueen
            text:'Select New Queen'
            text_size:self.size
            halign:'center'
            valign:'center'
            size_hint:1,None
            height:40
            on_press:root.select_new_queen()
        BoxLayout:

            size_hint:1,.5
""")

class Result(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
       
        self._name = "Result Window"

    def select_new_queen(self):
        self.parent.parent.current='scrn_main1'
class ResultApp(App):
    def build(self):
        return Result()


if __name__=='__main__':

    ResultApp().run()