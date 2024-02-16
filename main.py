import msvcrt
import os
class lib:
    def __init__(self):
        self.dosya_yolu = os.path.join("books.txt")
        self.dosya = open(self.dosya_yolu, "a+")
        self.baslik_goster()
        print("The Gramr'a hoşgeldin! Devam etmek için herhangi bir tuşa bas.")
        input()


    def __del__(self):
        self.dosya.close()

    def baslik_goster(self):
        print("\n")
        print(" _____ _             ____                          ")
        print("|_   _| |__   ___   / ___|_ __ __ _ _ __ ___  _ __ ")
        print("  | | | '_ \ / _ \ | |  _| '__/ _` | '_ ` _ \| '__|")
        print("  | | | | | |  __/ | |_| | | | (_| | | | | | | |   ")
        print("  |_| |_| |_|\___|  \____|_|  \__,_|_| |_| |_|_|   ")
        print("          DEVELOPED BY REZAN CANPOLAT              ")

    def wait_for_key(self):
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                break

    def kitaplari_listele(self):
        try:
            self.dosya.seek(0)
            kitap_satirlari = self.dosya.read().splitlines()
            for satir in kitap_satirlari:
                kitap_bilgisi = satir.split(',')
                print(f"Kitap: {kitap_bilgisi[0]} || Yazar: {kitap_bilgisi[1]} || Yayınyılı: {kitap_bilgisi[2]} || Sayfa Sayısı: {kitap_bilgisi[3]}  ")
        except KeyboardInterrupt:
            print("\n Ana menüye dönüşüyor")
    def kitap_ekle(self):
        try:
            while True:
                print("işlemi iptal etmek için CTRL + C yapınız.")
                baslik = input("Kitap başlığını girin: ").strip()
                if not baslik:
                    print("Lütfen bir kitap başlığı girin.")
                    continue

                yazar = input("Yazarı girin: ").strip()
                if not yazar:
                    print("Lütfen bir yazar adı girin.")
                    continue

                while True:
                    yayin_yili = input("Yayın yılını girin: ").strip()
                    if not yayin_yili.isdigit():
                        print("Lütfen geçerli bir yıl girin.")
                        continue
                    else:
                        break

                while True:
                    sayfa_sayisi = input("Sayfa sayısını girin: ").strip()
                    if not sayfa_sayisi.isdigit():
                        print("Lütfen geçerli bir sayfa sayısı girin.")
                        continue
                    else:
                        break

                kitap_bilgisi = f"{baslik},{yazar},{yayin_yili},{sayfa_sayisi}\n"
                self.dosya.write(kitap_bilgisi)
                print(f"Kitap '{baslik}' eklendi")
                break
        except KeyboardInterrupt:
            print("\n Ana menüye dönülüyor")


    def kitap_kaldir(self):
        try:
            while True:
                print("işlemi iptal etmek için CTRL + C yapınız.")
                kaldirilacak_baslik = input("Kaldırılacak kitabın başlığını gir: ").strip()
                if not kaldirilacak_baslik:
                    print("Lütfen bir kitap başlığı girin.")
                    continue

                self.dosya.seek(0)
                kitap_satirlari = self.dosya.readlines()
                guncellenmis_kitaplar = [satir for satir in kitap_satirlari if kaldirilacak_baslik not in satir.strip()]

                self.dosya.seek(0)
                self.dosya.truncate()
                self.dosya.writelines(guncellenmis_kitaplar)
                print(f"Kitap '{kaldirilacak_baslik}' kaldırıldı")
                break
        except KeyboardInterrupt:
            print("\n Ana menüye dönülüyor.")


    def YARDIM(self):
        print( )
        print("1 Eklenmiş olan kitapları listeler.")
        print("2 Eklemek istediğiniz kitaba isim, yazar, yayın yılı, sayfa sayısı girdisi alarak kitabı ekler.")
        print("3 Eklediğiniz kitabın ismini yazarak silmenizi sağlar.")
        print("5 Programı sonlandırır.")

lib_nesnesi = lib()

try:
    while True:
        print("\n--- MENU ---")
        print("1 - Kitapları Listele")
        print("2 - Kitap Ekle")
        print("3 - Kitap Kaldır")
        print("4 - YARDIM")
        print("5 - Çıkış")

        secim = msvcrt.getwch()

        if secim in ["1", "2", "3", "4", "5"]:
            if secim == "1":
                lib_nesnesi.kitaplari_listele()
            elif secim == "2":
                lib_nesnesi.kitap_ekle()
            elif secim == "3":
                lib_nesnesi.kitap_kaldir()
            elif secim == "4":
                lib_nesnesi.YARDIM()
            elif secim == "5":
                print("Programdan çıkılıyor")
                break
        else:
            print("Lütfen 1 ile 5 arası bir sayı girin.")

except KeyboardInterrupt:
    print("\nAna menüye dönülüyor...")
