
import requests   #python HTTP客户端库,编写爬虫和测试服务器响应数据经常会用到的
import re
import random #随机生成一个实数，取值范围[0,1]


def spiderPic(html,keyword):
    print('正在查找:'+keyword+'对应的图片，正在从百度图像库中下载文件，请稍等')

    for addr in re.findall('"objURL":"(.*?)"',html,re.S):

         #print('现在正在爬取的URL地址:'+str(addr))
        
        print('现在正在爬取的URL地址:'+str(addr)[0:50]+'......')

        try:
            
            pics = requests.get(addr,timeout=10)#请求图像URL地址（最大时间10s)


        except requests.exceptions.ConnectionError:
             print("你当前的URL地址请求错误!")

             continue

        fn = open('D:\\Python-Spider\\img'+(str(random.randrange(0,1000,5))+'.jpg'),'wb')#重命名,二进制存储
        fn.write(pics.content)
        fn.close()

        
        


#Python主方法
if __name__=="__main__":
    print("hello")



    word = input("请输入你想要获取的图像的关键词:")

    result = requests.get('https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word)

    spiderPic(result.text,word)
