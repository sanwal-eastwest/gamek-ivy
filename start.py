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
<Start>
    size_hint:1,1
    padding:1
    spacing:5
    orientation:'vertical'
    canvas.before:
        Color:
            rgba:(0,0,0,1)
        Rectangle:
            pos:self.pos
            size:self.size
    BoxLayout:
        size_hint:1,.30
        Label:
            text:"Welcome To COLONY"
            text_size:self.size
            halign:'center'
            valign:'center'
            font_size:20
    BoxLayout:
        id:picture_box
        size_hint:1,1
        padding:2
        # canvas.before:
        #     Color:
        #         rgba:(1,1,1,1)
        #     Rectangle:
        #         pos:self.pos
        #         size:self.size
                    
        Image:
            source:'img.jpg'
    BoxLayout:
        size_hitn:1,.5
        orientation:'vertical'
        padding:5
        spacing:5
        Button:
            id:btn_howToPlay
            text:'How To Play'
            text_size:self.size
            halign:'center'
            valign:'center'
            size_hint:1,None
            height:40
            on_press:root.call_help()
        Button:
            id:btn_startNewGame
            text:'Start New Game'
            text_size:self.size
            halign:'center'
            valign:'center'
            size_hint:1,None
            height:40
            on_press:root.new_game()
        Button:
            id:btn_continueGame
            text:'Continue Game'
            text_size:self.size
            halign:'center'
            valign:'center'
            size_hint:1,None
            height:40
            on_press:root.continue_game()
        BoxLayout:
            size_hint:1,None
            height:40
            
""")

class Start(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
       
        self._name = "Start Window"

    def call_help(self):
        App.get_running_app().HelpCaller = 0
        self.parent.parent.current='scrn_help'

    def new_game(self):
        self.parent.parent.current='scrn_main1'
    def continue_game(self):
        self.parent.parent.current='scrn_location'
        
class StartApp(App):
    def build(self):
        return Start()


if __name__=='__main__':

    StartApp().run()