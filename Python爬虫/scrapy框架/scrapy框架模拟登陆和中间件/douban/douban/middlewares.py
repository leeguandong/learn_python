# -*- coding: utf-8 -*-

import random
import base64

from settings import USER_AGENTS
from settings import PROXIES

# 随机的User-Agent
class RandomUserAgent(object):
    # 之前中间里面的方法都可以忽视，但是这个方法是一定要重写的
    def process_request(self, request, spider):
        useragent = random.choice(USER_AGENTS)
        request.headers.setdefault('User-Agent', useragent)

# 随机的代理池，是从代理池中选择代理，但是有密码的私有代码是需要将密码转成base64编码形式的组成请求信令
class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)

        if proxy['user passwd'] is None:
            # 没有代理账户验证的代理使用方式
            request.meta['proxy'] = 'http://' + proxy['ip_prot']

        else:
            # 对账户密码进行base64编码转换
            base64_userpasswd = base64.b64encode(proxy['user_passwd'])
            # 对应到代理服务器的信令格式里,注意Bsaic 后面有一个空格
            request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpasswd

            request.meta['proxy'] = "http://" + proxy['ip_port']
