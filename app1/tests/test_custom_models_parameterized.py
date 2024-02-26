import pytest
from app1.models import Product


@pytest.mark.parametrize(
    "title, description, slug, regular_price, discount_price, validity",
    [
        ("Product1", "Description1", "product_1", 100.00, 90.00, True),
        ("Product2", "Description2", "product_2", 200.00, 180.00, True),
        ("Product4", "Description4", "product_4", 400.00, 360.00, True),
    ],
)
def test_product(
    db,
    product_factory,
    title,
    description,
    slug,
    regular_price,
    discount_price,
    validity,
):
    product = product_factory.create(
        name=title,
        # category=category,
        description=description,
        slug=slug,
        regular_price=regular_price,
        discount_price=discount_price,
    )
    item = Product.objects.all().count()
    assert item == validity
