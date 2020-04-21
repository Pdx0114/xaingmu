# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:48:40 2020

@author: pan
"""

import requests
import time
import json
import csv
timeout=20
requests.packages.urllib3.disable_warnings()
info_list=[]
post_url ='https://api.eol.cn/gkcx/api/?access_token=&keyword=&page=1&province_id=&school_type=&signsafe=&size=20&sort=view_month&sorttype=desc&type=&uri=apidata/api/gk/school/lists'

headers={
     'Accept': 'application/json, text/plain, */*',
     'Referer':  'https://gkcx.eol.cn/linepro?province=%E8%BE%BD%E5%AE%81&schoolpc=',
     'Sec-Fetch-Dest': 'empty',
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
     'Connection': 'close' ,
     }
page=1
while page<3:
    data ={
        'page':page,
        }
    page+=1
    #测试
    print(page)
    try:
        time.sleep(10)
        response = requests.post(url=post_url,headers=headers,verify=False,data=data,timeout=30).json()
        requests.close()
        data_list =response['data']['item']
        #print(info_list)

        data_dict = {}
        for a in data_list:
            
            data_dict['学校']=a.get('name')
            data_dict['排名']=a.get('rank')
            data_dict['地区']=a.get('city_name')
            data_dict['院校类型']=a.get('type_name')
            data_dict['办学类型']=a.get('level_name')
            data_dict['总人气']=a.get('view_total')
            data_dict['月人气']=a.get('view_month')
            data_dict['周人气']=a.get('view_week')
            data_dict['是否985']=a.get('f985')
            data_dict['是否211']=a.get('f211')
            data_dict['是否双一流']=a.get('dual_class_name')        
            info_list.append(data_dict)
            print(data_dict)        
    except:
        print( "产生异常")
with open('报考热度排名.json', 'w', encoding='utf-8') as f:
    json.dump(info_list, f, ensure_ascii=False, indent=4)
    print('json文件保存成功')
# 将数据存储为csv文件
# 表头
title = info_list[0].keys()
with open('报考热度排名.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, title)
    # 写入表头
    writer.writeheader()
    # 写入数据
    writer.writerows(info_list)
    print('csv文件保存成功')