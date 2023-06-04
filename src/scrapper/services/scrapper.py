import json
import requests

from bs4 import BeautifulSoup
from src.scrapper.sql import query
from src.scrapper.utils import parse_prices

class ScrapperService:
    
    def __init__(self, _opts: dict = {}):
        self._opts = {}
        self._opts.update(_opts)

    def _raise_if_not_valid(self, _opts: dict):

        if not _opts.get('connection'):
            raise Exception("Connection is required")

        if not _opts.get('options'):
            raise Exception("Options are required")

        if not _opts.get('url'):
            raise Exception("URL is required")

    def _scrape_dollar_price(self, compra_selector: str, venta_selector: str):

        url = self._opts.get('url')
        
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        buy_val = soup.select_one(compra_selector).text.strip()
        sell_val = soup.select_one(venta_selector).text.strip()
        
        return {
            "buy_price": buy_val,
            "sell_price": sell_val
        }

    def _build_price_dict(self, option):

        label = option.get('label')
        compra = option.get('compra_selector')
        venta = option.get('venta_selector')

        return {
            "label": label,
            "prices": self._scrape_dollar_price(compra, venta)
        }

    def _save_to_mysql(self, price_dict: dict):

        connection = self._opts.get('connection')

        label = price_dict.get('label')
        prices = price_dict.get('prices')
        buy_price = prices.get('buy_price')
        sell_price = prices.get('sell_price')

        parsed_buy_price, parsed_sell_price = parse_prices(buy_price, sell_price)

        prices = {
            "buy_price": parsed_buy_price,
            "sell_price": parsed_sell_price
        }

        values = (json.dumps(prices), label)

        try: 
            cursor = connection.cursor()
            cursor.execute(query, values)
            connection.commit()
        except Exception as e:  
            return {"message": "Error while saving data to db", "error": e}

    def _scrape_and_save_data(self):

        options = self._opts.get('options')

        for option_key, option_value in options.items():
            option = option_value
            price_dict = self._build_price_dict(option)
            self._save_to_mysql(price_dict)

    def update(self):

        self._raise_if_not_valid(self._opts)
        
        try:
            self._scrape_and_save_data()
            return {"message": "Data updated successfully"}
        except Exception as e:
            return {"message": "Error while updating data", "error": e}