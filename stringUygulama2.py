website = "https://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
# sonuc=' Hello World '
# sonuc=sonuc.strip() #lstrip soldan, rstrip sağdan siler. parantez içerisine yazdığın karakterleri de siler yazılmazsa boşluk siler.
# sonuc=website.lstrip('htp:/s') #sadece sol baştan
# sonuc=sonuc.rstrip('.com') #sadece sağ baştan
# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
# sonuc='www.sadikturan.com'
# sonuc=f"{sonuc[sonuc.index(".")+1:sonuc.index(".com")]}"
#2. yol
# sonuc='www.sadikturan.com'
# sonuc=sonuc.strip('w.com')

# 3- 'kursAdi' karakter dizisinin tüm karakterlerini küçük harf yapın.
# sonuc=kursAdi.lower()

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
# sonuc=website.count("a")

# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
# sonuc=website.startswith("www") and website.endswith("com")

# 6- 'website' içinde '.com' ifadesi var mı?
# sonuc=website.__contains__(".com") #contains yok galiba bu sebeple index numarasını bul find veya index ile
# sonuc=website.find(".com")

# 7- 'kursAdi' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
# sonuc=kursAdi.isalpha() # sadece a-z arası karakterleri içeriyorsa true
# sonuc=kursAdi.isdigit() # sadece 0-9 arası karakterleri içeriyorsa true
# sonuc=kursAdi.isalnum() # sadece a-z arası karakterleri ve 0-9 arası karakterleri içeriyorsa true

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
# x="Contents"
# sonuc=x.center(50,"*")

# 9- 'kursAdi' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
# sonuc=kursAdi.replace(" ","-")

# 10-'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
# x='Hello World'
# sonuc=x.replace("World","There")

# 11-'kursAdi' karakter dizisini boşluk karakterlerinden ayırın.
# sonuc=kursAdi.split()

print(sonuc)