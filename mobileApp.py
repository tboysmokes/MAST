from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition, NoTransition
from kivy.core.window import Window
Window.size = (320, 600)

class CreatePlaylistScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class AddScreen(Screen):
    pass

class PlaylistScreen(Screen):
     pass

Sm = ScreenManager(transition=NoTransition())
Sm.add_widget(HomeScreen(name='Home'))
Sm.add_widget(AddScreen(name='add'))
Sm.add_widget(PlaylistScreen(name='playlist'))
Sm.add_widget(CreatePlaylistScreen(name='createPlaylist'))



class M_A_S_T(MDApp):
    def build(self):
        screen = Builder.load_file('ScreenSaver.kv')
        return screen
    
    def getaudio(self):
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
