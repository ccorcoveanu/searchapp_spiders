from scrapy.spiders import Spider
import re

from spiders.items import EmagItem

class EmagSpider(Spider):

	name            = 'emag'
	allowed_domains = 'emag.ro'
	filename        = 'emag.txt'

	start_urls = [
		'http://www.emag.ro/all-departments?ref=hdr_mm_14'
	]

	def parse(self, response):
		for item in response.xpath('//div[@id="department-expanded"]/ul/li/ul/li/a/@href'):
			print item.extract()

	def cssSelectorParse(self, response):
		item = EmagItem()
		item['title'] = response.xpath('//div[@id="offer-title"]/h1/text()').extract_first()
		item['brand'] = response.xpath('//div[@id="box-specificatii-produs"]/div[@class="brand"]/a/text()').extract_first()
		item['price'] = response.xpath('//div[@id="offer-price-stock"]/div[@class="prices"]/span[@class="money-int"]/text()').extract_first()
		

	def regexpParse(self, response):
		header   = response.xpath('//head/script[re:test(text(), "ecommerce")]/text()')
		header   = header.extract()
		with open(filename, 'wb') as f:
			for text in header:
				f.write(text.encode('utf-8'))

	def testParse(self, response):
		for item in response.xpath('//div[@id="department-expanded"]/ul/li/ul/li/a/@href'):
			print item.extract()