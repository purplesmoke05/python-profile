import os
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

DB_FILE_NAME = "sample_db.sqlite3"

def main():
    engine = create_engine('sqlite:///'+DB_FILE_NAME, echo=True)
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
    got_test_model: Optional[TestModel] = session1.query(TestModel).first()

    # then result by session1 query is not rolled back
    assert got_test_model is not None
    assert got_test_model.data == "hoge1"

    # commit in session1
    session1.commit()

    # Query test model in session2
    _test_model_in_session2 = session2.query(TestModel).first()

    # Update test model in session1
    _test_model = session1.query(TestModel).first()
    _test_model.data = "hoge2"
    session1.merge(_test_model)
    session1.commit()

    # Query test model in session2 but the record found is not latest one.
    _test_model_in_session2 = session2.query(TestModel).first()
    assert _test_model_in_session2 is not None
    assert _test_model_in_session2.data == "hoge1"





if __name__ == "__main__":
    os.remove(DB_FILE_NAME)
    main()

