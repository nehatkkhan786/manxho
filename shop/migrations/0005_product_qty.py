# Generated by Django 4.0.4 on 2022-05-20 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_category_alter_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]