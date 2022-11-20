import speech_recognition
import gtts
from playsound import playsound
import wikipedia
import webbrowser

def get_audio():
    recognition=speech_recognition.Recognizer()
    mic=speech_recognition.Microphone()
    with mic as audio_file:
        audio=recognition.listen(audio_file)
        text=""
        try:
            text = recognition.recognize_google(audio, language='ru-Ru')
        except Exception as e:
            print("Exception"+str(e))

        return text.lower()
wakeup="алиса"
hello=gtts.gTTS("я слышу вас",lang="ru")
hello.save("hello.mp3")
wikipedia.set_lang("ru")
while True:
    print("listening......")
    text=get_audio()
    if text.count(wakeup)>0:
        print("I'am ready")
        playsound("hello.mp3")
        text=get_audio()
        print(text)
        if text.count("что такое")>0:
            result= wikipedia.summary(text.replace("что такое",""))
            info=gtts.gTTS(result,lang="ru")
            info.save("info.mp3")
            playsound("info.mp3")
            print(result)
        if text.count("открой youtube")>0:
            webbrowser.open("https://www.youtube.com/")









