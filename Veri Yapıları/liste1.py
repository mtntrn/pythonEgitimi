# # 1-  "Samsung S5,Samsung S6,Samsung S7,Samsung S8" elemanlarına sahip bir liste oluşturunuz.
# liste=["Samsung S5","Samsung S6","Samsung S7","Samsung S8"]

# # 2-  Liste Kaç elemanlıdır ?
# sonuc=len(liste)

# # 3-  Listenin ilk ve son elemanı nedir ?
# sonuc=f"ilk: {liste[0]}, son: {liste[-1]}"

# # 4-  "Samsung S5" değerini "Samsung S9" ile değiştirin.
# liste[0]="Samsung S9"
# sonuc=liste

# # 5-  "Samsung S6" listenin bir elemanı mıdır ?
# sonuc="Samsung S6" in liste

# # 6-  Listenin -3 indeksindeki değer nedir ?
# sonuc=liste[-3]

# # 7-  Listenin ilk 2 elemanını alın.
# sonuc=liste[:2]

# # 8-  Listenin son 2 elemanı yerine "Samsung S9" ve "Samsung S10" değerlerini ekleyin.
# # liste[len(liste)-2]="Samsung S9"
# # liste[len(liste)-1]="Samsung S10" #bu ikisi kötü yol.
# liste[-2:]=["Samsung S9","Samsung S10"]
# sonuc=liste

# # 9-  Listenin üzerine "IPhone X" ve "IPhone XR" değerlerini ekleyin.
# liste=liste+["IPhone X"]+["IPhone XR"]
# sonuc=liste

# # 10- Listenin son elemanını silin.
# del(liste[-1])
# sonuc=liste

# # 11- Liste elemanlarını tersten yazdırınız.
# sonuc=liste[::-1]

# # 12- Aşağıdaki verileri bir liste içinde saklayınız. 

#       # kullaniciA: Yiğit Bilgi 2010, (70,60,70)
#       # kullaniciB: Sena Turan  1999, (80,80,70)
#       # kullaniciC: Ahmet Turan 1998, (80,70,90) 

# kullanicilar=[["kullaniciA:", "Yiğit", "Bilgi", 2010, (70,60,70)],["kullaniciB:", "Sena", "Turan",  1999, (80,80,70)],["kullaniciC:", "Ahmet", "Turan", 1998, (80,70,90)]]
# sonuc=kullanicilar[0][2]

# # 13- Liste elemanlarını ekrana yazdırınız.
# for i in kullanicilar:
#       print(i)

# print(sonuc)
