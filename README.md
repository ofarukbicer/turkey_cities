# 🏙️ TRSehirler

![Repo Boyutu](https://img.shields.io/github/repo-size/omerfarukbicer0446/turkey_cities) ![Views](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/omerfarukbicer0446/turkey_cities&title=Profile%20Views)

*Türkiye Cumhuriyeti Devleti Şehirlerini; İl, Plaka, Telefon veya İlçe bilgisinden bulun..*

## 🚀 Kurulum

```bash
# Yüklemek
composer require omerfarukbicer0446/turkey_cities

# Güncellemek
composer update omerfarukbicer0446/turkey_cities
```

## 📝 Proje İlerlemesi

- [x] *Veritabanı itinayla* *~* **[keyiflerolsun/TRSehirler](https://github.com/keyiflerolsun/TRSehirler)***'den `dızz 🐍`'lanmıştır..*

## 📒 Kullanım

```php
require "vendor/autoload.php";

use TurkeyCities\Sehir;

$cities = new Sehir;

/* Büyük küçük harf duyarsızdır */

// İl ile il sorgusu
print_r($cities->il("istanbul"));

// İlçe ile il sorgusu
print_r($cities->ilce("esenyurt"));

// Plaka ile il sorgusu
print_r($cities->plaka("34"));

// Telefon kodu ile il sorgusu
print_r($cities->telefon("212"));

/* 
*stdClass Object
*(
*    [plaka] => 34
*    [il] => İstanbul
*    [telefon] => Array
*        (
*            [0] => 212
*            [1] => 216
*        )
*
*    [buyuksehir_den_beri] => 1984
*    [bolge] => Marmara
*    [ilceler] => Array
*        (
*            [0] => Adalar
*            [1] => Arnavutköy
*            [2] => Ataşehir
*            ...
*        )
*
*)
*/

// İllerin ilçelerine ait detaylı bilgiler
print_r($cities->ilceler_detay("istanbul"));

/* 
*stdClass Object
*(
*    [1] => stdClass Object
*        (
*            [Adalar] => stdClass Object
*                (
*                    [Burgazada] => stdClass Object
*                        (
*                            [posta_kodu] => 34975
*                            [mahalleler] => Array
*                                (
*                                    [0] => Burgazada Mah
*                                )
*
*                        )
*                )
*        )    
*   ....
*)  
*/
```

## 🌐 Telif Hakkı ve Lisans

* *Copyright (C) 2021 by* [omerfarukbicer0446](https://github.com/omerfarukbicer0446) ❤️️
* [MIT LICENSE](https://github.com/omerfarukbicer0446/turkey_cities/blob/master/LICENSE) *Koşullarına göre lisanslanmıştır..*

## ♻️ İletişim

*Benimle iletişime geçmek isterseniz, **Telegram**'dan mesaj göndermekten çekinmeyin;* [@omerfarukbicer](https://t.me/omerfarukbicer)


> **[www.cibza.com](https://www.cibza.com)** *için yazılmıştır..*