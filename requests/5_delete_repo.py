import requests

def delete_repo(url):
    token = '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'
    headers = {'Authorization': f'token {token}'}

    response = requests.delete(url, headers=headers)
    print("Response status code:", response.status_code)

if __name__ == "__main__":
    owner = 'emnyc1221'
    repo = 'repo-created-with-api'
    url = f'https://api.github.com/repos/{owner}/{repo}'

    delete_repo(url)
