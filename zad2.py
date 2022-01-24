import sys

import funkcje as f

if __name__ == '__main__':
    try:
        f.pobierz(f.url_dzisiaj(), f.nazwa_dzisiaj())
        print("Czy chcesz wyświetlić pobrany plik?")
        x = input("Wprowadź odpowiednią literę: T - wyświetl, N - zakończ działanie programu: ")
        while (x != "N" and x != 'T'):
            x = input("Wprowadź odpowiednią literę: T - wyświetl, N - zakończ działanie programu: ")
            if  x == 'T':
                f.pokaz_zdjecie(f.nazwa_dzisiaj())
            else:
                print("Wpisz T lub N")
        if x == 'N':
            sys.exit(1)
    except (Exception) as err:
        print("Błąd: ", err)