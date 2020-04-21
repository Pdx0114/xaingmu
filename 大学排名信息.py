 # -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:15:20 2020

@author: pan
"""
import requests
import json
import csv
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'contentType': 'application/x-www-form-urlencoded; charset=utf-8',
    'Cookie': 'Hm_lvt_0430cf9439364c83153612c9fbd31838=1581402157; Hm_lpvt_0430cf9439364c83153612c9fbd31838=1581402164',
    'Host': 'gaokao.afanti100.com',
    'media': 'PC',
    'Referer': 'https://gaokao.afanti100.com/university.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

data_list = []

def get_index():    

    page = 1
    while True:
        if page > 188:
            break
        url = 'http://gaokao.afanti100.com/api/v1/universities/?degree_level=0&directed_by=0' \
        '&university_type=0&location_province=0&speciality=0&page={}'.format(page)
        # page自增一实现翻页
        page += 1
        # 请求url并返回的是json格式
        resp = requests.get(url, headers=headers).json()
        # 取出大学所在的键值对
        university_lsts = resp.get('data').get('university_lst')
        if university_lsts:
            get_info(university_lsts)
        else:
            continue


def get_info(university_lsts):
    # 判断列表是否不为空
    if university_lsts:
        # 遍历列表取出每个大学的信息
        for university_lst in university_lsts:
            # 声明一个字典存储数据
            data_dict = {}

            # 大学名字
            data_dict['名字'] = university_lst.get('name')
            # 大学排名
            data_dict['排名'] = university_lst.get('ranking')
            # 大学标签
            data_dict['标签'] = university_lst.get('tag_lst')
            # 大学重点学科
            data_dict['大学重点学科'] = university_lst.get('key_major_count')
            # 硕士点数
            data_dict['硕士点数'] = university_lst.get('graduate_program_count')
            # 博士点数
            data_dict['博士点数'] = university_lst.get('doctoral_program_count')
            # 是否211
            data_dict['是否211'] = university_lst.get('is_211')
            # 是否985
            data_dict['是否985'] = university_lst.get('is_985')
            # 哪个省
            data_dict['省份'] = university_lst.get('location_province')
            # 哪个城市
            data_dict['城市'] = university_lst.get('location_city')
            # 大学类型
            data_dict['大学类型'] = university_lst.get('university_type')

            data_list.append(data_dict)
            print(data_dict)


def save_file():
    # 将数据存储为json文件
    with open('大学排名信息.json', 'w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)
    print('json文件保存成功')

    # 将数据存储为csv文件
    # 表头
    title = data_list[0].keys()
    with open('大学排名信息.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, title)
        # 写入表头
        writer.writeheader()
        # 写入数据
        writer.writerows(data_list)
    print('csv文件保存成功')


def main():
    get_index()
    save_file()


if __name__ == '__main__':
    main()