from urllib.request import urlopen, Request
import gzip
import io
import csv
import threading
import time


class Data(threading.Thread):
    url = "https://data.brasil.io/dataset/covid19/caso_full.csv.gz"
    headers = {
        "User-Agent": "python-urllib/brasilio-client-0.1.0",
    }

    def __init__(self):
        threading.Thread.__init__(self)
        print('DataThread starting')

    def run(self):
        while True:
            request = Request(self.url, headers=self.headers)
            response = urlopen(request)
            decompressedFile = io.TextIOWrapper(gzip.GzipFile(fileobj=response), encoding='utf-8')
            reader = csv.reader(decompressedFile)
            with open('app/file/caso_full.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for row in reader:
                    writer.writerow(row)
            time.sleep(86400)