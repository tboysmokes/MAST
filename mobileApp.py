from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from SreenSaver import screen_helper
from kivy.uix.filechooser import FileChooser




class HomeScreen(Screen):
    pass


class AddScreen(Screen):
    pass


class PlaylistScreen(Screen):
     pass


Sm = ScreenManager()
Sm.add_widget(HomeScreen(name='Home'))
Sm.add_widget(AddScreen(name='add'))
Sm.add_widget(PlaylistScreen(name='playlist'))


class M_A_S_T(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen
    
    def getaudio(self):
        file  = FileChooser(filters=['*.mp3', '*.wav'])
        print("successful")

    def on_tab_press(self, tab_name):
        if tab_name == 'home':
            self.root.current = 'Home'
        elif tab_name == 'addSong':
            self.root.current = 'add'
        elif tab_name == 'playlist':
            self.root.current = 'playlist'




if (__name__) == "__main__":
    M_A_S_T().run()