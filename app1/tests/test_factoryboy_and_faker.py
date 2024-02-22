import pytest

def test_new_user_from_faker(user_factory):
    print(user_factory.username)
    assert True