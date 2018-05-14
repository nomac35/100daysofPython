import requests
from pprint import pprint
import collections
import webbrowser

Result = collections.namedtuple('Result', 'category id url title description')
def main():

    print("Welcome to the search Engine!!!")
    search_name = input("What would you like to search for")
    api = "http://search.talkpython.fm/api/search?q={}".format(search_name)
    data = get_results(api)
    r,m = parse_data(data)
    display_results(r)
    response = input("Would you like to review any of these results? Y/N")
    print()
    if response == 'y':
        number = input("Please type the number you would like to review")
        url = "https://talkpython.fm{}".format(m[int(number)-1])
        webbrowser.open(url)


def get_results(api):
    request = requests.get(api)
    request.raise_for_status()
    data = request.json()
    #pprint(data)
    return data

def  parse_data(data):
    #pprint(data)
    r =[]
    w =[]
    for k,i in enumerate(data['results'],1):
        record = Result(**i)
        p = "{}. {} ".format(k,record.title)
        sites = "{}".format(record.url)
        r.append(p)
        w.append(sites)
    return r,w
def display_results(r):
    print("We have found {} results".format(len(r)))
    print()

    for i in r:
        print(i)
def view_site():
    pass

if __name__ == '__main__':
    main()
