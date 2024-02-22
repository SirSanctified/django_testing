import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_new_user_from_faker(create_new_user_fb):
    user = create_new_user_fb
    count = User.objects.count()
    print(count, user.username)
    assert True