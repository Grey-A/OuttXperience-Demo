from fastapi import APIRouter, status

from app.book import schemas, selectors, services
from app.common.annotations import DatabaseSession

router = APIRouter()


# This endpoint creates a new book
@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="Create a new book",
    response_description="The created book",
    response_model=schemas.Book,
)
def books_create(book: schemas.BookCreate, db: DatabaseSession):
    """This endpoint creates a new book"""
    return services.create_book(data=book, db=db)


@router.get(
    "/{book_id}",
    status_code=status.HTTP_200_OK,
    summary="Get book details",
    response_description="The book's details",
    response_model=schemas.Book,
)
def books_detail(book_id: int, db: DatabaseSession):
    """This endpoint gets the book details"""
    return selectors.get_book_by_id(book_id=book_id, db=db)


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    summary="Get book list",
    response_description="The list of books",
    response_model=list[schemas.Book],
)
def books_list(db: DatabaseSession):
    """This endpoint gets the list of books"""
    return selectors.get_books_list(db=db)


@router.put(
    "/{book_id}",
    status_code=status.HTTP_200_OK,
    summary="Update a book",
    response_description="The updated book",
    response_model=schemas.Book,
)
def books_update(book_id: int, data: schemas.BookEdit, db: DatabaseSession):
    """This endpoint updates a book"""
    book = selectors.get_book_by_id(book_id=book_id, db=db)
    for field, value in data.model_dump(exclude_none=True, exclude_unset=True).items():
        setattr(book, field, value)
    db.commit()
    db.refresh(book)
    return book


@router.delete(
    "/{book_id}",
    status_code=status.HTTP_200_OK,
    summary="Delete a book",
    response_description="The book was deleted",
)
def books_delete(book_id: int, db: DatabaseSession):
    """This endpoint deletes a book"""
    book = selectors.get_book_by_id(book_id=book_id, db=db)
    db.delete(book)
    db.commit()
    return {"detail": "Book deleted successfully"}
