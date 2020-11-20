# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

YAZAR       = 'keyiflerolsun'
YAZAR_POSTA = 'keyiflerolsun@gmail.com'

PAKET       = 'TRSehirler'

VERSIYON    = '0.1.1'

REPO        = 'https://github.com/keyiflerolsun/TRSehirler'
ACIKLAMA    = 'Türkiye Cumhuriyeti Devleti Şehirlerini; İl, Plaka, Telefon veya İlçe bilgisinden bulun..'
ANAHTAR_KLM = [PAKET, 'KekikAkademi', 'keyiflerolsun']

with open(f'{PAKET}/requirements.txt') as dosya:
    GEREKSINIM = dosya.read().splitlines()

from TRSehirler.Sehirler import Sehir