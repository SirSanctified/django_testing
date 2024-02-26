import factory
from django.contrib.auth.models import User
from faker import Faker
from app1.models import Category, Product

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    is_staff = False


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "django"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = "product_title"
    description = fake.text()
    category = factory.SubFactory(CategoryFactory)
    regular_price = 100
    discount_price = 50
