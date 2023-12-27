# Statystyka Kalkulator ![GitHub forks](https://img.shields.io/badge/Version-0.0.1-red)

Interface in Polish lang

# Opis
Prosta aplikacja webowa zbudowana na Fast Api

Rozwiązuje zadania z ostatnich ćwiczeń ze statystyki - idealne na kolosa.

## Licencja

Aplikacja działa na licencji MIT

# Instalacja

## Windows albo linux

## Kopiowanie repozytorium

```
git clone https://github.com/0lch4/Statystyka.git
```

## Instalowanie bibliotek

Wymagane jest `poetry`, należy wpisać w terminalu:

```
pip install poetry
```

Potem w głównej lokalizacji:

```
poetry install
```

A następnie:

```
poetry shell
```

# Użycie

Gdy wszystko gotowe, w głownej lokalizacji należy wpisać

```
uvicorn app.main:app --reload
```

Aplikacja działa na:

```
http://localhost:8000
```