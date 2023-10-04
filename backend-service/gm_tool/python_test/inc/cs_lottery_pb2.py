# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs_lottery.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import dgame_define_pb2 as dgame__define__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cs_lottery.proto',
  package='CS',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x63s_lottery.proto\x12\x02\x43S\x1a\x12\x64game_define.proto\"#\n\x11GetLotteryFreeReq\x12\x0e\n\x06unused\x18\x01 \x01(\r\"\xf0\x02\n\x11GetLotteryFreeRsp\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12#\n\x1bgold_next_free_left_seconds\x18\x02 \x01(\r\x12&\n\x1e\x64iamond_next_free_left_seconds\x18\x03 \x01(\r\x12\x1c\n\x14gold_left_free_times\x18\x04 \x01(\r\x12%\n\x1d\x64iamond_get_hero_remain_times\x18\x05 \x01(\r\x12#\n\x1brune_next_free_left_seconds\x18\x06 \x01(\r\x12#\n\x1btotal_lottery_diamond_times\x18\x07 \x01(\x05\x12\'\n\x1ftotal_lottery_diamond_ten_times\x18\x08 \x01(\r\x12 \n\x18total_lottery_rune_times\x18\t \x01(\x05\x12$\n\x1ctotal_lottery_rune_ten_times\x18\n \x01(\r\"3\n\x12LotteryDrawCardReq\x12\x1d\n\x04type\x18\x01 \x01(\x0e\x32\x0f.CS.LotteryType\"\xab\x02\n\x12LotteryDrawCardRsp\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12/\n\x0clottery_item\x18\x02 \x01(\x0b\x32\x19.dgame.ExtractGiftBagItem\x12\x1e\n\x16next_free_left_seconds\x18\x03 \x01(\r\x12\x1c\n\x14gold_left_free_times\x18\x04 \x01(\r\x12\x18\n\x10is_cost_material\x18\x05 \x01(\x08\x12\x18\n\x10\x63ost_material_id\x18\x06 \x01(\r\x12\x19\n\x11\x63ost_material_num\x18\x07 \x01(\r\x12\x15\n\rcost_gold_num\x18\x08 \x01(\r\x12\x18\n\x10\x63ost_diamond_num\x18\t \x01(\r\x12\x16\n\x0enext_350_times\x18\n \x01(\r*\xa0\x01\n\x0bLotteryType\x12\x13\n\x0fLOTTERY_DEFAULT\x10\x00\x12\x10\n\x0cLOTTERY_GOLD\x10\x01\x12\x13\n\x0fLOTTERY_DIAMOND\x10\x02\x12\x17\n\x13LOTTERY_DIAMOND_TEN\x10\x03\x12\x14\n\x10LOTTERY_GOLD_TEN\x10\x04\x12\x10\n\x0cLOTTERY_RUNE\x10\x05\x12\x14\n\x10LOTTERY_RUNE_TEN\x10\x06\x62\x06proto3'
  ,
  dependencies=[dgame__define__pb2.DESCRIPTOR,])

_LOTTERYTYPE = _descriptor.EnumDescriptor(
  name='LotteryType',
  full_name='CS.LotteryType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LOTTERY_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOTTERY_GOLD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOTTERY_DIAMOND', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOTTERY_DIAMOND_TEN', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOTTERY_GOLD_TEN', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOTTERY_RUNE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOTTERY_RUNE_TEN', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=808,
  serialized_end=968,
)
_sym_db.RegisterEnumDescriptor(_LOTTERYTYPE)

LotteryType = enum_type_wrapper.EnumTypeWrapper(_LOTTERYTYPE)
LOTTERY_DEFAULT = 0
LOTTERY_GOLD = 1
LOTTERY_DIAMOND = 2
LOTTERY_DIAMOND_TEN = 3
LOTTERY_GOLD_TEN = 4
LOTTERY_RUNE = 5
LOTTERY_RUNE_TEN = 6



_GETLOTTERYFREEREQ = _descriptor.Descriptor(
  name='GetLotteryFreeReq',
  full_name='CS.GetLotteryFreeReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='unused', full_name='CS.GetLotteryFreeReq.unused', index=0,
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
  serialized_start=44,
  serialized_end=79,
)


