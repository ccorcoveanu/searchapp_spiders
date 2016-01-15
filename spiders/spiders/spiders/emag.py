from scrapy.spiders import Spider
import re

from spiders.items import EmagItem

class EmagSpider(Spider):

	name            = 'emag'
	allowed_domains = 'emag.ro'
	filename        = 'emag.txt'

	start_urls = [
		'http://www.emag.ro/scaun-sitness-chief-200-textil-scaun-executiv-tapitat-cu-stofa-din-poliester-crem-0982/pd/DXTNVMBBM/?ref=hp_prod_widget_live_1_2&utm_source=receng_hp_prod_widget_live_1_v1&utm_medium=site&utm_content=recent_buy_std&utm_campaign=wd_ce_se_cumpara_acum_emag_hp'
	]

	def parse(self, response):
		self.cssSelectorParse(response)

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