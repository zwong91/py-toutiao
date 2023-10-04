#!/usr/bin/python3
import sys
sys.path.append("../../python_test/inc/")
import login_pb2

def PromptHeader(header, msg_full_name):
	header.roleid = 6031758556196308067
	header.seq = 4421551
	header.sessionid = "asdfss"
	header.re_send_cnt = 155588
	header.msg_full_name = msg_full_name
	
def PromptLogin(login):
	login.uid = 1
	login.seq = 2
	login.sessionid = "sessionid"
	
def PromptAccountLogin(account_login, account = "account"):
	account_login.account = account
	account_login.pwd = "pwd"
	#account_login.pwd = ""
	
def PromptRoleList(role_list, uid = 6032457398914975683):
	role_list.uid = uid
	
def PromptShardLogin(shard_login, uid = 6032457398914975683):
	shard_login.uid = uid
	
def PromptRoleLogin(role_login , roleid = 6032457398914975683):
	role_login.roleid = roleid
	
def PromptRoleLogout(role_logout):
	role_logout.unused = False

def PromptCreateRole(create_role, uid = 123456, role_name = "test_role_name"):
	create_role.uid = uid
	create_role.role_name = role_name
	create_role.plat = login_pb2.ANDROID
	create_role.head_id = 1
	
def PromptRandomName(random_name):
	role_logout.unused = 1
	
def PromptUniqueAccount(unique_account):
	unique_account.unused = 1
	
def PromptAddHero(add_hero, heroid = 110002):
	add_hero.heroid = heroid
	
def PromptSetRoleAttr(set_role_attr, type = 1, num = 10):
	set_role_attr.type = type
	set_role_attr.num = num
	
def PromptSetHeroAttr(set_role_attr, hero_gid = 6034763877957304961, type = 1, num = 10):
	set_role_attr.gid = hero_gid
	set_role_attr.type = type
	set_role_attr.num = num

