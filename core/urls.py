from django.urls import path, include

from .views import IndexPage, RedirectPage
urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('<str:slug>', RedirectPage.as_view(), name='redirect'),
]