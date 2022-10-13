import sys
from json.decoder import JSONDecodeError
from datetime import datetime

import requests
from requests import RequestException
from structlog import get_logger

from db import RPiBlogDatabase


db = RPiBlogDatabase('db.sqlite')
logger = get_logger()

URLS = [
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
        logger.exception(exc)
        return []


if __name__ == '__main__':
    for url in URLS:
        page = 1
        posts = True

        while posts:
            logger.info("Fetching posts", url=url, page=page)
            posts = get_posts(url, page)
            for post in posts:
                slug = post['slug']
                link = post['link']
                title = post['title']['rendered']
                pub_date = datetime.fromisoformat(post['date'])
                if first_run or not db.post_in_db(link):
                    logger.info("Adding post", slug=slug)
                    db.insert_post(link, title, pub_date)
                else:
                    posts = False
            page += 1
