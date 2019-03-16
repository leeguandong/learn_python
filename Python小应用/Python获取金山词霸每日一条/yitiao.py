from __future__ import unicode_literals
import requests
import itchat


def get_news():
    url = 'http://open.iciba.com/dsapi'
    r = requests.get(url)
    contents = r.json()['content']
    translation = r.json()['translation']
    return contents, translation


def send_news():
    try:
        # 登录你的微信账号，会弹出网页二维码，扫描即可
        itchat.auto_login(hotReload=True)
        # 备注好友姓名
        gf = itchat.search_friends(name='叶宝贝')
        # 获取对应名称的一串数字
        Yebaby = gf[0]['UserName']
        # 获取金山字典的内容
        message1 = str(get_news()[0])
        content = str(get_news()[1][17:])
        message2 = str(content)
        # message3 = '那个很适合你的人'
        message3 = '天才李冠东'

        # 发送消息
        itchat.send(message1, toUserName=Yebaby)
        itchat.send(message2, toUserName=Yebaby)
        itchat.send(message3, toUserName=Yebaby)
        # 每天发送一次
        # t = time(86400, send_news())
        # t.start()
    except:
        message4 = ''
        itchat.send(message4, toUserName=Yebaby)


def main():
    send_news()


if __name__ == '__main__':
    main()
