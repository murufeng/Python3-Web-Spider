import requests
import re
import json
import time

def get_one_page(url):
	headers = {
	      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
	}
	response =requests.get(url,headers=headers)
	if response.status_code == 200:
		return response.text
	return None

#解析网页源代码信息
def parse_one_page(html):
	pattern = re.compile(
		'<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
	#item = re.findall(pattern,html)
	#print(item)

	#将匹配结果进行处理一下，遍历提取结果并生成字典
	items = re.findall(pattern,html)
	for item in items:
		yield{
		     'index': item[0],
		     'image': item[1],
		     'title': item[2].strip(),
		     'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
		     'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
		     'score': item[5].strip()+item[6].strip()
		}

def main():
	url = 'https://maoyan.com/board/7'
	html = get_one_page(url)
	#print(html)
	for item in parse_one_page(html):
		print(item)

if __name__ == '__main__':
	main()
