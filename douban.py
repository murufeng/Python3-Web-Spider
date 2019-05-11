import requests
import re
from bs4 import BeautifulSoup



print('正在豆瓣电影pipTOP 250中抓取数据')

for  page in range(10):
    #按页爬取数据
    print('========正在抓取第'+str(page+1)+'页===========')

    url = 'https://movie.douban.com/top250?start='+str(page*25)+'&filter='

    html = requests.get(url)
    #print(html)
    soup = BeautifulSoup(html.text,'html.parser') #通过网页解析库来实现网页信息抓取
    soup = str(soup) #将文本转换成字符串
    #print(soup)
    
    # 1 取出电影名字
    title = re.compile(r'<span class="title">(.*)</span>')
    names = re.findall(title,soup)
    '''for name in names :
        if name.find('/')==-1:   #剔除英文名（英文名特征是含有‘/’的
           print(name)'''

    
    # 2 取出评分
    retStars = r'.*?"v:average">(.*?)</span>'
    regStars = re.compile(retStars)
    starts = re.findall(regStars, soup)

    # 3 取出评价
    regCommend = r'<span>(.*?)</span>'
    regCommends = re.compile(regCommend)
    commends = []
    commends = re.findall(regCommends, soup)
    commends.remove('·')
    commends.remove('更多')
    commends.remove('{{= year}}')
    commends.remove('{{= sub_title}}')
    commends.remove('{{= address}}')
    commends.remove('集数未知')
    commends.remove('共{{= episode}}集')

    # 4 取出导演，剧情
    regDoc= r'.*?<p class>(.*?)<br>'
    regxDoc = re.compile(regDoc)
    list_doc = re.findall(regxDoc,soup)

    # 5 取出引言  希望让人自由
    regScrip = r'.*?"inq">(.*?)</span>'
    regx_scrip = re.compile(regScrip)
    list_scrip = re.findall(regx_scrip, soup)
    
    nums =0 
    ver_info =list(zip(names,starts,commends,list_scrip))
    for ver in ver_info:
       varStr = 'No.%d\t%-30s%s\t(描述:)%-30s%-30s' % (nums,ver[0], ver[1],ver[2],ver[3])
       print(varStr)
       nums +=1
          

              
    
print('抓取OK')



#Python主方法
if __name__ == '__main__':
    print('豆瓣数据爬取Top250')
