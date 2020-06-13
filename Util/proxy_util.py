# -*- coding: utf-8 -*-

# the api of free proxy ip
#
# See documentation in:
# https://github.com/jhao104/proxy_pool
import requests


def get_proxy():
    """获取一个代理ip"""
    # return '52.218.92.199:7255'
    return (requests.get("http://127.0.0.1:5010/get/")).json().get('proxy')


def get_proxies():
    """获取已经组装好的代理字典"""
    proxy = get_proxy()
    proxies = {
        "http": proxy,
        "https": proxy,
    }
    return proxies


def get_proxy_all():
    """获取所有代理ip"""
    return requests.get("http://127.0.0.1:5010/get_all/")


def delete_proxy(proxy):
    """删除一个代理，可以时ip字符 或 代理字典"""
    print('del proxy: {}'.format(proxy))
    if type(proxy) is dict:
        requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy['http'].replace('http://')))
    else:
        requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


def test_proxy_with_clear_and_url(proxy, url_test='http://www.example.com'):
    """测试代理有效性, 并清理无效的"""
    # ....
    retry_count = 5
    while retry_count > 0:
        try:
            if type(proxy) is dict:
                html = requests.get(url_test, proxies=proxy)
            else:
                html = requests.get(url_test, proxies={"http": "http://{}".format(proxy), "https": "https://{}".format(proxy)})
            # 使用代理访问
            print('正常代理：{}'.format(proxy))
            return html
        except Exception:
            retry_count -= 1
    # 出错5次, 删除代理池中代理
    delete_proxy(proxy)
    return None


def test_proxy_with_clear(url_test):
    """检测某链接代理的可用性并清楚无用代理"""
    _proxy_list = get_proxy_all().json()
    for proxy in _proxy_list:
        test_proxy_with_clear_and_url(proxy.get('proxy'), url_test)
