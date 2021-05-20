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
