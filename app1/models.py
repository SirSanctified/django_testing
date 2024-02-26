from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, null=True)
    regular_price = models.DecimalField(
        verbose_name="Regular Price",
        help_text="Maximum 999.99",
        max_digits=5,
        decimal_places=2,
        default=0.0,
    )
    discount_price = models.DecimalField(
        verbose_name="Discount Price",
        help_text="Maximum 999.99",
        max_digits=5,
        decimal_places=2,
        default=0.0,
    )

    def __str__(self):
        return str(self.name)
