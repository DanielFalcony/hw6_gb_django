from django.urls import path
from seminar3_app import views

app_name = 'seminar3_app'

urlpatterns = [
    path('', views.index, name='base.html'),
    path('heads_game/<int:count>', views.HeadsGame.as_view(), name='heads_game'),
    path('dice_game/<int:count>', views.DiceGame.as_view(), name='dice_game'),
]
