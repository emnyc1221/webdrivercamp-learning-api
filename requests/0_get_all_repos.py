import requests


def get_repos(url):
    response = requests.get(url)
    print("Response status code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        total_count = data.get('total_count', 0)
        print("Total count of found items:", total_count)

        items = data.get('items', [])
        return sorted(items, key=lambda x: x['full_name'])
    else:
        return []


if __name__ == "__main__":
    url = "https://api.github.com/search/repositories?q=webdrivercamp-learning-python"

    list_of_items = get_repos(url)
    print()

    for item in list_of_items:
        user = item['owner']['login']
        repo = item['name']

        print(f"{user:15}", repo)
