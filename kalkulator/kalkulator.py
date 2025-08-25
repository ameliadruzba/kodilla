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

while True:
    zapytanie_o_dzialanie = input(f'Podaj jakie dzialanie chcesz wykonac:\n1.dodawanie\n2.odejmowanie\n3.mnozenie\n4.dzielenie\n5.koniec programu\n')
    if zapytanie_o_dzialanie == "1":
        liczby = (input('Podaj liczby po spacji jakie chcesz do siebie dodac: ')).split(' ')
        liczby = [float(x.strip()) for x in liczby]
        print(dodawanie(*liczby))
    if zapytanie_o_dzialanie == "2":
        ode = (input('Podaj liczby po spacji jakie chcesz do siebie odjac: ')).split(' ')
        ode = [float(x) for x in ode]
        print(odejmowanie(*ode))
    if zapytanie_o_dzialanie == "3":
        mno = (input('Podaj liczby po spacji jakie chcesz pomnozyc: ')).split(' ')
        mno = [float(x) for x in mno]
        print(mnozenie(*mno))
    if zapytanie_o_dzialanie == "4":
        dzie = (input('Podaj liczby po spacji jakie chcesz podzielic: ')).split(' ')
        dzie = [float(x) for x in dzie]
        print(dzielenie(*dzie))
    if zapytanie_o_dzialanie == "5":
        break