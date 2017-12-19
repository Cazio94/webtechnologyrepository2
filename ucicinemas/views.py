from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all().order_by('title')
    return render(request, 'ucicinemas/index.html', {'movies': movies})
