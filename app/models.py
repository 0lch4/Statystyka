from pydantic import BaseModel


class RozkladNormalny(BaseModel):
    wartosc: float
    mean: float
    sd: float


class PrawdopodobienstwoPrzedzialu(BaseModel):
    mean: float
    sd: float
    first: float
    second: float


class PrawdopodobienstwoZeWieksze(BaseModel):
    number: float
    mean: float
    sd: float


class KwantylStandardowy(BaseModel):
    quantile: float


class KwantylRozkladuNormalnego(BaseModel):
    mean: float
    sd: float
    probability: float


class UczciwyRzutKostka(BaseModel):
    rng: int


class NieUczciwyRzutKostka(BaseModel):
    rng: int
    fthrow1: float
    fthrow2: float


class AnalizaDanychZRozkladu(BaseModel):
    lenn: float
    mean: float
    sd: float
