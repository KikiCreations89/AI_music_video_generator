import librosa

def analyze_audio(audio_path):
    y, sr = librosa.load(audio_path)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    return tempo, len(beats)
