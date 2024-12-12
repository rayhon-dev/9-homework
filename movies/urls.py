from django.urls import path
from . import views


app_name = 'movies'


urlpatterns =[
    path('list/', views.movie_list, name='list'),
    path('create/', views.movie_create, name='create'),
    path('detail/<int:pk>/', views.movie_detail, name='detail'),
    path('delete/<int:pk>/', views.movie_delete, name='delete'),
    path('update/<int:pk>/', views.movie_update, name='update'),
]