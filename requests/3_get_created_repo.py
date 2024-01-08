import requests

def get_created_repo(url):

    token = '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'
    headers = {'Authorization': f'token {token}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repo = response.json()
        print(repo)

        try:
            assert repo['has_wiki'] == False
            assert repo['private'] == True
            assert repo['name'] == 'repo-created-with-api'
            assert repo['owner']['login'] == 'emnyc1221'
            print("Repository details are as expected.")
        except AssertionError as e:
            print("Assertion failed:", e)
    else:
        print("Failed to retrieve repository.")

    print("Response status code:", response.status_code)

if __name__=="__main__":
    url = "https://api.github.com/repos/emnyc1221/webdrivercamp-learning-api"

    get_created_repo(url)
