import pytest
import unittest
from prikfy.transform import UnitTransform
unit=UnitTransform()

def test_positive_whole_numbers():
    assert unit.number_to_word(0) == "zero"
    assert unit.number_to_word(1) == "one"
    assert unit.number_to_word(10) == "ten"
    assert unit.number_to_word(100) == "one hundred"
    assert unit.number_to_word(1000) == "one thousand"
    assert unit.number_to_word(1234) == "one thousand two hundred thirty four"
    assert unit.number_to_word(1000000) == "one million"
    assert unit.number_to_word(1000000000) == "one billion"
    assert unit.number_to_word(1234567890) == "one billion two hundred thirty four million five hundred sixty seven thousand eight hundred ninety"

def test_negative_whole_numbers():
    assert unit.number_to_word(-1) == "minus one"
    assert unit.number_to_word(-10) == "minus ten"
    assert unit.number_to_word(-100) == "minus one hundred"
    assert unit.number_to_word(-1000) == "minus one thousand"
    assert unit.number_to_word(-1234) == "minus one thousand two hundred thirty four"
    assert unit.number_to_word(-1000000) == "minus one million"
    assert unit.number_to_word(-1000000000) == "minus one billion"
    assert unit.number_to_word(-1234567890) == "minus one billion two hundred thirty four million five hundred sixty seven thousand eight hundred ninety"

def test_positive_decimal_numbers():
    assert unit.number_to_word(3.14) == "three point one four"
    assert unit.number_to_word(123.456) == "one hundred twenty three point four five six"
    assert unit.number_to_word(1000.001) == "one thousand point zero zero one"
    assert unit.number_to_word(12345.6789) == "twelve thousand three hundred forty five point six seven eight nine"

def test_negative_decimal_numbers():
    assert unit.number_to_word(-3.14) == "minus three point one four"
    assert unit.number_to_word(-123.456) == "minus one hundred twenty three point four five six"
    assert unit.number_to_word(-1000.001) == "minus one thousand point zero zero one"
    assert unit.number_to_word(-12345.6789) == "minus twelve thousand three hundred forty five point six seven eight nine"

def test_zero():
    assert unit.number_to_word(0) == "zero"
    


def test_get_symbols_by_name():
    assert unit.get_currency_symbols_by_name("Leke") == ['Lek']
    assert unit.get_currency_symbols_by_name("Colón") == ['₡']
    

def test_get_names_by_symbol():
    assert unit.get_currency_names_by_symbol('Lek') == ['Leke']
    assert unit.get_currency_names_by_symbol('$') == ['Dollars', 'Pesos', 'Colones', 'Zimbabwean dollar']

def test_get_codes_by_symbol():
    assert unit.get_currency_codes_by_symbol('Lek') == ['ALL']
    assert unit.get_currency_codes_by_symbol('₡') == ["CRC"]

def test_get_info_by_symbol():
    assert unit.get_currency_info_by_symbol('$') == [('Dollars', 'USD'), ('Pesos', 'ARS'), ('Dollars', 'AUD'), ('Dollars', 'BSD'), ('Dollars', 'BBD'), ('Dollars', 'BMD'), ('Dollars', 'BND'), ('Dollars', 'CAD'), ('Dollars', 'KYD'), ('Pesos', 'CLP'), ('Pesos', 'COP'), ('Dollars', 'XCD'), ('Colones', 'SVC'), ('Dollars', 'FJD'), ('Dollars', 'GYD'), ('Dollars', 'HKD'), ('Dollars', 'LRD'), ('Pesos', 'MXN'), ('Dollars', 'NAD'), ('Dollars', 'NZD'), ('Dollars', 'SGD'), ('Dollars', 'SBD'), ('Dollars', 'SRD'), ('Dollars', 'TVD'), ('Zimbabwean dollar', 'ZWL')]

def test_get_country_codes_by_name():
    assert unit.get_country_codes_by_name("India") == {
        "Alpha-2 code": "IN",
        "Alpha-3 code": "IND"
    }
    assert unit.get_country_codes_by_name("United States of America") == {
        "Alpha-2 code": "US",
        "Alpha-3 code": "USA"
    }
    assert unit.get_country_codes_by_name("Canada") == {
        "Alpha-2 code": "CA",
        "Alpha-3 code": "CAN"
    }
    # Add more test cases for different country names and their expected codes

def test_get_alpha2_by_country():
    assert unit.get_alpha2_by_country("India") == "IN"
    assert unit.get_alpha2_by_country("United States of America") == "US"
    assert unit.get_alpha2_by_country("Canada") == "CA"
    # Add more test cases for different country names and their expected Alpha-2 codes

def test_get_alpha3_by_country():
    assert unit.get_alpha3_by_country("India") == "IND"
    assert unit.get_alpha3_by_country("United States of America") == "USA"
    assert unit.get_alpha3_by_country("Canada") == "CAN"
    # Add more test cases for different country names and their expected Alpha-3 codes

def test_get_country_by_alpha2():
    assert unit.get_country_by_alpha2("IN") == "India"
    assert unit.get_country_by_alpha2("US") == "United States of America"
    assert unit.get_country_by_alpha2("CA") == "Canada"
    # Add more test cases for different Alpha-2 codes and their expected country names

def test_get_country_by_alpha3():
    assert unit.get_country_by_alpha3("IND") == "India"
    assert unit.get_country_by_alpha3("USA") == "United States of America"
    assert unit.get_country_by_alpha3("CAN") == "Canada"
    # Add more test cases for different Alpha-3 codes and their expected country names
