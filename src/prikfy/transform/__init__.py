from ..utils.operation.number_to_word import number_to_word
from ..utils.operation.convert_abbreviation import convert_abbreviation


class UnitTransform:
    def __init__(self):
        # Initialize any necessary variables or configurations
        pass

    def number_to_word(self, value):
        try:
            # Call the number_to_word function from prikfy.operation.number_to_word
            return number_to_word(value)
        except Exception as e:
            print("Warning: Error occurred while converting number to words. Returning original value.")
            return value
class CommonAbbreviations:
    def __init__(self):
        pass

    def convert_abbreviation(self, value) :
        #try:
            return convert_abbreviation(value)
        #except:
         #   print("Warning: An error has been encountered while converting abbrevation. Returning original value")
         #   return value
 


class Transformation:
    pass