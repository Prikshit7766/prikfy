import pytest
from prikfy.operation.number_to_word import number_to_words

def test_positive_whole_numbers():
    assert number_to_words(0) == "zero"
    assert number_to_words(1) == "one"
    assert number_to_words(10) == "ten"
    assert number_to_words(100) == "one hundred"
    assert number_to_words(1000) == "one thousand"
    assert number_to_words(1234) == "one thousand two hundred thirty four"
    assert number_to_words(1000000) == "one million"
    assert number_to_words(1000000000) == "one billion"
    assert number_to_words(1234567890) == "one billion two hundred thirty four million five hundred sixty seven thousand eight hundred ninety"

def test_negative_whole_numbers():
    assert number_to_words(-1) == "minus one"
    assert number_to_words(-10) == "minus ten"
    assert number_to_words(-100) == "minus one hundred"
    assert number_to_words(-1000) == "minus one thousand"
    assert number_to_words(-1234) == "minus one thousand two hundred thirty four"
    assert number_to_words(-1000000) == "minus one million"
    assert number_to_words(-1000000000) == "minus one billion"
    assert number_to_words(-1234567890) == "minus one billion two hundred thirty four million five hundred sixty seven thousand eight hundred ninety"

def test_positive_decimal_numbers():
    assert number_to_words(3.14) == "three point one four"
    assert number_to_words(123.456) == "one hundred twenty three point four five six"
    assert number_to_words(1000.001) == "one thousand point zero zero one"
    assert number_to_words(12345.6789) == "twelve thousand three hundred forty five point six seven eight nine"

def test_negative_decimal_numbers():
    assert number_to_words(-3.14) == "minus three point one four"
    assert number_to_words(-123.456) == "minus one hundred twenty three point four five six"
    assert number_to_words(-1000.001) == "minus one thousand point zero zero one"
    assert number_to_words(-12345.6789) == "minus twelve thousand three hundred forty five point six seven eight nine"

def test_zero():
    assert number_to_words(0) == "zero"
    

