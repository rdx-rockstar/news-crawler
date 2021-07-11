from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clear', views.clear,name='clear'),
    path('ajax/load', views.loadArticles,name='reload'),
    path('ajax/status', views.status,name='crawl'),
    path('ajax/crawl', views.fetchArticles,name='crawl'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('defence', views.defence, name='defence'),
    path('nondefence', views.nondefence, name='nondefence'),
    path('unclassified', views.unclassified, name='unclassified'),
]