from datetime import date, datetime
import html
from time import sleep

from twython import Twython
from db import RPiBlogDatabase

from auth import *

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

db = RPiBlogDatabase()

now = datetime.now()
month = now.date().month
day = now.date().day
year = 2002 + now.time().hour  # 9am = 2011
post_date = date(year, month, day)
posts = db.get_posts_by_date(post_date)

for post in posts:
    title = html.unescape(post['title'])
    url = post['url']

    tweet = f"On this day in {year}: {title} {url}"
    print(f"Tweeting: {tweet}")
    twitter.update_status(status=tweet)
    sleep(60)
