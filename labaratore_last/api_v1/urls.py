from django.urls import include, path
from rest_framework import routers
from api_v1 import views
from rest_framework.authtoken.views import obtain_auth_token
from api_v1.views import RatingAdd, RatingDelete


router = routers.DefaultRouter()
router.register('quote', views.QuoteAPI)

app_name = 'api_v1'


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('rating_add/<int:pk>', RatingAdd.as_view(), name='rating_add'),
    path('rating_delete<int:pk>', RatingDelete.as_view(), name='rating_delete')
]