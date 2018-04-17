#!/usr/bin/python

from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sys

if len(sys.argv)>1:
	my_url= sys.argv[1]
else:
	my_url='https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
	
uClient =uReq(my_url)
page_html=uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers=page_soup.findAll("div",{"class":"item-container"})

filename='cproducts.csv'
fp=open(filename,'w')
header='Brand,product_name,price,shipping\n' 
fp.write(header)
for container in containers:
	brand =container.div.div.a.img['title']
	title_container = container.findAll("a",{"class":"item-title"})
	product_name=title_container[0].text
	shipping_container=container.findAll("li",{"class":"price-ship"})
	shipping=shipping_container[0].text.strip()
	price_container=container.findAll("li",{"class":"price-current"})
	price_line=price_container[0].text.strip()
	price=price_line[2:9]
	if price[0]!= '$':
		price=price_line[0:7]
	
	print("brand:"+brand)
	print("product_name:"+product_name)
	print("price:"+price)
	print("shipping:"+shipping+'\n')

	fp.write(brand+','+product_name.replace(',','|')+','+price+','+shipping+'\n')

fp.close()
