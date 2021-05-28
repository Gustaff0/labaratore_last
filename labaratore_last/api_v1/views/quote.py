from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode
from rest_framework import generics
from api_v1.serializers import QuoteSerializer
from webapp.models import Quote
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        print(request.method)
        if view.action == 'partial_update' or view.action == 'destroy':
            return request.user.is_authenticated and request.user.is_superuser
        else :
            return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            if obj.status != 'moder':
                return request.user.is_authenticated and request.user.is_superuser
            else:
                return True
        return True



class QuoteAPI(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = (IsOwnerOrReadOnly,)


    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Quote.objects.filter(status='moder')
        else:
            return Quote.objects.all()










