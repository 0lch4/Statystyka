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
    assert "nie_uczciwy_rzut_kostka" in str(response.content)
    assert "analiza_rozkladu" in str(response.content)


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


def test_submit_kwantyl_nie_uczciwy_rzut_kostka(client: Any = client) -> None:
    response = client.post("/submit", data={"option": "nie_uczciwy_rzut_kostka"})
    assert response.status_code == 200
    assert RedirectResponse("/nie_uczciwy_rzut_kostka")


def test_submit_analiza_rozkladu(client: Any = client) -> None:
    response = client.post("/submit", data={"option": "analiza_rozkaladu"})
    assert response.status_code == 200
    assert RedirectResponse("/analiza_rozkaladu")


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


def test_nie_uczciwy_rzut_kostka(client: Any = client) -> None:
    response = client.get("/nie_uczciwy_rzut_kostka")
    assert response.status_code == 200


def test_analiza_rozkladu(client: Any = client) -> None:
    response = client.get("/analiza_rozkladu")
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
        data={"rng": "100"},
    )
    assert response.status_code == 200
    assert True
    assert RedirectResponse("/results")


def test_nie_uczciwy_rzut_kostka_form_reszka(client: Any = client) -> None:
    response = client.post(
        "/nie_uczciwy_rzut_kostka",
        data={"rng": "100", "fthrow1": "0", "fthrow2": "1"},
    )
    assert response.status_code == 200
    assert "reszka" in str(response.content)
    assert "orzel" not in str(response.content)
    assert RedirectResponse("/results")


def test_nie_uczciwy_rzut_kostka_form_orzel(client: Any = client) -> None:
    response = client.post(
        "/nie_uczciwy_rzut_kostka",
        data={"rng": "100", "fthrow1": "1", "fthrow2": "0"},
    )
    assert response.status_code == 200
    assert "orzel" in str(response.content)
    assert "reszka" not in str(response.content)
    assert RedirectResponse("/results")


def test_analiza_rozkladu_form(client: Any = client) -> None:
    response = client.post(
        "/analiza_rozkladu",
        data={"lenn": "5", "mean": "5", "sd": "5"},
    )
    assert response.status_code == 200
    assert """[{'whiskers': [<matplotlib.lines.Line2D object at 0x0000026C38498A90>,
        <matplotlib.lines.Line2D object at 0x0000026C384AB010>], 'caps':
        [<matplotlib.lines.Line2D object at 0x0000026C384ABC10>,
        <matplotlib.lines.Line2D object at 0x0000026C384B4910>], 'boxes':
        [<matplotlib.lines.Line2D object at 0x0000026C384A99D0>], 'medians':
        [<matplotlib.lines.Line2D object at 0x0000026C384B5410>], 'fliers':
        [<matplotlib.lines.Line2D object at 0x0000026C384B5F10>], 'means':
        []}, (array([1., 0., 0., 0., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 2.]), array([1.01356498, 1.46262406, 1.91168314, 2.36074223,
        2.80980131, 3.25886039, 3.70791947, 4.15697856, 4.60603764, 5.05509672,
        5.5041558 , 5.95321489, 6.40227397, 6.85133305, 7.30039213, 7.74945122,
        8.1985103 , 8.64756938, 9.09662846, 9.54568755, 9.99474663]), <BarContainer
        object of 20 artists>)]""" not in str(
        response.content
    )
    assert RedirectResponse("/results")
