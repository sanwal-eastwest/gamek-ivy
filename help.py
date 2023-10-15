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
<Help>
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
        id:main_help
        padding:30
        spacing:2
        orientation:'vertical'
        size_hint:1,1
        
""")
Builder.load_string(""" 
<Help1>:
    size_hint:1,1
    orientation:'vertical'
    padding:0
    spacing:0
    Label:
        id:lbl_help
        text:"This is game about guiding the evolution of your aunts through the ages. For doing this, you have very limited set of choices. First select the Queen that you consider the most fit for creating your next colony. The states represents the current attributes of your Queen. The genes are responsible for affecting the states. Once you selected the Queeen, you have to select the place to start your colony. Places like forests or grasslands have abundant food, but also have competition. Places like  Desert are hard to survive on, but may guid your evolution in interesting ways."
        text_size:self.size
        halign:'left'
        valign:'center'
        size_hint:1,1
    BoxLayout:
        size_hint:1,.3
        orientation:'horizontal'
        spacing:5
        AnchorLayout:
            anchor_x:'center'
            anchor_y:'center'
            size_hint:1,1
            # Button:
            #     id:btn_prev
            #     text:'Previous'
            #     text_size:self.size
            #     halign:'center'
            #     valign:'center'
            #     size_hint:None,None
            #     height:40
            #     width:100
            #     on_press:root.btn_prev_clicked()
        AnchorLayout:
            anchor_x:'center'
            anchor_y:'center'
            size_hint:1,1
            Button:
                id:btn_back
                text:'Back'
                text_size:self.size
                halign:'center'
                valign:'center'
                size_hint:None,None
                height:40
                width:100
                on_press:root.btn_back_clicked()
        AnchorLayout:
            anchor_x:'center'
            anchor_y:'center'
            size_hint:1,1
            Button:
                id:btn_next
                text:'Next'
                text_size:self.size
                halign:'center'
                valign:'center'
                size_hint:None,None
                height:40
                width:100
                on_press:root.btn_next_clicked()
        

""")

    
        
Builder.load_string(""" 
<Help2>:
    size_hint:1,1
    orientation:'vertical'
    padding:0
    spacing:0

    Label:
        id:lbl_help
        text:"Help screen 2.This is game about guiding the evolution of your aunts through the ages. For doing this, you have very limited set of choices. First select the Queen that you consider the most fit for creating your next colony. The states represents the current attributes of your Queen. The genes are responsible for affecting the states. Once you selected the Queeen, you have to select the place to start your colony. Places like forests or grasslands have abundant food."
        text_size:self.size
        halign:'left'
        valign:'center'
        size_hint:1,1
    
    BoxLayout:
        size_hint:1,.3
        orientation:'horizontal'
        spacing:5
        AnchorLayout:
            anchor_x:'center'
            anchor_y:'center'
            size_hint:1,1
            Button:
                id:btn_prev
                text:'Previous'
                text_size:self.size
                halign:'center'
                valign:'center'
                size_hint:None,None
                height:40
                width:100
                on_press:root.btn_prev_clicked()
        AnchorLayout:
            anchor_x:'center'
            anchor_y:'center'
            size_hint:1,1
            Button:
                id:btn_back
                text:'Back'
                text_size:self.size
                halign:'center'
                valign:'center'
                size_hint:None,None
                height:40
                width:100
                on_press:root.btn_back_clicked()
        AnchorLayout:
            anchor_x:'center'
            anchor_y:'center'
            size_hint:1,1
            Button:
                id:btn_next
                text:'Next'
                text_size:self.size
                halign:'center'
                valign:'center'
                size_hint:None,None
                height:40
                width:100
                on_press:root.btn_next_clicked()
  
""")

       
Builder.load_string(""" 
<Help3>:
    size_hint:1,1
    orientation:'vertical'
    padding:0
    spacing:0

    Label:
        id:lbl_help
        text:"Help screen 3.This is game about guiding the evolution of your aunts through the ages. For doing this, you have very limited set of choices. First select the Queen that you consider the most fit for creating your next colony."
        text_size:self.size
        halign:'left'
        valign:'center'
        size_hint:1,1
    BoxLayout:
        size_hint:1,.3
        orientation:'horizontal'
        spacing:5
        AnchorLayout:
            anchor_x:'center'
            anchor_y:'center'
            size_hint:1,1
            Button:
                id:btn_prev
                text:'Previous'
                text_size:self.size
                halign:'center'
                valign:'center'
                size_hint:None,None
                height:40
                width:100
                on_press:root.btn_prev_clicked()
        AnchorLayout:
            anchor_x:'center'
            anchor_y:'center'
            size_hint:1,1
            Button:
                id:btn_back
                text:'Back'
                text_size:self.size
                halign:'center'
                valign:'center'
                size_hint:None,None
                height:40
                width:100
                on_press:root.btn_back_clicked()
        AnchorLayout:
            anchor_x:'center'
            anchor_y:'center'
            size_hint:1,1
            # Button:
            #     id:btn_next
            #     text:'Next'
            #     text_size:self.size
            #     halign:'center'
            #     valign:'center'
            #     size_hint:None,None
            #     height:40
            #     width:100
            #     on_press:root.btn_next_clicked()
  
         

""")

       
class Help(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
       
        self._name = "Help Window"
        self.dynamic_area=self.ids.main_help
        self.load_help1()
        # self.load_help3()

    def load_help1(self):
        self.help1=Help1(self)
        self.dynamic_area.clear_widgets()
        self.dynamic_area.add_widget(self.help1)
    
    def load_help2(self):
        self.help2=Help2(self)
        self.dynamic_area.clear_widgets()
        self.dynamic_area.add_widget(self.help2)

    def load_help3(self):
        self.help3=Help3(self)
        self.dynamic_area.clear_widgets()
        self.ids.main_help.add_widget(self.help3)

    def back_clicked(self):
        
        helpcaller = App.get_running_app().HelpCaller
        if helpcaller == 0:
            #load startscreen
            self.parent.parent.current='scrn_start'
        elif helpcaller == 1:
            # load main1
            self.parent.parent.current='scrn_main1'
        else:
            # load main2
            self.parent.parent.current='scrn_main2'

class Help1(BoxLayout):
    def __init__(self,_parent,**kwargs):
        super().__init__(**kwargs)
        self._parent=_parent

    def btn_next_clicked(self):
        self._parent.load_help2()

    def btn_back_clicked(self):
        self._parent.back_clicked()

class Help2(BoxLayout):
    def __init__(self,_parent,**kwargs):
        super().__init__(**kwargs)
        self._parent=_parent

    def btn_next_clicked(self):
        self._parent.load_help3()

    def btn_prev_clicked(self):
        self._parent.load_help1()

    def btn_back_clicked(self):
        self._parent.back_clicked()

class Help3(BoxLayout):
    def __init__(self,_parent,**kwargs):
        super().__init__(**kwargs)
        self._parent=_parent

    def btn_prev_clicked(self):
        self._parent.load_help2()

    def btn_back_clicked(self):
        
        self._parent.back_clicked()

class HelpApp(App):
    def build(self):
        return Help()


if __name__=='__main__':

    HelpApp().run()