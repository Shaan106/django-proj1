from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render


#importing database model
from .models import Movie

#each function is a view, and takes a "request" and gives an http response

def movies(request):
    #data refers to all movie object retrieved.
    #data being retrieved from database created
    data = Movie.objects.all()
    #data has to be given in a dictionary, also key of dictionary has to be the name used to refer to the data in the html.
    return render(request, 'movies/movies.html', {'movies': data})

def home(request):
    return HttpResponse("Home page")

#remember to create path too when creating a view
def detail(request, id):
    #getting the specific movie attached to the id shown in the url
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data})

def add(request):
    #getting data submitted in form via POST
    title = request.POST.get('title')
    year = request.POST.get('year')

    #if data has been submitted, add it to database
    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        #redirects to movie list after a movie is added
        return HttpResponseRedirect('/movies')

    return render(request, 'movies/add.html')

def delete(request, id):
    try: 
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404('Movie does not exist')

    movie.delete()
    return HttpResponseRedirect('/movies')