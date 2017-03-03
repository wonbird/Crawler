# encoding=utf-8
from connectdb import *
import urllib.request
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent': user_agent, }
timeout = 15

target_list = get_target_list()
for target in target_list:
    id = target[0]
    word = target[1]

    URL = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=' + word\
          + '%20%E7%99%BE%E5%BA%A6%E7%99%BE%E7%A7%91&rsv_pq=c381916800002378&'\
          + 'rsv_t=01ffeRS%2Fz6BxblQbwCjvpD1OX8Ztgw8HPq6jUyu3PLsqTIaPIy3ZL%2Flon2I&'\
          + 'rqlang=cn&rsv_enter=1&rsv_n=2&rsv_sug3=1'

    request = urllib.request.Request(URL, None, headers)
    response = urllib.request.urlopen(request, timeout=timeout)

    plain_text = response.read()
    soup = BeautifulSoup(plain_text, 'html.parser')

    content_table = soup.find('div', {'class': 'result-op c-container xpath-log'})
    image = content_table.find('div', class_='c-span6').find('img')
    image_url = ''
    if image:
        image_url = image['src']
    print(image_url)
    image = open('C:/Apache24/htdocs/photo/' + str(id) + '.jpg', 'wb')
    down_img = urllib.request.urlopen(image_url)
    image.write(down_img.read())
    image.close()
