"""
author: sunshawn
this program use a regular expression to match the datas and make a data frame.
date: 2020.7.8
"""


import re
import pandas as pd


# constant value definition
# these constant values are used to map the data frame.
# if don't, the AI will not be able to identify the datas.
WEATHERS = {
        '晴': 0,
        '多云': 1,
        '阴': 2,
        '小雨': 3,
        '中雨': 4,
        '大雨': 5,
        '暴雨': 6,
        '小到中雨': 7,
        '中到大雨': 8,
        '大到暴雨': 9,
        '阵雨': 10,
        '雷阵雨': 11,
        '小雪': 12,
        '中雪': 13,
        '大雪': 14,
        '暴雪': 15,
        '小到中雪': 16,
        '中到大雪': 17,
        '大到暴雪': 18,
        '雨夹雪': 19
}

WIND_DIRECTIONS = ['东风', '东北风', '北风', '西北风', '西风', '西南风', '南风', '东南风']

WIND_STRENGTH = ['1-2级', '2-3级', '3-4级', '4-5级', '5-6级', '6-7级', '7-8级']


count = 0
WIND = dict()
for io in WIND_DIRECTIONS:
    for jo in WIND_STRENGTH:
        WIND[io + ' ' + jo] = count
        count += 1
print(WIND)


def scratch_info(html):
    """
    used to scratch the useful information of the document
    :param html: the html file
    :return: the weather, the temperature, and the wind.
    """
    # \u4e00-\u9fa5 中文
    weather = re.findall('\r\n +([\u4e00-\u9fa5]+)\r\n +/([\u4e00-\u9fa5]+)</td>', html)
    temperature = re.findall('<td>\r\n +(-?\d)+℃\r\n +/\r\n +(-?\d)+℃\r\n +</td>', html)
    wind = re.findall('<td>\r\n +([\u4e00-\u9fa5]+风) (.+?)级\r\n +/([\u4e00-\u9fa5]+风) (.+?)级</td>', html)
    return weather, temperature, wind


def turn_info(info):
    """
    turn the information into a list
    because the form of the source datas is ('...', '...') due to the morning and evening weather differences
    :param info: the information scratched
    :return: the completed list
    """
    target = []
    for i in info:  # the list form
        for j in i:  # the tuple form
            target.append(j)
    return target


def convert_data(dataframe):
    """
    convert the string type of datas into integer type of datas
    :param dataframe: the data frame wanted to map
    :return: the mapped data frame
    """
    dataframe['weather'] = dataframe['weather'].map(WEATHERS)
    dataframe['wind'] = dataframe['wind'].map(WIND)
    return dataframe


def make_dataframe(weather, temperature, wind):
    """
    the function to make a data frame
    :param weather: weather list
    :param temperature: temperature list
    :param wind: wind list
    :return: data frame
    """
    df = pd.DataFrame([weather, temperature, wind], columns=['weather', 'temperature', 'wind'])
    df = convert_data(df)
    return df
