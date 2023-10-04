#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from dgame.models import gift

import logging

import sys
import os
sys.path.append("/usr/local/dgame/python_test/inc")

PYTHON_CONF_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PYTHON_CONF_DIR, 'python_test/inc'))
import python_conf

PROTO_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PROTO_DIR, 'pb2'))
import ss_router_pb2

# python debug use 
#import ptvsd
#ptvsd.enable_attach()

SPECIAL_ROLEID  = 9999

ZoneId = int(python_conf._ZoneId_)
DB_ADDR0 = python_conf._GameDbAddr0_
DB_ADDR1 = python_conf._GameDbAddr1_
DB_ADDR2 = python_conf._GameDbAddr2_
DB_ADDR3 = python_conf._GameDbAddr3_
DB_ADDR4 = python_conf._GameDbAddr4_
DB_PAY_ADDR = python_conf._AccountDbAddr_
DB_USER_NAME    = python_conf._GameDbUser_
DB_USER_PSW             = python_conf._GameDbPswd_
DB_NAME                 = "dgame"
DB_DGAME_PAY            = "dgame_pay"

CDKEY_SEARCH_DB_ADDR = "127.0.0.1"
#从帐号服拉取服务器列表 svr_id 映射 ip
PROTOLSERVER    = "127.0.0.1"
#配置global.ini 的master_svr 对外端口
PROTOLSERVERPORT= 10801

white_ip_list = ["14.28.138.201"]

def index(request):
	
	remote_ip = request.META['REMOTE_ADDR'] 
	logging.info("remote ip : "+ remote_ip)
	
	'''
	is_white = False
	for ip in white_ip_list:
		if remote_ip == ip:
			is_white = True
	if is_white == False:
		return HttpResponse("这里没有东西")
	'''
	
	if request.user.is_authenticated == 0:
		return HttpResponse("请登录")
	gift_list = gift.objects.all().order_by('gift_id')[:5]
	context = {'gift_list': gift_list}
	return render(request, 'dgame/index.html', context)
		
import xml.dom.minidom
dom_matinfo = xml.dom.minidom.parse('xml/MaterialBaseInfo.xml')
root_matinfo = dom_matinfo.documentElement
materialBaseInfos = root_matinfo.getElementsByTagName('MaterialBaseInfo')

dom_giftbag = xml.dom.minidom.parse('xml/Vip_GiftBag.xml')
root_giftbag = dom_giftbag.documentElement
giftbags = root_giftbag.getElementsByTagName('GiftBag')

dom_equip = xml.dom.minidom.parse('xml/EquipBaseInfo.xml')
root_equip = dom_equip.documentElement
equips = root_equip.getElementsByTagName('EquipBaseInfo')

#查看礼包内物品信息
def ajax(request, gift_id):
	if request.user.is_authenticated == 0:
		return HttpResponse("请登录")
	gift_id = int(gift_id)
	data = ''
	behave = 0 	#在Vip_GiftBag.xml中当礼包的功能ID为0时，检查是否所选礼包的物品
	
	#在MaterialBaseInfo.xml查询礼包的功能ID，然后在Vip_GiftBag.xml中查询礼包内的物品ID，最后在MaterialBaseInfo.xml查询对应礼包物品ID的名字
	for materialBaseInfo in materialBaseInfos:		
		id = materialBaseInfo.getElementsByTagName('Id')[0]
		id_data = id.childNodes[0].data
		id_data = int(id_data)
		if id_data == gift_id:
			funcParam = materialBaseInfo.getElementsByTagName('FuncParam')[0]
			funcParam_data = int(funcParam.childNodes[0].data)
			
			for giftbag in giftbags:
				gid = giftbag.getElementsByTagName('Id')[0]
				gid_data = int(gid.childNodes[0].data)
				if gid_data == funcParam_data or (gid_data == 0  and behave==1):
					behave = 1
					materialId = int(giftbag.getElementsByTagName('Id')[1].childNodes[0].data)
					materialMinNum = int(giftbag.getElementsByTagName('MinCnt')[0].childNodes[0].data)
					materialMaxNum = int(giftbag.getElementsByTagName('MaxCnt')[0].childNodes[0].data)
					materialNum = 0
					if materialMinNum == materialMaxNum:
						materialNum = materialMinNum
					else:
						materialNum = materialMinNum +'~'+ materialMaxNum
					if materialId == 0:
						#查询Type标签
						materialType = giftbag.getElementsByTagName('Type')[0].childNodes[0].data
						str_materialType = str(materialType)
						if str_materialType == "RES_ITEM_TYPE_GOLD ":
							materialName = '金币'
						elif str_materialType == "RES_ITEM_TYPE_DIAMOND ":
							materialName = '钻石'
						else:
							materialName = '未知物品'

					else:
						for materialBaseInfo2 in materialBaseInfos:
							id2 = int(materialBaseInfo2.getElementsByTagName('Id')[0].childNodes[0].data)
							if id2 == materialId:
								materialName = materialBaseInfo2.getElementsByTagName('Name')[0].childNodes[0].data														
								break
					data += materialName + '*' + str(materialNum) +'<pre>'
				else:
					behave = 0
			
	return HttpResponse(data)
	
