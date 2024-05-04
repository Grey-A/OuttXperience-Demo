from sqlalchemy.orm import Session

from app.book import models, schemas


def create_book(data: schemas.BookCreate, db: Session):
    """This function creates a new book entry in the db

    Args:
        data (schemas.BookCreate): The book's data
        db (Session): The database session

    Returns:
        models.Book: The created book obj
    """
    obj = models.Book(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
