import psycopg2
from psycopg2.extras import DictCursor


class RPiBlogDatabase:
    def __init__(self):
        self.conn = psycopg2.connect(
            'dbname=rpi_otd',
            cursor_factory=DictCursor
        )

    def insert_post(self, url, title, pub_date):
        values = (url, title, pub_date)
        query = """
        INSERT INTO
            rpi_posts (url, title, pub_date)
        VALUES
            (%s, %s, %s)
        """
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(query, values)

    def get_post_by_url(self, url):
        query = """
        SELECT
            1
        FROM
            rpi_posts
        WHERE
            url = %s
        """
        values = (url, )
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(query, values)
                return cur.fetchone()

    def get_posts_by_date(self, date):
        query = """
        SELECT
            url, title
        FROM
            rpi_posts
        WHERE
            pub_date::date = date %s
        """
        values = (date, )
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(query, values)
                return cur.fetchall()
