import requests
import pytest

@pytest.fixture(scope = "session")
def app_url():
    return "http://pulse-rest-testing.herokuapp.com/"

@pytest.fixture(scope = "session")
def book(app_url):
    response = requests.post(app_url + "books/", data={"title": "AnnaK", "author": "LevT"})
    return response.json()

@pytest.fixture()
def role(book):
    return {"name": "Peppi Longsocks", "type": "orange-hero", "level": 1, "book": book["id"]}

@pytest.fixture()
def init_role(book):
    return {"name": "Mumu", "type": "animal", "level": 1, "book": book["id"]}
