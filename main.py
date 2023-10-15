import kivy
from kivy.app import App
from kivy.lang import Builder   
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty

from start import Start
from main1 import Main1
from main2 import Main2
from location import Location
from help import Help
from result import Result
from kivy.core.window import Window 

Window.size = (600, 700) 

class MainWindow(BoxLayout):
    startscr=Start()
    main1scr=Main1()
    main2scr=Main2()
    locationscr=Location()
    helpscr=Help()
    resultscr=Result()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.scrn_start.add_widget(self.startscr)
        self.ids.scrn_main1.add_widget(self.main1scr)
        self.ids.scrn_main2.add_widget(self.main2scr)
        self.ids.scrn_location.add_widget(self.locationscr)
        
        self.ids.scrn_help.add_widget(self.helpscr)
        self.ids.scrn_result.add_widget(self.resultscr)
        self._name = "Main Window"

        
class MainApp(App):
    def build(self):
        self.HelpCaller = 0
        return MainWindow()


if __name__=='__main__':

    MainApp().run()

