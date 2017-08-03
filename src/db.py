import psycopg2
from psycopg2.extras import DictCursor

class RPiBlogDatabase:
    def __init__(self):
        self.conn = psycopg2.connect(
            'dbname=rpi_otd',
            cursor_factory=DictCursor
        )

    def insert_post(self, slug, title, pub_date):
        values = (slug, title, pub_date)
        query = """
        INSERT INTO
            rpi_posts (slug, title, pub_date)
        VALUES
            (%s, %s, %s)
        """
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(query, values)

    def get_post_by_slug(self, slug):
        query = """
        SELECT
            1
        FROM
            rpi_posts
        WHERE
            slug = %s
        """
        values = (slug, )
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(query, values)
                return cur.fetchone()

    def get_post_by_date(self, date):
        query = """
        SELECT
            slug, title
        FROM
            rpi_posts
        WHERE
            pub_date::date = date %s
        """
        values = (date, )
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(query, values)
                return cur.fetchone()
