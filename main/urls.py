from django.urls import path
from . import views as mainViews

urlpatterns = [
    path('', mainViews.home, name='home'),
    path('contacts/', mainViews.contacts, name='contacts'),
    path('urlsadd/', mainViews.UrlsAdd.as_view(), name='urlsadd'),
]