from random import choice

class Olasilik:
    """
	Bu modülde zar atma | yazı & tura | taş, kağıt ve makas işlevleri vardır.
        Kullanım:
            zar_at()
            yazi_tura()
            tas_kagit_makas()

        This module functions returns head or tail, rock or paper or scissors,
        dice or roll.
        Usage:
            zar_at()
            yazi_tura()
            tas_kagit_makas()
    """
    def zar_at(self): # zar_at isimli fonksiyon tanımlanır.
        return choice(range(6)) # Aralığı 1-6 olan değerden rastgele seçim yapar.
    def yazi_tura(self): # yazi_tura isimli fonksiyon tanımlanır.
        return choice(["Yazı", "Tura"]) # Yazı Tura değerlerinden seçim yapar.
    def tas_kagit_makas(self):  # tas_kagit_makas isimli fonksiyon tanımlanır.
        return choice(["Taş", "Kağıt", "Makas"]) # Aynı şekilde 3 değerden birini rastgele seçer.

cekilis = Olasilik() # Olasilik sınıfı, cekilis adlı nesneye atanır.

print(cekilis.zar_at()) # Cekilis nesnesinin zar_at() fonksiyonu çalıştırılır ve sonucu ekrana yazdırılır.
print(cekilis.yazi_tura()) # Aynı işlem burada da yapılır.
print(cekilis.tas_kagit_makas()) #Burada da.
