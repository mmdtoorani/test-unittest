import json
import requests
import os


def get_data(url: str):
    response = requests.request('GET', url)
    return response


def combine_to_json():
    url = "https://jsonplaceholder.typicode.com/posts/"
    data = json.loads(get_data(url).text)
    return data


def create_file(data: [dict, list], path: str, filename: str):
    if not os.path.exists(path + filename):
        with open(path + filename, 'w', encoding='utf-8') as f:
            json.dump(data, f)


if __name__ == '__main__':
    create_file(combine_to_json(), "../files/", "myjson.json")
