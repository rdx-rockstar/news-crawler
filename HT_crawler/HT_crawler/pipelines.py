# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from main.models import article

class HtCrawlerPipeline:
    def process_item(self, item, spider):
        if(item.get('heading')!=None and (not article.objects.filter(heading=item.get('heading')).exists())):
            # print("saving new article\n\n\n\n.")
            newArticle= article(heading=item.get('heading'),description=item.get('description'),url=item.get('url'))
            newArticle.save()
        return item
        