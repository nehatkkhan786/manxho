# Generated by Django 4.0.4 on 2022-05-21 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_order_status_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]