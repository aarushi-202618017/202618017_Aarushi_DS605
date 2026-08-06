import scrapy

class BookSpider(scrapy.Spider):
    name = "books"
    start_urls = ['https://books.toscrape.com/catalogue/page-1.html']
    page_count = 1

    def parse(self, response):
        book_links = response.css('h3 a::attr(href)').getall()
        for link in book_links:
            yield response.follow(link, callback=self.parse_book)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page and self.page_count < 7:
            self.page_count += 1
            yield response.follow(next_page, callback=self.parse)

    def parse_book(self, response):
        def get_table_row(name):
            return response.xpath(f"//th[text()='{name}']/following-sibling::td/text()").get(default='').strip()

        yield {
            'title': response.css('div.product_main h1::text').get(default='').strip(),
            'category': response.xpath('//ul[@class="breadcrumb"]/li[3]/a/text()').get(default='').strip(),
            'price': response.css('p.price_color::text').get(default='').strip(),
            'rating': response.css('p.star-rating::attr(class)').get(default='').replace('star-rating', '').strip(),
            'availability': get_table_row('Availability'),
            'product_description': response.xpath('//div[@id="product_description"]/following-sibling::p/text()').get(default=''),
            'UPC': get_table_row('UPC'),
            'number_of_reviews': get_table_row('Number of reviews'),
            'product_url': response.url
        }
