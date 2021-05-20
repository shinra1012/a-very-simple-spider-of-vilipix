import re
from datetime import datetime
import pandas as pd
def datelist(beginDate, endDate):
    date_l=[datetime.strftime(x,'%Y%m%d') for x in list(pd.date_range(start=beginDate, end=endDate))]
    return date_l
def get_url(date_l = datelist('20201220','20210518'),check=None):

    urls= []
    for i in date_l:
        urls.append('https://www.vilipix.com/ranking?date='+str(i)+'&mode=daily&p=')
    if check is None:
        return urls
    else:
        return urls[int(check):]

def get(i):
    img_tag = i.find(name = 'img',attrs={'class':'el-image__inner'})
    img_str = str(img_tag)
    img_sea = re.search("src=.*",img_str)
    if img_sea is not None:
        img_sea = img_sea.group()
    else:
        return None,None,None
    img_t = str(img_sea)
    try:

        img_resized_url = img_t.split('\"')[1]
        img_full_url = re.search(r'.*\?',img_resized_url).group().split(r'?')[0]



        title_str = re.search("alt=.*",img_str).group().split('\"')[1]


        author_tag = i.find(name='a',attrs={'class':'user-name'}).string
    except BaseException:
        print('Error :'+img_str +'    '+title_str +'    '+author_tag)
        return None,None,None
    author = author_tag
    return img_full_url , title_str, author
