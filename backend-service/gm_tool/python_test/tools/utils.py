#!/usr/bin/python3
import sys
sys.path.append("../inc/")
import struct
import header_pb2
from buffer import *
import socket
import binascii

class GenerateProtocol:
	def __init__(self):
		self.packet_len = 0
		self.header_len = 0
		self.header_pb = ""
		self.packet_pb = ""
	
	def set(self, header_pb, packet_pb):
		self.header_pb = header_pb
		self.packet_pb = packet_pb
		self.packet_len = len(packet_pb) + len(header_pb) + 8
		self.header_len = len(header_pb)
		
	def encode(self, buffer):
		buffer.put_int(self.packet_len)
		buffer.put_int(self.header_len)
		buffer.put_string(self.header_pb)
		buffer.put_string(self.packet_pb)
		# print "packet_len:", self.packet_len
		# print "header_len:", self.header_len
		# print "header_pb:", binascii.b2a_hex(self.header_pb)
		# print "packet_pb:", binascii.b2a_hex(self.packet_pb)
		
		
class Connector:
	def __init__(self, ip, port):
		self.timeout = 3
		socket.setdefaulttimeout(self.timeout)
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connect(ip, port)
		self.header_pb = header_pb2.Header()
		self.buf = Xlbuf()
		self.header = ""
		self.msg = ""
	
	def connect(self, ip, port):
		try:
			self.sock.connect((ip, port))
			#self.sock.setdefaulttimeout(self.timeout)
		except:
			(ErrorType, ErrorValue, ErrorTB) = sys.exc_info()
			print ("connect error: ", ErrorType, ErrorValue, ErrorTB)
			
	def get_sock(self):
		return self.sock
		
	def set_header(self, roleid = 1, seq = 2, sessionid = "sessionid", re_send_cnt = 3, msg_full_name = "SS.CreateRoleReq"):
		self.header_pb.roleid = roleid
		self.header_pb.seq = seq
		self.header_pb.sessionid = sessionid
		self.header_pb.re_send_cnt = re_send_cnt
		self.header_pb.msg_full_name = msg_full_name
		
	def get_header_pb_str(self):
		str_header_pb = self.header_pb.SerializeToString()
		return str_header_pb
		
		
	def send(self, msg_pb):
		str_msg_pb_pb = msg_pb.SerializeToString()
		#print "str_msg_pb_pb len:", len(str_msg_pb_pb)
		to_send = GenerateProtocol()
		to_send.set(self.get_header_pb_str(), str_msg_pb_pb)
		self.buf = Xlbuf()
		to_send.encode(self.buf)
		#print "send len:", len(self.buf.buf)
		self.sock.sendall(self.buf.buf)
		
	def recv(self, msg_pb):
		response = self.sock.recv(1024*50)
		buf = Xlbuf(response)	
		packet_len = buf.get_int_from_pos(0)
		print ("recv packet_len:", packet_len)
		header_len = buf.get_int_from_pos(4)
		#print "recv header_len:", header_len
		self.header = buf.get_string(8, 8 + header_len)
		self.msg = buf.get_string(8 + header_len, packet_len)
		#print "recv:", binascii.b2a_hex(self.msg)
		
		msg_pb.ParseFromString(self.msg)
	
	def get_header(self):
		return self.header
		
	def get_parsed_header(self):
		pased_header = header_pb2.Header()
		pased_header.ParseFromString(self.header)
		return pased_header
		
	def get_msg(self):
		return self.msg
		
	def print_header(self):
		str_header_pb = self.get_parsed_header()
		print ("==================")
		print ("roleid: ", str_header_pb.roleid)
		print ("seq: ", str_header_pb.seq)
		print ("sessionid: ", str_header_pb.sessionid)
		print ("re_send_cnt: ", str_header_pb.re_send_cnt)
		print ("msg_full_name: ", str_header_pb.msg_full_name)
			
	def close(self):
		self.sock.close
			
