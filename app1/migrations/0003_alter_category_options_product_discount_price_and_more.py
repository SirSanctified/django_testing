# Generated by Django 5.0.2 on 2024-02-26 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_category_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Maximum 999.99', max_digits=5, verbose_name='Discount Price'),
        ),
        migrations.AddField(
            model_name='product',
            name='regular_price',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Maximum 999.99', max_digits=5, verbose_name='Regular Price'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=255, null=True),
        ),
    ]