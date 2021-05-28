from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import register_view
app_name = 'accounts'

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/reg/', register_view, name='registration')
]