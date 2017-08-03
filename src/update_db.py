import requests
from db import RPiBlogDatabase

db = RPiBlogDatabase()

url = 'https://www.raspberrypi.org/wp-json/wp/v2/posts?per_page=100'

posts = True
page = 1

while posts:
    request = '{}&page={}'.format(url, page)
    posts = requests.get(request).json()
    for post in posts:
        slug = post['slug']
        title = post['title']['rendered']
        pub_date = post['date']
        if db.get_post_by_slug(slug):
            posts = False
        else:
            print('Adding {}'.format(slug))
            db.insert_post(slug, title, pub_date)
    page += 1
