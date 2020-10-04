from db import DB
from unittest.mock import Mock



@pytest.fixture()
def mock_db():
    db = Mock()
    db.count.return_value = 1
    db.list_tables.return_value = ("users",)
    db.get.return_value = {
        "username": "asdasd",
        "first_name": "asd",
        "last_name": "asdasd",
        "email": "aaaaa@gmail.com",
    }
    return db


def test_count(mock_db):



def test_list_tables(mock_db):



def test_get(mock_db):
