from ..data import currency_data
from ...custom_exception import CustomException


def get_symbols_by_name(currency_name):
    """Get currency symbols by currency name.

    Args:
        currency_name (str): The name of the currency.

    Returns:
        list: A list of unique currency symbols associated with the given currency name.
    """
    symbols = []
    for symbol, currency_list in currency_data.items():
        for name, _ in currency_list:
            if name == currency_name and symbol not in symbols:
                symbols.append(symbol)
    return symbols


def get_names_by_symbol(currency_symbol):
    """Get currency names by currency symbol.

    Args:
        currency_symbol (str): The symbol of the currency.

    Returns:
        list: A list of unique currency names associated with the given currency symbol.
    """
    names = []
    for symbol, currency_list in currency_data.items():
        if symbol == currency_symbol:
            for name, _ in currency_list:
                if name not in names:
                    names.append(name)
    return names


def get_codes_by_symbol(currency_symbol):
    """Get currency codes by currency symbol.

    Args:
        currency_symbol (str): The symbol of the currency.

    Returns:
        list: A list of currency codes associated with the given currency symbol (without duplicates and preserving order).
    """
    codes = []
    for symbol, currency_list in currency_data.items():
        if symbol == currency_symbol:
            for _, code in currency_list:
                if code not in codes:
                    codes.append(code)
    return codes


def get_info_by_symbol(currency_symbol):
    """Get currency information by currency symbol.

    Args:
        currency_symbol (str): The symbol of the currency.

    Returns:
        list: A list of currency records associated with the given currency symbol.
              Each record contains the currency name and currency code (without duplicates and preserving order).
    """
    info = []
    for symbol, currency_list in currency_data.items():
        if symbol == currency_symbol:
            for name, code in currency_list:
                record = (name, code)
                if record not in info:
                    info.append(record)
    return info
