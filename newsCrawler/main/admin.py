from django.contrib import admin

# Register your models here.
from.models import article,defenceArticle,nonDefenceArticle,AIdefenceArticle,AInonDefenceArticle,unclassiedArticle

# Register your models here.
admin.site.register(article)
admin.site.register(defenceArticle)
admin.site.register(nonDefenceArticle)
admin.site.register(AIdefenceArticle)
admin.site.register(AInonDefenceArticle)
admin.site.register(unclassiedArticle)