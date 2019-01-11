# encoding: utf-8
"""
@version: python2.7
@author: ‘xin.tang‘
@license: Apache Licence 
@software: PyCharm
@file: data_saver.py
@time: 2019/1/11 6:27 PM
"""

import pymysql

PROVINCE = 2
CITY = 3
COUNTY = 4
COUNTRY = 5
VILLAGE = 6


class MyDataSaver:
	def __init__(self, databse):
		self.db = pymysql.connect(host=databse['host'], user=databse['user'],
		                          password=databse['password'], database=databse['db'], charset='utf8')
		self.cursor = self.db.cursor()

	def save_data(self, code, name, parent_code, level, province_code, city_code=0, county_code=0, country_code=0, village_code=0):
		sql="insert into stats (code,name,parent_code,level,province_code,city_code,county_code,country_code,village_code) value('{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(code, name, parent_code, level, province_code, city_code, county_code, country_code, village_code)
		self.cursor.execute(sql)
		self.db.commit()


	def __exit__(self):
		print 'exit'
		self.cursor.close()

	def __del__(self):
		print 'del'
		self.cursor.close()

"""
Code：统计用区划代码
name：名称
Parent_code: 父级统计用区划代码code
Level:  层级（枚举：2省级、3地级、4县级、5乡级、6村级）
province_code: 省级统计用区划代码
city_code: 地级统计用区划代码
county_code: 县级统计用区划代码
country_code: 乡级统计用区划代码
village_code: 村级统计用区划代码"""

""""
create table stats (
code varchar(20),
name varchar(20),
parent_code varchar(20),
level varchar(20),
province_code varchar(20),
city_code varchar(20),
county_code varchar(20),
country_code varchar(20),
village_code varchar(20)
);
"""

