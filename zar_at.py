import random

enaz = 1 # Zar veya herhangi bir nesnede olabilecek en az değer girilir.
enfazla = 6 # Zar veya herhangi bir nesnede olabilecek en fazla değer girilir.
zar_at = "evet" # zar_at değişkeni için başlangıç değeri olarak 'evet' verilir.

while zar_at == "evet" or zar_at == "e" or zar_at == "yes" or zar_at == "y": # While döngüsü ile kullanıcıdan gelecek 4 farklı cevap türüne göre aşağıdaki işlemler yaptırılır.
    print("Zar atılıyor. Gelen zarlar: ") # Ekrana mesajı yazar.
    print(random.randint(enaz, enfazla) , " ve " , random.randint(enaz, enfazla)) # random ile belirlenen aralıkta rastgele bir sayı yazdırır, ikinci zar için aynı komut kullanılır.
    zar_at = input("Tekrar zar atılsın mı?") # Kullanıcıya soru sorularak bir input yani giriş alınırak, zar_at değişkenine atanır. Verilen cevap koşulu sağlıyorsa döngü çalışmaya devam eder.
