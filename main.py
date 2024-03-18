import funkcje as f
import numpy as np
import matplotlib.pyplot as plt

x = 1
a = 3
b = -4
iteracje = 8
epsilon = 0.1
wspolczynniki = [-2, 4, 4, 5]
wybrana_trygonometryczna = np.sin
rodzaj_funkcji = 1
przedzial_poczatek = 0
przedzial_koniec = 5

stopien = 1
zlozenie = 1
zwyniki = []
iloscf = 0

rodzaj_funkcji = 1

menu = int(input("""Czy chcesz odtworzyć gotowe funkcje, czy samemu podać wartości?
                 0 - Porównanie wybranych funkcji ze sprawozdania
                 1 - Nowe wartości
                 Cokolwiek innego - Crash i wyjście z programu
                 Wybór: """))

print()
if menu == 0:
    print()

    print(f"Porównanie metod iteracyjnie dla funkcji 3^x - 4 dla 100 max iteracji")

    print(f"Przedzial: 0-5")

    print(f.bisekcja_iteracyjnie(1, 0, 5, 53, a, b,
                                 wspolczynniki, stopien, wybrana_trygonometryczna))

    print(f.stycznie_iteracyjnie(1, 0, 5, 8, a, b,
                                 wspolczynniki, stopien, wybrana_trygonometryczna))

    rootb = f.bisekcja_iteracyjnie(1, przedzial_poczatek, przedzial_koniec, iteracje, a, b,
                                  wspolczynniki, stopien, wybrana_trygonometryczna)

    roots = f.stycznie_iteracyjnie(1, przedzial_poczatek, przedzial_koniec, iteracje, a, b,
                                   wspolczynniki, stopien, wybrana_trygonometryczna)
    print()