#连接数据库
import pymysql
pymysql.install_as_MySQLdb()
#查询CDKey信息
def search(request,cdkid):
	if request.user.is_authenticated == 0:
		return HttpResponse("请登录")
	sqlquery = "SELECT expire_time, has_drawn FROM cdkey WHERE cdkey ='"+cdkid + "'"
	db = MySQLdb.connect(DB_ADDR, DB_USER_NAME, DB_USER_PSW, DB_NAME, charset = "utf8")
	
	cursor = db.cursor()
	cursor.execute(sqlquery)
	result = cursor.fetchone()

	if str(result) == 'None':
		return HttpResponse("查无此记录")
	haveuse = "已使用"
	if result[1] == 0: 	#未被使用过
		haveuse = "未使用"
	db.close()
	return HttpResponse(haveuse+"<pre>"+"过期时间:<pre>"+str(result[0]))

#查询礼包类别使用情况
def searchtype(request, typeid):
	if request.user.is_authenticated == 0:
		return HttpResponse("请登录")
	sqlquery = "SELECT COUNT(*) FROM cdkey WHERE cdkey LIKE '"+typeid + "%' And has_drawn = 1"
	db = MySQLdb.connect(DB_ADDR,DB_USER_NAME,DB_USER_PSW,DB_NAME, charset = "utf8" )
	
	cursor = db.cursor()
	cursor.execute(sqlquery)
	result = cursor.fetchone()
	return HttpResponse(result)


#添加奖励玩家
def addPlayers(request, channel, server):
	if request.user.is_authenticated == 0:
		return HttpResponse("请登录")
	context={'channel':channel,'server':server}
	return render(request, 'dgame/addPlayers.html', context)

def searchPlayers2(request, type, para, channel, server):	
	if request.user.is_authenticated == 0:
		return HttpResponse("请登录")
	if server=="10000":
		DB_ADDR = DB_ADDR0
	elif server=="1":
		DB_ADDR = DB_ADDR1
	elif server == "2":
		DB_ADDR = DB_ADDR2
	elif server == "3":
		DB_ADDR = DB_ADDR3
	elif server == "4":
		DB_ADDR = DB_ADDR4
	else:
		return HttpResponse('Server Error')
	db = MySQLdb.connect(DB_ADDR,DB_USER_NAME,DB_USER_PSW,DB_NAME,charset = "utf8")
	cursor = db.cursor()
	sqlquery = ""
	if type=="roleid":
#		num = int(para)%100
		sqlquery = "select roleid, role_name from player where roleid ="+para

	else:
		str_name = para.encode('utf-8')
		sqlquery = "select roleid, role_name from player where role_name ='"+str_name+"'"
	
	cursor.execute(sqlquery)
	result = cursor.fetchall()
	str_result = ""
	cursor.close()
	if result == None:
		return HttpResponse("null")
	else:
		for player in result:
			str_result=str_result + str(player[0])+":"+player[1]+";"
		return HttpResponse(str_result)	

		
def ajaxGetInfo(request, type):
	if request.user.is_authenticated == 0:
		return HttpResponse("请登录")
	data=""
	if type=="RES_ITEM_TYPE_TOOL":
		for materialBaseInfo in materialBaseInfos:	
			Mtype = materialBaseInfo.getElementsByTagName('Type')[0].childNodes[0].data
			if str(Mtype) == "RES_ITEM_TYPE_TOOL ":
				mID = int(materialBaseInfo.getElementsByTagName('Id')[0].childNodes[0].data)
				MName=materialBaseInfo.getElementsByTagName('Name')[0].childNodes[0].data
				data = data + str(mID) + ":" + MName +";"
	elif type=="RES_ITEM_TYPE_MATERIAL":
		for materialBaseInfo in materialBaseInfos:	
			Mtype = materialBaseInfo.getElementsByTagName('Type')[0].childNodes[0].data
			if str(Mtype) == "RES_ITEM_TYPE_MATERIAL ":
				mID=int(materialBaseInfo.getElementsByTagName('Id')[0].childNodes[0].data)
				MName = materialBaseInfo.getElementsByTagName('Name')[0].childNodes[0].data
				data = data + str(mID) + ":" + MName +";"
	elif type == "RES_ITEM_TYPE_EQUIP":
		for equip in equips:
			mID = int(equip.getElementsByTagName('Id')[0].childNodes[0].data)
			MName = equip.getElementsByTagName('Name')[0].childNodes[0].data
			data = data + str(mID) + ":" + MName +";"
		
	return HttpResponse(data)

