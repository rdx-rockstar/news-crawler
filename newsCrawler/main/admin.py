from django.contrib import admin

# Register your models here.
from.models import article,defenceArticle,nonDefenceArticle,mlArticle

# Register your models here.
admin.site.register(article)
admin.site.register(defenceArticle)
admin.site.register(nonDefenceArticle)
admin.site.register(mlArticle)