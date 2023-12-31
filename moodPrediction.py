from features import tempos, rhythmies, pitchs, Zerocrossingrating
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn import svm


# create a mood algorithm
def mood_prediction(music):
    # data collection
    data = {
        "happy": [
            "static/happy_love/Rema_-_Charm.mp3",
            "static/happy_love/BTS-Dynamite-(TrendyBeatz.com).mp3",
            "static/happy_love/Ckay-La-La-Ft-Davido-(TrendyBeatz.com).mp3",
            "static/happy_love/Kizz-Daniel-Twe-Twe-(TrendyBeatz.com).mp3",
            "static/happy_love/BNXN-fka-Buju-Ft-Kizz-Daniel-and-Seyi-Vibez-Gwagwalada-(TrendyBeatz.com).mp3",
            "static/happy_love/Rema-DND-(TrendyBeatz.com).mp3",
            "static/happy_love/Tyla-Water-(TrendyBeatz.com).mp3",
            "static/happy_love/Davido-Ft-Adekunle-Gold-High-(TrendyBeatz.com).mp3",
            "static/happy_love/Bnxn-Bad-Since-97-(TrendyBeatz.com).mp3"
        ],
        "sad": [
            "static/sad_heartbreak/Omah_Lay_-_Reason.mp3",
            "static/sad_heartbreak/CKay-Felony-(TrendyBeatz.com).mp3",
            "static/sad_heartbreak/Juice_WRLD_-_Hear_Me_Calling_(thinknews.com.ng).mp3",
            "static/sad_heartbreak/Omah-Lay-I'm-A-Mess-(TrendyBeatz.com).mp3"
        ],
        "chill": [
            "static/chill/Melvitto-Ft-Gabzy-In-Fact-(TrendyBeatz.com).mp3",
            "static/chill/Omah-Lay-Attention-ft-Justin-Bieber-(TrendyBeatz.com).mp3",
            "static/chill/Omah-Lay-Do-Not-Disturb.mp3",
            "static/chill/Qing-Madi-Ft-BNXN-Ole-New-Song-(TrendyBeatz.com).mp3",
            "static/chill/Omah-Lay-Holy-Ghost-(TrendyBeatz.com).mp3",
            "static/chill/Oxlade-Ft-Dave-Intoxycated-(TrendyBeatz.com).mp3",
            "static/chill/Wizkid-Ft-Tay-Iwar-Projexx-True-Love-[TrendyBeatz.com].mp3",
            "static/chill/Justin-Bieber-Sorry-.mp3",
            "static/chill/Asake-Dull-New-Song-(TrendyBeatz.com).mp3",
            "static/chill/Rema-Calm-Down-(TrendyBeatz.com).mp3"
        ]
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


audio = 'static/musicF/Banky-W-Yes-No.mp3'
mood  = mood_prediction(audio)
print(mood)