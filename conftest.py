import requests
import pytest
# one fixture for 2 tests
@pytest.fixture(scope = "session")
def app_url():
    return "http://pulse-rest-testing.herokuapp.com/"

@pytest.fixture(scope = "session")
def book(app_url):
    response = requests.post(app_url + "books/", data={"title": "Anna2", "author": "Lev2"})
    return response.json()
    # yield book  # additional deleting 3 strings
    # r = requests.delete(app_url + "books/{}/".format(book["id"]))

@pytest.fixture()
def role(book):
    return {"name": "Peppi Longsocks", "type": "orange-hero", "level": 1, "book": book["id"]}
