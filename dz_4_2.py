from requests import get
from decimal import Decimal


def currency_rates(currency_code):
    # get currency code dict from the site
    response = get("http://www.cbr.ru/scripts/XML_daily.asp")
    if response.status_code != 200:
        return None

    currency_dict = {}
    content = response.content.decode(encoding=response.encoding)

    for el in content.split("<CharCode>")[1:]:
        currency_code_of_el = el[:3]
        currency_value_of_el = el.split("<Value>")[1].split("</Value>")[0]
        currency_value_of_el = Decimal(currency_value_of_el.replace(",", "."))
        currency_dict.setdefault(currency_code_of_el, currency_value_of_el)

    return currency_dict.get(currency_code.upper())


print(currency_rates('usd'))
print(currency_rates('EUR'))
print(currency_rates('tugric'))
