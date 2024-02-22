import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_user_create():
    User.objects.create_user("test", "test@test.com", "test_user")
    assert User.objects.count() == 1

@pytest.mark.django_db
def test_set_check_password(user_1):
    user_1.set_password("new user")
    assert user_1.check_password("new user") is True

def test_new_user(new_user):
    print(new_user.first_name)
    assert new_user.first_name == "MyName"

def test_new_Staff_user(new_staff_user):
    print(new_staff_user.first_name, new_staff_user.is_staff)
    assert new_staff_user.first_name == "MyName" and new_staff_user.is_staff is True