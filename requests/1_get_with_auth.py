import requests


def get_with_auth(url):
    token = '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'
    headers = {'Authorization': f'token {token}'}

    response = requests.get(url, headers=headers)
    print("Response status code:", response.status_code)

    if response.status_code == 200:
        repos = response.json()
        return len(repos), response.headers
    else:
        return 0, response.headers


if __name__ == "__main__":
    url = "https://api.github.com/user/repos"

    num_of_repos, headers = get_with_auth(url)

    print(f"Total Repos: {num_of_repos}")
    print(f"Response headers: {headers}")
