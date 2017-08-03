# Raspberry Pi OTD Twitter Bot

A Twitter bot which tweets "on this day" blog posts from Raspberry Pi's blog archive: [@raspberrypi_otd](https://twitter.com/raspberrypi_otd)

## Requirements

- Twython
- Postgresql

```bash
sudo apt install postgresql libpq-dev postgresql-client postgresql-client-common
sudo pip3 install twython psycopg2
```

## Usage

- Clone this repo
- Get your Twitter application's API keys from [apps.twitter.com](http://apps.twitter.com/) and export them to environment variables - **do not put these in your GitHub repo**
- Set up postgres (see [fullstackpython](https://www.fullstackpython.com/blog/postgresql-python-3-psycopg2-ubuntu-1604.html))
- Create a database called `rpi_otd`
- Run the import script:
    - `cat rpiblog.sql | psql rpi_otd`
- Run `python3 update_db.py` with Python initially to populate the database
- Add it to cron daily so it keeps the database up-to-date
- Run `bot.py` to test it works - you should see it posts a single tweet
- Add it to cron hourly between 9am and 3pm to tweet every day
    - The year looked up is 2002 + the current hour, so 9am = 2011
