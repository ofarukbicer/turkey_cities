# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

def degistir(yazi, sozluk):
    for anahtar, deger in sozluk.items():
        yazi = yazi.replace(anahtar, deger)
    return yazi

def yaml2json():
    import yaml, json, os

    if not os.path.isdir('GeciciVeri/ilceler/'):
        os.makedirs('GeciciVeri/ilceler/')

    sehirler_degistir = {
        "plate_number" : "plaka",
        "name"         : "il",
        "phone_code"   : "telefon",
        "metropolitan_municipality_since"   : "buyuksehir_den_beri",
        "region"       : "bolge",
        "districts"    : "ilceler"
    }
    with open('DIZVeri/cities.yaml', 'r+') as okunan_sehirler:
        duzenlenen_veri = degistir(okunan_sehirler.read(), sehirler_degistir)
        json_veri       = yaml.load(duzenlenen_veri, Loader=yaml.FullLoader)

    with open('GeciciVeri/sehirler.json', 'w+') as yazilacak_sehirler:
        yazilacak_sehirler.write(json.dumps(json_veri, sort_keys=False, indent=2, ensure_ascii=False))


    ilceler_degistir = {
        "postcode"      : "posta_kodu",
        "neighborhoods" : "mahalleler"
    }
    for dosya in os.listdir("DIZVeri/districts/"):
        with open(f'DIZVeri/districts/{dosya}', 'r+') as okunan_ilceler:
            duzenlenen_veri = degistir(okunan_ilceler.read(), ilceler_degistir)
            json_veri       = yaml.load(duzenlenen_veri, Loader=yaml.FullLoader)

        uzanti_degis = dosya.replace('yaml', 'json')
        with open(f'GeciciVeri/ilceler/{uzanti_degis}', 'w+') as yazilacak_ilceler:
            yazilacak_ilceler.write(json.dumps(json_veri, sort_keys=False, indent=2, ensure_ascii=False))

def json2db():
    import os, json, tinydb

    if not os.path.isdir('KullanilacakVeri/ilceler/'):
        os.makedirs('KullanilacakVeri/ilceler/')

    # create a new storage for the database
    iller_db = tinydb.TinyDB("KullanilacakVeri/sehirler.json", ensure_ascii=False, indent=2)

    with open("GeciciVeri/sehirler.json", "r") as okunan_sehirler_verisi:
        # parse its JSON
        sehirler_json_verisi = json.load(okunan_sehirler_verisi)

    # iterate over each entry in the `tag.tg`
    for girdi in sehirler_json_verisi:
        # insert it in the DB
        iller_db.insert(girdi)

    for dosya in os.listdir("GeciciVeri/ilceler/"):
        ilce_db = tinydb.TinyDB(f"KullanilacakVeri/ilceler/{dosya}", ensure_ascii=False, indent=2)

        with open(f"GeciciVeri/ilceler/{dosya}", "r") as okunan_ilce_verisi:
            ilce_json_verisi = json.load(okunan_ilce_verisi)
            ilce_db.insert(ilce_json_verisi)

    import shutil
    shutil.rmtree('GeciciVeri/')
    shutil.move('KullanilacakVeri', '../')

if __name__ == '__main__':
    yaml2json()
    json2db()