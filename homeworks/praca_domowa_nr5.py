import requests
import datetime
import time
import json

def pobierzDaneKursu():
    return requests.get('https://api.exchangeratesapi.io/latest?base=EUR')

def zmierzCzas(x, y):
    return y-x

def sprawdzKurs():
        dataWykonania = datetime.datetime.now()
        print('Data i godzina: ', dataWykonania)
        try:
            r = pobierzDaneKursu()
            y = datetime.datetime.now()
            czasWykonania = zmierzCzas(dataWykonania, y)
        except :
            print('blad wywolania strony')
        else:
            czasWykonania = czasWykonania.microseconds/1000
            print("czas wykonania {} ms".format(czasWykonania))
            j = json.loads(r.text)
            kursWaluty = j['rates']['PLN']
            print('Kurs Euro: ', kursWaluty)

            f = open("./dane.csv", "a")
            f.write("{},{}ms,{}zl\n".format(dataWykonania, czasWykonania, kursWaluty))
            f.close()

while True:
    sprawdzKurs()
    time.sleep(15)





