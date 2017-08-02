from twython import Twython
import os
import random
from datetime import datetime
import html
from db import RPiBlogDatabase

twitter = Twython(
    os.environ['RPOTD_CON_KEY'],
    os.environ['RPOTD_CON_SEC'],
    os.environ['RPOTD_ACC_TOK'],
    os.environ['RPOTD_ACC_SEC']
)

db = RPiBlogDatabase()

date = datetime.now().date()
month = date.month
day = date.day
posts = db.get_posts_on_date(month=month, day=day)

post = random.choice(posts)

year = int(post['year'])
title = html.unescape(post['title'])
slug = post['slug']
url = 'https://www.raspberrypi.org/blog/{}'.format(slug)

tweet = "On this day in {}: {} {}".format(year, title, url)
print('Tweeting: {}'.format(tweet))
twitter.update_status(status=tweet)
