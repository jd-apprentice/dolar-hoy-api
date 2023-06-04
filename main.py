from src.config import connection
from src.dolar.const import label
from src.dolar.services import DolarService
from src.scrapper.services import ScrapperService
from src.scrapper.auth import authenticate
from src.shared.constants import *
from fastapi import FastAPI, Depends

app = FastAPI()

Dolar = DolarService({
    "connection": connection,
    "label": label
})

Scrapper = ScrapperService({
    "options": options,
    "url": URL,
    "connection": connection
})

@app.get("/dolar/{currency}")
def get_dolar(currency: str):
    return Dolar.get_dollar_price(currency)

@app.post("/manual", dependencies=[Depends(authenticate)])
def manual_scrape():
    return Scrapper.update()