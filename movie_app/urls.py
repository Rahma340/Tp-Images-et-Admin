from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movie/add/', views.movie_create, name='add_movie'),
    path('movie/<int:pk>/edit/', views.movie_update, name='update_movie'),
]
