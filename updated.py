# -*- coding:utf-8 -*-
import os
import sys
import time
import pandas as pd
import urllib.request as ur
from bs4 import BeautifulSoup as bs4

base_path = 'D:/视频/电视剧/'

following = ['flash',
			 'xman',
			 'scor',
			 'inhuman'
			 ]

episode_url = {
	'flash'   : 'http://www.hao6v.com/mj/2014-10-08/24087.html',
	'xman'    : 'http://www.hao6v.com/mj/2017-10-03/29934.html',
	'scor'    : 'http://www.hao6v.com/mj/2014-09-23/23969.html',
	'inhuman' : 'http://www.hao6v.com/mj/2017-09-30/29922.html'
}

local_location = {
	'flash'   : base_path+'闪电侠第四季',
	'xman'    : base_path+'天赋异禀第一季',
	'scor'    : base_path+'天蝎计划第四季',
	'inhuman' : base_path+'异人族第一季' 	
}

print('正在查找是否有更新...')
#%%
temp_i = 0
url_to_be_open = []
for meiju in following:
	url = episode_url[meiju]
	url_read = bs4(ur.urlopen(url).read(),'html.parser')

	temp_info=url_read.find('table').find_all('td')
	current_season = 0
	for line in temp_info:
		if line.find('a') != None:
			current_season += 1

	already_got = len(os.listdir(local_location[meiju]))
	missed = current_season-already_got
	#print('{} 已经更新至第 {} 集, 当前已经下载 {} 集.'.format(os.path.basename(local_location[meiju]), current_season, already_got))
	if current_season - already_got == 0:
		continue
	else:
		temp_i = 1
		missed = current_season-already_got
		url_to_be_open.append(episode_url[meiju])
		print('{} 有 {} 集更新.'.format(os.path.basename(local_location[meiju]), missed))
		
if temp_i == 0:
	print('\n目前没有美剧更新')
# Open corresponding website if there is updated episode
if url_to_be_open != []:
	for u in url_to_be_open:
		os.system('python -m webbrowser -t {}'.format(u))
 