@csrf_exempt  
def searchPlayerInfo(request):
	if request.user.is_authenticated == 0:
		return HttpResponse("请登录")
		
	channel = request.POST.get("channel",'')
	server  = request.POST.get("server",'')
	type    = request.POST.get("type",'')
	para    = request.POST.get("para",'')
	str_uid = ""
	data = ""
	if type == "roleid":
		sqlquery = "select roleid, uid, role_name, level, vip_level, last_login_time, total_recharge_number,channel from player where roleid="+para

	else:	#角色名
		str_name = para.encode('utf-8')
		sqlquery = "select roleid, uid, role_name, level, vip_level, last_login_time, total_recharge_number,channel from player where role_name='"+str_name+"'"
	if server=="10000":
		DB_ADDR = DB_ADDR0
		#DB_PAY_ADDR = DB_PAY_ADDR0
	elif server=="1":
		DB_ADDR = DB_ADDR1
		#DB_PAY_ADDR = DB_PAY_ADDR1
	elif server == "2":
		DB_ADDR = DB_ADDR2
		#DB_PAY_ADDR = DB_PAY_ADDR2
	elif server == "3":
		DB_ADDR = DB_ADDR3
		#DB_PAY_ADDR = DB_PAY_ADDR3
	elif server == "4":
		DB_ADDR = DB_ADDR4
		#DB_PAY_ADDR = DB_PAY_ADDR4
	else:
		return HttpResponse('Server Error')
	db = MySQLdb.connect(DB_ADDR,DB_USER_NAME,DB_USER_PSW,DB_NAME, charset = "utf8" )
	cursor = db.cursor()
	cursor.execute(sqlquery)
	result = cursor.fetchone()
	cursor.close()
	if result == None:
		return HttpResponse("-_-_-_-_-_-_-$")
	str_uid=str(result[1])
	str_rolename = result[2].encode('utf-8')
	str_roleid = str(result[0])	
	data = str_roleid+"_"+str(result[1])+"_"+result[2]+"_"+str(result[3])+"_"+str(result[4])+"_"+str(result[5])+"_"+str(result[6])+"_"+str(result[7]) + "_"
	str_channel = str(result[7])
	#查询渠道ID
	db = MySQLdb.connect(DB_PAY_ADDR,DB_USER_NAME,DB_USER_PSW,"dgame_account", charset = "utf8" )
	sqlquery = "select account_id, channel from user where uid = "+str_uid;
	cursor = db.cursor()
	cursor.execute(sqlquery)
	result = cursor.fetchone()
	cursor.close()
	if result!=None:
		
		if str_channel == 'mzw':
			str_accountId = str_accountId[0:len(str_accountId)-3]
		elif str_channel == 'xiaomi':
			str_accountId = str_accountId[0:len(str_accountId)-6]
		elif str_channel == 'uc':
			str_accountId = str_accountId[0:len(str_accountId)-2]
		elif str_channel == 'baidu':
			str_accountId = str_accountId[0:len(str_accountId)-5]
		elif str_channel == 'qihu':
			str_accountId = str_accountId[0:len(str_accountId)-4]
		elif str_channel == 'tencent':
			str_accountId = str_accountId[0:len(str_accountId)-7]
		else:
			# 越狱渠道xy haima i4
			str_accountId = result[0]
	data += str_accountId
	data += "$"
	#暂时屏蔽充值的
	#return HttpResponse(data)  
	#查询充值记录	
	sqlquery = ""
	if channel=="mzw":
		sqlquery = "select insert_time, money from dgame_pay.mzw_pay where uid="+str_uid
		
	elif channel=="xiaomi":
		sqlquery = "select insert_time, payFee from dgame_pay.xiaomi_pay where uid='"+str_uid+"'"
		
	elif channel=="uc":
		sqlquery = "select insert_time, amount from dgame_pay.uc_pay where uid="+str_uid	
		
	elif channel=="baidu":
		sqlquery = "select insert_time, OrderMoney from dgame_pay.baidu_pay where uid="+str_uid	
	
	elif channel=="qihu":
		sqlquery = "select insert_time, amount from dgame_pay.qihu_pay where uid="+str_uid	
	
	elif channel=="tencent":
		sqlquery = "select insert_time, amt from dgame_pay.tencent_pay where uid="+str_uid	
	
	else:
		#越狱渠道
		sqlquery = "select insert_time, amount, is_drawn, zoneid from dgame_pay.moyo_pay where uid="+str_uid

	if sqlquery != "":
		cursor = db.cursor()
		cursor.execute(sqlquery)
		result = cursor.fetchall()	
		if result != None:
			for record in result:
				#只显示该区的充值记录
				zoneid = record[3]
				if zoneid != ZoneId and zoneid != 0:
					continue
				if channel == "MZW" or channel == "XM" or channel == "UC":
					data =data + record[0].strftime("%Y-%m-%d %H:%M:%S")+"_"+record[1]+"_"
				else:
					data =data + record[0].strftime("%Y-%m-%d %H:%M:%S")+"_"+str(record[1])+"_"+str(record[2])+"_"+str(zoneid)+"_"
	return HttpResponse(data)		

import cs_manage_pb2
from .utils import *
from item_prompt_pb import *
import string
import socket
import time

