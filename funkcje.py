import numpy as np


def wielomian(x, arr):
    wynik = 0  # Inicjujemy zmienną wynik wartością 0
    for i in range(len(arr)):
        wynik += arr[i] * x ** (len(arr) - i - 1)  # Liczymy wartość wielomianu, uwzględniając kolejność współczynników
    return wynik
def wielomian_horner(x, wsp, st):
    wynik = wsp[0]
    for i in range(1, st + 1):
        wynik = wynik * x + wsp[i]

    return wynik


def pochodna_wielomianu(x, arr):
    poly = np.poly1d(arr)
    derivative_poly = np.polyder(poly)
    return derivative_poly(x)


# Funkcja wykładnicza
def wykladnicza(x, a, b):
    return a**x + b

def pochodna_wykladniczej(x, a):
    return (a**x) * np.log(a)


# Funkcja trygonometryczna
def trygonometryczna(x, funkcja, a, b):
    return a * funkcja(x) + b


# Pochodna funkcji trygonometrycznej
def pochodna_trygonometrycznej(x, a, funkcja):
    if funkcja == np.sin:
        return a * np.cos(x)
    elif funkcja == np.cos:
        return -a * np.sin(x)
    elif funkcja == np.tan:
        return a / np.cos(x)**2
    elif funkcja == (lambda x: 1 / np.tan(x)):
        return -a / np.sin(x)**2
    elif funkcja == np.arctan:
        return a / (1 + x**2)
    elif funkcja == np.arcsin:
        return a / np.sqrt(1 - x**2)
    elif funkcja == np.arccos:
        return -a / np.sqrt(1 - x**2)
    elif funkcja == (lambda x: np.pi / 2 - np.arctan(x)):
        return -a / (1 + x**2)

# def zlozona(x, a):
#     return 0


# Funkcja pochodnej
def pochodna_funkcji(rodzaj_funkcji, x, a=None, wspolczynniki=None, wybrana_trygonometryczna=None):
    if rodzaj_funkcji == 0:  # Wielomianowa
        return pochodna_wielomianu(x, wspolczynniki)
    elif rodzaj_funkcji == 1:  # Wykładnicza
        return pochodna_wykladniczej(x, a)
    elif rodzaj_funkcji == 2:  # Trygonometryczna
        return pochodna_trygonometrycznej(x, a, wybrana_trygonometryczna)
    else:
        raise ValueError("Nieprawidłowy rodzaj funkcji.")




def wartosc_funkcji(rodzaj_funkcji, x, a=None, b=None, wspolczynniki=None, stopien = None, wybrana_trygonometryczna=None):
    if rodzaj_funkcji == 0:  # Wielomianowa
        if wspolczynniki is None:
            raise ValueError("Brak współczynników dla funkcji wielomianowej.")
        return wielomian_horner(x,wspolczynniki, stopien)
    elif rodzaj_funkcji == 1:  # Wykładnicza
        if a is None or b is None:
            raise ValueError("Brak współczynników dla funkcji wykładniczej.")
        return wykladnicza(x, a, b)
    elif rodzaj_funkcji == 2:  # Trygonometryczna
        if a is None or b is None:
            raise ValueError("Brak współczynników dla funkcji trygonometrycznej.")
        elif wybrana_trygonometryczna is None:
            raise ValueError("Brak wybrania funkcji trygonometrycznej.")
        return trygonometryczna(x, wybrana_trygonometryczna, a, b)
    else:
        raise ValueError("Nieprawidłowy rodzaj funkcji.")


def bisekcja_iteracyjnie(rodzaj_funkcji, a, b, iteracje, parametr1=None, parametr2=None, wspolczynniki=None, stopien = None, wybrana_trygonometryczna = None):
    srodek = (a + b) / 2
    print("wartosc testowa funkcji poza petla, x u gory kodu: ",
          wartosc_funkcji(rodzaj_funkcji, srodek, parametr1, parametr2, wspolczynniki, stopien, wybrana_trygonometryczna))

    for i in range(iteracje):

        srodek = (a + b) / 2
        wartosc_srodka = wartosc_funkcji(rodzaj_funkcji, srodek, parametr1, parametr2, wspolczynniki, stopien,
                                         wybrana_trygonometryczna)
        wartosc_a = wartosc_funkcji(rodzaj_funkcji, a, parametr1, parametr2, wspolczynniki, stopien, wybrana_trygonometryczna)

        if wartosc_srodka == 0:
            print(f'Miejscem zerowym tej funkcji jest {srodek}, znaleziony po {i} iteracjach')
            return srodek

        if np.real(wartosc_a * wartosc_srodka) < 0:
            b = srodek
        else:
            a = srodek

    print(f'po {iteracje} iteracjach miejsce zerowe przyblizone zostało do {srodek}')
    return srodek

