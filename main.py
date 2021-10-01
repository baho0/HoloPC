#Gerekli kütüphaneleri ekleme.
import pythonSpeach
import os
from bs4 import BeautifulSoup
import requests

# Ana döngü
while True:
    
    said = pythonSpeach.mic("") #Ses tanıma işlemi. Tanınan ses bir değişkene verilir.
    print(said) #Tanınan ses konsola yazılır
    if(said != None): #Eğer ses algılandıysa
        if("merhaba" in said): #algılanan ses merhaba ise
            pythonSpeach.speak("Merhaba")

        elif(said == "not yaz"): #algılanan ses not yaz ise boş bir dosya açılır ve istenilen şey dosyaya yazılır.
            said = pythonSpeach.mic("ne yazmamı istersiniz")
            with open("unnamed.txt", "w+") as f: 
                f.write(said)
                pythonSpeach.speak("kaydettim")   

        elif(said == "klasör oluştur"): #algılanan ses klasör oluştur ise belirtilen isimde klasör oluşturulur
            said = pythonSpeach.mic("klasör oluşturuluyor") 
            saidSplit = said.split(" ")
            name = saidSplit[2]          
            os.system("mkdir "+"")
            pythonSpeach.speak("klasör oluşturuldu")

        elif(said == "oku"):#Daha önce not yazıldıysa onu okur
            try:
                with open("unnamed.txt","r") as f:
                    pythonSpeach.speak(f.read())
                    f.close()
                    os.remove("unnamed.txt")
                    
            except Exception as e:
                print("Error occured -> " + str(e))

        elif(said == "kapat"): #programı kapatır
            pythonSpeach.speak("görüşmek üzere")
            break
        
        elif("ara " in said):  #aranmak istenen şey aranır
            searchText = "start chrome www.google.com/search?q="
            if(" " in said):
                said = said.split(" ")
                queue = 1
                
                while(queue < len(said)):
                    searchText += said[queue]
                    searchText += "+"
                    queue += 1
                os.system(searchText)
            elif(said != ""):
                said = str(said)
                searchText += said
                os.system(searchText)
            else:
                pythonSpeach.speak("hata")

        elif(said == "faresiz kullan"): #bilgisayarı el ile yönetmek için gereken programı çalıştırır.
            os.system("hand.py")
            
        elif("hava durumu" in said):# belirtilen şehirin hava durumu bilgisini söyler.
            saidSplit = said.split(" ")
            url = "https://www.havadurumu15gunluk.xyz/havadurumu7/90/ankara-hava-durumu-7-gunluk.html"
            try:
                url = url.replace("ankara",saidSplit[2])
            except:
                url = "https://www.havadurumu15gunluk.xyz/havadurumu7/90/ankara-hava-durumu-7-gunluk.html"
            r = requests.get(url)
            veri = 0
            soup = BeautifulSoup(r.content,"html.parser")
            veri = soup.find_all("div",{"class":"box"}) 
            veri = soup.find_all("span",{"class":"temperature type-1"})
            veri = veri[0].text
            pythonSpeach.speak("internetten edindiğim verilere göre bu gün "+veri)
        elif("nedir" in said):
            saidSplit = said.split(" ")
            url = "https://www.nedir.com/" + saidSplit[0]
            r = requests.get(url)
            soup = BeautifulSoup(r.content,"html.parser")
            veri = soup.find_all("article") 
            veri = soup.find_all("p")
            veri = veri[0].text
            pythonSpeach.speak(veri)
        
        if("aç" in said or "çalıştır" in said or "başlat" in said):#daha önce eklenen uygulamaları çalıştırır.
            saidSplit = said.split(" ")
            try:
                uygulama = saidSplit[1]
                paths = {"chrome" : "chrome","kod" : "code","discord" : "C:/Users/Administrator/AppData/Local/Discord/Update.exe --processStart Discord.exe","word":"C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"}
                path = paths[uygulama]
                os.system("start "+ path)
            except:
                print("HATA!")


