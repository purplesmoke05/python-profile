from typing import List, Optional
from datetime import datetime
from datetime import date as datetime_date
import time

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    BigInteger,
    String,
    DateTime
)


class BaseModel(object):
    # created datetime(UTC)
    created = Column(DateTime, default=datetime.utcnow)
    # modified datetime(UTC)
    modified = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @staticmethod
    def datetime_to_timestamp(date):
        if isinstance(date, datetime_date):
            return int(time.mktime(date.timetuple()))
        else:
            return None


Base = declarative_base(cls=BaseModel)


class TestModel(Base):
    """INDEX Transfer"""
    __tablename__ = "test_model"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    data = Column(String(254))


from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine


def main():
    engine = create_engine('sqlite:///sample_db.sqlite3', echo=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

    Base.metadata.create_all(engine)

    # create 2 session
    session1: Session = SessionLocal()
    session2: Session = Session(autocommit=False, autoflush=True, bind=engine)

    # operate "add" in a session
    _test_model = TestModel()
    _test_model.id = 1
    _test_model.data = "hoge1"
    session1.add(_test_model)

    got_test_model: Optional[TestModel] = session1.query(TestModel).first()
    assert got_test_model is not None
    assert got_test_model.data == "hoge1"

    # operate "rollback" in another session
    session2.rollback()
    got_test_model: Optional[TestModel] = session2.query(TestModel).first()

    # then result by session1 query is rollbacked
    assert got_test_model is None


if __name__ == "__main__":
    main()
