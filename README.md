# 🏙️ TRSehirler

![Repo Boyutu](https://img.shields.io/github/repo-size/keyiflerolsun/TRSehirler) ![Views](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/keyiflerolsun/TRSehirler&title=Profile%20Views) [![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/keyiflerolsun/TRSehirler)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/TRSehirler)
![PyPI - Status](https://img.shields.io/pypi/status/TRSehirler)
![PyPI](https://img.shields.io/pypi/v/TRSehirler)
![PyPI - Downloads](https://img.shields.io/pypi/dm/TRSehirler)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/TRSehirler)
![PyPI - License](https://img.shields.io/pypi/l/TRSehirler)

*Türkiye Cumhuriyeti Devleti Şehirlerini; İl, Plaka, Telefon veya İlçe bilgisinden bulun..*

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/keyiflerolsun/)

## 🚀 Kurulum

```bash
# Yüklemek
pip install TRSehirler

# Güncellemek
pip install -U TRSehirler
```

## 📝 Proje İlerlemesi

- [x] *Proje itinayla* *~* **[sarslanoglu/turkish_cities](https://github.com/sarslanoglu/turkish_cities)***'den `dızz 🐍`'lanmıştır..*
- [x] `v0.1.0` *ile* **[Sehir](https://github.com/keyiflerolsun/TRSehirler#-sehir)** *Objesi Eklenmiştir..*
- [x] `v0.1.1` *ile* **nesne** *statik metodu oluşturuldu..*

### 🌆 Sehir

```python
from TRSehirler import Sehir

sehir = Sehir()

print(sehir.il('Çanakkale'))
'''
İl ile il Sorgusu

{'plaka': 17, 'il': 'Çanakkale', 'telefon': 286, 'buyuksehir_den_beri': None, 'bolge': 'Marmara', 'ilceler': ['Ayvacık', 'Bayramiç', 'Biga', 'Bozcaada', 'Çan', 'Eceabat', 'Ezine', 'Gelibolu', 'Gökçeada', 'Lapseki', 'Merkez', 'Yenice']}
'''

print(sehir.plaka(17))
'''
Plaka ile il Sorgusu

{'plaka': 17, 'il': 'Çanakkale', 'telefon': 286, 'buyuksehir_den_beri': None, 'bolge': 'Marmara', 'ilceler': ['Ayvacık', 'Bayramiç', 'Biga', 'Bozcaada', 'Çan', 'Eceabat', 'Ezine', 'Gelibolu', 'Gökçeada', 'Lapseki', 'Merkez', 'Yenice']}
'''

print(sehir.telefon(286))
'''
Telefon Kodu ile il Sorgusu

{'plaka': 17, 'il': 'Çanakkale', 'telefon': 286, 'buyuksehir_den_beri': None, 'bolge': 'Marmara', 'ilceler': ['Ayvacık', 'Bayramiç', 'Biga', 'Bozcaada', 'Çan', 'Eceabat', 'Ezine', 'Gelibolu', 'Gökçeada', 'Lapseki', 'Merkez', 'Yenice']}
'''

print(sehir.ilce('Lapseki'))
'''
İlçe ile il Sorgusu

{'plaka': 17, 'il': 'Çanakkale', 'telefon': 286, 'buyuksehir_den_beri': None, 'bolge': 'Marmara', 'ilceler': ['Ayvacık', 'Bayramiç', 'Biga', 'Bozcaada', 'Çan', 'Eceabat', 'Ezine', 'Gelibolu', 'Gökçeada', 'Lapseki', 'Merkez', 'Yenice']}
'''

##

print(sehir.gorsel(sehir.plaka(17)))
'''
json verisini insanın okuyabileceği formatta döndürür

{
  "plaka": 17,
  "il": "Çanakkale",
  "telefon": 286,
  "buyuksehir_den_beri": null,
  "bolge": "Marmara",
  "ilceler": [
    "Ayvacık",
    "Bayramiç",
    "Biga",
    "Bozcaada",
    "Çan",
    "Eceabat",
    "Ezine",
    "Gelibolu",
    "Gökçeada",
    "Lapseki",
    "Merkez",
    "Yenice"
  ]
}
'''

print(sehir.tablo(sehir.telefon(286)))
'''
Tabulate verisi döndürür

+-----------+
| ilceler   |
|-----------|
| Ayvacık   |
| Bayramiç  |
| Biga      |
| Bozcaada  |
| Çan       |
| Eceabat   |
| Ezine     |
| Gelibolu  |
| Gökçeada  |
| Lapseki   |
| Merkez    |
| Yenice    |
+-----------+
'''

print(sehir.anahtarlar(sehir.ilce('Lapseki')))
'''
Var olan anahtarları döndürür

['plaka', 'il', 'telefon', 'buyuksehir_den_beri', 'bolge', 'ilceler']
'''

print(sehir.nesne(sehir.ilce('Lapseki')))
'''
json verisini python nesnesine dönüştürür

AttrDict({'plaka': 17, 'il': 'Çanakkale', 'telefon': 286, 'buyuksehir_den_beri': None, 'bolge': 'Marmara', 'ilceler': ['Ayvacık', 'Bayramiç', 'Biga', 'Bozcaada', 'Çan', 'Eceabat', 'Ezine', 'Gelibolu', 'Gökçeada', 'Lapseki', 'Merkez', 'Yenice']})
'''
```

## 🌐 Telif Hakkı ve Lisans

* *Copyright (C) 2020 by* [keyiflerolsun](https://github.com/keyiflerolsun) ❤️️
* [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/keyiflerolsun/keyifUserBot/blob/master/LICENSE) *Koşullarına göre lisanslanmıştır..*

## ♻️ İletişim

*Benimle iletişime geçmek isterseniz, **Telegram**'dan mesaj göndermekten çekinmeyin;* [@keyiflerolsun](https://t.me/keyiflerolsun)

##

> **[@KekikAkademi](https://t.me/KekikAkademi)** *için yazılmıştır..*