def searchBanInfo(request, type, para, channel, server):
	if request.user.is_authenticated == 0:
		return HttpResponse("请登录")
	str_roleid=""
	str_uid=""
	str_rolename=""
	str_banlogintime=""
	if type=="roleid":
		sqlquery = "select roleid, uid, role_name, ban_login_time from player where roleid=" +para

	else:
		str_name = para.encode('utf-8')
		sqlquery = "select  roleid, uid, role_name, ban_login_time from player where role_name='" +str_name+"'"
	
	# 连游戏服
	if server=="10000":
		DB_ADDR = DB_ADDR0
	elif server=="1":
		DB_ADDR = DB_ADDR1
	elif server == "2":
		DB_ADDR = DB_ADDR2
	elif server == "3":
		DB_ADDR = DB_ADDR3
	elif server == "4":
		DB_ADDR = DB_ADDR4
	else:
		return HttpResponse('Server Error')
	db = MySQLdb.connect(DB_ADDR,DB_USER_NAME,DB_USER_PSW,DB_NAME, charset = "utf8" )
	cursor = db.cursor()
	cursor.execute(sqlquery)
	result = cursor.fetchone()
	cursor.close()
	if result == None:
		return HttpResponse("-_-_-_-")
	str_roleid =  str(result[0])
	str_uid	   =  str(result[1])
	str_rolename= result[2].encode('utf-8')
	str_banlogintime = str(result[3])


	#根据roleid构造message发送给服务器，返回禁言状态和禁言截止时间
	queryChatReq = cs_manage_pb2.QueryBanUserChatStatusReq()
	queryChatReq.player_roleid = int(str_roleid)

	#发送message
	#服务器id
	if server != '':
		#连接帐号服数据库----dgame_account库， 查询服务器列表IP表 ----shard表
		db = MySQLdb.connect(DB_PAY_ADDR,DB_USER_NAME,DB_USER_PSW,"dgame_account", charset = "utf8" )
		str_svr_id = server.encode('utf-8')
		sqlquery = "select id, name, ip, port  from shard where id='"+str_svr_id+"'";
		cursor = db.cursor()
		cursor.execute(sqlquery)
		result = cursor.fetchone()
		cursor.close()
		if result!=None:
			PROTOLSERVER = result[2]
			conn = Connector(PROTOLSERVER, PROTOLSERVERPORT)	
			conn.set_header(SPECIAL_ROLEID, 2, "sessionid", 4, "protocol.RegistSession")
			RegistSession = ss_router_pb2.RegistSession()
			RegistSession.session_name = "gmt"
			conn.send(RegistSession)

			conn.set_header(SPECIAL_ROLEID, 2, "sessionid", 4, "CS.QueryBanUserChatStatusReq")
			conn.send(queryChatReq)

			#接收message
			queryChatRsp = cs_manage_pb2.QueryBanUserChatStatusRsp()
			conn.recv(queryChatRsp)

			if queryChatRsp.ban_finish_time < time.time():
				statue = "正常"
			else:
				statue = "禁言"
			ban_finish_time =str(queryChatRsp.ban_finish_time)
			data = str_roleid+"_"+str_uid+"_"+str_rolename+"_"+statue+"_"+ban_finish_time+"_"+str_banlogintime
			conn.close()
			return HttpResponse(data)
		else:
			return HttpResponse("server error")

