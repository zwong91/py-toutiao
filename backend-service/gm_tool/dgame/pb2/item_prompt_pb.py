#!/usr/bin/python3
import sys
sys.path.append("../../../python_test/inc/")
import login_pb2

def PromptHeader(header, msg_full_name):
	header.roleid = 6033575731089440930
	header.seq = 4421551
	header.sessionid = "asdfss"
	header.re_send_cnt = 155588
	header.msg_full_name = msg_full_name
	
def PromptEnchantEquip(enchant_equip, equip_gid, material_id):
	enchant_equip.equip_gid = equip_gid 
	enchant_equip.material_id = material_id 
	
def PromptEnhanceEquip(enchant_equip, equip_gid):
	enchant_equip.equip_gid = equip_gid 
	
def PromptAddBag(add_bag, type, id, num):
	add_bag.type = type 
	add_bag.id = id 
	add_bag.num = num 
	
def PromptGetBag(get_bag):
	get_bag.unused = 0 

	
