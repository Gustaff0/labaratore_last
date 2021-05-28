from django.db import models
# Create your models here.
choices = [('new', 'New'), ('moder', 'Moder')]
from django.contrib.auth import get_user_model

class QuoteRating(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='user', on_delete=models.CASCADE, verbose_name='Пользователь')
    quote = models.ForeignKey('webapp.Quote', on_delete=models.CASCADE, related_name='quote', verbose_name='Цитата')

class Quote(models.Model):
    text = models.CharField(max_length=3000, null=False, blank=False)
    name = models.CharField(max_length=300, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    rating = models.ManyToManyField(get_user_model(), related_name='rating', through='webapp.QuoteRating' )
    status = models.CharField(max_length=300, null=False, blank=False, choices=choices, default='new')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Quote'
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'

    def __str__(self):
        return f"{self.name} - {self.date} : {self.rating}"