import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename='loggi.log')

def dodawanie(*args:float):
    logging.debug(f'wartosci podane dla dzialania DODAWANIE to {(list(args))}\nroznica wynosi = {sum(args)}')
    return sum(args)

def odejmowanie(*args:float):
    baza = args[0]
    for i in args[1:]:
        baza -= i
    logging.debug(f'wartosci podane dla dzialania ODEJMOWANIE to {(list(args))}\nroznica wynosi = {baza}')
    return baza

def mnozenie(*args:float):
    liczba = 1
    for i in args:
        liczba *= i
    logging.debug(f'wartosci podane dla dzialania MNOŻENIA to {(list(args))}\nwynik wynosi = {liczba}')
    return liczba


def dzielenie(*args:float):
    start = args[0]
    for i in args[1:]:
        start /= i
    logging.debug(f'wartosci podane dla dzialania DZIELENIA to {(list(args))}\nwynik wynosi = {start}')
    return start