# Generated by Django 4.2.5 on 2023-09-09 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_album_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(default='none.jpeg', upload_to='albums/'),
        ),
    ]
