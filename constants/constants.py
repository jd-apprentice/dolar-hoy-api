URL = "https://dolarhoy.com/"

options = {
    'BLUE': {
        'label': 'Dolar Blue',
        'compra_selector': '.is-5 > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)',
        'venta_selector': '.is-5 > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)'
    },
    'CRYPTO': {
        'label': 'Dolar Crypto',
        'compra_selector': 'div.is-7:nth-child(2) > div:nth-child(5) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)',
        'venta_selector': 'div.is-7:nth-child(2) > div:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)'
    },
    'OFICIAL': {
        'label': 'Dolar Oficial',
        'compra_selector': 'div.is-7:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)',
        'venta_selector': 'div.is-7:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)'
    },
    'MEP': {
        'label': 'Dolar MEP',
        'compra_selector': 'div.is-7:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)',
        'venta_selector': 'div.is-7:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)'
    }
}