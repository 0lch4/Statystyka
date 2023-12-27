from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
from typing import Any


def rozklad_normalny(
    value: float, mean: float, sd: float
) -> np.ndarray[float, np.dtype[float]]:
    return norm.cdf(value, loc=mean, scale=sd)


def prawdopodobienstwo_przedzialu(
    mean: float, sd: float, first: float, second: float
) -> np.ndarray[float]:
    return norm.cdf(second, loc=mean, scale=sd) - norm.cdf(first, loc=mean, scale=sd)


def prawdopodobienstwo_ze_wieksze(
    number: float, mean: float, sd: float
) -> np.ndarray[np.signedinteger[float]]:
    return 1 - norm.cdf(number, loc=mean, scale=sd)


def kwantyl_standardowy(quantile: float) -> np.ndarray[float, np.dtype[float]]:
    return norm.ppf(quantile)


def kwantyl_rozkladu_normalnego(
    mean: float, sd: float, probability: float
) -> np.ndarray[float, np.dtype[float]]:
    return norm.ppf(probability, loc=mean, scale=sd)


def uczciwy_rzut_kostka(rng: int) -> np.ndarray[str, str]:
    return np.random.choice(["orzel", "reszka"], size=rng)


def nie_uczciwy_rzut_kostka(
    rng: int, fthrow1: float, fthrow2: float
) -> np.ndarray[str, str]:
    return np.random.choice(["orzel", "reszka"], size=rng, p=[fthrow1, fthrow2])


def analiza_danych_z_rozkladu(lenn: int, mean: float, sd: float) -> list[Any]:
    data = np.random.normal(mean, sd, lenn)
    plt.figure(figsize=(8, 6))
    finall_data = []
    finall_data.append(
        plt.boxplot([data], labels=[f"Dane dla sd: {sd}, mean: {mean}, lenn: {lenn}"])
    )
    plt.title("Boxplot danych")
    plt.show()
    plt.figure(figsize=(8, 6))
    finall_data.append(
        plt.hist(
            data,
            bins=20,
            alpha=0.7,
            label=f"Dane dla sd: {sd}, mean: {mean}, lenn: {lenn}",
        )
    )
    plt.title("Histogram danych")
    plt.legend()
    plt.show()
    plt.close()
    return finall_data
