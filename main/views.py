from django.shortcuts import render

from .models import Album


# Create your views here.
def show_main(request):
    albums = Album.objects.all()
    return render(request, "main.html", {'albums' : albums, 'nama_aplikasi' : 'The Vault', 'nama' : 'Muhammad Irfan Firmansyah', 'kelas' : 'PBP - B'})