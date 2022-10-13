from sqlalchemy import Column, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class BlogPost(Base):
    __tablename__ = 'blogposts'

    url = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    pub_date = Column(DateTime, nullable=False)


if __name__ == '__main__':
    import sys

    db_file = sys.argv[1]
    engine = create_engine(f"sqlite:///{db_file}")
    BlogPost.__table__.create(bind=engine)