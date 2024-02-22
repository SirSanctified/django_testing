import pytest
from django.contrib.auth.models import User
from pytest_factoryboy import register
from .factories import UserFactory


register(UserFactory)

@pytest.fixture
def user_1(db):
    user = User.objects.create_user("test_user")
    return user

@pytest.fixture
def create_user_factory(db):
    def create_app_user(
            username: str,
            password: str = None,
            first_name: str = "firstname",
            last_name: str = "lastname",
            email: str = "test@test.com",
            is_staff: bool = False,
            is_superuser: bool = False,
            is_active: bool = True
    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active
            )
        return user
    return create_app_user

@pytest.fixture
def new_user(db, create_user_factory):
    return create_user_factory("Test_User", "password", "MyName")

@pytest.fixture
def new_staff_user(db, create_user_factory):
    return create_user_factory("Test_User", "password", "MyName", is_staff=True)