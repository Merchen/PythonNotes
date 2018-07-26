import os
import requests
from concurrent import futures
import time

class DownloadFlags():
    countries = ['CN', 'IN', 'US', 'BR', 'PK', 'NG']
    base_url = 'http://flupy.org/data/flags'
    base_path = os.path.dirname(__file__)

    try:
        # print(os.path.exists('../module'))
        os.makedirs('./flags', exist_ok=False)
    except:
        pass

    def download(self, country):
        url = '{}/{c}/{c}.gif'.format(self.base_url, c=country.lower())
        return requests.get(url).content

    def save(self, image, name):
        path = os.path.join(self.base_path, 'flags/' + name + '.gif')
        with open(path, 'wb') as img:
            img.write(image)

    def execute(self):
        t0 = time.time()
        for country in self.countries:
            print("Downloading %s's flag" % country)
            image = self.download(country)
            print("Saving %s's flag" % country)
            self.save(image, country)
        print('%.6fs' % (time.time() - t0))

# import test0.test1.hello as hello


import PythonNotes.module






def _ThreadPoolExecutor():
    pass