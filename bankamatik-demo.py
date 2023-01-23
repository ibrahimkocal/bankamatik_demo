import json

kullaniciHesap = input("Hesap Adı: ").title().strip()
ad = input("Adınız ve soyadınız:").title().strip()
bakiye = int(input("Kaç paran var:"))
ekhesap = int(input("Ek hesapta kaç paran var: "))
hesapNo = input("Hesap numaranız: ")


kullaniciHesap = {
    "ad" : ad,
    "bakiye": bakiye,
    "ekhesap": ekhesap,
    "hesapNo": hesapNo,
}



def paraCek(hesap, miktar): 
    
    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print("Paranızı alabilirsiniz.")
        bakiyeSorgula(kullaniciHesap)
    else:
        toplam = hesap["bakiye"] + hesap["ekhesap"]
        ekHesapKullanimi = input("Bakiyenizde çekmek istediğiniz kadar para yok. Ek hesabınızı kullanmak ister misiniz? (e/h diye cevaplayınız): ")     
        if ekHesapKullanimi == "e":
                    if (toplam>= miktar):
                        ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                        hesap['bakiye'] = 0
                        hesap['ekhesap'] -= ekHesapKullanilacakMiktar
                        print("Paranızı alabilirsiniz.")
                        bakiyeSorgula(kullaniciHesap)
                    else:
                        print("Bakiye ve ek hesap, çekmek istediğiniz miktara yetmedi. İşlem gerçekleştirilemedi.")    
        elif ekHesapKullanimi == "h":
            print("Para çekme işlemi iptal edildi.")
                
        else:
            print("Yanlış işlem yaptınız, tekrar deneyiniz.")
            bakiyeSorgula(kullaniciHesap)


def paraYatir(hesap,yatirilanpara):        
    hesap["bakiye"] += yatirilanpara
    
def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesabınızda ise {hesap['ekhesap']} TL bulunmaktadır.")

def hesapbilgilerikaydet(kullaniciHesap):
    with open ("hesap_bilgileri.json","a", encoding= "utf-8") as file:
        json.dump(kullaniciHesap, file)

while True:
    print("MENÜ".center(50, "*"))
    print(f"Merhaba {kullaniciHesap['ad']}, yapmak istediğiniz işlemi seçiniz.")
    secim = input("1- Para Yatırma\n2- Para Çekme\n3- Bakiye Öğrenme\n4- Çıkış\nİŞLEM SAYISINI GİRİNİZ: ")
    if secim == "1":
        yatirilanpara = int(input("Para yatıralacak tutarı giriniz. (*Yatırılan para ana hesabınıza gidecek): "))
        print("Para yatırma işlemi gerçekleşti.")
        paraYatir(kullaniciHesap, yatirilanpara)
        bakiyeSorgula(kullaniciHesap)
        hesapbilgilerikaydet(kullaniciHesap)
    elif secim == "2":     
        tutar = int(input("Para çekilecek tutarı giriniz:"))
        paraCek(kullaniciHesap, tutar)
        bakiyeSorgula(kullaniciHesap)
        hesapbilgilerikaydet(kullaniciHesap)
    elif secim == "3":
        bakiyeSorgula(kullaniciHesap)
        hesapbilgilerikaydet(kullaniciHesap)
    elif secim == "4":
        break
    else:
        print("Yanlış işlem yaptınız. Tekrar deneyiniz.")
        
hesapbilgilerikaydet(kullaniciHesap)        