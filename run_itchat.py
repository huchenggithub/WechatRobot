#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Newton_apple time:2018-02-26
# itchat模块实现微信信息接收

import itchat
import TulingRobot

@itchat.msg_register('Text', isGroupChat=False)  # 不监控群消息
def text_reply(msg):
	"""监控微信消息"""
	content = msg['Content']
	fromuser = msg['FromUserName']
	# print(msg)

	message = TulingRobot.autochat(content, fromuser)
	itchat.send(message, fromuser)


'''
{'MsgId': '6894666882930930866', 'FromUserName': '@b063ab41f0c323d9bd5567c4792e2d6d3f5b59fca4c71e69b54d6907eacf29bb',
'ToUserName': '@79aa2296fbb9cc974a3cd28906a5226615a2991c1a2c2dc445d56ca8cc95164a', 'MsgType': 1,
'Content': '是不是能够获取信息了', 'Status': 3, 'ImgStatus': 1, 'CreateTime': 1519633384, 'VoiceLength': 0,
'PlayLength': 0, 'FileName': '', 'FileSize': '', 'MediaId': '', 'Url': '', 'AppMsgType': 0, 'StatusNotifyCode': 0,
'StatusNotifyUserName': '', 'RecommendInfo': {'UserName': '', 'NickName': '', 'QQNum': 0, 'Province': '', 'City': '',
'Content': '', 'Signature': '', 'Alias': '', 'Scene': 0, 'VerifyFlag': 0, 'AttrStatus': 0, 'Sex': 0, 'Ticket': '',
'OpCode': 0}, 'ForwardFlag': 0, 'AppInfo': {'AppID': '', 'Type': 0}, 'HasProductId': 0, 'Ticket': '', 'ImgHeight': 0,
'ImgWidth': 0, 'SubMsgType': 0, 'NewMsgId': 6894666882930930866, 'OriContent': '', 'EncryFileName': '',
'User': <User: {'MemberList': <ContactList: []>, 'Uin': 0,
'UserName': '@b063ab41f0c323d9bd5567c4792e2d6d3f5b59fca4c71e69b54d6907eacf29bb', 'NickName': '牛顿的苹果',
'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=659500565&username=@b063ab41f0c323d9bd5567c4792e2d6d3f5b59fca4c71e69b54d6907eacf29bb&skey=@crypt_bb9141de_c41d4ccdae6c2dd2918cb92a4de17628',
'ContactFlag': 3, 'MemberCount': 0, 'RemarkName': '', 'HideInputBarFlag': 0, 'Sex': 1, 'Signature': '吾与城北徐公孰美？',
'VerifyFlag': 0, 'OwnerUin': 0, 'PYInitial': 'NDDPG', 'PYQuanPin': 'niududepingguo', 'RemarkPYInitial': '',
'RemarkPYQuanPin': '', 'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 0, 'AttrStatus': 135205, 'Province': '四川',
'City': '', 'Alias': '', 'SnsFlag': 1, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': '',
'EncryChatRoomId': '', 'IsOwner': 0}>, 'Type': 'Text', 'Text': '是不是能够获取信息了'}
'''

if __name__ == '__main__':
	itchat.login()
	itchat.run()
