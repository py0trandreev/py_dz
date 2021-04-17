from requests import get
from decimal import Decimal
from datetime import datetime


def currency_rates(currency_code):
    # get currency code dict from the site
    response = get("http://www.cbr.ru/scripts/XML_daily.asp")
    if response.status_code != 200:
        return None

    currency_dict = {}
    content = response.content.decode(encoding=response.encoding)
    date_of_values = 0;
    # print(content)

    currency_code_dirty = content.split("<CharCode>")
    for el in currency_code_dirty:
        if currency_code_dirty.index(el) == 0:
            # it's date to extract here
            date_of_el = el.split('<ValCurs Date="')[1].split('" ')[0]
            date_of_el = datetime.strptime(date_of_el, "%d.%m.%Y").strftime("%d.%m.%Y")
        else:
            currency_code_of_el = el[:3]
            currency_value_of_el = el.split("<Value>")[1].split("</Value>")[0]
            currency_value_of_el = Decimal(currency_value_of_el.replace(",", "."))
            currency_dict.setdefault(currency_code_of_el, currency_value_of_el)

    return "{0} - {2} руб. на {1}г.".format(currency_code.upper(), date_of_el, currency_dict.get(currency_code.upper()))


if __name__ == "__main__":
    print(currency_rates('usd'))
    print(currency_rates('EUR'))
