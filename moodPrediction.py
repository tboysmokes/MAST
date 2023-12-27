from features import tempos, rhythmies, pitchs, Zerocrossingrating
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn import svm


# create a mood algorithm
def mood_prediction(music):
    # data collection
    data = {
        "happy": [
            "static/happy_love/BTS (방탄소년단) 'Butter' Official MV.mp4",
            "static/happy_love/David Guetta & Bebe Rexha - I'm Good (Blue) [Official Music Video].mp4",
            "static/happy_love/Ed Sheeran - Shivers [Official Performance Video].mp4",
            "static/happy_love/Rema, Selena Gomez - Calm Down (Official Music Video).mp4",
            "static/happy_love/Rema_-_Charm.mp3",
            "static/happy_love/BTS-Dynamite-(TrendyBeatz.com).mp3",
        ],
        "sad": [
            "static/sad_heartbreak/Adele - Someone Like You (Official Music Video).mp4",
            "static/sad_heartbreak/Giveon - Heartbreak Anniversary (Audio).mp4",
            "static/sad_heartbreak/Olivia Rodrigo - traitor (Official Video).mp4",
            "static/sad_heartbreak/R.E.M. - Everybody Hurts (Official Music Video).mp4",
            "static/sad_heartbreak/With_Or_Without_You.mp4",
            "static/sad_heartbreak/Omah_Lay_-_Reason.mp3",
            "static/sad_heartbreak/CKay-Felony-(TrendyBeatz.com).mp3",
            "static/sad_heartbreak/Juice_WRLD_-_Hear_Me_Calling_(thinknews.com.ng).mp3",
            "static/sad_heartbreak/Lewis Capaldi - Wish You The Best (Live from The Voice).mp4",
        ],
    }
    # feature extraction
    feature = []
    labels = []

    for mood, audio_list in data.items():
        for audio in audio_list:
            tempo = tempos(audio)
            rythm = rhythmies(audio)
            pitch = pitchs(audio)
            zeroCR = Zerocrossingrating(audio)

            feature.append([tempo, rythm, pitch, zeroCR])
            labels.append([mood])

    # split data
    label_encoder = LabelEncoder()
    encoded_labels = label_encoder.fit_transform(labels)

    X_train, X_test, Y_train, Y_test = train_test_split(
        feature, encoded_labels, test_size=0.1, random_state=42
    )

    # machine learning model
    model = svm.SVC(kernel="linear", C=1)
    model.fit(X_train, Y_train)

    tem = tempos(music=music)
    rhyth = rhythmies(music=music)
    pitc = pitchs(music=music)
    zercr = Zerocrossingrating(music=music)

    # prediction
    data = [[tem, rhyth, pitc, zercr]]
    Y_pred = model.predict(data)

    return label_encoder.classes_[Y_pred[0]]
    # evalute the model
