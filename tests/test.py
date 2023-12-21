import pytest
from fastapi.testclient import TestClient
from fastapi.responses import RedirectResponse
from app.main import app
from typing import Any

client = TestClient(app)


def test_main_site(client: Any = client) -> None:
    response = client.get("/")
    assert response.status_code == 200


def test_dropdown(client: Any = client) -> None:
    response = client.get("/")
    assert "rozklad_normalny" in str(response.content)
    assert "prawdopodobienstwo_przedzialu" in str(response.content)
    assert "prawdopodobienstwo_ze_wieksze" in str(response.content)
    assert "kwantyl_standardowy" in str(response.content)
    assert "kwantyl_rozkladu_normalnego" in str(response.content)
    assert "uczciwy_rzut_kostka" in str(response.content)


######################################################


def test_submit_rozklad_normalny(client: Any = client) -> None:
    response = client.post("/submit", data={"option": "rozklad_normalny"})
    assert response.status_code == 200
    assert RedirectResponse("/rozklad_normalny")


def test_submit_prawdopodobienstwo_przedzialu(client: Any = client) -> None:
    response = client.post("/submit", data={"option": "prawdopodobienstwo_ze_wieksze"})
    assert response.status_code == 200
    assert RedirectResponse("/prawdopodobienstwo_ze_wieksze")


def test_submit_prawdopodobienstwo_ze_wieksze(client: Any = client) -> None:
    response = client.post("/submit", data={"option": "prawdopodobienstwo_ze_wieksze"})
    assert response.status_code == 200
    assert RedirectResponse("/prawdopodobienstwo_ze_wieksze")


def test_submit_kwantyl_standardowy(client: Any = client) -> None:
    response = client.post("/submit", data={"option": "kwantyl_standardowy"})
    assert response.status_code == 200
    assert RedirectResponse("/kwantyl_standardowy")


def test_submit_kwantyl_rozkladu_normalnego(client: Any = client) -> None:
    response = client.post("/submit", data={"option": "kwantyl_rozkladu_normalnego"})
    assert response.status_code == 200
    assert RedirectResponse("/kwantyl_rozkladu_normalnego")

def test_submit_kwantyl_uczciwy_rzut_kostka(client: Any = client) -> None:
    response = client.post("/submit", data={"option": "uczciwy_rzut_kostka"})
    assert response.status_code == 200
    assert RedirectResponse("/uczciwy_rzut_kostka")


########################################################


def test_rozklad_normalny(client: Any = client) -> None:
    response = client.get("/rozklad_normalny")
    assert response.status_code == 200


def test_prawdopodobienstwo_przedzialu(client: Any = client) -> None:
    response = client.get("/prawdopodobienstwo_przedzialu")
    assert response.status_code == 200


def test_prawdopodobienstwo_ze_wieksze(client: Any = client) -> None:
    response = client.get("/prawdopodobienstwo_ze_wieksze")
    assert response.status_code == 200


def test_kwantyl_standardowy(client: Any = client) -> None:
    response = client.get("/kwantyl_standardowy")
    assert response.status_code == 200


def test_kwantyl_rozkladu_normalnego(client: Any = client) -> None:
    response = client.get("/kwantyl_rozkladu_normalnego")
    assert response.status_code == 200

def test_uczciwy_rzut_kostka(client: Any = client) -> None:
    response = client.get("/uczciwy_rzut_kostka")
    assert response.status_code == 200


#########################################################


def test_rozklad_normalny_form(client: Any = client) -> None:
    response = client.post(
        "/rozklad_normalny", data={"wartosc": "1", "mean": "2", "sd": "3"}
    )
    assert response.status_code == 200
    assert "0.36944134018176367" in str(response.content)
    assert RedirectResponse("/results")


def test_prawdopodobienstwo_przedzialu_form(client: Any = client) -> None:
    response = client.post(
        "/prawdopodobienstwo_przedzialu",
        data={"mean": "1", "sd": "2", "first": "3", "second": "4"},
    )
    assert response.status_code == 200
    assert "0.09184805266259899" in str(response.content)
    assert RedirectResponse("/results")


def test_prawdopodobienstwo_ze_wieksze_form(client: Any = client) -> None:
    response = client.post(
        "/prawdopodobienstwo_ze_wieksze", data={"number": "1", "mean": "2", "sd": "3"}
    )
    assert response.status_code == 200
    assert "0.6305586598182363" in str(response.content)
    assert RedirectResponse("/results")


def test_kwantyl_standardowy_form(client: Any = client) -> None:
    response = client.post("/kwantyl_standardowy", data={"quantile": "0.95"})
    assert response.status_code == 200
    assert "1.6448536269514722" in str(response.content)
    assert RedirectResponse("/results")


def test_kwantyl_rozkladu_normalnego_form(client: Any = client) -> None:
    response = client.post(
        "/kwantyl_rozkladu_normalnego",
        data={"mean": "2.2", "sd": "4.3", "probability": "0.3"},
    )
    assert response.status_code == 200
    assert "-0.05492220464457542" in str(response.content)
    assert RedirectResponse("/results")

def test_uczciwy_rzut_kostka_form(client: Any = client) -> None:
    response = client.post(
        "/uczciwy_rzut_kostka",
        data={"rng":"100"},
    )
    assert response.status_code == 200
    assert "reszka" in str(response.content)
    assert RedirectResponse("/results")
