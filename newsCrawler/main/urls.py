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
    path('ajax/UC_to_NDF',views.uc_to_ndf,name='crawl'),
    path('ajax/UC_to_ML',views.uc_to_ml,name='crawl'),
    path('ajax/UC_to_DEL',views.uc_to_del,name='crawl'),
    path('ajax/DF_to_UC',views.df_to_uc,name='crawl'),
    path('ajax/DF_to_NDF',views.df_to_ndf,name='crawl'),
    path('ajax/DF_to_ML',views.df_to_ml,name='crawl'),
    path('ajax/DF_to_DEL',views.df_to_del,name='crawl'),
    path('ajax/NDF_to_UC',views.ndf_to_uc,name='crawl'),
    path('ajax/NDF_to_DF',views.ndf_to_df,name='crawl'),
    path('ajax/NDF_to_ML',views.df_to_ml,name='crawl'),
    path('ajax/NDF_to_DEL',views.ndf_to_del,name='crawl'),
    path('ajax/ML_to_UC',views.ml_to_uc,name='crawl'),
    path('ajax/ML_to_DF',views.ml_to_df,name='crawl'),
    path('ajax/ML_to_NDF',views.ml_to_ndf,name='crawl'),
    path('ajax/ML_to_DEL',views.ml_to_del,name='crawl'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('defence', views.defence, name='defence'),
    path('nondefence', views.nondefence, name='nondefence'),
    path('unclassified', views.unclassified, name='unclassified'),
    path('ml', views.ml, name='unclassified'),
]
