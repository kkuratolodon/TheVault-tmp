from django.contrib import admin

from .models import Album

# Register your models here.
admin.site.register(Album)

from django.contrib.auth.models import User

username = 'admin';
password = 'rafliwibu';
email = 'tes@gmail.com';

if User.objects.filter(username=username).count()==0:
    User.objects.create_superuser(username, email, password);
    print('Superuser created.');
else:
    print('Superuser creation skipped.')