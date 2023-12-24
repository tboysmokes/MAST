from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition, NoTransition
from kivy.core.window import Window
from dotenv import load_dotenv


Window.size = (320, 600)


load_dotenv()



class CreatePlaylistScreen(Screen):
    pass

class AudioPlayer(Screen):
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
Sm.add_widget(AudioPlayer(name='audio_player'))



class M_A_S_T(MDApp):
    def build(self):
        screen = Builder.load_file('ScreenSaver.kv')
        return screen
    
    def addSong(self):
        print("successful")

    def createplaylistfu(self, choose):
        if choose == 'typed_parm':
            playlistname1 = self.root.get_screen('createPlaylist').ids.playlist_names.text
            rhythm = self.root.get_screen('createPlaylist').ids.parm_one.text
            pitch = self.root.get_screen('createPlaylist').ids.parm_two.text
            tempo = self.root.get_screen('createPlaylist').ids.parm_three.text

        elif choose == 'upload':
            playlistname2 = self.root.get_screen('createPlaylist').ids.playlistnames.text


       


    def auidoPlayerS(self, tab_name):
        if tab_name == 'happy':
            self.root.current = 'audio_player'
            self.root.get_screen('audio_player').ids.playlistname.text = 'Happy playlist'
            self.root.get_screen('audio_player').ids.playlistImage.source = 'static/happy.png'
        elif tab_name == 'sad':
            self.root.current = 'audio_player'
            self.root.get_screen('audio_player').ids.playlistname.text = 'Sad playlist'
            self.root.get_screen('audio_player').ids.playlistImage.source = 'static/sadnigga.png'
        elif tab_name == 'chill':
            self.root.current = 'audio_player'
            self.root.get_screen('audio_player').ids.playlistname.text = 'Chill playlist'
            self.root.get_screen('audio_player').ids.playlistImage.source = 'static/chill_guy.jpg'


    def searchSong(self, search):
        search = self.root.get_screen('playlist').ids.Searchs.text
        if search:
            pass




if (__name__) == "__main__":
    M_A_S_T().run()