@csrf_exempt  
def sendMail(request):
	if request.user.is_authenticated == 0:
		return HttpResponse("请登录")
		
	privilege = len(request.user.get_all_permissions())
	if 0 == privilege:
		return HttpResponse("你没有该模块权限")
			
	sendMailReq = cs_manage_pb2.SendManageSystemMailReq()
	#接收从页面传送过来的数据
	uidlist		= request.POST.get("uidlist",'')
	server		= request.POST.get("server",'')
	mailtitle 	= request.POST.get("mailtitle",'')
	mailcontent = request.POST.get("mailcontent",'')
	isAllPlayer = request.POST.get("isAllPlayer",'')
	strRewardType  = request.POST.get("RewardType",'')
	strRewardId    = request.POST.get("RewardId",'0')
	strRewardCount = request.POST.get("RewardCount",'')
	uids = uidlist.split(',')
	#判断邮件受众类型
	if str(isAllPlayer) == "true":
		sendMailReq.player_type = cs_manage_pb2.MAIL_PLAYER_TYPE_ALL
	elif len(uids) == 1:
		sendMailReq.player_type = cs_manage_pb2.MAIL_PLAYER_TYPE_SINGLE
	else:
		sendMailReq.player_type = cs_manage_pb2.MAIL_PLAYER_TYPE_MULTIPLE
		
	if isAllPlayer == "false":
		for uid in uids:
			if uid != '':
				sendMailReq.roleid_list.append(string.atol(uid))
	
	sendMailReq.mail.title = mailtitle
	sendMailReq.mail.msg   = mailcontent
	
	RewardTypes = strRewardType.split('|')
	RewardIds = strRewardId.split('|')
	RewardCounts = strRewardCount.split('|')
	#假如物品数量为0，则不发送奖励，只是发送普通的系统邮件
	for i in range(0, len(RewardIds)):
		if RewardTypes[i] != '' and RewardCounts[i] != '':
			print (RewardTypes[i], RewardIds[i], RewardCounts[i])
			attach = sendMailReq.mail.attach_list.attach.add()
			attach.num = int(RewardCounts[i])
			attach.goods_id = int(RewardIds[i])
			if RewardTypes[i] == "RES_ITEM_TYPE_MATERIAL":
				attach.type = 1
			elif RewardTypes[i] == "RES_ITEM_TYPE_TOOL":
				attach.type = 2
			elif RewardTypes[i] == "RES_ITEM_TYPE_EQUIP":
				attach.type = 11
			elif RewardTypes[i] == "RES_COST_TYPE_GOLD":
				attach.type = 6
			elif RewardTypes[i] == "RES_ITEM_TYPE_DRAGON_BLOOD":
				attach.type = 16
			elif RewardTypes[i] == "RES_ITEM_TYPE_MAGIC_CRYSTAL":
				attach.type = 18
			elif RewardTypes[i] == "RES_ITEM_TYPE_TAILSMAN":
				attach.type = 19
			else:
				attach.type = 7
		#	attach.num = 1
		#	attach.goods_id = 51000001
		#	attach.type = 	12
			print ("attach: {}, {}, {}", attach.type, attach.num, attach.goods_id)
 #服务器id
	if server != '':
		#连接帐号服数据库----dgame_account库， 查询服务器列表IP表 ----shard表
		db = MySQLdb.connect(DB_PAY_ADDR,DB_USER_NAME,DB_USER_PSW,"dgame_account", charset = "utf8" )
		str_svr_id = server.encode('utf-8')
		sqlquery = "select id, name, ip, port  from shard where id='"+str_svr_id+"'";
		cursor = db.cursor()
		cursor.execute(sqlquery)
		result = cursor.fetchone()
		cursor.close()
		if result!=None:
			PROTOLSERVER = result[2]
			conn = Connector(PROTOLSERVER, PROTOLSERVERPORT)	
			conn.set_header(SPECIAL_ROLEID, 2, "sessionid", 4, "protocol.RegistSession")
			RegistSession = ss_router_pb2.RegistSession()
			RegistSession.session_name = "gmt"
			conn.send(RegistSession)
	
			conn.set_header(9999, 2, "sessionid", 4, "CS.SendManageSystemMailReq")
			conn.send(sendMailReq)
			print (sendMailReq)

			sendMailRsp = cs_manage_pb2.SendManageSystemMailRsp()
			conn.recv(sendMailRsp)
			conn.close()
			print (sendMailRsp.result)
	
		if sendMailRsp.result == 0:
			return HttpResponse("邮件发送成功")
		else:
			return HttpResponse("邮件发送失败")
	
