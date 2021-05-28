from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode
from rest_framework import generics
from api_v1.serializers import QuoteSerializer
from webapp.models import Quote
from rest_framework import viewsets
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    View
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, BasePermission

class RatingAdd(View):
    def get(self, request, *args, **kwargs):
        quote = get_object_or_404(Quote, pk=kwargs.get('pk'))
        user = self.request.user
        if user in quote.rating.all():
            raise ValueError("Рейтинг Уже был поставлен")
        else :
            quote.rating.add(user)
            quote.save()
        return JsonResponse({"data": "www"})


class RatingDelete(View):
    def get(self, request, *args, **kwargs):
        quote = get_object_or_404(Quote, pk=kwargs.get('pk'))
        user = self.request.user
        quote.rating.remove(user)
        quote.save()
        return JsonResponse({"data": "www"})