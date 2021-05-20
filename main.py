from selenium import webdriver
import selenium
import os
import time
global page,author_num
from time import sleep
import requests
from bs4 import BeautifulSoup
import os
import argparse
import json
import traceback
from file_io import check_deleted
from req import get
from tar import get_url,datelist
'''headers = {
'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'
    }'''

def save_img(img_url,author,title='default'):
    global work_num
    global temp
    global author_num
    if not os.path.exists(os.path.join(opt.outf, str(author_num))):
        os.makedirs(os.path.join(opt.outf, str(author_num)))
    with open(os.path.join(opt.outf,str(author_dic[author]),title+'_'+str(work_num)+'.jpg'),'wb') as img:
        temp += 1
        img_file = requests.get(img_url).content
        img.write(img_file)
        print('Saving ' + str(work_num+temp) +'th images' +'   title:'+title +'   author:'+author + '   author_id：'+str(author_dic[author]))
if __name__ == '__main__':
    try :
        today = time.strftime('%Y%m%d')
        parser = argparse.ArgumentParser()
        parser.add_argument('--outf', type=str, default='./output', help='output folder')
        parser.add_argument('--check_point', type=str, default='./default_check_point.json',
                            help='check_point')
        parser.add_argument('--adp', type=str, default='./default_author_dic.json',
                            help='author_dic_path')
        parser.add_argument('--std', type=str, default='20201220',
                            help='start_date')
        parser.add_argument('--end', type=str, default=today,
                            help='start_date')
        opt = parser.parse_args()
        print(opt)
        global page
        global author_num
        global work_num
        global temp
        temp =0
       
        f = open(opt.check_point, encoding='utf-8') 
        res = f.read()  
        dict = json.loads(res)
        work_num = int(dict['work_num'])

        author_dic_path = dict['author_dic_path']
        f = open(author_dic_path, encoding='utf-8')  
        res = f.read() 
        author_dic = json.loads(res)
        check_deleted(opt,author_dic)
        start_page = int(dict['page'])
        start_date = dict['start_date']
        end_date = dict['end_date']
        check = dict['check']

        #
        author_num = len(author_dic)
        urls = get_url(datelist(start_date,end_date),check)

        option = webdriver.ChromeOptions()
        option.add_argument('headless')
      
        for j,url in enumerate(urls):
            if j ==0:
                page = start_page
            else:
                page = 1
            url_ = url+str(page)
            driver = selenium.webdriver.Chrome(options=option)
            driver.set_window_size(10000, 60000)
            html = driver.get(url_)

            sleep(6)
            html = driver.page_source
            soup = BeautifulSoup(html, "lxml")

            while(soup.find_all(name = 'li',attrs= {'class':'pix-card'}) !=[] ) :

                for i in soup.find_all(name = 'li',attrs= {'class':'pix-card'}):
                    try:
                        img_full_url, title, author = get(i)
                        if img_full_url is None and title is None and author is None:
                            continue
                        if author in author_dic.keys():
                            #num = author_dic[author]
                            if author_dic[author] == -1:
                                pass
                            else:
                                save_img(img_full_url,author,title)
                        else:
                            author_num += 1
                            author_dic[author] = str(author_num)

                            save_img(img_full_url, author, title)
                    except Exception:
                        continue
                work_num += temp
                temp =0
                driver.close()
                print(url_+' Complete')
                page+=1
                url_ = url + str(page)
                driver = selenium.webdriver.Chrome(options = option)
                driver.set_window_size(10000, 60000)
                html = driver.get(url_)

                sleep(6)
                html = driver.page_source
                soup = BeautifulSoup(html, "lxml")
    except BaseException as e:
        print('End at :'+url_)
        print('Saving...')
        json_author = json.dumps(author_dic,ensure_ascii=False)
        json_check_point = json.dumps({'check':j,'start_date':opt.std,'page':page,'end_date':opt.end,'author_dic_path':opt.adp,'work_num':str(work_num)},ensure_ascii=False)
        fileObject = open('author_dic.json', 'w',encoding="utf-8")
        fileObject.write(json_author)
        fileObject.close()
        fileObject_2 = open('check_point.json', 'w',encoding="utf-8")
        fileObject_2.write(json_check_point)
        fileObject_2.close()
        print('Saved')
        print(e)
        traceback.print_exc()