@csrf_exempt
def banPlayer(request):
	if request.user.is_authenticated == 0:
		return HttpResponse("请登录")
	privilege = len(request.user.get_all_permissions())
	if 0 == privilege:
		return HttpResponse("你没有该模块权限")
			
	
	banType = request.POST.get("banType",'0')
	banTime = request.POST.get("banTime",'0')
	roleid  = request.POST.get("roleid",'0')
	server  = request.POST.get("server",'0')
	#服务器id
	if server != '':
		#连接帐号服数据库----dgame_account库， 查询服务器列表IP表 ----shard表
		db = MySQLdb.connect(DB_PAY_ADDR,DB_USER_NAME,DB_USER_PSW,"dgame_account", charset = "utf8" )
		str_svr_id = server.encode('utf-8')
		sqlquery = "select id, name, ip, port  from shard where id='"+str_svr_id+"'";
		cursor = db.cursor()
		cursor.execute(sqlquery)
		result = cursor.fetchone()
		cursor.close()
		if result!=None:
			PROTOLSERVER = result[2]
			print ("ban time: {}", banTime)
			conn = Connector(PROTOLSERVER, PROTOLSERVERPORT)	
			conn.set_header(SPECIAL_ROLEID, 2, "sessionid", 4, "protocol.RegistSession")
			RegistSession = ss_router_pb2.RegistSession()
			RegistSession.session_name = "gmt"
			conn.send(RegistSession)
	
			if banType == "0":			#禁言
				banUserChatReq = cs_manage_pb2.BanUserChatReq()
				banUserChatReq.player_roleid = int(roleid)
				banUserChatReq.ban_time_length = int(banTime)
				conn.set_header(SPECIAL_ROLEID, 2, "sessionid", 4, "CS.BanUserChatReq")
				conn.send(banUserChatReq)
				banUserChatRsp = cs_manage_pb2.BanUserChatRsp()
				conn.recv(banUserChatRsp)
				conn.close()
				print (banUserChatRsp.result)
				if banUserChatRsp.result == 0:
					return HttpResponse("禁言成功")
				else:
					return HttpResponse("禁言失败")
			
			elif banType == "1":		#封禁
				banUserAccountReq = cs_manage_pb2.BanUserAccountReq()
				banUserAccountReq.player_roleid = int(roleid)
				banUserAccountReq.ban_time_length = int(banTime)
				conn.set_header(SPECIAL_ROLEID, 2, "sessionid", 4, "CS.BanUserAccountReq")
				conn.send(banUserAccountReq)
				banUserAccountRsp = cs_manage_pb2.BanUserAccountRsp()
				conn.recv(banUserAccountRsp)
				conn.close()
				print (banUserAccountRsp.result)
				if banUserAccountRsp.result == 0:
					return HttpResponse("封禁成功")
				else:
					return HttpResponse("封禁失败")
		
			elif banType == "2":		#解除禁言
				liftBanChatReq = cs_manage_pb2.LiftBanChatReq()
				liftBanChatReq.player_roleid = int(roleid)
		
				conn.set_header(SPECIAL_ROLEID, 2, "sessionid", 4, "CS.LiftBanChatReq")
				conn.send(liftBanChatReq)
				liftBanChatRsp = cs_manage_pb2.LiftBanChatRsp()
				conn.recv(liftBanChatRsp)
				conn.close()
				print (liftBanChatRsp.result)
				if liftBanChatRsp.result == 0:
					return HttpResponse("解除禁言成功")
				else:
					return HttpResponse("解除禁言失败")
		
			elif banType == "3":		#解除封禁
				liftBanAccountReq = cs_manage_pb2.LiftBanAccountReq()
				liftBanAccountReq.player_roleid = int(roleid)
		
				conn.set_header(SPECIAL_ROLEID, 2, "sessionid", 4, "CS.LiftBanAccountReq")
				conn.send(liftBanAccountReq)
				liftBanAccountRsp = cs_manage_pb2.LiftBanAccountRsp()
				conn.recv(liftBanAccountRsp)
				conn.close()
				print ("liftBanAccountRsp.result: {}", liftBanAccountRsp.result)
				if liftBanAccountRsp.result == 0:
					return HttpResponse("解除封禁成功")
				else:
					return HttpResponse("解除封禁失败")
		
			else:
				return HttpResponse("error")
	else:
		return HttpResponse("server error")

def searchGmInfo(request, type, para, channel, server):
	if request.user.is_authenticated == 0:
		return HttpResponse("请登录")
	str_roleid=""
	str_uid=""
	str_rolename=""
	str_banlogintime=""
	if type=="roleid":
		sqlquery = "select roleid, role_name, gm_previllege from player where roleid=" +para

	else:
		str_name = para.encode('utf-8')
		sqlquery = "select roleid, role_name, gm_previllege from player where role_name='" +str_name+"'"
	
	if server=="10000":
		DB_ADDR = DB_ADDR0
	elif server=="1":
		DB_ADDR = DB_ADDR1
	elif server == "2":
		DB_ADDR = DB_ADDR2
	elif server == "3":
		DB_ADDR = DB_ADDR3
	elif server == "4":
		DB_ADDR = DB_ADDR4
	else:
		return HttpResponse('Server Error')
	db = MySQLdb.connect(DB_ADDR,DB_USER_NAME,DB_USER_PSW,DB_NAME, charset = "utf8" )
	cursor = db.cursor()
	cursor.execute(sqlquery)
	result = cursor.fetchone()
	cursor.close()
	if result == None:
		return HttpResponse("-_-_-")
	str_roleid =  str(result[0])
	str_rolename= result[1].encode('utf-8')
	str_gm_privilege = str(result[2])

	data = str_roleid+"_"+str_rolename+"_"+str_gm_privilege
	return HttpResponse(data)

@csrf_exempt
def setGmPrivilege(request, roleid, set_gm_privilege, server):
	if request.user.is_authenticated == 0:
		return HttpResponse("请登录")
	privilege = len(request.user.get_all_permissions())
	if 0 == privilege:
		return HttpResponse("你没有该模块权限")
			
	serverid = request.POST.get("server",'')
	print ("roleid : {}", roleid, "set_gm_privilege : {}", set_gm_privilege)
	#服务器id
	if server != '':
		#连接帐号服数据库----dgame_account库， 查询服务器列表IP表 ----shard表
		db = MySQLdb.connect(DB_PAY_ADDR,DB_USER_NAME,DB_USER_PSW,"dgame_account", charset = "utf8" )
		str_svr_id = server.encode('utf-8')
		sqlquery = "select id, name, ip, port  from shard where id='"+str_svr_id+"'";
		cursor = db.cursor()
		cursor.execute(sqlquery)
		result = cursor.fetchone()
		cursor.close()
		if result!=None:
			PROTOLSERVER = result[2]
			conn = Connector(PROTOLSERVER, PROTOLSERVERPORT)	
			conn.set_header(SPECIAL_ROLEID, 2, "sessionid", 4, "protocol.RegistSession")
			RegistSession = ss_router_pb2.RegistSession()
			RegistSession.session_name = "gmt"
			conn.send(RegistSession)
	
			set_gm_privilege_req = cs_manage_pb2.SetGmPrivilegeLevelReq()
			set_gm_privilege_req.roleid = int(roleid)
			set_gm_privilege_req.level = int(set_gm_privilege)
	
			conn.set_header(SPECIAL_ROLEID, 2, "sessionid", 4, "CS.SetGmPrivilegeLevelReq")
			conn.send(set_gm_privilege_req)
	
			set_gm_privilege_rsp = cs_manage_pb2.SetGmPrivilegeLevelRsp()
			conn.recv(set_gm_privilege_rsp)
			conn.close()
			print ("set_gm_privilege_rsp.result: {}", set_gm_privilege_rsp.result)
			if set_gm_privilege_rsp.result == 0:
				return HttpResponse("设置GM权限等级成功")
			else:
				return HttpResponse("玩家不在线")
		else:
			return HttpResponse('Server Error')

