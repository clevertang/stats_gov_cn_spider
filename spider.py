# encoding: utf-8
"""
@version: python2.7
@author: ‘xin.tang‘
@license: Apache Licence 
@software: PyCharm
@file: spider.py
@time: 2019/1/11 6:08 PM
"""

import requests
from lxml import etree

from data_saver import MyDataSaver
from settings import INDEX_URL, HOST


class MySpider:
	def __init__(self):
		self.session = requests.session()
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
		}
		self.session.headers = self.headers
		self.datasaver=MyDataSaver()

	def get_province(self):
		'''省级'''
		resp = self.session.get(INDEX_URL)
		html = etree.HTML(resp.content)
		sub_url = html.xpath("//tr[@class='provincetr']//a/@href")
		for url in sub_url:
			city_url = HOST + url
			self.get_city(city_url)

	def get_city(self, url):
		'''地级'''
		resp = self.session.get(url)
		html = etree.HTML(resp.content)
		countys = html.xpath("//tr[@class='citytr']")
		for county in countys:
			code = county.xpath("td[1]//text()")
			name = county.xpath("td[2]//text()")
			url = HOST + county.xpath("td[1]//a/@href")[0]
			self.datasaver.save_data(code=code, name=name)
			self.get_county(url)


	def get_county(self, url):
		'''县级'''
		pass

	def get_country(self, url):
		'''乡级'''
		pass

	def get_village(self, url):
		"""村级"""
		pass

	def run(self):
		self.get_province()


if __name__ == '__main__':
	worker = MySpider()
	worker.run()
