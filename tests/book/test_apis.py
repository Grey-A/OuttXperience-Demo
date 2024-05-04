from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.config.database import DBBase
from app.common.dependencies import get_db

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


DBBase.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


# Test case for creating a new book
def test_create_book():
    book_data = {
        "title": "Test Title",
        "author": "Test Author",
        "year": 1995,
        "isbn": "testisbn12345",
    }
    response = client.post("/books", json=book_data)
    assert response.status_code == 201
    assert response.json()["title"] == "Test Title"
    assert response.json()["author"] == "Test Author"


# Test case for getting book details
def test_get_book_detail():
    response = client.get("/books/1")
    assert response.status_code == 200


# Test case for getting the list of books
def test_get_books_list():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test case for updating a book
def test_update_book():
    update_data = {"title": "Updated Title"}
    response = client.put("/books/1", json=update_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"


# Test case for deleting a book
def test_delete_book():
    response = client.delete("/books/1")
    assert response.status_code == 200
    assert response.json()["detail"] == "Book deleted successfully"
