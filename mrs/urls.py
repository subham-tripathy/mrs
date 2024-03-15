from django.urls import path
from mrs import views
from services import views as servicesViews

urlpatterns = [
    path('', views.index, name='home'),
    path('movies/', views.movies, name='movies'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('movies/result.html', views.test, name='test'),
    path('movies/getMovie.html', views.getMovie, name='getMovie'),
    path('movies/comment.html', views.comment, name='comment'),
    path('signup/', servicesViews.signup, name='signup'),
    path('login/', servicesViews.user_login, name='login'),
    path('logout/', servicesViews.logout, name='logout')
]
