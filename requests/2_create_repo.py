import requests
from pprint import pprint


def create_repo(url):
    token = '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'
    headers = {
        'Authorization': f'token {token}',
        'Content-Type': 'application/json'
    }

    data = {
        'name': 'repo-created-with-api',
        'private': True,
        'has_wiki': False
    }

    response = requests.post(url, headers=headers, json=data)
    print("Response status code:", response.status_code)

    return response.json()


if __name__ == '__main__':
    url = 'https://api.github.com/user/repos'

    repo = create_repo(url)
    pprint(repo)
