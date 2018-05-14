import requests
import bs4
import collections
Weather = collections.namedtuple('Weather', 'location temp value')
def main():
    zipcode = input("What is your zip code?")
    #zipcode = 91601
    url = f'https://www.wunderground.com/weather/{zipcode}'
    data = get_html(url)
    parse_html(data)

def get_html(url):

    request = requests.get(url)
    request.raise_for_status()
    data = request.text
    return data

def parse_html(data):
    soup = bs4.BeautifulSoup(data, "html.parser")
    if __name__ == '__main__':
        location = soup.find('h1').getText().strip()
        temp = soup.select(".wu-value")[0].getText().strip()

        value = soup.select(".wu-label")[0].getText().strip()
        record = Weather(location=location, temp=temp, value=value)
        print(f'Weather in {record.location} is {record.temp} {record.value}')







if __name__ == '__main__':
    main()