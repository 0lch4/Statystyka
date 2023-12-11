from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


def rozklad_normalny(value, mean, sd):
    cdf_value = norm.cdf(value, loc=mean, scale=sd)
    return cdf_value


def prawdopodobienstwo_przedzialu():
    mean = int(input("podaj srednia μ: "))
    sd = int(input("podaj odchylenie σ: "))
    first = int(input("podaj poczatek przedzialu: "))
    second = int(input("podaj koniec przedzialu: "))

    result = norm.cdf(second, loc=mean, scale=sd) - norm.cdf(first, loc=mean, scale=sd)
    print(result)


def prawdopodobienstwo_ze_wieksze():
    liczba = int(input("podaj liczbe dla ktorej sprawdzany jest warunek: "))
    mean = int(input("podaj srednia dla x: "))
    sd = int(input("podaj odchylenie dla x: "))
    kwantyl = float(input("podaj wartosc kwantyla: "))

    probability = 1 - norm.cdf(liczba, loc=mean, scale=sd)
    print(f"Prawdopodobieństwo, że X > 9: {probability}")

    quantile = norm.ppf(kwantyl, loc=mean, scale=sd)
    print(f"Kwantyl dla progu {kwantyl}: {quantile}")


def kwantyl_rozkladu_normalnego():
    mean = int(input("podaj srednia dla x: "))
    sd = int(input("podaj odchylenie dla x: "))
    probability = float(input("podaj prawdopodobienstwo: "))
    quantile = norm.ppf(probability, loc=mean, scale=sd)
    print(f"Kwantyl: {quantile}")


def uczciwy_rzut_kostka():
    rng = int(input("Podaj ilość uczciwych rzutów które chcesz wykonać: "))
    results_fair = np.random.choice(["orzeł", "reszka"], size=rng)
    print(results_fair)


def nieuczciwy_rzut_kostka():
    rng = int(input("Podaj ilość uczciwych rzutów które chcesz wykonać: "))
    ftrow1 = float(
        input("Podaj prawdopodobienstwo dla orla (suma z reszka musi wynosic 1): ")
    )
    ftrow2 = float(
        input("Podaj prawdopodobienstwo dla reszki (suma z orlem musi wynosic 1): ")
    )
    results = np.random.choice(["orzeł", "reszka"], size=rng, p=[ftrow1, ftrow2])
    print(results)


def analiza_danych_z_rozkladu():
    data = []
    mean = []
    sd = []
    rng = int(input("podaj ile zestawow danych chcesz przeanalizowac: "))
    lenn = int(input("podaj ile wartosci ma byc w zestawie: "))
    basic_rng = rng
    while rng > 0:
        mean.append(int(input(f"podaj srednia dla zestawu {basic_rng-rng+1}: ")))
        sd.append(int(input(f"podaj odchylenie dla zestawu {basic_rng-rng+1}: ")))
        rng -= 1
    for s, m in zip(sd, mean):
        data.append(np.random.normal(m, s, lenn))
    for e, dat in enumerate(data):
        plt.figure(figsize=(8, 6))
        plt.boxplot([dat], labels=[f"Dane {e+1}"])
        plt.title("Boxplot danych")
        plt.show()
        plt.figure(figsize=(8, 6))
        plt.hist(dat, bins=20, alpha=0.7, label=f"Dane {e+1}")
        plt.title("Histogram danych")
        plt.legend()
        plt.savefig(f"histogram_{len(data)-e}.png")
        plt.show()
        plt.close()


def main():
    while True:
        print("Nie chce mi sie liczyc statystyki to zrobilem takie cos xD")
        inp = input(
            """Podaj co chcesz policzyc: \n
            rozklad normlany: 1\n
            prawdopodobienstwo przedzialu: 2\n
            prawdopodobienstwo ze x jest wieksze: 3\n
            kwantyl rozkladu normalnego: 4\n
            uczciwy rzut kostką: 5\n
            nieuczciwy rzut kostką: 6\n
            analiza danych z rozkładu: 7\n
            zamknij program: 0\n"""
        )
        if inp == "1":
            rozklad_normalny()
            input("nacisnij enter aby kontynuowac")
        if inp == "2":
            prawdopodobienstwo_przedzialu()
            input("nacisnij enter aby kontynuowac")
        if inp == "3":
            prawdopodobienstwo_ze_wieksze()
            input("nacisnij enter aby kontynuowac")
        if inp == "4":
            kwantyl_rozkladu_normalnego()
            input("nacisnij enter aby kontynuowac")
        if inp == "5":
            uczciwy_rzut_kostka()
            input("nacisnij enter aby kontynuowac")
        if inp == "6":
            nieuczciwy_rzut_kostka()
            input("nacisnij enter aby kontynuowac")
        if inp == "7":
            analiza_danych_z_rozkladu()
            input("nacisnij enter aby kontynuowac")
        if inp == "0":
            break


if __name__ == "__main__":
    main()
