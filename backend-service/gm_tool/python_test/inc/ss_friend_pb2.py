# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ss_friend.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ss_friend.proto',
  package='SS',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fss_friend.proto\x12\x02SS\"\"\n\x10GetFriendListReq\x12\x0e\n\x06unused\x18\x01 \x01(\r\";\n\x10GetFriendListRsp\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x17\n\x0f\x66ri_roleid_list\x18\x02 \x03(\x04\"P\n\x14GetFriGiftStaminaReq\x12\x17\n\x0f\x66ri_roleid_list\x18\x01 \x03(\x04\x12\x1f\n\x17max_can_get_stamina_num\x18\x02 \x01(\x04\"X\n\x14GetFriGiftStaminaRsp\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x17\n\x0fget_stamina_num\x18\x02 \x01(\r\x12\x17\n\x0fnew_stamina_num\x18\x03 \x01(\rb\x06proto3'
)




_GETFRIENDLISTREQ = _descriptor.Descriptor(
  name='GetFriendListReq',
  full_name='SS.GetFriendListReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='unused', full_name='SS.GetFriendListReq.unused', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=57,
)


_GETFRIENDLISTRSP = _descriptor.Descriptor(
  name='GetFriendListRsp',
  full_name='SS.GetFriendListRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='SS.GetFriendListRsp.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fri_roleid_list', full_name='SS.GetFriendListRsp.fri_roleid_list', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=118,
)


_GETFRIGIFTSTAMINAREQ = _descriptor.Descriptor(
  name='GetFriGiftStaminaReq',
  full_name='SS.GetFriGiftStaminaReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fri_roleid_list', full_name='SS.GetFriGiftStaminaReq.fri_roleid_list', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_can_get_stamina_num', full_name='SS.GetFriGiftStaminaReq.max_can_get_stamina_num', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=200,
)


_GETFRIGIFTSTAMINARSP = _descriptor.Descriptor(
  name='GetFriGiftStaminaRsp',
  full_name='SS.GetFriGiftStaminaRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='SS.GetFriGiftStaminaRsp.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='get_stamina_num', full_name='SS.GetFriGiftStaminaRsp.get_stamina_num', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_stamina_num', full_name='SS.GetFriGiftStaminaRsp.new_stamina_num', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=290,
)

DESCRIPTOR.message_types_by_name['GetFriendListReq'] = _GETFRIENDLISTREQ
DESCRIPTOR.message_types_by_name['GetFriendListRsp'] = _GETFRIENDLISTRSP
DESCRIPTOR.message_types_by_name['GetFriGiftStaminaReq'] = _GETFRIGIFTSTAMINAREQ
DESCRIPTOR.message_types_by_name['GetFriGiftStaminaRsp'] = _GETFRIGIFTSTAMINARSP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFriendListReq = _reflection.GeneratedProtocolMessageType('GetFriendListReq', (_message.Message,), {
  'DESCRIPTOR' : _GETFRIENDLISTREQ,
  '__module__' : 'ss_friend_pb2'
  # @@protoc_insertion_point(class_scope:SS.GetFriendListReq)
  })
_sym_db.RegisterMessage(GetFriendListReq)

GetFriendListRsp = _reflection.GeneratedProtocolMessageType('GetFriendListRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETFRIENDLISTRSP,
  '__module__' : 'ss_friend_pb2'
  # @@protoc_insertion_point(class_scope:SS.GetFriendListRsp)
  })
_sym_db.RegisterMessage(GetFriendListRsp)

GetFriGiftStaminaReq = _reflection.GeneratedProtocolMessageType('GetFriGiftStaminaReq', (_message.Message,), {
  'DESCRIPTOR' : _GETFRIGIFTSTAMINAREQ,
  '__module__' : 'ss_friend_pb2'
  # @@protoc_insertion_point(class_scope:SS.GetFriGiftStaminaReq)
  })
_sym_db.RegisterMessage(GetFriGiftStaminaReq)

GetFriGiftStaminaRsp = _reflection.GeneratedProtocolMessageType('GetFriGiftStaminaRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETFRIGIFTSTAMINARSP,
  '__module__' : 'ss_friend_pb2'
  # @@protoc_insertion_point(class_scope:SS.GetFriGiftStaminaRsp)
  })
_sym_db.RegisterMessage(GetFriGiftStaminaRsp)


# @@protoc_insertion_point(module_scope)