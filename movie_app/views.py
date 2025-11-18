from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm

def movie_list(request):
    movies = Movie.objects.all()

    # Récupérer la recherche par titre
    search_query = request.GET.get('search', '')
    if search_query:
        movies = movies.filter(title__icontains=search_query)

    # Récupérer la case "nouveaux films"
    show_new = request.GET.get('new') == '1'
    if show_new:
        movies = movies.filter(is_new=True)

    context = {
        'movies': movies,
        'search_query': search_query,
        'show_new': show_new,
    }
    return render(request, 'movie_list.html', context)
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie_detail.html', {'movie': movie})
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    
    return render(request, 'movie_form.html', {'form': form})
def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)

    return render(request, 'movie_form.html', {'form': form})
