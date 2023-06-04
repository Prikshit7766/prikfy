from IPython import display
from ...custom_exception import CustomException
from ..data import (abbreviations)
from ...logger import logging
import sys

def convert_abbreviation(str) :
        for k,v in abbreviations.items() :
            if str == k :
                str = v
                return str