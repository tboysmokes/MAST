from flask import Flask, render_template, redirect, url_for, request
from moodPrediction import mood_prediction
import features
import sqlite3
import os


connection = sqlite3.connect("music.db", check_same_thread=False)
cursor = connection.cursor()


query = '''CREATE TABLE IF NOT EXISTS userdetails(
            userID  INTEGER  PRIMARY KEY  AUTOINCREMENT,
            name     TEXT    NOT NULL,
            email    TEXT    NOT NULL UNIQUE,
            password TEXT    NOT NULL
        )'''

query1 = '''CREATE TABLE IF NOT EXISTS musics(
            userID  INTEGER,
            name    TEXT     NOT NULL, 
            path    TEXT     NOT NULL  UNIQUE,
            mood    TEXT     NOT NULL,
            tempo   TEXT     NOT NULL,
            pitch   TEXT     NOT NULL,
            rhythm  TEXT     NOT NULL,
            zeroCR  TEXT     NOT NULL, 
            FOREIGN KEY (userID) REFERENCES userdetails(userID)
        )'''



cursor.execute(query)
cursor.execute(query1)

app = Flask(__name__)
app.config['SECRET_EKY'] = "music"


def send_audio_to_backend(audio):
    user = 0
    for song in audio:
        name = song[:-4]
        user+=1
        directory = 'C:/Users/MYPC/Documents/unknowproject/'
        file_path = directory + song 
        temp = features.tempos(song)
        mood = mood_prediction(song)
        pitch = features.pitchs(song)
        rhythm = features.rhythmies(song)
        zeroCR = features.Zerocrossingrating(song)
        cursor.execute("INSERT INTO musics VALUES (?,?,?,?,?,?,?,?)",(user, name, file_path, mood, temp, pitch, rhythm, zeroCR))
        connection.commit()



def getUserId():
    lastUserID = cursor.execute("SELECT MAX(userID) FROM userdetails").fetchall()[0][0]
    newID = lastUserID + 1
    return newID


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form["name1"]
        email = request.form["email1"]
        password = request.form["pass1"]

        print(name, email, password)
        if name and email and password:
            userID = getUserId()
            cursor.execute("INSERT INTO userdetails VALUES (?,?,?,?)", (userID, name, email, password))
            connection.commit()
            return redirect(url_for("home"))
        else:
            error = "all required information must be filled"
            return render_template("form.html", error=error)
    return render_template("form.html")



@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form["email2"]
        password = request.form["pass1"]

        cursor.execute("SELECT email, password FROM userdetails WHERE email = '"+email+"' AND password = '"+password+"'")
        connection.commit()
        result = cursor.fetchall()

        if len(result) == 0:
            error = "incorrect password or email"
            return render_template("form.html", error=error)
        else:
           return redirect(url_for("/home"))

    return render_template("form.html")






@app.route("/create", methods=["GET", "POST"])
def createPlaylist():
    if request.method == "POST":
        name = request.form["ablumName"]
        audio_files = request.files.getlist("audioFileInput")

        query = ('''CREATE TABLE IF NOT EXISTS ?(
                   path    TEXT    NOT NULL UNIQUE,
                   mood    TEXT    NOT NULL,
                   FORIGN KEY (userID) REFERENCES userdetails(userID)
        )''', [name])

        
        for audio_file in audio_files:

            tempo = features.tempos(audio_file)
            rhythm = features.rhythmies(audio_file).shape[0]
            pitch = features.pitchs(audio_file).shape[0]
            Zero = features.Zerocrossingrating(audio_file).shape[1]
            
            mood = mood_prediction (music=audio_file)
        
        query1 = '''SELECT path FROM musics WHERE tempo =  AND rhythm = ? AND '''
        
    return render_template('frontend.html')
        



@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        audios = request.files.getlist("audioFileInput")

    for audio in audios:
        print(audio)

        directory = "C:/Users/MYPC/Documents/unknowproject/musicF"
        if not os.path.exists(directory):
            os.makedirs(directory)
        ''''''
        song = audio.filename
        name = song[:-4]
        temp = features.tempos(song)
        rhythm = features.rhythmies(song)
        pitch = features.pitchs(song)
        zeroCR = features.Zerocrossingrating(song)
        mood  = mood_prediction(song)

        data = cursor.execute("SELECT FROM musics WHERE tempo = '"+temp+"' AND pitch = '"+pitch+"' AND rhythm = '"+rhythm+"' AND zeroCR = '"+zeroCR+"' ").fetchall()

        if len(data) == 0:
            filepath = os.path.join(directory, audio.filename)
            cursor.execute("INSERT INTO musics VALUES (?,?,?,?,?,?,?)",(name, filepath, mood, temp, pitch, rhythm, zeroCR))
            connection.commit()
            try:
                audio.save(filepath)
                print(f'audio save at {filepath}')
                status = "playlist created successful"
                code = True
                while code:                
                    return render_template('', status=status)
                else:
                    code = False
            except FileNotFoundError as e:
                error  = "file not found"
                return
        else:
            error = "song already exists"
    return render_template('drone_index.html')




@app.route("/home", methods=["GET", "POST"])
def home():
    mood = "sad"
    path = cursor.execute("SELECT path FROM musics WHERE MOOD = '"+mood+"' ").fetchone()

    audio = path[0]
    return render_template("drone_index.html", audio=audio)





if __name__ == "__main__":
    app.run(debug=True)