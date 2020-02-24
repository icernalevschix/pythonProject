import scrapy
from data_scraper.items import PostItem
from django.contrib.auth.models import User

class JobsSpider(scrapy.Spider):
    name = 'jobs'

    def start_requests(self):
        url = 'https://www.rabota.md/ro/vacancies/category/it'

        yield scrapy.Request(url=url, callback=self.parse)

    def parse_content(self, response, title, sallary):
        item = PostItem()
        item['author'] = User(id=1)
        item['sallary'] = sallary
        item['title'] = title
        item['content'] = ' '.join(response.xpath("//*[contains(@class, 'preview')]/div[4]/text()").getall()).strip().replace('\r\n', '')
        
        yield item

    def parse(self, response):
        base_url = 'https://www.rabota.md'

        for job in response.css('.vacancy-block'):
            title = job.css('.vacancy-block__name::text').get()
            sallary  =job.css('.vacancy-block__salary::text').get().strip()

            next_page = job.css('.vacancy-block__heading a::attr(href)').getall()[1]
            request = scrapy.Request(base_url + next_page,
                            callback=self.parse_content)
            request.cb_kwargs['title'] = title
            request.cb_kwargs['sallary'] = sallary
            yield request
        
        next_page = response.xpath("//*[contains(@class, 'active')]/following-sibling::a/@href").get()
        
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)