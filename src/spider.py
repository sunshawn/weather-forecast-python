"""
author: sunshawn
this program use a web spider to get the data. website used: http://tianqihoubao.com/lishi/shanghai/
date: 2020.7.5
"""


from urllib import request


# constant value definition
URL_HEAD = 'http://tianqihoubao.com/lishi/shanghai/month/'
START_YEAR = 2018
END_YEAR = 2019
# use the datas of the year 2018 and 2019


def spider(url):
    """
    frame of web spider
    :param url: url of website
    :return: the html document of website
    """
    response = request.urlopen(url)
    html = response.read()
    html_decoded = html.decode('gbk')
    # print(html_decoded)
    return html_decoded


def scratch_weather():
    """
    used for scratching weather html documents
    :return: html of the weather website
    """
    url_tail_generated = ''
    for i in range(START_YEAR, END_YEAR + 1):
        for j in range(1, 13):
            if j < 10:
                month = '0' + str(j)
            else:
                month = str(j)
            url_tail_generated = str(i) + month + '.html'
    # Fixme: This indent should be here
    html = spider(URL_HEAD + url_tail_generated)
    return html
