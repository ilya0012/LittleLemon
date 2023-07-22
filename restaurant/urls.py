from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleItemView.as_view(), name='single menu item'),
    path('api-token-auth/', obtain_auth_token)
]