elif menu == 1:
    while zlozenie > 0:
        rodzaj_funkcji = -1  # Zresetowanie rodzaj_funkcji przed kolejną iteracją pętli

        while rodzaj_funkcji < 0 or rodzaj_funkcji >= 3:
            rodzaj_funkcji = int(input("""Wybierz funkcję:

            0 - Wielomianowa
            1 - Wykładnicza
            2 - Trygonometryczna

            Wybór: """))

        if rodzaj_funkcji == 0:  # Wielomianowa
            stopien = int(input("Podaj stopień wielomianu: "))
            while stopien < 1:
                stopien = int(input("Stopień wielomianu musi być większy od 0: "))

            wspolczynniki = []
            for index in range(stopien, -1, -1):
                wspolczynniki.append(int(input(f"Podaj współczynnik przy x^{index}: ")))

            print(f"Wartosc testowa, x gdzies u gory kodu")
            print(f.wielomian(x, wspolczynniki))
            print("Horner wielomian: ")
            print(f.wielomian_horner(x, wspolczynniki, stopien))
            print("forma pochodnej: ")
            print(np.polyder(np.poly1d(wspolczynniki)))
            print("wartosc pochodnej: ", f.pochodna_wielomianu(x, wspolczynniki))
            print(f.pochodna_funkcji(rodzaj_funkcji, x, a, wspolczynniki, wybrana_trygonometryczna))

        elif rodzaj_funkcji == 1:  # Wykładnicza
            a = int(input("Podaj współczynnik a: "))
            while a <= 0:
                a = int(input("Współczynnik a musi byc wiekszy od 0 by funkcja mogła byc ciagła, podaj a: "))

            b = int(input("Podaj współczynnik b (wyraz wolny): "))

            print(f"Wspolczynniki :", a, b)

            print(f"Wartosc testowa, x gdzies u gory kodu")
            print(f.wykladnicza(x, a, b))
            print("wartosc pochodnej wykladniczej: ")
            print(f.pochodna_wykladniczej(x, a))
            print(f.pochodna_funkcji(rodzaj_funkcji, x, a, wspolczynniki, wybrana_trygonometryczna))

        elif rodzaj_funkcji == 2:  # Trygonometryczna
            wybor_funkcji_trygonometrycznej = int(input("""Wybierz funkcję trygonometryczną:

            0 - sin(x)
            1 - cos(x)
            2 - tan(x)
            3 - ctg(x)
            4 - arctan(x)
            5 - arcsin(x)
            6 - arccos(x)
            7 - arcctg(x)

            Wybór: """))

            trygonometryczne = [np.sin, np.cos, np.tan, lambda x: 1 / np.tan(x), np.arctan, np.arcsin, np.arccos,
                                 lambda x: np.pi / 2 - np.arctan(x)]
            wybrana_trygonometryczna = trygonometryczne[wybor_funkcji_trygonometrycznej]

            a = int(input("Podaj współczynnik a: "))
            b = int(input("Podaj współczynnik b (wyraz wolny): "))
            print(a, b)
            # print(trygonometryczne[wybor_funkcji_trygonometrycznej])
            print(f"Wartosc testowa, x gdzies u gory kodu")
            print(f.trygonometryczna(x, wybrana_trygonometryczna, a, b))
            print("wartosc pochodnej trygonometrycznej: ")
            print(f.pochodna_trygonometrycznej(x, a, wybrana_trygonometryczna))
            print(f.pochodna_funkcji(rodzaj_funkcji, x, a, wspolczynniki, wybrana_trygonometryczna))

        print()
        # zlozenie = int(input("""Czy chcesz dodać złożenie funkcji?:
        #     0 - Nie
        #     1 - Dodawanie
        #     2 - Odejmowanie
        #     3 - Mnożenie
        #     4 - Dzielenie
        #     5 - Funkcja wewnętrzna
        #     6 - Funkcja zewnętrzna
        #
        #     Wybór: """))


        # print()
        # zlozenie = int(input("""Czy chcesz dodać złożenie funkcji?:
        #     0 - Nie
        #     1 - Dodaj funkcje zewnetrzna"""))
        #     # 2 - Odejmowanie
        #     # 3 - Mnożenie
        #     # 4 - Dzielenie
        #     # 5 - Funkcja wewnętrzna
        #     # 6 - Funkcja zewnętrzna
        #     #
        #     # Wybór: """))

        if zlozenie > 0:
            iloscf += 1
            print(a)
            print(b)

    print()
    print("wartość testowa funkcji poza pętlą, x u góry kodu: ",
          f.wartosc_funkcji(rodzaj_funkcji, x, a, b, wspolczynniki, stopien, wybrana_trygonometryczna))

    przedzial_wartosc = 1

    while przedzial_wartosc > 0:
        print()
        print("Podaj przedział, w którym funkcja ma różne znaki na końcach przedziałów")
        przedzial_poczatek = int(input("Podaj lewy koniec przedziału: "))
        przedzial_koniec = int(input("Podaj prawy koniec przedziału: "))

        # walidacja, czy wartości po przeciwnych stronach przedziału mają przeciwną wartość
        print(f.wartosc_funkcji(rodzaj_funkcji, przedzial_poczatek, a, b, wspolczynniki, stopien,
                                 wybrana_trygonometryczna))
        print(f.wartosc_funkcji(rodzaj_funkcji, przedzial_koniec, a, b, wspolczynniki, stopien,
                                 wybrana_trygonometryczna))
        przedzial_wartosc = f.wartosc_funkcji(rodzaj_funkcji, przedzial_poczatek, a, b, wspolczynniki, stopien,
                                               wybrana_trygonometryczna) * f.wartosc_funkcji(rodzaj_funkcji,
                                                                                                 przedzial_koniec,
                                                                                                 a, b,
                                                                                                 wspolczynniki,
                                                                                                 stopien,
                                                                                                 wybrana_trygonometryczna)

        print(f"walidacja, przedzial wartosc: ", przedzial_wartosc)

    metoda = int(input("""\nWybierz metodę

    0 - Metoda bisekcji iteracyjnie
    1 - Metoda bisekcji z użyciem epsilon
    2 - Metoda stycznych iteracyjnie
    3 - Metoda Stycznych z użyciem epsilon

    Wybór: """))

    if metoda % 2 == 0:
        iteracje = int(input("\nPodaj ilość iteracji: "))
    else:
        epsilon = float(input("\nPodaj wartość epsilon: "))

    if metoda == 0:
        print(f.bisekcja_iteracyjnie(rodzaj_funkcji, przedzial_poczatek, przedzial_koniec, iteracje, a, b,
                                      wspolczynniki, stopien, wybrana_trygonometryczna))
        root = f.bisekcja_iteracyjnie(rodzaj_funkcji, przedzial_poczatek, przedzial_koniec, iteracje, a, b,
                                       wspolczynniki, stopien, wybrana_trygonometryczna)
    elif metoda == 1:
        print(f.bisekcja_epsilon(rodzaj_funkcji, przedzial_poczatek, przedzial_koniec, epsilon, a, b, wspolczynniki,
                                  stopien, wybrana_trygonometryczna))
        root = f.bisekcja_epsilon(rodzaj_funkcji, przedzial_poczatek, przedzial_koniec, epsilon, a, b,
                                   wspolczynniki, stopien, wybrana_trygonometryczna)
    elif metoda == 2:
        print(f.stycznie_iteracyjnie(rodzaj_funkcji, przedzial_poczatek, przedzial_koniec, iteracje, a, b,
                                      wspolczynniki, stopien, wybrana_trygonometryczna))
        root = f.stycznie_iteracyjnie(rodzaj_funkcji, przedzial_poczatek, przedzial_koniec, iteracje, a, b,
                                       wspolczynniki, stopien, wybrana_trygonometryczna)
    elif metoda == 3:
        print(f.stycznie_epsilon(rodzaj_funkcji, przedzial_poczatek, przedzial_koniec, epsilon, a, b, wspolczynniki,
                                  stopien, wybrana_trygonometryczna))
        root = f.stycznie_epsilon(rodzaj_funkcji, przedzial_poczatek, przedzial_koniec, epsilon, a, b,
                                   wspolczynniki, stopien, wybrana_trygonometryczna)
    else:
        print("Błąd - wybierz jedną z opcji")
        raise SystemExit


    f.plot_function(rodzaj_funkcji, przedzial_poczatek, przedzial_koniec, a, b, wspolczynniki, stopien,
                    wybrana_trygonometryczna, root)
    f.plot_root(rodzaj_funkcji, przedzial_poczatek, przedzial_koniec, a, b, wspolczynniki, stopien,
                    wybrana_trygonometryczna, root)



else:
    print("Błąd - wybierz jedną z opcji")
    raise SystemExit
