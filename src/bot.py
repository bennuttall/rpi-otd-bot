from twython import Twython
import os
from datetime import date, datetime
import html
from db import RPiBlogDatabase

twitter = Twython(
    os.environ['RPOTD_CON_KEY'],
    os.environ['RPOTD_CON_SEC'],
    os.environ['RPOTD_ACC_TOK'],
    os.environ['RPOTD_ACC_SEC']
)

db = RPiBlogDatabase()

now = datetime.now()
month = now.date().month
day = now.date().day
year = 2002 + now.time().hour  # 9am = 2011
post_date = date(year, month, day)
post = db.get_post_by_date(post_date)

if post:
    title = html.unescape(post['title'])
    slug = post['slug']
    url = 'https://www.raspberrypi.org/blog/{}'.format(slug)

    tweet = "On this day in {}: {} {}".format(year, title, url)
    print('Tweeting: {}'.format(tweet))
    twitter.update_status(status=tweet)
