
import os
import csv
import collections

Record = collections.namedtuple('Record', 'date,actual_mean_temp,actual_min_temp,actual_max_temp,average_min_temp,average_max_temp,record_min_temp,record_max_temp,record_min_temp_year,record_max_temp_year,actual_precipitation,average_precipitation,record_precipitation')
data = []
base_file = os.path.dirname(__file__)
file = os.path.join(base_file, 'seattle.csv')


def init():
    with open(file, 'r') as fin:
        reader = csv.DictReader(fin)

        data.clear()
        for row in reader:
            record = parse_row(row)
            #print(record)
            data.append(record)



def parse_row(row):
    row['actual_mean_temp'] = int(row['actual_mean_temp'])
    row['actual_min_temp'] = int(row['actual_min_temp'])
    row['actual_max_temp'] = int(row['actual_max_temp'])
    row['average_min_temp'] = int(row['average_min_temp'])
    row['average_max_temp'] = int(row['average_max_temp'])
    row['record_min_temp'] = int(row['record_min_temp'])
    row['record_max_temp'] = int(row['record_max_temp'])
    row['record_min_temp_year'] = int(row['record_min_temp_year'])
    row['record_max_temp_year'] = int(row['record_max_temp_year'])
    row['actual_precipitation'] = float(row['actual_precipitation'])
    row['average_precipitation'] = float(row['average_precipitation'])
    row['record_precipitation'] = float(row['record_precipitation'])
    record = Record(**row)
    return record




print(init())
def hot_days():
    return sorted(data, key=lambda r: -r.actual_max_temp)

print(hot_days())
def cold_days():
    return sorted(data, key=lambda r: r.actual_max_temp)

def wet_days():
    return sorted(data, key=lambda r: -r.actual_precipitation)
