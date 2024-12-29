ad="Metin"
soyad="TURAN"
yas=32

# print("My name is {} {}. I'm {} old.".format(ad, soyad, yas)) # format string kullanımı
# print("My name is {0} {0}. I'm {0} old.".format(ad, soyad, yas)) # format string index kullanımı
# print("My name is {n} {s}. I'm {y} old.".format(n=ad, s=soyad, y=yas)) # format string değişken atama
print(f"My name is {ad} {soyad}. I'm {yas} old.") # fstring kullanımı
print(f"My name is {ad} {soyad[0:3]}. I'm {yas} old.")