from django.db import models
from django.db.models import Manager


class GameModel(models.Model):
    result = models.CharField(max_length=10)
    played = models.DateTimeField(auto_now_add=True)

    object = Manager()

    def __str__(self):
        return f'Результат броска: {self.result}, Время броска: {self.played}'

    class Meta:
        ordering = ['-played']

    @staticmethod
    def return_last(n):
        return GameModel.object.all()[:n]


class Authors(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField(max_length=1000)
    birthday = models.DateField()

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=200)
    post_text = models.TextField(max_length=1000)
    post_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    views = models.IntegerField(default=0)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.author} - {self.title} - {self.publish} - {self.post_date}'
