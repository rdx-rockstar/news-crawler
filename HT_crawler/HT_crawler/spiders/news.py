import scrapy

class QuotesSpider(scrapy.Spider):
    name = "news"
    def start_requests(self):
        urls = [
            'https://www.hindustantimes.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = f'res.txt'
        with open(filename, 'w') as f:
            for r in response.css('a'):
                if(r.css('a::attr(data-articleid)').get()!=None and r.css('a.dap-readmore').get()=='None'):
                    f.write(str(r.css('a::text').get()))
                    yield {
                        'title':str(r.css('a::text').get()),
                        'link':str(r.css('a::attr(href').get())
                    }
        self.log(f'Saved file {filename}')