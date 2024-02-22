import pytest
from app1.models import Category, Product


@pytest.mark.django_db
def test_create_category(create_new_category_fb):
    category = create_new_category_fb
    count = Category.objects.count()
    print(count, category.name)
    assert count == 1


@pytest.mark.django_db
def test_create_product(create_new_product_fb):
    product = create_new_product_fb
    count = Product.objects.count()
    print(count, product.description)
    assert count == 1