_GETLOTTERYFREERSP = _descriptor.Descriptor(
  name='GetLotteryFreeRsp',
  full_name='CS.GetLotteryFreeRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='CS.GetLotteryFreeRsp.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gold_next_free_left_seconds', full_name='CS.GetLotteryFreeRsp.gold_next_free_left_seconds', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='diamond_next_free_left_seconds', full_name='CS.GetLotteryFreeRsp.diamond_next_free_left_seconds', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gold_left_free_times', full_name='CS.GetLotteryFreeRsp.gold_left_free_times', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='diamond_get_hero_remain_times', full_name='CS.GetLotteryFreeRsp.diamond_get_hero_remain_times', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rune_next_free_left_seconds', full_name='CS.GetLotteryFreeRsp.rune_next_free_left_seconds', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_lottery_diamond_times', full_name='CS.GetLotteryFreeRsp.total_lottery_diamond_times', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_lottery_diamond_ten_times', full_name='CS.GetLotteryFreeRsp.total_lottery_diamond_ten_times', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_lottery_rune_times', full_name='CS.GetLotteryFreeRsp.total_lottery_rune_times', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_lottery_rune_ten_times', full_name='CS.GetLotteryFreeRsp.total_lottery_rune_ten_times', index=9,
      number=10, type=13, cpp_type=3, label=1,
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
  serialized_start=82,
  serialized_end=450,
)


_LOTTERYDRAWCARDREQ = _descriptor.Descriptor(
  name='LotteryDrawCardReq',
  full_name='CS.LotteryDrawCardReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='CS.LotteryDrawCardReq.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=452,
  serialized_end=503,
)


_LOTTERYDRAWCARDRSP = _descriptor.Descriptor(
  name='LotteryDrawCardRsp',
  full_name='CS.LotteryDrawCardRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='CS.LotteryDrawCardRsp.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lottery_item', full_name='CS.LotteryDrawCardRsp.lottery_item', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_free_left_seconds', full_name='CS.LotteryDrawCardRsp.next_free_left_seconds', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gold_left_free_times', full_name='CS.LotteryDrawCardRsp.gold_left_free_times', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_cost_material', full_name='CS.LotteryDrawCardRsp.is_cost_material', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cost_material_id', full_name='CS.LotteryDrawCardRsp.cost_material_id', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cost_material_num', full_name='CS.LotteryDrawCardRsp.cost_material_num', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cost_gold_num', full_name='CS.LotteryDrawCardRsp.cost_gold_num', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cost_diamond_num', full_name='CS.LotteryDrawCardRsp.cost_diamond_num', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_350_times', full_name='CS.LotteryDrawCardRsp.next_350_times', index=9,
      number=10, type=13, cpp_type=3, label=1,
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
  serialized_start=506,
  serialized_end=805,
)

_LOTTERYDRAWCARDREQ.fields_by_name['type'].enum_type = _LOTTERYTYPE
_LOTTERYDRAWCARDRSP.fields_by_name['lottery_item'].message_type = dgame__define__pb2._EXTRACTGIFTBAGITEM
DESCRIPTOR.message_types_by_name['GetLotteryFreeReq'] = _GETLOTTERYFREEREQ
DESCRIPTOR.message_types_by_name['GetLotteryFreeRsp'] = _GETLOTTERYFREERSP
DESCRIPTOR.message_types_by_name['LotteryDrawCardReq'] = _LOTTERYDRAWCARDREQ
DESCRIPTOR.message_types_by_name['LotteryDrawCardRsp'] = _LOTTERYDRAWCARDRSP
DESCRIPTOR.enum_types_by_name['LotteryType'] = _LOTTERYTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetLotteryFreeReq = _reflection.GeneratedProtocolMessageType('GetLotteryFreeReq', (_message.Message,), {
  'DESCRIPTOR' : _GETLOTTERYFREEREQ,
  '__module__' : 'cs_lottery_pb2'
  # @@protoc_insertion_point(class_scope:CS.GetLotteryFreeReq)
  })
_sym_db.RegisterMessage(GetLotteryFreeReq)

GetLotteryFreeRsp = _reflection.GeneratedProtocolMessageType('GetLotteryFreeRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETLOTTERYFREERSP,
  '__module__' : 'cs_lottery_pb2'
  # @@protoc_insertion_point(class_scope:CS.GetLotteryFreeRsp)
  })
_sym_db.RegisterMessage(GetLotteryFreeRsp)

LotteryDrawCardReq = _reflection.GeneratedProtocolMessageType('LotteryDrawCardReq', (_message.Message,), {
  'DESCRIPTOR' : _LOTTERYDRAWCARDREQ,
  '__module__' : 'cs_lottery_pb2'
  # @@protoc_insertion_point(class_scope:CS.LotteryDrawCardReq)
  })
_sym_db.RegisterMessage(LotteryDrawCardReq)

LotteryDrawCardRsp = _reflection.GeneratedProtocolMessageType('LotteryDrawCardRsp', (_message.Message,), {
  'DESCRIPTOR' : _LOTTERYDRAWCARDRSP,
  '__module__' : 'cs_lottery_pb2'
  # @@protoc_insertion_point(class_scope:CS.LotteryDrawCardRsp)
  })
_sym_db.RegisterMessage(LotteryDrawCardRsp)


# @@protoc_insertion_point(module_scope)