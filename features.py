import librosa


def tempos(music):
    try:
        y, sr = librosa.load(music)
        onset_env = librosa.onset.onset_strength(y=y, sr=sr)
        tempo, _ = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)

        return tempo
    except Exception as e:
        return None



def pitchs(music):
    try:
        audio, sr = librosa.load(music)

        pitch, magnitudes = librosa.piptrack(y=audio, sr=sr)
        pitch = pitch[magnitudes.argmax(axis=0)]

        return pitch.shape[0]
    except Exception as e:
        print(f"error in {e}")


def rhythmies(music):
    try:
        audio, sr = librosa.load(music)

        onset_env = librosa.onset.onset_strength(y=audio, sr=sr)
        _, beat_frame = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)

        return beat_frame.shape[0]
    except Exception as e:
        print(f"error {e}")
        return None


def Zerocrossingrating(music):
    audio, sr = librosa.load(music)
    zero_crossing_rating = librosa.feature.zero_crossing_rate(y=audio)
    return zero_crossing_rating.shape[1]



def arrange(files):
    tempsort  = sorted(files, key=lambda file: tempos(file))
    return tempsort



