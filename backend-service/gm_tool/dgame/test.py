import socket
import cs_manage_pb2
from utils import *
from item_prompt_pb import *
queryChatReq = cs_manage_pb2.QueryBanUserChatStatusReq()
queryChatReq.player_roleid = 9999

conn = Connector('192.168.0.138', 20701)	
conn.set_header(9999, 2, "sessionid", 4, "CS.QueryBanUserChatStatusReq")
conn.send(queryChatReq)

queryChatRsp = cs_manage_pb2.QueryBanUserChatStatusRsp()
conn.recv(queryChatRsp)
print queryChatRsp.ban_finish_time
print "over"



import json

f = file("gg.ini");
s = json.load(f)
print s
f.close

from django.test import TestCase
# Create your tests here.
