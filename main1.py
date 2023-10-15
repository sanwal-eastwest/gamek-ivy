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

<THead@Button+Label>:
    font_size:12
    text_size:self.size
    valign:'middle'
    halign:'center'
    color:(1,1,1,1)
    bold:True
    foreground_color:(1,1,1,1)
<CLabel@Label>:
    font_size:13
    text_size:self.size
    valign:'middle'
    halign:'center'
    color:(1,1,1,1)
    foreground_color:'0,0,1,1'
    
<TableRow@GridLayout>:
    rows:1
    size_hint_x:1
    size_hint_y:None
    height:30
    size:self.size
    padding:2
    spacing:5
    canvas.before:
        Color:
            rgba:(0,0,0,1)
        Rectangle:
            pos:self.pos
            size:self.size
#actual code 
<Main1>
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
        size_hint:1,.15
        orientation:'horizontal'
        spacing:10
        padding:5
        AnchorLayout:
            anchor_x:'center'
            anchor_y:'center'
            size_hint:.5,1
            Label:
                text:"Select Your Next Queen"
                text_size:self.size
                halign:'right'
                valign:'center'
                font_size:18
                color:(1,1,0,1)

        AnchorLayout:
            anchor_x:'center'
            anchor_y:'center'
            size_hint:.25,1
            Button:
                id:btn_seegenes
                text:"See Genes"
                size_hint:None,None
                height:30
                width:80
                on_press:root.call_scr_main2()
        AnchorLayout:
            anchor_x:'right'
            anchor_y:'center'
            size_hint:.20,1
            Button:
                id:btn_ask
                text:'?'
                size_hint:None,.5
                width:40
                on_press:root.call_help()
        
    BoxLayout:
        size_hint:1,.7
        id:box_table
        orientation:'vertical'
        spacing:1
        padding:0
        canvas.before:
            Color:
                rgba:(0,0,0,1)
            Rectangle:
                pos:self.pos
                size:self.size
        BoxLayout:
            text_size:self.size
            size_hint_x:1
            size_hint_y:1
            orientation:'vertical'
            padding:.2
            canvas.before:
                Color:
                    rgba:(0,0,0,1)
                Rectangle:
                    pos:self.pos
                    size:self.size
            GridLayout:
                id:colum_headings
                text_size:self.size
                size_hint_x:1
                rows:1
                size_hint_y:None
                height:30
                spacing:0
                canvas.before:
                    Color:
                        rgba:(0,0,0,1)
                    Rectangle:
                        pos:self.pos
                        size:self.size
                
                THead:
                    id:lbl_name
                    text:'Name'
                    size_hint_x:.5
                    on_press:root.thead_clicked()
                THead:
                    id:lbl_size
                    text:'Size'
                    size_hint_x:.5
                    on_press:root.thead_clicked(1)
                THead:
                    id:lbl_Fert
                    text:'Fert'
                    size_hint_x:.5
                    on_press:root.thead_clicked(2)
                THead:
                    id:lbl_lspan
                    text:'L.span'
                    size_hint_x:.5
                    on_press:root.thead_clicked(3)
                THead:
                    id:lbl_upkeep
                    text:'UpKeep'
                    size_hint_x:.5
                    on_press:root.thead_clicked(4)
                THead:
                    id:lbl_metabolsim
                    text:'Metabolism'
                    size_hint_x:.5
                    on_press:root.thead_clicked(5)
                THead:
                    id:lbl_mrate
                    text:'M.Rate'
                    size_hint_x:.5
                    on_press:root.thead_clicked(6)
                THead:
                    id:lbl_fight_power
                    text:'Fight Power'
                    size_hint_x:.5
                    on_press:root.thead_clicked(7)
                THead:
                    id:lbl_oconsump
                    text:'O.consump'
                    size_hint_x:.5
                    on_press:root.thead_clicked(8)
                CLabel:
                    id:lbl_
                    text:''
                    size_hint_x:.5

            GridLayout:
                cols:1
                id:btn_section
                orientation:'lr-tb'
                spacing:3
                size_hint_x:1
                size_hint_y:1
                ScrollView:
                    do_scroll_x: False
                    do_scroll_y: True
                    size:self.size
                    bar_width:20
                    bar_color: 0, 0, 0, .21   # red
                    effect_cls: "ScrollEffect"
                    scroll_type: ['bars', 'content']
                    GridLayout:
                        id:m1_rows_area
                        height:self.minimum_height
                        cols:1
                        size_hint_y: None
                        orientation: 'tb-lr'#'vertical'
                        spacing:0
                        


    BoxLayout:
        size_hint:1,.35
        Label:
            text:"Note:For simplicity, any stat that increases is marked in green, and any that decreases is marked in red, that does not mean that green is good and red and bad"
            color:(1,1,1,1)
            text_size:self.size
            halign:'center'
            valign:'center'
            font_size:17
        
            

""")

class Main1(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._name = "Main1 Window"
        self.table_area=self.ids.m1_rows_area
        self.dummy_data = [['q0',1,5,2,0,4,6,7,5], ['q1',0,0,13,0,4,6,7,5], ['q3',3,0,2,0,4,6,7,5]]

        self.fill_table()
    def fill_table(self):
        
        for d in self.dummy_data:
            trow=TableRow()
            trow.set_values(d, self.btn_select_clicked)
            self.table_area.add_widget(trow)

    def call_scr_main2(self):
        self.parent.parent.current='scrn_main2'

    def call_help(self):
        App.get_running_app().HelpCaller = 1
        self.parent.parent.current='scrn_help'

    def thead_clicked(self, index=None):
        if index:
            self.table_area.clear_widgets()
            self.dummy_data = sorted(self.dummy_data, key=lambda d:d[index])
            self.fill_table()
    
    def btn_select_clicked(self, source=None):
        self.parent.parent.current='scrn_location'

class CLabel(Label):
    pass

class THead(Button):
    pass    

class TableRow(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._row_widgets = []
    
    def set_values(self, values, select_callback):
        self._row_widgets.clear()
        for i, val in enumerate(values):
            w = CLabel()
            w.text = str(val)
            if i == 0:
                w.color = (0, 1, 0, 1)
            else:
                if val > 5:
                    w.color = (0, 1, 0, 1)
                elif val == 0: 
                    w.color = (1, 1, 1, 1)
                else:
                    w.color = (1, 0, 0, 1)
            self._row_widgets.append(w)
            self.add_widget(w)
        btn = THead()
        btn.text = "Select"
        btn.bind(on_press=select_callback)        
        self._row_widgets.append(btn)
        self.add_widget(btn)

    
    def _select_clicked(self, source):
        # self.parent.parent.parent.current='scrn_location'
        self.parent.btn_select_clicked()


class Main1App(App):
    def build(self):
        return Main1()


if __name__=='__main__':

    Main1App().run()