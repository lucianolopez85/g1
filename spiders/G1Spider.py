import scrapy


class G1spiderSpider(scrapy.Spider):
    name = 'G1Spider'
    allowed_domains = ['g1.globo.com']
    start_urls = ['https://g1.globo.com/economia/tecnologia/']

    def parse(self, response):
        news_list = response.css('.bastian-page .bastian-feed-item')
        
        for news in news_list:
            title = news.css('.feed-post-link::text').extract_first() # recebe apenas o texto do título
            description = news.css('.feed-post-body-resumo::text').extract_first() # recebe o texto da descrição
            image_url = news.css('.bstn-fd-picture-image::attr(src)').extract_first() # recebe o atributo do alemento src
            print({'title': title, 'description': description, 'image_url': image_url})
            exit()


    # def parse(self, response):
    #     new_list = response.css('.bastian-page .bastian-feed-item') # recebe toda a lista
    #     print(new_list)
    
    # def parse(self, response):
    #     page_title = response.css('title::text').extract_first()# recebe o conteúdo da pagina(o primeiro título)
    #     print(page_title)
