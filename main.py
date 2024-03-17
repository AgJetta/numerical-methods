import funkcje as f
import numpy as np
import matplotlib.pyplot as plt

x=1
a = 0
b = 0
wspolczynniki = 0

zlozenie = 1
zwyniki = []
iloscf = 0

while zlozenie > 0:

        rodzaj_funkcji = int(input("""Wybierz funkcję:
        
        0 - Wielomianowa
        1 - Wykładnicza
        2 - Trygonometryczna
        
        Wybór: """))


        if rodzaj_funkcji == 0: # Wielomianowa
            stopien = int(input("Podaj stopień wielomianu: "))
            while stopien < 1:
                stopien = int(input("Stopień wielomianu musi być większy od 0: "))

            wspolczynniki = []
            for index in range(stopien, -1, -1):
                wspolczynniki.append(float(input(f"Podaj współczynnik przy x^{index}: ")))

            print(f"Wartosc testowa, x gdzies u gory kodu")
            print(f.wielomian(x,wspolczynniki))


        elif rodzaj_funkcji == 1: # Wykładnicza
            a = float(input("Podaj współczynnik a: "))
            while a == 0:
                a = float(input("Współczynnik a nie może być równy 0: "))

            b = float(input("Podaj współczynnik b (wyraz wolny): "))

            print(f"Wspolczynniki :", a, b)

            print(f"Wartosc testowa, x gdzies u gory kodu")
            print(f.wykladnicza(x, a, b))


        elif rodzaj_funkcji == 2: # Trygonometryczna
            wybrana_trygonometryczna = int(input("""Wybierz funkcję trygonometryczną:
            
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

            wybrana_trygonometryczna = trygonometryczne[wybrana_trygonometryczna]

            print()
            a = float(input("Podaj współczynnik a: "))
            b = float(input("Podaj współczynnik b (wyraz wolny): "))
            print()

            print(f"Wspolczynniki :", a, b)
            print(f"Wybrana funkcja trygonometryczna: ", trygonometryczne[wybrana_trygonometryczna])

            print(f"Wartosc testowa, x gdzies u gory kodu")
            print(f.trygonometryczna(x, wybrana_trygonometryczna, a, b))


        else:
            print("Błąd - wybierz jedną z opcji")
            raise SystemExit

        print()
        zlozenie = int(input("""Czy chcesz dodac zlozenie funkcji?: 
            0 - Nie
            1 - Dodawanie
            2 - Odejmowanie
            3 - Mnozenie
            4 - Dzielenie
            5 - Funkcja wewnetrzna
            6 - Funkcja zewnetrzna
            
            Wybór: """))

        if zlozenie == 0:
            break
        else:
            iloscf += 1
            print(a)
            print(b)

print()
print("wartosc testowa funkcji poza petla, x u gory kodu: ", f.wartosc_funkcji(rodzaj_funkcji, x, a=a, b=b, wspolczynniki=wspolczynniki))

przedzial_wartosc = 1

while przedzial_wartosc > 0:
    print()
    print("Podaj przedzial, w ktorym funkcja ma rozne znaki na krancach przedzialow")
    przedzial_poczatek = int(input("Podaj lewy koniec przedziału przedziału: "))
    przedzial_koniec = int(input("Podaj prawy koniec przedziału: "))

    przedzial_wartosc = f.wartosc_funkcji(rodzaj_funkcji, przedzial_poczatek, a=a, b=b, wspolczynniki=wspolczynniki)* f.wartosc_funkcji(rodzaj_funkcji, przedzial_koniec, a=a, b=b, wspolczynniki=wspolczynniki)
    print(f"walidacja, przedzial wartosc: ", przedzial_wartosc)


metoda = int(input("""\nWybierz metodę

0 - Metoda bisekcji iteracyjnie
1 - Metoda bisekcji z użyciem epsilon
2 - Metoda stycznych iteracyjnie
3 - Metoda Stycznych z użyciem epsilon

Wybór: """))


if metoda%2==0:
    iteracje = int(input("\nPodaj ilość iteracji: "))
else:
    epsilon = float(input("\nPodaj wartosc epsilon: "))

if metoda==0:
    print(f.bisekcja_iteracyjnie(rodzaj_funkcji, przedzial_poczatek, przedzial_koniec, iteracje))
elif metoda==1:
    (f.bisekcja_epsilon(rodzaj_funkcji,przedzial_poczatek,przedzial_koniec,epsilon))
elif metoda==2:
    print(f.metoda_Newtona_iteracje(rodzaj_funkcji,przedzial_poczatek,przedzial_koniec,iteracje))
elif metoda==3:
    print(f.metoda_Newtona_epsilon(rodzaj_funkcji,przedzial_poczatek,przedzial_koniec,epsilon))
else:
    print("Błąd - wybierz jedną z opcji")
    raise SystemExit




# epsilon = None if metoda % 2 == 0 else float(input("Podaj epsilon w formacie ab.cdef:  "))
# iteracje = None if metoda % 2 == 1 else np.abs(int(input("Podaj ilość iteracji:  ")))
# przedzial = None if metoda > 1 else (float(input("Wybrano metodę bisekcji, podaj lewy kraniec przedziału:  ")), float(input("Podaj prawy kraniec przedziału:  ")))
# x0 = None if metoda < 2 else float(input("Wybrano metodę stycznych, podaj początkowy x:  "))

# t = time.time()
# rozw = f.metody[metoda](id_funkcji, iteracje=iteracje, epsilon=epsilon, przedzial=przedzial, x0=x0)
# print(time.time() - t)


# x = np.linspace(-10, 10, 10000)

# plt.plot(x, f.funkcje[id_funkcji](x), 'g')
# plt.plot(rozw, f.funkcje[id_funkcji](rozw), 'bo', lw=1)
# plt.grid()
# plt.show()


# a = float(input("Podaj lewą granicę przedziału: "))
# b = float(input("Podaj prawą granicę przedziału: "))

# print("Wybierz funkcję:")
# print("1. x^3 - 2x - 5")

# # Dodaj inne funkcje do wyboru

# choice = input()
# if choice == '1':
#     func = f
#     dfunc = df  # jeśli funkcja ma pochodną
# else:
#     print("Nieprawidłowy wybór.")
#     return

# print("Wybierz kryterium zatrzymania:")
# print("a) Spełnienie warunku nałożonego na dokładność")
# print("b) Osiągnięcie zadanej liczby iteracji")

# stop_criterion = input()
# if stop_criterion == 'a':
#     epsilon = float(input("Podaj wartość epsilon: "))

#     root_bisection = bisection_method(func, a, b, epsilon)
#     root_newton = newton_method(func, a, epsilon)

# elif stop_criterion == 'b':
#     max_iterations = int(input("Podaj maksymalną liczbę iteracji: "))

#     root_bisection = bisection_method(func, a, b, max_iterations)
#     root_newton = newton_method(func, a, max_iterations)

# else:
#     print("Nieprawidłowy wybór.")
#     return

# roots = [root_bisection, root_newton]
# print("Miejsce zerowe znalezione przez metodę bisekcji:", root_bisection)
# print("Miejsce zerowe znalezione przez metodę stycznych:", root_newton)
# plot_function(func, a, b, roots)