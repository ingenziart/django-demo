from django.shortcuts import render
from .models import movie

data = movie.objects.all()


def movies(request):
    return render(request, "movies/movies.html", {"name": data})
