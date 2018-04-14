# Parse the movie_metadata.csv, using csv.DictReader you get a bunch of OrderedDicts from which you only need the following k,v pairs:
#
# OrderedDict([...
#             ('director_name', 'Lawrence Kasdan'),
#             ...
#             ('movie_title', 'Mumford\xa0'),
#             ...
#             ('title_year', '1999'),
#             ...
#             ('imdb_score', '6.9'),
#             ...
# Only consider directors with a minimum of 4 movies, otherwise you get misrepresentative data. However going to min 5 movies we miss Sergio Leone :(
#
# Take movies of year >= 1960.
#
# Print the top 20 highest rated directors with their movies ordered desc on rating.
import urllib.request
import collections
import os
import csv
from collections import defaultdict, Counter
Movies = collections.namedtuple('Movies', 'year, title, score')

Movies = collections.namedtuple('Movies', 'title year score')
movies = "https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv"

folder = os.path.dirname(__file__)
file_path = os.path.join(folder, "movies.csv")

urllib.request.urlretrieve(movies, file_path)

directors =defaultdict(list)
with open(file_path, 'r') as fout:

    for i in csv.DictReader(fout):

        director = i["director_name"]
        title = i["movie_title"]
        year = i["title_year"]
        score = i["imdb_score"]
        m=Movies(year=year, title=title, score=score)
        directors[director].append(m)
#print(directors)

movie_total = {}
for k,v in directors.items():
    print(k, len(v))
    movie_total[k] = int(len(v))
#print(movie_total)


rating = {}
rate = 0
for k,v in directors.items():
    for p in v:
        rate+=float(p[2])
        print(rate)
# p = 1
# for i,k in movie_total.items():
#
#
#     if k  >5:
#         print("{}. {}".format(p,i ))
#         print("-" * 60)
#         for i in directors[i]:
#             print("{}] {} {}".format(i[1],i[0],i[2]))
#         print("")
#     p+=1