from ..utils.operation.number_to_word import number_to_word
from ..custom_exception import CustomException
from ..utils.operation.currency_mapping import get_symbols_by_name, get_names_by_symbol, get_codes_by_symbol, get_info_by_symbol

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
            return get_symbols_by_name(currency_name)
        except Exception as e:
            raise CustomException(str(e))

    def get_currency_names_by_symbol(self, currency_symbol):
        try:
            return get_names_by_symbol(currency_symbol)
        except Exception as e:
            raise CustomException(str(e))

    def get_currency_codes_by_symbol(self, currency_symbol):
        try:
            return get_codes_by_symbol(currency_symbol)
        except Exception as e:
            raise CustomException(str(e))

    def get_currency_info_by_symbol(self, currency_symbol):
        try:
            return get_info_by_symbol(currency_symbol)
        except Exception as e:
            raise CustomException(str(e))

class Transformation:
    pass