import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class IcrawlerSpider(CrawlSpider):
    name = 'icrawler'

    def __init__(self, *args, **kwargs):
        # We are going to pass these args from our django view.
        # To make everything dynamic, we need to override them inside __init__ method
        self.url = kwargs.get('url')
        self.domain = kwargs.get('domain')
        self.start_urls = [self.url]
        self.allowed_domains = [self.domain]
        IcrawlerSpider.rules = [
           Rule(LinkExtractor(unique=True), callback='parse_item'),
        ]
        super(IcrawlerSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        for r in response.css('a'):
            if(r.css('a::attr(data-articleid)').get()!=None and str(r.css('a::text').get())!='READ FULL STORY' and str(r.css('a::text').get())!='None'):
                url=r'https://www.hindustantimes.com'+r.css('a::attr(href)').get()
                print('url is '+url)
                yield scrapy.Request(url, callback = self.parse_article)

    def parse_article(self,response):
        heading=response.css('h1.hdg1::text').get();
        description=''
        for i in response.css('p::text').getall():
            description+=i+"\n\n"
        url=response.request.url
        print('heading :'+heading)
        yield{
            'heading':heading,
            'description' :description,
            'url' : url
        }
