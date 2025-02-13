import pytest

from masogram.utils.auth_widget import check_integrity

TOKEN = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"


@pytest.fixture
def data():
    return {
        "id": "42",
        "first_name": "John",
        "last_name": "Smith",
        "username": "username",
        "photo_url": "https://t.me/i/userpic/320/picname.jpg",
        "auth_date": "1565810688",
        "hash": "c303db2b5a06fe41d23a9b14f7c545cfc11dcc7473c07c9c5034ae60062461ce",
    }


class TestCheckIntegrity:
    def test_ok(self, data):
        assert check_integrity(TOKEN, data) is True

    def test_fail(self, data):
        data.pop("username")
        assert check_integrity(TOKEN, data) is False
