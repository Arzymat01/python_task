import playsound
import  speech_recognition as sr
from gtts import gTTS
import random

def konuş(yazı):
    tts = gTTS(text = yazı, lang= "ru")
    dosya_ismi = "ses"+ str(random.randint(0,1000000000000000000000)) + ".mp3"
    tts.save(dosya_ismi)
    playsound.playsound(dosya_ismi)

def sesi_kaydet():
    r = sr.Recognizer()

    with sr.Microphone() as kaynak:
        ses = r.listen(kaynak)

        söylenen_cümle = ""

        try:
            söylenen_cümle = r.recognize_google(ses, language="ru-Ru")
            print(söylenen_cümle)

        except Exception:
            konuş("Я не мог понять предложение, которое вы сказали")

    return söylenen_cümle

while True:
    yazı = sesi_kaydet()
    if "Привет" in yazı:
        konuş("Я в порядке, как ты")

