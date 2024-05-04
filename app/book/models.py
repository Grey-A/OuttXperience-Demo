from sqlalchemy import Column, Integer, String
from app.config.database import DBBase


class Book(DBBase):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    isbn = Column(String(13), nullable=False)
