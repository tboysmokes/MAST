from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.slider import MDSlider
from kivy.core.window import Window
from kivy.network.urlrequest import UrlRequest
from kivy.uix.image import AsyncImage
import firebase_admin
import json
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


def chooseColor():
    color = [['#706e40'], ['#3f5efb'], ['#fc466b'], ['#224da7'], ['#23a226'], ['#b40101']]
    number = 0
    for col in color:
        number += 1
        for _ in range(number):
            random_choose = random.choice(color)
            return random_choose[0]
        

class M_A_S_T(MDApp):
    def build(self):
        
        screen = Builder.load_file('ScreenSaver.kv')
        return screen
    
    def addSong(self):
        print("successful")

    def createplaylistfu(self, choose):
        screenid = self.root.get_screen('createPlaylist')
        playlistcolor = chooseColor()
        playlist_ref = db.reference('playlistT')
        bucket = storage.bucket()
        

        if choose == 'typed_parm':

            playlistname1 = screenid.ids.playlist_names.text
            playlsitid = playlistname1+'_mix'
            playlistname = playlistname1+' tune'
            rhythm = screenid.ids.parm_one.text
            pitch = screenid.ids.parm_two.text
            tempo = screenid.ids.parm_three.text

            if playlistname1 and rhythm and pitch and tempo:

                playlist_data = {
                    'playlistname': playlistname,
                    'playlistcolor': playlistcolor,
                }
                playlist_ref.child(playlsitid).set(playlist_data)

        elif choose == 'upload':
            playlistname2 = self.root.get_screen('createPlaylist').ids.playlistnames.text



    def playmusic(self):
        icon = self.root.get_screen('audio_player').ids.playicon.icon 
        if icon == 'play':
            self.root.get_screen('audio_player').ids.playicon.icon = 'pause'
        elif icon == 'pause':
             self.root.get_screen('audio_player').ids.playicon.icon = 'play'



       


    def audioPlayerS(self, tab_name):
        print(tab_name)
        playlist_ref = db.reference('playlistT')
        playlistdata = playlist_ref.get()
        screenid = self.root.get_screen('audio_player')
        nameBox = screenid.ids.audioNameList

        slidbox = screenid.ids.Sliderbox

        for playlistid, playlistitem in playlistdata.items():
        #content of the screen changes based of the button pressed
            if tab_name == playlistid:
                self.root.current = 'audio_player'
                image_url = playlistitem['playlistimage']
                screenid.ids.playlistImage.clear_widgets()

                image = AsyncImage(source=image_url, width='180dp', height='180dp', 
                                   size_hint_x= None, size_hint_y=None, allow_stretch=True)
                
                screenid.ids.playlistname.text = playlistitem['playlistname'].capitalize()
                
                screenid.ids.playlistImage.add_widget(image)
                screenid.ids.carditem.md_bg_color = playlistitem['playlistcolor']

                slider = MDSlider()
                slidbox.add_widget(slider)

                muiscName = ['tomiwa', 'fikky', 'olododo', 'raheem', 'tumininu']
                for musicn in muiscName:
                    item = TwoLineListItem(text=musicn, secondary_text='now playing'.lower(), text_color='#ffffff')
                    nameBox.add_widget(item)


    def searchSong(self, search):
        search = self.root.get_screen('playlist').ids.Searchs.text
        if search:
            pass



    def playlistpage(self):
        playlist_ref = db.reference('playlistT')
        playlistdata = playlist_ref.get()

        self.root.current = 'playlist'
        screenid = self.root.get_screen('playlist').ids.innerbox
        screenid.clear_widgets()

        for playlistid, playlistitem in playlistdata.items():
            playlistname = playlistitem['playlistname'].capitalize()
            playlistcolor = playlistitem['playlistcolor']

            
            card  = MDCard( size_hint_y=None, height='72dp', md_bg_color=playlistcolor,
                        radius=15, elevation=2)
            card.add_widget(MDLabel(text=playlistname, text_color='#ffffff', bold=True, 
                                    font_size=30, halign='left', padding=('10dp', '5dp')))
            screenid.add_widget(card)
            card.bind(on_press=lambda x, playlist_id=playlistid: self.audioPlayerS(playlist_id))
            
        
        






if __name__ == "__main__":
    M_A_S_T().run()