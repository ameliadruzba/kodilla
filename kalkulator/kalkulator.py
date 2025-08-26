from funkcje import add, sub, multi, div

while True:
    operation = input(f'Podaj jakie dzialanie chcesz wykonac:\n1.dodawanie\n2.odejmowanie\n3.mnozenie\n4.dzielenie\n5.koniec programu\n')
    if operation == "1":
        number = (input('Podaj liczby po spacji jakie chcesz do siebie dodac: ')).split(' ')
        number = [float(x.strip()) for x in number]
        print(add(*number))
    if operation == "2":
        subtraction = (input('Podaj liczby po spacji jakie chcesz do siebie odjac: ')).split(' ')
        subtraction = [float(x) for x in subtraction]
        print(sub(*subtraction))
    if operation == "3":
        multiply = (input('Podaj liczby po spacji jakie chcesz pomnozyc: ')).split(' ')
        multiply = [float(x) for x in multiply]
        print(multi(*multiply))
    if operation == "4":
        division = (input('Podaj liczby po spacji jakie chcesz podzielic: ')).split(' ')
        division = [float(x) for x in division]
        print(div(*division))
    if operation == "5":
        break