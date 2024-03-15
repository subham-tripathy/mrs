from django.shortcuts import render
from django.http import HttpResponse
from recommend import recommend, getMovieDetails
from sentiment import get_sentence_score
from services.models import comments

def test(request):
    movieName = request.GET.get('movieName')
    if movieName:
        data = recommend(movieName)
        return render(request, 'movies/result.html', {'data': data})

def getMovie(request):
    movieName = request.GET.get('movieName')
    if movieName:
        data = getMovieDetails(movieName)
        commentData = comments.objects.filter(film=movieName)
        return render(request, 'movies/getMovie.html', {'data': data, 'commentData':commentData})

def comment(request):
    if request.COOKIES.get('mrsUser'):
        username = request.COOKIES.get('mrsUser')[:]
        commentData = request.POST.get('comment')[:]
        film = request.POST.get('movieName')[:]
        commentRating = int(get_sentence_score(request.POST.get('comment')))
        data = {
            'username': username,
            'commentData': commentData,
            'film': film,
            'commentRating': commentRating
        }
        commentModel = comments.objects.create(user=username, film=film,comment=commentData, rating=commentRating)
        commentModel.save()
        return render(request, 'movies/comment.html', {'data': data})
    else:
        return render(request, 'movies/comment.html', {'msg': 'notloggedin'})


def index(request):
    if request.COOKIES.get('mrsUser'):
        return render(request, 'home/index.html', {'username': request.COOKIES.get('mrsUser')})
    else:
        return render(request, 'home/index.html', {'login': 'Login'})

def about(request):
    return render(request, 'about/index.html')

def movies(request):
    if request.COOKIES.get('mrsUser'):
        return render(request, 'movies/index.html')
    else:
        return render(request, 'movies/index.html', {'msg': 'notloggedin'})
        

def contact(request):
    return render(request, 'contact/index.html')
