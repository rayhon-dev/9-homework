from django.urls import path
from . import views


app_name = 'sports'


urlpatterns =[
    path('list/', views.sport_list, name='list'),
    path('create/', views.sport_create, name='create'),
    path('detail/<int:pk>/', views.sport_detail, name='detail'),
    path('delete/<int:pk>/', views.sport_delete, name='delete'),
    path('update/<int:pk>/', views.sport_update, name='update'),
]