# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from tinydb import TinyDB, Query
from tabulate import tabulate
from attrdict import AttrDict
import json, os

BURDAYIZ = os.path.dirname(os.path.abspath(__file__))

class Sehir(object):
    """
    Sehir : Plaka, Telefon ve İlçe ile şehir bilgileri..

    Methodlar
    ----------
        .il(il:str) -> dict:
        .plaka(plaka:int) -> dict:
        .telefon(telefon:int) -> dict:
        .ilce(ilce:str) -> dict:
        .gorsel(veri:dict) -> str:
        .tablo(veri:dict) -> str:
        .anahtarlar(veri:dict) -> list:
    """
    def __init__(self):
        "TinyDB Modelini Sorguya Hazırladık."
        self.db     = TinyDB(f'{BURDAYIZ}/Veriler/sehirler.json')
        self.sorgu  = Query()

    def il(self, il:str) -> dict:
        """
        İl ile il Sorgusu

        Argüman:
            il (str): 17

        Dönüş:
            dict: {'plaka': 17, 'il': 'Çanakkale', 'telefon': 286, 'buyuksehir_den_beri': None, 'bolge': 'Marmara', 'ilceler': ['Ayvacık', 'Bayramiç', 'Biga', 'Bozcaada', 'Çan', 'Eceabat', 'Ezine', 'Gelibolu', 'Gökçeada', 'Lapseki', 'Merkez', 'Yenice']}
        """
        try:
            sorgu = self.db.search(self.sorgu.il == il.capitalize())[0]
            return json.loads(json.dumps(sorgu, ensure_ascii=False))
        except IndexError:
            return {"Hata": f"'{il}' | diye bir il bulunamadı.."}

    def plaka(self, plaka:int) -> dict:
        """
        Plaka ile il Sorgusu

        Argüman:
            plaka (int): 17

        Dönüş:
            dict: {'plaka': 17, 'il': 'Çanakkale', 'telefon': 286, 'buyuksehir_den_beri': None, 'bolge': 'Marmara', 'ilceler': ['Ayvacık', 'Bayramiç', 'Biga', 'Bozcaada', 'Çan', 'Eceabat', 'Ezine', 'Gelibolu', 'Gökçeada', 'Lapseki', 'Merkez', 'Yenice']}
        """
        try:
            sorgu = self.db.search(self.sorgu.plaka == plaka)[0]
            return json.loads(json.dumps(sorgu, ensure_ascii=False))
        except IndexError:
            return {"Hata": f"'{plaka}' | diye bir plaka bulunamadı.."}

    def telefon(self, telefon:int) -> dict:
        """
        Telefon Kodu ile il Sorgusu

        Argüman:
            telefon (int): 286

        Dönüş:
            dict: {'plaka': 17, 'il': 'Çanakkale', 'telefon': 286, 'buyuksehir_den_beri': None, 'bolge': 'Marmara', 'ilceler': ['Ayvacık', 'Bayramiç', 'Biga', 'Bozcaada', 'Çan', 'Eceabat', 'Ezine', 'Gelibolu', 'Gökçeada', 'Lapseki', 'Merkez', 'Yenice']}
        """
        try:
            sorgu = self.db.search(self.sorgu.telefon == telefon)[0]
            return json.loads(json.dumps(sorgu, ensure_ascii=False))
        except IndexError:
            try:
                return self.db.search(self.sorgu.telefon.any(str(telefon)))[0]
            except IndexError:
                return {"Hata": f"'{telefon}' | diye bir telefon bulunamadı.."}

    def ilce(self, ilce:str) -> dict:
        """
        İlçe ile il Sorgusu

        Argüman:
            ilce (str): 'Lapseki'

        Dönüş:
            dict: {'plaka': 17, 'il': 'Çanakkale', 'telefon': 286, 'buyuksehir_den_beri': None, 'bolge': 'Marmara', 'ilceler': ['Ayvacık', 'Bayramiç', 'Biga', 'Bozcaada', 'Çan', 'Eceabat', 'Ezine', 'Gelibolu', 'Gökçeada', 'Lapseki', 'Merkez', 'Yenice']}
        """
        try:
            sorgu = self.db.search(self.sorgu.ilceler.any(ilce.capitalize()))[0]
            return json.loads(json.dumps(sorgu, ensure_ascii=False))
        except IndexError:
            return {"Hata": f"'{ilce}' | diye bir ilçe bulunamadı.."}

    @staticmethod
    def gorsel(veri, girinti:int=2, alfabetik:bool=False) -> str:
        """
        json verisini insanın okuyabileceği formatta döndürür

        Argüman:
            veri : sehir.plaka(17)
            girinti (int, optional): Varsayılan 2.
            alfabetik (bool, optional): Varsayılan False.

        Dönüş:
            str: {
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
        """
        return json.dumps(veri, indent=girinti, sort_keys=alfabetik, ensure_ascii=False)

    @staticmethod
    def tablo(veri, tablo_turu:str='psql') -> str:
        """
        Tabulate verisi döndürür

        Argüman:
            veri : sehir.plaka(17)
            tablo_turu (str, optional): Varsayılan 'psql'.

        Dönüş:
            str: +-----------+
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
        """
        try:
            return tabulate(zip(veri['ilceler']), headers=['ilceler'], tablefmt=tablo_turu)
        except KeyError:
            print(veri['Hata'])
            return tabulate(zip(veri['Hata'].split(' | ')), headers=['Hata'], tablefmt=tablo_turu)

    @staticmethod
    def anahtarlar(veri) -> list:
        """
        Var olan anahtarları döndürür

        Argüman:
            veri : sehir.plaka(17)

        Dönüş:
            list: ['plaka', 'il', 'telefon', 'buyuksehir_den_beri', 'bolge', 'ilceler']
        """
        return [anahtar for anahtar in veri.keys()]

    @staticmethod
    def nesne(veri) -> AttrDict:
        """
        json verisini python nesnesine dönüştürür

        Argüman:
            veri : sehir.plaka(17)

        Dönüş:
            AttrDict: AttrDict({'plaka': 17, 'il': 'Çanakkale', 'telefon': 286, 'buyuksehir_den_beri': None, 'bolge': 'Marmara', 'ilceler': ['Ayvacık', 'Bayramiç', 'Biga', 'Bozcaada', 'Çan', 'Eceabat', 'Ezine', 'Gelibolu', 'Gökçeada', 'Lapseki', 'Merkez', 'Yenice']})
        """
        return AttrDict(veri)