from random import randint
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView


def index(request):
    return HttpResponse('Home page')


class GameView(TemplateView):
    template_name = 'seminar3_app/game.html'


class HeadsGame(GameView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = [('TAILS', 'HEADS')[randint(0, 1)] for i in range(int(self.kwargs['count']))]
        context['results'] = results
        context['title'] = 'Игра Орел или Решка'
        return context


class DiceGame(GameView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = [randint(0, 6) for i in range(int(self.kwargs['count']))]
        context['results'] = results
        context['title'] = 'Игра в кости'
        return context
