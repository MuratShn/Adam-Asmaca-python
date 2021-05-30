import random
import requests
from bs4 import BeautifulSoup

kelimeler = []

response = requests.get("https://huseyindemirtas.net/turkcedeki-guzel-kelimeler/")
soup = BeautifulSoup(response.content,"html.parser")

for i in soup.find("div",{"class": "nv-content-wrap entry-content"}).find_all("li"):
    if not(" " in i.text or "," in i.text):
        kelimeler.append(i.text)

def kelimeSec():
    kelime = random.choice(kelimeler)
    return kelime.upper()

def oyna(kelime):
    kelimeErkanı = "_"*len(kelime)
    tahminEt = False
    tahminHarfi = []
    tahminKelimeleri = []
    hak = 10
    
    print(f"OYUN BASLADI KELİME {len(kelime)} HARFLİ")
    print(kelimeErkanı)
    
    while(hak > 0 and tahminEt == False):
        tahmin = input("Tahmin yapınız: ").upper()
        
        if(len(tahmin)==1 and tahmin.isalpha()):
            
            if(tahmin in tahminHarfi):
                print(f"{tahmin} harfini zaten tahmin ettiniz")                
            
            elif(tahmin not in kelime):
                hak -=1
                print(f"Harf bulunamamaktadır kalan hakkınız {hak}")
                tahminHarfi.append(tahmin)
            else:
                print(f"{tahmin} Kelimede mevcut.")
                tahminHarfi.append(tahmin)
                kelimeDizisi = list(kelimeErkanı)
                indexler = []

                for i in range (len(kelime)):
                    if tahmin == kelime[i]:
                        indexler.append(i)

                for index in indexler:
                    kelimeDizisi[index] = tahmin
                    
                kelimeErkanı = "".join(kelimeDizisi)
                
                if("_" not in kelimeErkanı):
                    print("Tebrikler Doğru bildiniz")
                    tahminEt = True
                print(kelimeErkanı)
                    
        
        elif(len(tahmin)==len(kelime) and tahmin.isalpha()):
            
            if(tahmin in tahminKelimeleri):
                print(f"Bu tahmini Daha önce Yaptınız {tahmin}")
            
            elif(tahmin == kelime):
                print("Tebrikler Doğru bildiniz")
                print(kelime)
                tahminEt = True
            else:
                print(f"Kelimeniz doğru değil kalan hakknıız:{hak}")
                tahminKelimeleri.append(tahmin)
    
        else:
            hak -=1
            print(f"Harf bulunamadı hakkınız: {hak}")
            
def calistir():
    kkk = kelimeSec()
    oyna(kkk)
    while input("Tekrar oynamak istermisiniz = E/H:").upper() == "E":
        kkk = kelimeSec()
        oyna(kkk)

calistir()