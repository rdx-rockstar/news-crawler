from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clearUnclassified', views.clearUnclassified,name='clear'),
    path('clearDefence', views.clearDefence,name='clear'),
    path('clearNonDefence', views.clearNonDefence,name='clear'),
    path('clearAIDefence', views.clearAIDefence,name='clear'),
    path('clearAINonDefence', views.clearAINonDefence,name='clear'),
    path('ajax/status', views.status,name='crawl'),
    path('ajax/crawl', views.fetchArticles,name='crawl'),
    path('ajax/UC_to_DF', views.uc_to_df,name='crawl'),
    path('ajax/UC_to_NDF',views.uc_to_ndf,name='crawl'),
    path('ajax/UC_to_DEL',views.uc_to_del,name='crawl'),
    path('ajax/DF_to_UC',views.df_to_uc,name='crawl'),
    path('ajax/DF_to_NDF',views.df_to_ndf,name='crawl'),
    path('ajax/DF_to_DEL',views.df_to_del,name='crawl'),
    path('ajax/NDF_to_UC',views.ndf_to_uc,name='crawl'),
    path('ajax/NDF_to_DF',views.ndf_to_df,name='crawl'),
    path('ajax/NDF_to_DEL',views.ndf_to_del,name='crawl'),
    path('ajax/AI_DF_to_NDF',views.ai_df_to_ndf,name='crawl'),
    path('ajax/AI_DF_to_DEL',views.ai_df_to_del,name='crawl'),
    path('ajax/AI_NDF_to_DF',views.ai_ndf_to_df,name='crawl'),
    path('ajax/AI_NDF_to_DEL',views.ai_ndf_to_del,name='crawl'),
    path('ajax/manual',views.manual,name='crawl'),
    path('ajax/AI',views.AI,name='crawl'),
    path('AIdefence', views.AIdefence, name='defence'),
    path('AInondefence', views.AInondefence, name='nondefence'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('defence', views.defence, name='defence'),
    path('nondefence', views.nondefence, name='nondefence'),
    path('unclassified', views.unclassified, name='unclassified'),
]
