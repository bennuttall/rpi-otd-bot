import sys
from json.decoder import JSONDecodeError

import requests
from requests import RequestException

from db import RPiBlogDatabase


db = RPiBlogDatabase()

urls = [
    'https://www.raspberrypi.com/wp-json/wp/v2/posts',
    'https://www.raspberrypi.org/wp-json/wp/v2/posts',
]

first_run = len(sys.argv) > 1 and sys.argv[1] == '--first-run'

def get_posts(url, page=1):
    params = {
        'per_page': 100,
        'page': page,
    }
    try:
        response = requests.get(url, params)
        response.raise_for_status()
        return response.json()
    except (RequestException, JSONDecodeError) as exc:
        print(exc)
        return []

if __name__ == '__main__':
    for url in urls:
        page = 1
        posts = True

        while posts:
            print("Fetching posts from {}, page {}".format(url, page))
            posts = get_posts(url, page)
            for post in posts:
                slug = post['slug']
                link = post['link']
                title = post['title']['rendered']
                pub_date = post['date']
                if first_run or not db.get_post_by_url(link):
                    print(f"Adding {slug}")
                    db.insert_post(link, title, pub_date)
                else:
                    posts = False
            page += 1
