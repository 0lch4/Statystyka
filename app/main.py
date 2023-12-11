from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Any
from app.calculator.calculator import rozklad_normalny

app = FastAPI()

templates = Jinja2Templates(directory="app/templatesx")

app.mount("/static", StaticFiles(directory="app/static"), name="static")


class RozkladNormalnyForm(BaseModel):
    wartosc: str
    mean: str
    sd: str


@app.get("/", response_class=HTMLResponse)
async def main_site(request: Request) -> Any:
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/submit", response_class=HTMLResponse)
async def submit_form(option: str = Form(...)) -> Any:
    print(f"Received option: {option}")
    if option == "rozklad_normalny":
        return RedirectResponse("/rozklad_normalny", status_code=303)
    return None


@app.get("/rozklad_normalny", response_class=HTMLResponse)
async def rozklad_normalny_template(request: Request) -> Any:
    return templates.TemplateResponse("rozklad_normalny.html", {"request": request})


@app.post("/rozklad_normalny", response_class=HTMLResponse)
async def rozklad_normalny_form(
    request: Request,
    wartosc: str = Form(...),
    mean: str = Form(...),
    sd: str = Form(...),
) -> Any:
    form_data = RozkladNormalnyForm(wartosc=wartosc, mean=mean, sd=sd)
    finall_data = rozklad_normalny(
        float(form_data.wartosc), float(form_data.mean), float(form_data.sd)
    )
    rozklad_ = f"Wynik dla rozkładu normalnego o danych {form_data} to :"
    context_data = {
        "request": request,
        "finall_data": finall_data,
        "rozklad_": rozklad_,
    }
    print("finall_data in rozklad_normalny_form:", finall_data)
    return templates.TemplateResponse("results.html", context_data)


@app.get("/results", response_class=HTMLResponse)
async def results(finall_data: dict[str, str], rozklad_:str) -> Any:
    print(rozklad_, finall_data)
    return rozklad_
