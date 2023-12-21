from pydantic import BaseModel


class RozkladNormalnyForm(BaseModel):
    wartosc: str
    mean: str
    sd: str


class PrawdopodobienstwoPrzedzialu(BaseModel):
    mean: str
    sd: str
    first: str
    second: str


class PrawdopodobienstwoZeWieksze(BaseModel):
    number: str
    mean: str
    sd: str


class KwantylStandardowy(BaseModel):
    quantile: str


class KwantylRozkladuNormalnego(BaseModel):
    mean: str
    sd: str
    probability: str

class UczciwyRzutKostka(BaseModel):
    rng: str

class NieUczciwyRzutKostka(BaseModel):
    rng:str
    fthrow1:str
    fthrow2:str
