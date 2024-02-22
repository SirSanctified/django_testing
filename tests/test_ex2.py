import pytest

# Fixtures
# function  runs ones per test
# class     runs once per class of tests
# module    runs once per module
# session   runs once per session

@pytest.fixture(scope="session")
def fixture_1():
    print("run fixture 1")
    return 2

def test_with_fixture(fixture_1):
    print("run test example 1")
    num = fixture_1
    assert num == 2


def test_with_fixture2(fixture_1):
    print("run test example 2")
    num = fixture_1
    assert num == 2
