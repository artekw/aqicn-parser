### aqicn-parser
Strona [aqicn.org](http://aqicn.org) udostępnia dane o jakości powietrza. Obecnie API tej strony nie pozwala na dostęp do danych w formacie JSON. Do swojego projektu potrzebowałem danych dla Suwałk. Przy okazji dostępne są da innch miast w pobliżu. Możliwe, że po delikatiej modyfiakacji można dosstosować dla innnych miast Polski/Świata


__Dostępne miasta__:

    Zegrzyńska, Legionowo, Mazowieckie, Polska
    Konarskiego, Siedlce, Mazowieckie, Polska
    Pułaskiego, Piastów, Mazowieckie, Polska
    Targówek, Warszawa, Mazowieckie, Polska
    Marszałkowska, Warszawa, Mazowieckie, Polska
    Komunikacyjna, Warszawa, Mazowieckie, Polska
    Reja, Płock, Mazowieckie, Polska
    Białystok-Miejska, Polska
    Suwałki-Miejska, Polska
    Klaipėda Šilutės Pl., Litwa
    Naujoji Akmenė, Litwa
    Kaunas Petrašiūnai, Litwa
    Łomża-Miejska, Polska
    Vilnius Žirmūnai, Litwa
    Kaunas Noreikiskes, Litwa
    Biała Podlaska, Polska
    KPN, Granica, Mazowieckie, Polska
    Ursynów, Warszawa, Mazowieckie, Polska

Ustaw miasto w pliku, zmianna 'city'


## Użycie:

      $ python aqi.py
      Wyjście:

      Miasto: Suwałki-Miejska, Polska
      Data: N, 24 sty 2016 12:00
      Jakość powietrza: Niezdrowe(153)
