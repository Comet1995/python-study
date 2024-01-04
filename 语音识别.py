import speech_recognition as sr

with sr.Microphone() as source:
    r = sr.Recognizer()
    # read the audio data from the default microphone

    audio_data = r.record(source, duration=1)

    print("Recognizing…")

    # convert speech to text

    text = r.recognize_google(audio_data,language="zh-ZH")

    print(text)
