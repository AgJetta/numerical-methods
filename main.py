import funkcje as f
import numpy as np
import matplotlib.pyplot as plt


rodzaj_funkcji = int(input("""\nWybierz funkcję:
0 - Wielomianowa
1 - Wykładnicza
2 - Trygonometryczna
3 - Złożona

Wybór: """))

metoda = int(input("""\nWybierz metodę
0 - Metoda bisekcji iteracyjnie
1 - Metoda bisekcji z użyciem epsilon
2 - Metoda stycznych iteracyjnie
3 - Metoda Stycznych z użyciem epsilon

Wybór: """))


if rodzaj_funkcji == 0: # Wielomianowa
    stopien = int(input("Podaj stopień wielomianu: "))

    while stopien < 1:
        stopien = int(input("Stopień wielomianu musi być większy od 0: "))

    index_wspolczynnika = stopien;
    wspolczynniki = []

    while index_wspolczynnika >= 0:
        wspolczynniki.append(float(input(f"Podaj współczynnik przy x^{index_wspolczynnika}:  ")))
        index_wspolczynnika -= 1;

    # print(wspolczynniki)
    # print(f.wielomian(wspolczynniki, 0))


elif rodzaj_funkcji == 1: # Wykładnicza
    a = float(input("Podaj współczynnik a: "))

    while a == 0:
        a = float(input("Współczynnik a nie może być równy 0: "))

    b = float(input("Podaj współczynnik b (wyraz wolny): "))

    # print(f.wykladnicza(0, a, b))

elif rodzaj_funkcji == 2: # Trygonometryczna
    metoda = int(input("""\nWybierz funkcje trygonometryczną:
0 - sin(x)
1 - cos(x)
2 - tan(x)

Wybór: """))

    trygonometryczne = [np.sin, np.cos, np.tan]
    wybrana_funkcja = trygonometryczne[metoda]

    a = float(input("Podaj współczynnik a: "))
    b = float(input("Podaj współczynnik b (wyraz wolny): "))

    print(f.trygonometryczna(0, wybrana_funkcja, a, b))


elif rodzaj_funkcji == 3:
    #TODO: Dorobić funkcję złożoną
    pass

else:
    print("Błąd - wybierz jedną z opcji\n")
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