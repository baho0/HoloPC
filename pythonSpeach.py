#gerekli kütüphaneler eklenir
import speech_recognition as sr
import os
from gtts import gTTS
from playsound import playsound

def speak(val): #içindeki değerde verilen metini okutur.
    tts = gTTS(text=val,lang="tr",slow=False)
    file = "asnwer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

def mic(val):#ses algılar ve içindeki değeri okur.
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        if(val != ""):
            speak(val)
        audio = rec.listen(mic)
        print(">>>")
        try:
            
            said = rec.recognize_google(audio, language="tr-TR")
            if(said != ""):
                said = said.lower()
            return said
        except Exception as e:
            print("Error occured -> " + str(e))
