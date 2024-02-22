import pytest

# Fixtures
# function  runs ones per test
# class     runs once per class of tests
# module    runs once per module
# session   runs once per session

@pytest.fixture
def fixture_1():
    return 2

def test_with_fixture(fixture_1):
    num = fixture_1
    assert num == 2