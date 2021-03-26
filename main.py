from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.app import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 

class HomeScreen(Screen): 
    pass
   
class FirstScreen(Screen): 
    pass
     
sm = ScreenManager() 
sm.add_widget(HomeScreen(name='homescreen'))
sm.add_widget(FirstScreen(name='fisrtscreen'))
   
class MainApp(MDApp):
    def build(self):
        return Builder.load_file("front_end.kv") 

MainApp().run()