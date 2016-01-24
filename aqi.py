#!/usr/bin/env python#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
import json


city = u'Suwałki-Miejska, Polska'
"""
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
"""

html = requests.get('http://aqicn.org/city/poland/bialystok/suwalki-miejska/pl/')
soup = BeautifulSoup(html.text)
script = soup.find('script', text=re.compile('var mapStationData'))
json_text = re.search('({.*}])',script.string, flags=re.DOTALL | re.MULTILINE).group(1)
json_text = json_text + '}'
json_data = json.loads(json_text)

scale = {
        (0,50):u'Dobra',
        (51,100):u'Średnia',
        (101,150):u'Niezdrowe dla wrażliwych osób',
        (151,200):u'Niezdrowe',
        (201,300):u'Bardzo niezdrowe',
        (301,999):u'Niebezpieczny'
}

for c in json_data['Poland/Bialystok/Suwa%C5%82ki-Miejska']:
    if c['city'] == city:
        sensor_data = c

print "%s: %s" % ("Miasto",  sensor_data['city'])
print "%s: %s" % ("Data",  sensor_data['utime'])

try:
    for s in scale.keys():
        if s[0] <= int(sensor_data['aqi']) <= s[1]:
            aqi = scale[s]
except ValueError:
        aqi = 'Brak danych'
finally:
        print "%s: %s(%s)" % (u'Jakość powietrza', aqi, sensor_data['aqi'])
