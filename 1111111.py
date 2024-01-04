import speech_recognition as sr

recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Say something please !")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="zh-CN", show_all=False)
            print("You said : {}".format(text))

        except:
            print("Sorry I can't hear you!")
