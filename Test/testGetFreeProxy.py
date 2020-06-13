# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     testGetFreeProxy
   Description :   test model ProxyGetter/getFreeProxy
   Author :        J_hao
   date：          2017/7/31
-------------------------------------------------
   Change Activity:
                   2017/7/31:function testGetFreeProxy
-------------------------------------------------
"""
__author__ = 'J_hao'

import re

from ProxyGetter.getFreeProxy import GetFreeProxy
from Config.ConfigGetter import config
from Util.WebRequest import WebRequest
from Util.proxy_util import get_proxies
from Util.utilFunction import getHtmlTree


def testGetFreeProxy():
    """
    test class GetFreeProxy in ProxyGetter/GetFreeProxy
    :return:
    """
    proxy_getter_functions = config.proxy_getter_functions
    for proxyGetter in proxy_getter_functions:
        proxy_count = 0
        for proxy in getattr(GetFreeProxy, proxyGetter.strip())():
            if proxy:
                print('{func}: fetch proxy {proxy},proxy_count:{proxy_count}'.format(func=proxyGetter, proxy=proxy,
                                                                                     proxy_count=proxy_count))
                proxy_count += 1
        # assert proxy_count >= 20, '{} fetch proxy fail'.format(proxyGetter)


def freeProxy16(max_page=34):
    """
    66代理 http://www.66ip.cn
    :return:
    """
    base_url = 'http://www.66ip.cn/areaindex_{}/1.html'
    request = WebRequest()
    for page in range(1, max_page + 1):
        url = base_url.format(page)
        r = request.get(url, timeout=10)
        proxies = re.findall(
            r'<td.*?>[\s\S]*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})[\s\S]*?</td>[\s\S]*?<td.*?>[\s\S]*?(\d+)[\s\S]*?</td>',
            r.text)
        for proxy in proxies:
            print(proxy)


def freeProxy18_():
    """
    66代理 http://www.66ip.cn
    :return:
    """
    urls = ['https://proxy.mimvp.com/freesecret',

            ]
    request = WebRequest()
    for url in urls:
        r = request.get(url, timeout=10)
        proxies = re.findall(
            r'<td.*?>[\s\S]*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(\d+)[\s\S]*?</td>',
            # r'<td.*?>[\s\S]*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})[\s\S]*?</td>[\s\S]*?<td.*?>[\s\S]*?(\d+)[\s\S]*?</td>',
            r.text)
        for proxy in proxies:
            print(proxy)


def freeProxy17():
    """
    小幻HTTP代理 https://ip.ihuan.me
    :return:
    """
    base_url = 'https://ip.ihuan.me{}'
    request = WebRequest()
    url = base_url.format('/today.html')
    r = request.get(url, timeout=10)
    urls = re.findall(
        r'<a href="([^"]+)"[^>]+',
        r.text)
    for url in urls:
        if 'today' in url:
            url_detail = base_url.format(url)
            print(url_detail)
            r_detail = request.get(url_detail, timeout=10)
            proxys = re.findall(
                '(\d{2,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{2,5})',
                r_detail.text)
            for proxy in proxys:
                print(proxy)
            break


def freeProxy18():
    """
    站大爷 https://www.zdaye.com/dayProxy.html
    :return:
    """
    base_url = 'https://www.zdaye.com{}'
    request = WebRequest()
    url = base_url.format('/dayProxy.html')
    print(url)
    r = request.get(url, timeout=10)
    urls = re.findall(
        r'<a href="([^"]+)"+',
        r.text)
    for url in urls:
        if 'dayProxy' in url:
            url_detail = base_url.format(url)
            print(url_detail)
            r_detail = request.get(url_detail, timeout=10)
            proxys = re.findall(
                '(\d{2,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{2,5})',
                r_detail.text)
            for proxy in proxys:
                print(proxy)
            break



if __name__ == '__main__':
    # testGetFreeProxy()
    # freeProxy16()
    # freeProxy17()
    freeProxy18()
