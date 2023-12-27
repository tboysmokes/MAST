from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.list import TwoLineListItem
from kivy.core.window import Window
import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials, db, storage
import random, os

Window.size = (320, 600)

load_dotenv()
databaseurl = os.getenv('DATABASEURL')
storagebucket = os.getenv('STORAGEBUCKET')

print(databaseurl, storagebucket)
cred = credentials.Certificate('mast-4ad62-firebase-adminsdk-ebtqm-7e3335028b.json')
firebase_admin.initialize_app(cred, {'databaseURL': databaseurl,
                                     'storageBucket': storagebucket
})

music_ref = db.reference('musicT')
playlist_ref = db.reference('playlistT')

playlistname = "example_mix"
playlistdata={
    "playlistimage": "something.png",
    "playlistcolor": "#23a226"
}

music_ref.child(playlistname).set(playlistdata)

store_ref = storage.bucket()
audio_path = 'static/musicF/Banky-W-Yes-No.mp3'
audio_name ='YesNo.mp3'
boo = store_ref.blob(audio_name)
boo.upload_from_filename(audio_path)





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

Sm = ScreenManager()
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
        screenid = self.root.get_screen('createPlaylist')
        if choose == 'typed_parm':
            playlistname1 = screenid.ids.playlist_names.text
            rhythm = screenid.ids.parm_one.text
            pitch = screenid.ids.parm_two.text
            tempo = screenid.ids.parm_three.text

        elif choose == 'upload':
            playlistname2 = self.root.get_screen('createPlaylist').ids.playlistnames.text


    def playmusic(self):
        icon = self.root.get_screen('audio_player').ids.playicon.icon 
        if icon == 'play':
            self.root.get_screen('audio_player').ids.playicon.icon = 'pause'
        elif icon == 'pause':
             self.root.get_screen('audio_player').ids.playicon.icon = 'play'
       


    def auidoPlayerS(self, tab_name):

        screenid = self.root.get_screen('audio_player')
        nameBox = self.root.get_screen('audio_player').ids.audioNameList

        #content of the screen changes based of the button pressed
        if tab_name == 'happy':
            self.root.current = 'audio_player'
            screenid.ids.playlistname.text = 'Happy playlist'
            screenid.ids.playlistImage.source = 'static/burna.jpeg'

            muiscName = ['tomiwa', 'fikky', 'olododo', 'raheem', 'tumininu']
            for musicn in muiscName:
                item = TwoLineListItem(text=musicn, secondary_text='now playing'.lower(), text_color='#ffffff')
                nameBox.add_widget(item)


                

        elif tab_name == 'sad':
            self.root.current = 'audio_player'
            screenid.ids.playlistname.text = 'Sad playlist'
            screenid.ids.playlistImage.source = 'static/sadnigga.png'

            muiscName = ['tomiwa', 'fikky', 'olododo', 'raheem', 'tumininu']
            for musicn in muiscName:
                pass


        elif tab_name == 'chill':
            self.root.current = 'audio_player'
            screenid.ids.playlistname.text = 'Chill playlist'
            screenid.ids.playlistImage.source = 'static/chill_guy.jpg'

            muiscName = ['tomiwa', 'fikky', 'olododo', 'raheem', 'tumininu']
            for musicn in muiscName:
                pass




    def searchSong(self, search):
        search = self.root.get_screen('playlist').ids.Searchs.text
        if search:
            pass



    def playlistpage(self):
        self.root.current = 'playlist'
        screenid = self.root.get_screen('playlist').ids.innerbox
        playnames = ['tomiwa', 'omotomiwa', 'raheem', 'sean', 'olododo', 'olluma']

        for playname in playnames:
            playname = playname+' playlist'
            card  = MDCard( size_hint_y=None, height='72dp', md_bg_color='#fc466b',
                        radius=15, elevation=2)
            card.add_widget(MDLabel(text= playname.capitalize(), color='#ffffff', bold=True, 
                                    font_size=30, halign='left', padding=('10dp', '5dp')))
            screenid.add_widget(card)




def chooseColor():
    color = ['#706e40', '#45fc48', '#3f5efb', '#fc466b', '#224da7', '#23a226']
    number = 0
    for col in color:
        number += 1
        for _ in range[number]:
            random_choose = random.choice(color)
            return random_choose


if __name__ == "__main__":
    M_A_S_T().run()