from ..utils.operation.number_to_word import number_to_word
from ..custom_exception import CustomException
from ..utils.operation.currency_mapping import get_currency_symbols_by_name, get_currency_names_by_symbol, get_currency_codes_by_symbol, get_currency_info_by_symbol
from ..utils.operation.country_mapping import get_country_codes_by_name, get_alpha2_by_country, get_alpha3_by_country, get_country_by_alpha2, get_country_by_alpha3
class UnitTransform:
    def __init__(self):
        # Initialize any necessary variables or configurations
        pass

    def number_to_word(self, value):
        try:
            # Call the number_to_word function from prikfy.operation.number_to_word
            return number_to_word(value)
        except Exception as e:
            raise CustomException(str(e))

    def get_currency_symbols_by_name(self, currency_name):
        try:
            return get_currency_symbols_by_name(currency_name)
        except Exception as e:
            raise CustomException(str(e))

    def get_currency_names_by_symbol(self, currency_symbol):
        try:
            return get_currency_names_by_symbol(currency_symbol)
        except Exception as e:
            raise CustomException(str(e))

    def get_currency_codes_by_symbol(self, currency_symbol):
        try:
            return get_currency_codes_by_symbol(currency_symbol)
        except Exception as e:
            raise CustomException(str(e))

    def get_currency_info_by_symbol(self, currency_symbol):
        try:
            return get_currency_info_by_symbol(currency_symbol)
        except Exception as e:
            raise CustomException(str(e))
        
    def get_country_codes_by_name(self, country_name):
        try:
            return get_country_codes_by_name(country_name)
        except Exception as e:
            raise CustomException(str(e))

    def get_alpha2_by_country(self, country_name):
        try:
            return get_alpha2_by_country(country_name)
        except Exception as e:
            raise CustomException(str(e))

    def get_alpha3_by_country(self, country_name):
        try:
            return get_alpha3_by_country(country_name)
        except Exception as e:
            raise CustomException(str(e))

    def get_country_by_alpha2(self, alpha2_code):
        try:
            return get_country_by_alpha2(alpha2_code)
        except Exception as e:
            raise CustomException(str(e))

    def get_country_by_alpha3(self, alpha3_code):
        try:
            return get_country_by_alpha3(alpha3_code)
        except Exception as e:
            raise CustomException(str(e))
        

class Transformation:
    pass