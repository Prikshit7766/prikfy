import csv

def sym_to_name (symbol: str) -> str:

    """
    syn_to_name (convert contry code to country fullname)
    Returns country full name based on a symbol given as an argument.
    The symbol argument is case-insensitive
    If given symbol is not included in the csv file, returns None.
    The function uses country_name_code.csv file.

    The file was downloaded from:
    https://pkgstore.datahub.io/core/country-list/data_csv/data/d7c9d7cfb42cb69f4422dec222dbbaa8/data_csv.csv
    """ 
    
    with open('country_name_code.csv') as file:
        reader = csv.reader(file)

        for row in reader:
            if(row[1]==symbol.upper()):
                return row[0]
