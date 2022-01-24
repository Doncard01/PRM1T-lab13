import funkcje, sys

if __name__ == '__main__':
    try:
        funkcja.pobierz('https://www.pw.edu.pl/design/pw2021/images/logo-pw.png', 'logo.png')
        funkcja.pobierz('http://atlas2022.uw.edu.pl/wp-content/uploads/sites/416/nggallery/mapy/wiedzmin.png',
                         'wiedzmin.png')
        funkcja.pobierz('http://api.open-notify.org/astros.json', 'dane.json')
        funkcja.pobierz('https://studia.elka.pw.edu.pl/', 'strona.html')
    except (Exception) as err:
        print("Błąd: ", err)