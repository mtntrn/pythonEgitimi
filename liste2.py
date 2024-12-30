# isimler = ['Ada','Yiğit','Hasan','Beril']
# yaslar = [1998, 2000, 1998, 1987,1987]

# # 1-  "Cenk" ismini listenin sonuna ekleyiniz.
# isimler.append("Cenk")

# # 2-  "Sena" değerini listenin başına ekleyiniz.
# isimler.insert(0,"Sena")

# # 4-  "Yiğit" isminin indeksi nedir ?
# print(isimler.index("Yiğit"))

# # 3-  "Yiğit" ismini listeden siliniz.
# isimler.remove("Yiğit")

# # 5-  "Beril" listenin bir elemanı mıdır ?
# print("Beril" in isimler)

# # 6-  Liste elemanlarını ters çevirin.
# isimler.reverse()
# yaslar.reverse()

# # 7-  Liste elemanlarını alfabetik olarak sıralayınız.
# isimler.sort()
# yaslar.sort()

# # 8-  yaslar listesini rakamsal büyüklüğe göre sıralayınız.
# yaslar.sort(reverse=True)

# # 9-  s = "IPhone X,IPhone XR" karakter dizisini listeye çeviriniz.
# s = "IPhone X,IPhone XR"
# s=s.split(",")

# # 10- yaslar dizisinin en büyük ve en küçük elemanı nedir ?
# print(min(yaslar))
# print(max(yaslar))

# # 11- yaslar dizisinde kaç tane 1998 değeri vardır ?
# # print(yaslar.count(1987))

# # 12- yaslar dizisinin tüm elemanlarını siliniz.
# yaslar.clear()

# # 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
# markalar=[]
# markalar.append(input("Bir marka giriniz: "))
# markalar.append(input("Bir marka giriniz: "))
# markalar.append(input("Bir marka giriniz: "))
# ## veya
# i=0
# while (i<3):
#     markalar.append(input("Bir marka giriniz: "))
#     i+=1

# print(markalar)

# print(isimler)
# print(yaslar)
# print(s)