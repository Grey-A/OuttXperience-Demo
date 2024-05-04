from datetime import datetime
from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    title: str = Field(
        description="The title of the book", min_length=1, max_length=255
    )
    author: str = Field(
        description="The author of the book", min_length=1, max_length=255
    )
    year: int = Field(
        description="The year the book was published", ge=1900, le=datetime.now().year
    )
    isbn: str = Field(description="The ISBN of the book", min_length=13, max_length=13)


class BookEdit(BaseModel):
    title: str | None = Field(
        description="The title of the book", min_length=1, max_length=255, default=None
    )
    author: str | None = Field(
        description="The author of the book", min_length=1, max_length=255, default=None
    )
    year: int | None = Field(
        description="The year the book was published",
        ge=1900,
        le=datetime.now().year,
        default=None,
    )
    isbn: str | None = Field(
        description="The ISBN of the book", min_length=13, max_length=13, default=None
    )


class Book(BaseModel):
    id: int = Field(description="The ID of the book")
    title: str = Field(description="The title of the book")
    author: str = Field(description="The author of the book")
    year: int = Field(description="The year the book was published")
    isbn: str = Field(description="The ISBN of the book")
