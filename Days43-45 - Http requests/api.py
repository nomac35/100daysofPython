import requests
from pprint import pprint
import collections

Result = collections.namedtuple('Result', 'director imdb_score title year')
def main():

    print("Welcome to the movie search Engine!!!")
    movie_name = input("What movie would you like to search")
    api = "http://movie_service.talkpython.fm/api/search/{}".format(movie_name)
    data = get_results(api)
    r = parse_data(data)
    display_results(r)



def get_results(api):
    request = requests.get(api)
    request.raise_for_status()
    data = request.json()
    #pprint(data)
    return data

def  parse_data(data):
    pprint(data)
    r =[]
    for k,i in enumerate(data['hits'],1):
        record = Result(director=i['director'], imdb_score=i['imdb_score'], title=i['title'], year=i['year'])
        p = "{}. {} directed by {} in {} and it has an imdb score of {}".format(k,record.title, record.director, record.year, record.imdb_score)
        r.append(p)
    return r
def display_results(r):
    print("We have found {} results".format(len(r)))
    print()

    for i in r:
        print(i)


if __name__ == '__main__':
    main()
