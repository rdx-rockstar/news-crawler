import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class IcrawlerSpider2(CrawlSpider):
    name = 'icrawler2'
    def __init__(self, *args, **kwargs):
        self.url = kwargs.get('url')
        self.domain = kwargs.get('domain')
        # print("init2 ------------------------"+self.url+" "+self.domain)
        self.start_urls = [self.url]
        self.allowed_domains = [self.domain]
        self.handle_httpstatus_list = [403]
        IcrawlerSpider2.rules = [
           Rule(LinkExtractor(unique=True), callback=self.parse_item),
        ]
        super(IcrawlerSpider2, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        print("got response 2 ------------------------")
        for url in response.css('div.story-card a::attr(href)').getall():
            # print('url is '+url)
            yield scrapy.Request(url, callback = self.parse_article)

    def parse_article(self,response):
        print("got article ------------------------")
        heading=response.css('h1.title::text').get()  
        description=response.css('h2.intro::text').get();
        for i in response.css('div p::text').getall():
            description+=i+"\n\n"
        url=response.request.url
        print('heading :'+heading)
        yield{
            'heading':heading,
            'description' :description,
            'url' : url
        }
