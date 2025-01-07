'''
    player 1: 
        id           => 1
        name         => Cristiano Ronaldo
        yearOfBirth  => 1985
        nationality  => Portugal
        current_team => Portugal
        history      => Juventus,Real Madrid,Portugal

    player 2: 
        id           => 2
        name         => Lionel Messi
        yearOfBirth  => 1987
        nationality  => Argentina
        current_team => Barcelona,
        history      => Barcelona,Argentina,Portugal
'''

# 1- Yukarıda verilen bilgileri liste içerisinde saklayınız.

players={ # İçiçe sözlük
    0:{
        "name" : "Cristiano Ronaldo",
        "yearOfBirth" : 1985,
        "nationality" : "Portugal",
        "current_team" : "Portugal",
        "history" : ["Juventus","Real Madrid","Portugal"]
    },
    1:{
        "name" : "Lionel Messi",
        "yearOfBirth" : 1987,
        "nationality" : "Argentina",
        "current_team" : "Barcelona",
        "history" : ["Barcelona","Argentina","Portugal"]
    }
}

# players=[ #Liste
#     {
#         "id" : 1,
#         "name" : "Cristiano Ronaldo",
#         "yearOfBirth" : 1985,
#         "nationality" : "Portugal",
#         "current_team" : "Portugal",
#         "history" : "Juventus,Real Madrid,Portugal"
#     },
#     {
#         "id" : 2,
#         "name" : "Lionel Messi",
#         "yearOfBirth" : 1987,
#         "nationality" : "Argentina",
#         "current_team" : "Barcelona",
#         "history" : "Barcelona,Argentina,Portugal"
#     }
# ]
sonuc=players
# # 2- id' e göre arama yapınız.
id=int(input("Aramak istediğiniz oyuncuya ait ID bilgisini giriniz: "))-1
# sonuc=players[id].get("history")[1]
sonuc=players.get(id).get("history")[1]

# 2- id' e göre kayıt silniz.
# print(sonuc)
# id=int(input("Silmek istediğiniz oyuncuya ait ID bilgisini giriniz: "))-1
# players.pop(id)
# sonuc=players
print(sonuc)