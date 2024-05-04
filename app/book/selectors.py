from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from app.book import models


def get_book_by_id(book_id: int, db: Session):
    """This function gets the book by its id

    Args:
        book_id (int): The book's id
        db (Session): The database session

    Raises:
        HTTPException[404]: Book not found

    Returns:
        models.Book: The book obj
    """
    if obj := db.query(models.Book).filter_by(id=book_id).first():
        return obj
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with id {book_id} not found",
    )


def get_books_list(db: Session):
    """This function gets the list of books

    Args:
        db (Session): The database session

    Returns:
        list[models.Book]: The list of books
    """
    return db.query(models.Book).all()