@csrf_exempt  #全服邮件奖励
def sendAllMail(request):
	if request.user.is_authenticated == 0:
		return HttpResponse("请登录")
		
	privilege = len(request.user.get_all_permissions())
	if 0 == privilege:
		return HttpResponse("你没有该模块权限")
			
	sendMailReq = cs_manage_pb2.SendManageSystemMailReq()
	#接收从页面传送过来的数据
	serverlist		= request.POST.get("ServerList",'')
	MailLimitLowerLevel 	= request.POST.get("MailLimitLowerLevel",'')
	MailLimitHigherLevel = request.POST.get("MailLimitHigherLevel",'')
	MailLimitLowerVipLevel = request.POST.get("MailLimitLowerVipLevel",'')
	MailLimitHigherVipLevel  = request.POST.get("MailLimitHigherVipLevel",'')
	MailStartTime    = request.POST.get("MailStartTime",'0')
	MailEndTime = request.POST.get("MailEndTime",'')
	
	mailtitle 	= request.POST.get("mailtitle",'')
	mailcontent = request.POST.get("mailcontent",'')
	isAllPlayer = request.POST.get("isAllPlayer",'')
	strRewardType  = request.POST.get("RewardType",'')
	strRewardId    = request.POST.get("RewardId",'0')
	strRewardCount = request.POST.get("RewardCount",'')
	
	sendMailReq.cond.MailLimitLowerLevel = string.atol(MailLimitLowerLevel)
	sendMailReq.cond.MailLimitHigherLevel = string.atol(MailLimitHigherLevel)
	sendMailReq.cond.MailLimitLowerVipLevel = string.atol(MailLimitLowerVipLevel)
	sendMailReq.cond.MailLimitHigherVipLevel = string.atol(MailLimitHigherVipLevel)
	sendMailReq.cond.MailStartTime = MailStartTime
	sendMailReq.cond.MailEndTime = MailEndTime
	
	#邮件受众类型
	sendMailReq.player_type = cs_manage_pb2.MAIL_PLAYER_TYPE_COND_MULTIPLE
	serverids = serverlist.split(',')
	dict_server_arr = {}
	data = ""
	#服务器id
	for server in serverids:
		if server != '':
			#连接帐号服数据库----dgame_account库， 查询服务器列表IP表 ----shard表
			db = MySQLdb.connect(DB_PAY_ADDR,DB_USER_NAME,DB_USER_PSW,"dgame_account", charset = "utf8" )
			str_svr_id = server.encode('utf-8')
			sqlquery = "select id, name, ip, port  from shard where id='"+str_svr_id+"'";
			cursor = db.cursor()
			cursor.execute(sqlquery)
			result = cursor.fetchone()
			cursor.close()
			if result!=None:
				dict_server_arr[server] = result[2]
	sendMailReq.mail.title = mailtitle
	sendMailReq.mail.msg   = mailcontent
	RewardTypes = strRewardType.split('|')
	RewardIds = strRewardId.split('|')
	RewardCounts = strRewardCount.split('|')
	#假如物品数量为0，则不发送奖励，只是发送普通的系统邮件
	for i in range(0, len(RewardIds)):
		if RewardTypes[i] != '' and RewardCounts[i] != '':
			print (RewardTypes[i], RewardIds[i], RewardCounts[i])
			attach = sendMailReq.mail.attach_list.attach.add()
			attach.num = int(RewardCounts[i])
			attach.goods_id = int(RewardIds[i])
			if RewardTypes[i] == "RES_ITEM_TYPE_MATERIAL":
				attach.type = 1
			elif RewardTypes[i] == "RES_ITEM_TYPE_TOOL":
				attach.type = 2
			elif RewardTypes[i] == "RES_ITEM_TYPE_EQUIP":
				attach.type = 11
			elif RewardTypes[i] == "RES_COST_TYPE_GOLD":
				attach.type = 6
			elif RewardTypes[i] == "RES_ITEM_TYPE_DRAGON_BLOOD":
				attach.type = 16
			elif RewardTypes[i] == "RES_ITEM_TYPE_MAGIC_CRYSTAL":
				attach.type = 18
			elif RewardTypes[i] == "RES_ITEM_TYPE_TAILSMAN":
				attach.type = 19
			else:
				attach.type = 7
		#	attach.num = 1
		#	attach.goods_id = 51000001
		#	attach.type = 	12
			print ("attach: {}, {}, {}", attach.type, attach.num, attach.goods_id)
	# 遍历server id数组， 创建socket链接
	import types
	for k in dict_server_arr:
		v = dict_server_arr.get(k)
		if type(v) is types.ListType: #如果数据是list类型，继续遍历
			print (k, '---')
			for kk, vv in enumerate(v):
				print (kk, vv)
			print ('---')
		else:
			#之前的这个gmt直连game_svr进行通信,  现在要gmt ---> master_svr ---> game_svr 
			# 读global.ini, 设置master_svr 端口
			PROTOLSERVER = dict_server_arr.get(k)
			conn = Connector(PROTOLSERVER, PROTOLSERVERPORT)	
			conn.set_header(SPECIAL_ROLEID, 2, "sessionid", 4, "protocol.RegistSession")
			RegistSession = ss_router_pb2.RegistSession()
			RegistSession.session_name = "gmt"
			conn.send(RegistSession)
			
			conn.set_header(9999, 2, "sessionid", 4, "CS.SendManageSystemMailReq")
			conn.send(sendMailReq)
			print (sendMailReq)

			sendMailRsp = cs_manage_pb2.SendManageSystemMailRsp()
			conn.recv(sendMailRsp)
			conn.close()
			print (sendMailRsp.result)
			
			if sendMailRsp.result == 0:
				data += '<pre>'"^_^" + PROTOLSERVER.encode('utf-8') + "区邮件发送成功"+'</pre>'
			else:
				data += '<pre>'"^_^" + PROTOLSERVER.encode('utf-8') + "区邮件发送失败"+'</pre>'
	
	return HttpResponse(data)


