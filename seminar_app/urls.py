from django.urls import path
from seminar_app import views

app_name = 'seminar_app'

urlpatterns = [
    path('', views.index, name='index.html'),
    path('game/', views.game, name='game'),
    path('last_game/', views.last_game, name='last_game'),
    path('authors/', views.author, name='authors'),
    path('post/', views.post, name='posts')
]
