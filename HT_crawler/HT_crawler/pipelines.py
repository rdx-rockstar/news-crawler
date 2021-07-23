# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import date
from main.models import article,unclassiedArticle,defenceArticle,nonDefenceArticle,AIdefenceArticle,AInonDefenceArticle

class HtCrawlerPipeline:
    def process_item(self, item, spider):
        heading=item.get('heading')
        if(heading==None):
            return item;
        heading=heading.strip()
        if(heading!='' and not(article.objects.filter(heading=heading).exists() or defenceArticle.objects.filter(heading=heading).exists() or nonDefenceArticle.objects.filter(heading=heading).exists()  or unclassiedArticle.objects.filter(heading=heading).exists() or AIdefenceArticle.objects.filter(heading=heading).exists() or AInonDefenceArticle.objects.filter(heading=heading).exists())):
            newArticle= article(heading=item.get('heading'),description=item.get('description'),url=item.get('url'),date=date.today().strftime("%d/%m/%Y"))
            newArticle.save()
        return item
        