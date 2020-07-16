# -*- coding: utf-8 -*-
# @Author: zcc 
# @Date: 2020/07/16
# coding=utf-8

import urllib.request,re
import string
from urllib.parse import quote
import urllib

path_save = '/home/zhangchengcheng/tools/Spider_zcc/riot1'  # path to save
paths = ['https://www.shutterstock.com/zh/search/riot']  # the url of imageset , the last word is your key word
for i in range(2,15):
#	t = 'https://www.shutterstock.com/zh/search/military+tank'+'?page='+str(i)
	t = 'https://www.shutterstock.com/zh/search/riot'+'?page='+str(i)  # page from 2 to 14
	paths.append(t)

img_path = []
for path in paths:
	response = urllib.request.urlopen(path)
	html = response.read().decode('utf-8')
	pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+') # get all url from html
	ttt = re.findall(pattern,html)
	for i in ttt:
		if('jpg' in i): # get the urls of jpg from all of urls
			img_path.append(i)

# for python to download image
name = path_save.split("/")[-1]
i = 0
for line in img_path:
	url = line
	try:
		i+=1
		request = urllib.request.Request(url)
		response = urllib.request.urlopen(request)
		get_img = response.read()
		with open(path_save+'/'+name+'_'+str(i)+".jpg",'wb') as fp:
			fp.write(get_img)
		print(url)
	except:
		continue

