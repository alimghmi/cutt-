from django.urls import path, include

from .views import (
    IndexPage, 
    RedirectPage, 
    CreateShortenURLAPI,
    DeleteShortenURLAPI
)

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('api/create', CreateShortenURLAPI.as_view(), name='create_shorturl'),
    path('api/delete', DeleteShortenURLAPI.as_view(), name='delete_shorturl'),
    # path('api/all', ShortenURLAPI.as_view(), name='redirect'),
    # path('api/update', ShortenURLAPI.as_view(), name='redirect'),
    path('<str:slug>', RedirectPage.as_view(), name='redirect'),
]