import json

from src.dolar.sql import query
from src.dolar.utils import parse_date

class DolarService:
    
    def __init__(self, _opts: dict = {}):
        self._opts = {}
        self._opts.update(_opts)
    
    def _get_price_from_db(self, currency: str):
        label = self._opts.get('label')
        connection = self._opts.get('connection')

        try:
            cursor = connection.cursor()
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
            return {"message": message, "status": 400, "error": e }
        
    def get_dollar_price(self, currency: str):
        currency = currency.upper()
        price_data = self._get_price_from_db(currency)
        if price_data:
            return price_data
        else:
            return {"error": "Currency not found"}
