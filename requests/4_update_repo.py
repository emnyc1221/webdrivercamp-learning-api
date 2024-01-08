import requests

def update_repo(url):
    token = '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'
    headers = {
        'Authorization': f'token {token}',
        'Content-Type': 'application/json'
    }

    # Data to update
    data = {
        'description': 'I know Python Requests!'
    }

    response = requests.patch(url, headers=headers, json=data)
    print("Response status code:", response.status_code)

    return response.json()

if __name__=='__main__':
    url = 'https://api.github.com/repos/emnyc1221/webdrivercamp-learning-api'

    repo = update_repo(url)
    assert repo['description'] == 'I know Python Requests!'
