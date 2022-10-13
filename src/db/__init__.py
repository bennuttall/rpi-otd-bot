from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .tables import BlogPost


class RPiBlogDatabase:
    def __init__(self, db_file: str):
        self.engine = create_engine(f"sqlite:///{db_file}")

    def insert_post(self, url: str, title: str, pub_date: datetime):
        """
        Insert a new blog post into the database
        """
        with Session(self.engine, autocommit=True) as session:
            post = BlogPost(url=url, title=title, pub_date=pub_date)
            session.add(post)
            session.flush()

    def post_in_db(self, url: str) -> bool:
        """
        Determine whether the post is already in the database
        """
        with Session(self.engine) as session:
            query = (
                BlogPost.__table__.select()
                .where(BlogPost.url == url)
            )
            post = session.execute(query).one_or_none()
            return post is not None

    def get_posts_by_date(self, date: datetime) -> list[BlogPost]:
        """
        Retrieve all blog posts on a particular date
        """
        with Session(self.engine) as session:
            query = (
                BlogPost.__table__.select()
                .where(BlogPost.pub_date == date)
            )
            return session.execute(query).mappings().all()
