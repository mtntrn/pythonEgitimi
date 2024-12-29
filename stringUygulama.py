site="https://www.metinturan.com"
kursAdi="Sıfırdan İleri Seviye Python Öğreniyorum."

#Kurs adı kaç karakter.
print(f"Bu kursun adı {len(kursAdi)} karakterden oluşmaktadır.")
#www kısmını al
print(f"www: {site[8:11]}")
#com karakterini al
print(f"com: {site[-3:]}")
#Kurs adı ilk 5 ve son 5 karakeri al
print(f"İlk 5ten son 5e: {kursAdi[4:-4]}")
#kurs adını tersten yaz
print(kursAdi[::-1])
#Hello world ifadesindeki w karakterini W karakteri ile değiştir.
hello="Hello world"
hello=str.replace(hello,hello,"Hello World")
print(hello)
#abc ifadesini 3 defa yan yana yazdır
print("{0}{0}{0}".format("abc"))
print("abx"*3)
#######
name, surname, year, job="Metin","TURAN",32,"Öğretmen"
#Yukarıdaki ifadelerle 'Benim adım Ali KÖKLÜ. 55 yaşındayım ve Mühendisim.' yazıdr.
name="Ali"
surname="KÖKLÜ"
year=55
job="Mühendis"
print("Benim adım {} {}. {} yaşındayım ve {}im.".format(name,surname,year,job))
