# Generated by Django 4.2.5 on 2023-09-09 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_product_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(default='none.jpeg', upload_to=''),
        ),
    ]