import os
import re
import json
# 公告管理
def notice(request):
	if request.user.is_authenticated == 0:
		return HttpResponse("请登录")
	channelNumber		= request.GET.get("channelNumber",'')
	subChannelNumber	= request.GET.get("subChannelNumber",'')
	serverNumber 		= request.GET.get("serverNumber",'')
	title1				= request.GET.get("title1",'')
	title2				= request.GET.get("title2",'')
	title3				= request.GET.get("title3",'')
	title4				= request.GET.get("title4",'')
	title5				= request.GET.get("title5",'')
	content				= request.GET.get("content",'')
	contentArr = content.split('akb48');
	if content != "" :
		data = ""
		data += "[Server]\n"
		data += "channelNumber=" + channelNumber +"\n"
		data += "subChannelNumber=" + subChannelNumber +"\n"
		data += "serverNumber=" + serverNumber +"\n"
		data += "[TitleList]\n"
		data += "title1=" +'"'+title1+'"' + "\n"
		data += "title2=" +'"'+title2+'"' + "\n"
		data += "title3=" +'"'+title3 +'"'+ "\n"
		data += "title4=" +'"'+title4+'"' + "\n"
		data += "title5=" +'"'+title5+'"' + "\n"
		data += "[ContentList]\n"
		for index, cont in enumerate(contentArr):
			if cont != '':
				data += "msg"+str(index +1)+"="+'"'+ cont+'"' + "\n"
		strinfo = re.compile('<br />')
		data = strinfo.sub('',data)
		strinfo = re.compile('&nbsp;')
		data = strinfo.sub(' ',data)
		strinfo = re.compile('<div>')
		data = strinfo.sub('',data)
		strinfo = re.compile('</div>')
		data = strinfo.sub('',data)
		strinfo = re.compile('<span>')
		data = strinfo.sub('',data)
		strinfo = re.compile('</span>')
		data = strinfo.sub('',data)
		strinfo = re.compile('<p>')
		data = strinfo.sub('',data)
		strinfo = re.compile('</p>')
		data = strinfo.sub('',data)
		#json 格式数据
		#json_data = json.dumps(strdata)
		f = file('gg.ini', 'w') # open for 'w'riting 
		f.write(data.encode('utf-8')) 
		f.close() # close the file
		return HttpResponse("公告发布成功")
	else:
		return render(request, 'dgame/notice/news.html')


def saveRTF(request,channelNumber, subChannelNumber, serverNumber, title, content):
	if request.user.is_authenticated == 0:
		return HttpResponse("请登录")
		
	privilege = len(request.user.get_all_permissions())
	if 0 == privilege:
		return HttpResponse("你没有该模块权限")
	
	#接收从页面传送过来的数据
	channelNumber		= request.POST.get("channelNumber",'')
	subChannelNumber	= request.POST.get("subChannelNumber",'')
	serverNumber 		= request.POST.get("serverNumber",'')
	title				= request.POST.get("title",'')
	content				= request.POST.get("content",'')

#if sendMailRsp.result == 0:
	return HttpResponse("公告发布成功!")
#else:
#	return HttpResponse("公告发布失败")