def bisekcja_epsilon(rodzaj_funkcji, a, b, epsilon, parametr1=None, parametr2=None, wspolczynniki=None, stopien = None, wybrana_trygonometryczna=None):
    if epsilon <= 0:
        raise ValueError("Epsilon powinien być większy od zera.")

    srodek = (a + b) / 2
    print("Wartość testowa funkcji poza pętlą, x u góry kodu: ",
          wartosc_funkcji(rodzaj_funkcji, srodek, parametr1, parametr2, wspolczynniki, stopien, wybrana_trygonometryczna))

    iteracje = 0

    while abs(b - a) > epsilon:
        srodek = (a + b) / 2
        wartosc_srodka = wartosc_funkcji(rodzaj_funkcji, srodek, parametr1, parametr2, wspolczynniki, stopien,
                                          wybrana_trygonometryczna)
        wartosc_a = wartosc_funkcji(rodzaj_funkcji, a, parametr1, parametr2, wspolczynniki, stopien, wybrana_trygonometryczna)

        if wartosc_srodka == 0:
            print(f'Miejscem zerowym tej funkcji jest {srodek}, znalezione po {iteracje} iteracjach')
            return srodek

        if np.real(wartosc_a * wartosc_srodka) < 0:
            b = srodek
        else:
            a = srodek

        iteracje += 1

    print(f'Po {iteracje} iteracjach miejsce zerowe zostało przybliżone do {srodek}')
    return srodek


def stycznie_iteracyjnie(rodzaj_funkcji, a, b, iteracje, parametr1=None, parametr2=None, wspolczynniki=None, stopien=None, wybrana_trygonometryczna=None):
    # Sprawdź, czy została podana prawidłowa liczba iteracji
    if iteracje <= 0:
        raise ValueError("Ilość iteracji musi być dodatnią liczbą.")

    # Warunki początkowe
    x = a

    # Pętla iteracyjna
    for i in range(iteracje):
        # Oblicz wartość funkcji i jej pochodnej w punkcie x
        f_x = wartosc_funkcji(rodzaj_funkcji, x, parametr1, parametr2, wspolczynniki, stopien, wybrana_trygonometryczna)
        f_prim_x = pochodna_funkcji(rodzaj_funkcji, x, parametr1, wspolczynniki, wybrana_trygonometryczna)

        # Oblicz następny przybliżony punkt zerowy
        x_nastepny = x - f_x / f_prim_x

        # Przygotuj się do następnej iteracji
        x = x_nastepny

    print(f'po {iteracje} iteracjach miejsce zerowe przyblizone zostało do {x_nastepny}')

    return x_nastepny

def stycznie_epsilon(rodzaj_funkcji, a, b, epsilon, parametr1=None, parametr2=None, wspolczynniki=None, stopien=None, wybrana_trygonometryczna=None):
    if epsilon <= 0:
        raise ValueError("Epsilon powinien być większy od zera.")

    # Warunki początkowe
    iteracja = 0
    x = a

    # Pętla iteracyjna
    while abs(b - a) > epsilon and iteracja < 1000:  # Zabezpieczenie przed nieskończoną pętlą
        # Oblicz wartość funkcji i jej pochodnej w punkcie x
        f_x = wartosc_funkcji(rodzaj_funkcji, x, parametr1, parametr2, wspolczynniki, stopien, wybrana_trygonometryczna)
        f_prim_x = pochodna_funkcji(rodzaj_funkcji, x, parametr1, wspolczynniki, wybrana_trygonometryczna)

        # Oblicz następny przybliżony punkt zerowy
        x_nastepny = x - f_x / f_prim_x

        # Przygotuj się do następnej iteracji
        x = x_nastepny
        iteracja += 1

    if iteracja == 1000:
        print("Nie udało się osiągnąć wymaganego przybliżenia po 1000 iteracjach. To jest zabezpieczenie przed nieskończoną pętlą.")

    print(f'Po {iteracja} iteracjach miejsce zerowe zostało przybliżone do {x_nastepny}')
    return x_nastepny


# def plot_function(f, a, b, roots=None):
#     x = np.linspace(a, b, 400)
#     y = f(x)
#     plt.plot(x, y, label='f(x)')
#     plt.xlabel('x')
#     plt.ylabel('f(x)')
#     plt.grid(True)
#     if roots:
#         plt.scatter(roots, [0] * len(roots), color='red', label='Roots')
#     plt.legend()
#     plt.show()