# Raspberry Pi OTD Twitter Bot

A Twitter bot which tweets "on this day" blog posts from Raspberry Pi's blog
archive: [@raspberrypi_otd](https://twitter.com/raspberrypi_otd)

Updated October 2021 to cover both raspberrypi.com and raspberrypi.org

![](made-in-the-uk.png)

## Requirements

- Twython
- sqlalchemy
- structlog

```bash
pip install -r requirements.txt
```

## Usage

- Clone this repo
- Get your Twitter application's API keys from [dev.twitter.com](http://dev.twitter.com/)
and add them to `auth.py` (**Do not publish these on your GitHub**)
- Run `python db/tables.py db.sqlite` to create the database schema
- Run `python update_db.py` to populate the database
- Add it to cron daily so it keeps the database up-to-date
- Run `python bot.py` to test it works - you should see it posts a single tweet
- Add it to cron hourly to tweet every matching hour every day
    - The year looked up is 2002 + the current hour, so 9am = 2011
