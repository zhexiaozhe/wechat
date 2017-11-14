# -*- coding: utf-8 -*-
'''
@author: 程哲
@contact: 909991719@qq.com
@file: log.py
@time: 2017/11/14 17:06
'''
import itchat

# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#     return msg.text
# itchat.auto_login()
# itchat.run()

itchat.auto_login(hotReload = True)
#想给谁发信息，先查找到这个朋友
users = itchat.search_friends(name=u'方')
#找到UserName
userName = users[0]['UserName']
#然后给他发消息
itchat.send('干什么',toUserName = userName)
#退出登录
itchat.logout()