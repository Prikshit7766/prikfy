from ..data import country_codes_dict
from ...custom_exception import CustomException

def get_country_codes_by_name(country_name):
    for country, codes in country_codes_dict.items():
        if country.lower() == country_name.lower():
            return codes
    return None

def get_alpha2_by_country(country_name):
    for country, codes in country_codes_dict.items():
        if country.lower() == country_name.lower():
            return codes.get("Alpha-2 code")
    return None

def get_alpha3_by_country(country_name):
    for country, codes in country_codes_dict.items():
        if country.lower() == country_name.lower():
            return codes.get("Alpha-3 code")
    return None

def get_country_by_alpha2(alpha2_code):
    for country, codes in country_codes_dict.items():
        if codes.get("Alpha-2 code") == alpha2_code.upper():
            return country
    return None

def get_country_by_alpha3(alpha3_code):
    for country, codes in country_codes_dict.items():
        if codes.get("Alpha-3 code") == alpha3_code.upper():
            return country
    return None