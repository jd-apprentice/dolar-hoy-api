def parse_prices(buy_price, sell_price):
    parsed_buy_price = buy_price.replace("$", "")
    parsed_sell_price = sell_price.replace("$", "")

    if "." in parsed_buy_price:
        parsed_buy_price = parsed_buy_price[:parsed_buy_price.index(".")]

    if "." in parsed_sell_price:
        parsed_sell_price = parsed_sell_price[:parsed_sell_price.index(".")]

    return int(parsed_buy_price), int(parsed_sell_price)