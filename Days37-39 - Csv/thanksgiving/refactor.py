import os
import csv
import collections

data = []
Record = collections.namedtuple('Record', ' region main_dish first_dish second_dish third_dish celeb forth_dish')
def init():
    base_file = os.path.dirname(__file__)
    file_name = os.path.join(base_file, 'thanksgiving.csv')

    with open(file_name, 'r') as fin:
        reader = csv.DictReader(fin)

        for row in reader:
            records = parse_row(row)
            data.append(records)
            #print(f'{records.region} {records.main_dish}')

def parse_row(row):
    record = Record(

                    region=row['US Region'],
                    main_dish=row['What is typically the main dish at your Thanksgiving dinner?'],
                    first_dish=row['Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Brussel sprouts'],
                    second_dish=row['Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Carrots'],
                    third_dish=row['Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Cauliflower'],
                    forth_dish=row['Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Cornbread'],
                    celeb=row['Do you celebrate Thanksgiving?'])
    return record

def main_dish(place):
    #for i in data:
        #if place == i.region:
    p= [i for i in data if place == i.region]
    count = collections.Counter(p)
    most_common = count.most_common(1)
    return (list(most_common[0][0])[1])

print(init())

print(data)
print(main_dish(place='Middle Atlantic'))
