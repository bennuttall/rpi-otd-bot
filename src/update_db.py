import requests

from db import RPiBlogDatabase


db = RPiBlogDatabase()

urls = [
    'https://www.raspberrypi.com/wp-json/wp/v2/posts',
    'https://www.raspberrypi.org/wp-json/wp/v2/posts',
]

params = {
    'per_page': 100,
    'page': 1,
}

for url in urls:
    posts = True

    while posts:
        posts = requests.get(url, params).json()
        for post in posts:
            try:
                slug = post['slug']
                url = post['link']
                title = post['title']['rendered']
                pub_date = post['date']
            except TypeError:
                posts = None
                break
            if db.get_post_by_url(url):
                posts = False
            else:
                print(f"Adding {slug}")
                db.insert_post(url, title, pub_date)
        params['page'] += 1
