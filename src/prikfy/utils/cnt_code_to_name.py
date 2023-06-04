from data import sym_cnt_dict


def sym_to_name(symbol: str) -> str:

    """
    syn_to_name (convert contry code to country fullname)
    Returns country full name based on a symbol given as an argument.
    The symbol argument is case-insensitive
    If given symbol is not included in the dictionary,
    returns None. The function uses sym_cnt_dict dictionary, located in
    data.py file.

    The original csv file based on which {country_symbol: country_name} dictionary in data.py file was created, was downloaded from:
    https://pkgstore.datahub.io/core/country-list/data_csv/data/d7c9d7cfb42cb69f4422dec222dbbaa8/data_csv.csv
    """
    if not isinstance(symbol, str):
        raise ValueError("Wrong value used as a parameter - string is expected")
    symbol = symbol.upper()
    for sym in sym_cnt_dict:
        if sym == symbol:
            return sym_cnt_dict[sym]
