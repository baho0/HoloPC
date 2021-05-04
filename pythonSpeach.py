import speech_recognition as sr
import os
from gtts import gTTS
from playsound import playsound

def speak(val):
    tts = gTTS(text=val,lang="tr",slow=False)
    file = "asnwer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

def mic(val):
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
"""
while True:
    said = mic("")

    if("merhaba" in said):
        speak("Merhaba")

    if(said == "yazı yaz"):
        said = mic("ne yazmamı istersiniz")
        with open("unnamed.txt", "w+") as f:
            f.write(said)
            speak("kaydettim")   

    if(said == "klasör oluştur"):
        said = mic("klasör oluşturuluyor")           
        os.system("mkdir "+said)
        speak("klasör oluşturuldu")

    if(said == "oku"):
        try:
            with open("unnamed.txt","r") as f:
                speak(f.read())
                f.close()
                os.remove("unnamed.txt")
                
        except Exception as e:
            print("Error occured -> " + str(e))

    if(said == "kapat"):
        speak("görüşmek üzere")
        break

    if(said == "elsiz yönetim"):
        os.system("pythonSpeach.py")
    
    if(said == ara):
        #netten aratma
        pass
    """