import requests
import bs4

def main():

    url='https://pybit.es/pages/projects.html'
    html_code = get_html(url)
    parse_html(html_code)

def get_html(url):
    request = requests.get(url)
    request.raise_for_status()
    return request.text

def parse_html(html_code):

    soup = bs4.BeautifulSoup(html_code, "html.parser")
    project = soup.select('.projectHeader')
    #print(project)
    headerlist = [i.getText() for i in project]

    for i in headerlist:
        print(i)



if __name__ == '__main__':
    main()