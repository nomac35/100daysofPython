import requests
from pprint import pprint


def main():
    user, repo = get_info()

    # url = 'https://api.github.com/repos/mikeckennedy/consuming_services_python_demos'
    url = 'https://api.github.com/repos/{}/{}'.format(user, repo)
    data = get_repo(url)
    print(get_clone(data))
    # pprint(data)


def get_info():
    user = input("what is your github name")
    repo = input('what is your input name?')

    return user, repo


def get_repo(url):
    request = requests.get(url)
    data = request.json()

    if request.status_code != 200:
        print("Error: {}".format(request.status_code))
    return data


def get_clone(data):
    return("To Clone this repo use : git clone {}".format(data['clone_url']))


if __name__ == '__main__':
    main()
