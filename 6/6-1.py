from urllib import urlretrieve

# urlretrieve('http://table.finance.yahoo.com/table.csv?s=000001.sz', 'pingan.csv')

import csv

rf = open('pingan.csv', 'rb')
reader = csv.reader(rf)

for row in reader:
    print row
