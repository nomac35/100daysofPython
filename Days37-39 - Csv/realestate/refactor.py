import os
import csv
import collections
import statistics

data = []
Record = collections.namedtuple('Record', ' street,city,zip,state,beds,baths,sq__ft,type,sale_date,price,latitude,longitude')
def init():
    base_file = os.path.dirname(__file__)
    file_name = os.path.join(base_file, 'SacramentoRealEstateTransactions2008.csv')

    with open(file_name, 'r') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            record = parse_row(row)
            data.append(record)

def parse_row(row):
    row['beds'] = int(row['beds'])
    row['baths'] = int(row['baths'])
    row['sq__ft'] = int(row['sq__ft'])
    row['price'] = float(row['price'])
    row['zip'] = int(row['zip'])
    record = Record(**row)
    return record

def most_expensive():
    p= (max(data, key=lambda r: r.price))

    return (f'Most Expensive house: {p.beds}-bed, {p.baths}-bath house for {p.price} in {p.city}')

def least_expensive():
    p= (min(data, key=lambda r: r.price))
    return (f'Least Expensive house: {p.beds}-bed, {p.baths}-bath house for {p.price} in {p.city}')
def avarage():
    avarage_price = [i.price for i in data]


    return "The avarage price is ${:,}".format(statistics.mean(avarage_price))

print(init())
print(data)
print(most_expensive())
print(least_expensive())
print(avarage())