from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clear', views.clear,name='clear'),
    path('clearDefence', views.clearDefence,name='clear'),
    path('clearNonDefence', views.clearNonDefence,name='clear'),
    path('clearML', views.clearML,name='clear'),
    path('ajax/status', views.status,name='crawl'),
    path('ajax/crawl', views.fetchArticles,name='crawl'),
    path('ajax/UC_to_DF', views.uc_to_df,name='crawl'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('defence', views.defence, name='defence'),
    path('nondefence', views.nondefence, name='nondefence'),
    path('unclassified', views.unclassified, name='unclassified'),
    path('ml', views.ml, name='unclassified'),
]