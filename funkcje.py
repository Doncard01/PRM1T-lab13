import requests, datetime
import matplotlib.pyplot as plt

def pobierz(url, nazwa):
    response = requests.get(url)
    if response:
        with open(nazwa, 'wb') as file:
            file.write(response.content)
        print('Pobrano plik poprawnie')
        return True
    else:
        return False
def url_dzisiaj():
    x = str(datetime.datetime.now())
    dzien = x[2] + x[3] + x[5] + x[6] + x[8] + x[9]
    url = "https://apod.nasa.gov/apod/ap" + dzien + ".html"
    return url
def data_godzina():
    x = str(datetime.datetime.now())
    dzisiaj = x[0:4] + x[5] + x[6] + x[8] + x[9] +x[11:13] + x[14:16]
    return dzisiaj

def nazwa_dzisiaj():
    nazwa = "RigelWitchHead_Mtanous_" + data_godzina() + '.jpg'
    return nazwa
def pokaz_zdjecie(sciezka):
    img = plt.imread(sciezka)
    plt.imshow(img)
    plt.axis('off')