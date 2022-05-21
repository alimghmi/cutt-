from django.urls import path, include

from .views import (
    IndexPage, 
    RedirectPage, 
    CreateShortenURLAPI,
    DeleteShortenURLAPI,
    StatsShortenURLAPI
)

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('api/create', CreateShortenURLAPI.as_view(), name='create_shorturl'),
    path('api/delete', DeleteShortenURLAPI.as_view(), name='delete_shorturl'),
    path('api/stats', StatsShortenURLAPI.as_view(), name='stats_shorturl'),
    # path('api/update', ShortenURLAPI.as_view(), name='redirect'),
    path('<str:slug>', RedirectPage.as_view(), name='redirect'),
]