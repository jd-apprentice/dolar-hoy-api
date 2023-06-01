import requests
import json

from config import connection
from auth import authenticate
from constants import *
from utils import *
from bs4 import BeautifulSoup
from fastapi import FastAPI, Depends

app = FastAPI()

def scrape_dollar_price(compra_selector: str, venta_selector: str):
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    buy_val = soup.select_one(compra_selector).text.strip()
    sell_val = soup.select_one(venta_selector).text.strip()
    return {
        "buy_price": buy_val,
        "sell_price": sell_val
    }

def build_price_dict(option: dict):
    return {
        "label": option['label'],
        "prices": scrape_dollar_price(option['compra_selector'], option['venta_selector'])
    }

def save_to_mysql(price_dict: dict):

    label = price_dict['label']
    prices = price_dict['prices']

    parsed_buy_price, parsed_sell_price = parse_prices(prices['buy_price'], prices['sell_price'])

    prices = {
        "buy_price": parsed_buy_price,
        "sell_price": parsed_sell_price
    }

    values = (json.dumps(prices), label)
    try: 
        cursor = connection.cursor()
        query = """
                UPDATE prices
                SET prices = %s, updated_at = CURRENT_TIMESTAMP
                WHERE label = %s
            """
        cursor.execute(query, values)
        connection.commit()
    except Exception as e:  
        return {"message": "Error while saving data to db", "error": e}

def scrape_and_save_data():
    for option in options.items():
        price_dict = build_price_dict(option)
        save_to_mysql(price_dict)

def get_price_from_db(currency: str):

    try:
        label = {
            "BLUE": options['BLUE']['label'],
            "CRYPTO": options['CRYPTO']['label'],
            "OFICIAL": options['OFICIAL']['label'],
            "MEP": options['MEP']['label']
        }

        cursor = connection.cursor()
        query = "SELECT label, prices, updated_at FROM prices WHERE label = %s"
        cursor.execute(query, (label[currency],))
        result = cursor.fetchone()
        if result:
            label, prices, updated_at = result
            last_update = parse_date(updated_at)
            return {
                "label": label,
                "prices": json.loads(prices),
                "last_update": last_update
            }
        else:
            return None
    except Exception as e:
        message = f'Error while getting {currency} price from db'
        return { "message": message, "status": 400 }

@app.get("/dolar/{currency}")
def get_dollar_price(currency: str):
    currency = currency.upper()
    price_data = get_price_from_db(currency)
    if price_data:
        return price_data
    else:
        return {"error": "Currency not found"}

@app.post("/manual", dependencies=[Depends(authenticate)])
def update():
    try:
        scrape_and_save_data()
        return {"message": "Data updated successfully"}
    except Exception as e:
        return {"error": "Error while updating data"}