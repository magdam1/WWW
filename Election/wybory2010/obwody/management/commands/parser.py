import urllib3
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError
from obwody.models import Wojewodztwo, Powiat_Miasto, Gmina_Miasto, Obwod

class Command(BaseCommand):
    help = 'Pobieram obwody wyborcze z oficjalnej strony wyborów prezydenckich 2010'

    def circuit(self, n, prev, adress):
        if n > 0:
            http = urllib3.PoolManager()
            page = http.urlopen('GET', adress, preload_content = False)

            soup = BeautifulSoup(page)

            table = soup.find(id='s0').find('tbody')

            for link in table.find_all('a'):
                output = link.string

                if n == 4:
                    woj = Wojewodztwo(nazwa = output)
                    woj.save()
                    print("Dodano "+output)
                    id = woj
                elif n == 3:
                    pm = Powiat_Miasto(nazwa = output, wojewodztwo = prev)
                    pm.save()
                    print("Dodano "+output)
                    id = pm
                elif n == 2:
                    sufix = link.get('href')
                    if sufix[0] == '.':
                        var = Obwod(nazwa = output, miasto = prev)
                    else:
                        var = Gmina_Miasto(nazwa = output, powiat = prev)
                        p = Powiat_Miasto.objects.get(id = prev.id)
                        p.ma_gminy = 1
                        p.save()

                    var.save()
                    print("Dodano "+output)
                    id = var
                elif n == 1:
                    obw = Obwod(nazwa = output, gmina = prev)
                    obw.save()
                    print("Dodano "+output)

                sufix = link.get('href')
                if sufix[0] != '.':
                    self.circuit(n-1, id, 'http://prezydent2010.pkw.gov.pl/PZT/PL/WYN/W/'+link.get('href'))

        return 0

    def handle(self, *args, **options):
        self.circuit(4, 0, 'http://prezydent2010.pkw.gov.pl/PZT/PL/WYN/W/')
        


