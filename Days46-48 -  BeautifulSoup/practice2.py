import requests
import bs4

def main():

    url='https://pybit.es/pages/articles.html'
    html_code = get_html(url)
    parse_html(html_code)

def get_html(url):
    request = requests.get(url)
    request.raise_for_status()
    return request.text

def parse_html(html_code):

    soup = bs4.BeautifulSoup(html_code, "html.parser")
    project = soup.main.find_all('li')
    for i in project:
        print(i.string)




if __name__ == '__main__':
    main()