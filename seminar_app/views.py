from random import randint

from django.http import HttpResponse
from django.shortcuts import render

from seminar_app.models import GameModel, Authors, Post


def index(request):
    return HttpResponse(f'You on the start! <br>'
                        f'We have next indexes: <br>'
                        f'/game/<br> - Орел или решка'
                        f'/last_game/<br> - Результаты последних игр'
                        f'/author/<br> - Авторы статей'
                        f'/post/<br> - Посты Авторов'
                        )


def game(request):
    result = ('TAILS', 'HEADS')[randint(0, 1)]

    game = GameModel(result=result)
    game.save()

    return HttpResponse(f'{game}')


def last_game(request):
    last = GameModel().return_last(5)
    last_str = ['<br>' + str(result) for result in last]
    return HttpResponse(last_str)


def author(request):
    res = Authors.objects.all()
    result = [str(i) + '<br>' for i in res]
    return HttpResponse(result)


def post(request):
    res = Post.objects.all()
    result = [str(i) + '<br>' for i in res]
    return HttpResponse(result)
