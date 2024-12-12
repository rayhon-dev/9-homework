from django.shortcuts import render, redirect, get_object_or_404
from .models import Music


def home(request):
    return render(request,'index.html')

def music_list(request):
    music = Music.objects.all()
    ctx = {'music': music }
    return render(request, 'music/music-list.html', ctx)

def music_create(request):
    if request.method == 'POST':
        album_title = request.POST.get('album_title')
        artist = request.POST.get('artist')
        release_year = request.POST.get('release_year')
        genre = request.POST.get('genre')

        if album_title and artist and release_year and genre :
            Music.objects.create(
                album_title=album_title,
                artist=artist,
                release_year=release_year,
                genre=genre
            )

            return redirect('music:list')
    return render(request, 'music/music-form.html')



# def music_detail(request, pk):
#     movie = get_object_or_404(Music, pk=pk)
#     ctx = {'music':music}
#     return render(request, 'music/music-detail.html', ctx)

def music_detail(request, pk):
    music = get_object_or_404(Music, pk=pk)
    ctx = {'music': music}
    return render(request, 'music/music-detail.html', ctx)

def music_delete(request, pk):
    music = get_object_or_404(Music, pk=pk)
    music.delete()
    return redirect('music:list')


def music_update(request, pk):
    music = get_object_or_404(Music, pk=pk)
    if request.method == 'POST':
        album_title = request.POST.get('album_title')
        artist = request.POST.get('artist')
        release_year = request.POST.get('release_year')
        genre = request.POST.get('genre')

        if album_title and artist and release_year and genre:
            music.album_title=album_title
            music.artist=artist
            music.release_year=release_year
            music.genre=genre
            music.save()

            return redirect(music.get_detail_url())
    ctx = {'music': music}
    return render(request, 'music/music-form.html', ctx)

