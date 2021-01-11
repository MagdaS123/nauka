import requests
import datetime
import lxml.html


try:
    def myfunction():
        r = requests.get('https://exchangeratesapi.io/')
        print(r)

        titles = new_releases.xpath('.//div[@class="http px-5"]/text()')

        print(titles)

    myfunction()
except:
    print('w module try zostal znaleziony blad')

def czas():
    x = datetime.datetime.now()
    print(x)

czas()
