import json
import requests
from pprint import pprint
import collections

Movie = collections.namedtuple('Movie', 'Title, Year')


def main():
    api_key= "9719db6"
    movie_name = input("please enter a movie name")
    url = "http://www.omdbapi.com/?s={}&page=2&apikey={}".format(movie_name, api_key)
    get_movies(url)

def get_movies(url):
    request = requests.get(url)
    data = request.json()
    #pprint(data)
    #record = Movie(Title="Title", Year="Year")
    if data["Response"] == "True":
        for i,k in enumerate(data['Search'],1):
        #print("{}. {}, year:{}".format(i,k['Title'],k['Year']))
            record = Movie(Title=k["Title"], Year=k["Year"])
            print("{} {}, year:{}".format(i, record.Title, record.Year))
    else:
        print(data["Error"])


def parse_data():
    record = Movie(Title="Title", Year="Year")
    return record




if __name__ == '__main__':
    main()

