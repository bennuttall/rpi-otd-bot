from datetime import date, datetime
import html
from time import sleep

from twython import Twython
from structlog import get_logger

from db import RPiBlogDatabase
from auth import *


twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

db = RPiBlogDatabase('db.sqlite')
logger = get_logger()

now = datetime.now()
month = now.date().month
day = now.date().day
year = 2002 + now.time().hour  # 9am = 2011
post_date = date(year, month, day)
logger.info("Getting posts", date=post_date)
posts = db.get_posts_by_date(post_date)
logger.info("Number of posts found", n=len(posts))

for post in posts:
    title = html.unescape(post['title'])
    url = post['url']

    tweet = f"On this day in {year}: {title} {url}"
    logger.info("Tweeting:", tweet=tweet)
    twitter.update_status(status=tweet)
    sleep(60)
