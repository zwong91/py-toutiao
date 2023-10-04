# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: activity_db.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='activity_db.proto',
  package='dgame',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x61\x63tivity_db.proto\x12\x05\x64game\"\xdf\x01\n\x1dRoleAccumRechargeActivityData\x12\x0e\n\x06roleid\x18\x01 \x01(\x04\x12\x0b\n\x03seq\x18\x02 \x01(\r\x12\x19\n\x11recharged_diamond\x18\x03 \x01(\r\x12V\n\x15\x64rawn_reward_seq_list\x18\x04 \x01(\x0b\x32\x37.dgame.RoleAccumRechargeActivityData.DrawnRewardSeqList\x1a.\n\x12\x44rawnRewardSeqList\x12\x18\n\x10\x64rawn_reward_seq\x18\x01 \x03(\r\"\xdc\x01\n\x1cRoleAccumConsumeActivityData\x12\x0e\n\x06roleid\x18\x01 \x01(\x04\x12\x0b\n\x03seq\x18\x02 \x01(\r\x12\x18\n\x10\x63onsumed_diamond\x18\x03 \x01(\r\x12U\n\x15\x64rawn_reward_seq_list\x18\x04 \x01(\x0b\x32\x36.dgame.RoleAccumConsumeActivityData.DrawnRewardSeqList\x1a.\n\x12\x44rawnRewardSeqList\x12\x18\n\x10\x64rawn_reward_seq\x18\x01 \x03(\r\"\xe1\x01\n\x1eRoleRechargeRebateActivityData\x12\x0e\n\x06roleid\x18\x01 \x01(\x04\x12\x0b\n\x03seq\x18\x02 \x01(\r\x12\x19\n\x11recharged_diamond\x18\x03 \x01(\r\x12W\n\x15\x64rawn_reward_seq_list\x18\x04 \x01(\x0b\x32\x38.dgame.RoleRechargeRebateActivityData.DrawnRewardSeqList\x1a.\n\x12\x44rawnRewardSeqList\x12\x18\n\x10\x64rawn_reward_seq\x18\x01 \x03(\r\"\xd4\x02\n\x0fRedEnvelopeData\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nproduct_id\x18\x03 \x01(\t\x12\x14\n\x0csplit_pieces\x18\x04 \x01(\r\x12\x13\n\x0bleft_pieces\x18\x05 \x01(\r\x12\x12\n\npiece_gold\x18\x06 \x01(\r\x12\x15\n\rpiece_diamond\x18\x07 \x01(\r\x12\r\n\x05giver\x18\x08 \x01(\x04\x12\x12\n\ngiver_name\x18\t \x01(\t\x12\x16\n\x0egenerated_time\x18\n \x01(\r\x12\x11\n\tsent_time\x18\x0b \x01(\r\x12\x13\n\x0b\x65xpire_time\x18\x0c \x01(\r\x12:\n\rreceiver_list\x18\r \x01(\x0b\x32#.dgame.RedEnvelopeData.ReceiverList\x1a\x1e\n\x0cReceiverList\x12\x0e\n\x06roleid\x18\x01 \x03(\x04\"d\n\x16\x43onsumeAndLimitBuyData\x12\x13\n\x0bsub_task_id\x18\x01 \x01(\r\x12\x18\n\x10has_buy_item_num\x18\x02 \x01(\r\x12\x1b\n\x13last_purchased_time\x18\x03 \x01(\rb\x06proto3'
)




_ROLEACCUMRECHARGEACTIVITYDATA_DRAWNREWARDSEQLIST = _descriptor.Descriptor(
  name='DrawnRewardSeqList',
  full_name='dgame.RoleAccumRechargeActivityData.DrawnRewardSeqList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='drawn_reward_seq', full_name='dgame.RoleAccumRechargeActivityData.DrawnRewardSeqList.drawn_reward_seq', index=0,
      number=1, type=13, cpp_type=3, label=3,
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
  serialized_start=206,
  serialized_end=252,
)

_ROLEACCUMRECHARGEACTIVITYDATA = _descriptor.Descriptor(
  name='RoleAccumRechargeActivityData',
  full_name='dgame.RoleAccumRechargeActivityData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='roleid', full_name='dgame.RoleAccumRechargeActivityData.roleid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seq', full_name='dgame.RoleAccumRechargeActivityData.seq', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recharged_diamond', full_name='dgame.RoleAccumRechargeActivityData.recharged_diamond', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='drawn_reward_seq_list', full_name='dgame.RoleAccumRechargeActivityData.drawn_reward_seq_list', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ROLEACCUMRECHARGEACTIVITYDATA_DRAWNREWARDSEQLIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=252,
)


_ROLEACCUMCONSUMEACTIVITYDATA_DRAWNREWARDSEQLIST = _descriptor.Descriptor(
  name='DrawnRewardSeqList',
  full_name='dgame.RoleAccumConsumeActivityData.DrawnRewardSeqList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='drawn_reward_seq', full_name='dgame.RoleAccumConsumeActivityData.DrawnRewardSeqList.drawn_reward_seq', index=0,
      number=1, type=13, cpp_type=3, label=3,
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
  serialized_start=206,
  serialized_end=252,
)

_ROLEACCUMCONSUMEACTIVITYDATA = _descriptor.Descriptor(
  name='RoleAccumConsumeActivityData',
  full_name='dgame.RoleAccumConsumeActivityData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='roleid', full_name='dgame.RoleAccumConsumeActivityData.roleid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seq', full_name='dgame.RoleAccumConsumeActivityData.seq', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='consumed_diamond', full_name='dgame.RoleAccumConsumeActivityData.consumed_diamond', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='drawn_reward_seq_list', full_name='dgame.RoleAccumConsumeActivityData.drawn_reward_seq_list', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ROLEACCUMCONSUMEACTIVITYDATA_DRAWNREWARDSEQLIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=255,
  serialized_end=475,
)


_ROLERECHARGEREBATEACTIVITYDATA_DRAWNREWARDSEQLIST = _descriptor.Descriptor(
  name='DrawnRewardSeqList',
  full_name='dgame.RoleRechargeRebateActivityData.DrawnRewardSeqList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='drawn_reward_seq', full_name='dgame.RoleRechargeRebateActivityData.DrawnRewardSeqList.drawn_reward_seq', index=0,
      number=1, type=13, cpp_type=3, label=3,
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
  serialized_start=206,
  serialized_end=252,
)

_ROLERECHARGEREBATEACTIVITYDATA = _descriptor.Descriptor(
  name='RoleRechargeRebateActivityData',
  full_name='dgame.RoleRechargeRebateActivityData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='roleid', full_name='dgame.RoleRechargeRebateActivityData.roleid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seq', full_name='dgame.RoleRechargeRebateActivityData.seq', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recharged_diamond', full_name='dgame.RoleRechargeRebateActivityData.recharged_diamond', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='drawn_reward_seq_list', full_name='dgame.RoleRechargeRebateActivityData.drawn_reward_seq_list', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ROLERECHARGEREBATEACTIVITYDATA_DRAWNREWARDSEQLIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=478,
  serialized_end=703,
)


_REDENVELOPEDATA_RECEIVERLIST = _descriptor.Descriptor(
  name='ReceiverList',
  full_name='dgame.RedEnvelopeData.ReceiverList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='roleid', full_name='dgame.RedEnvelopeData.ReceiverList.roleid', index=0,
      number=1, type=4, cpp_type=4, label=3,
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
  serialized_start=1016,
  serialized_end=1046,
)

_REDENVELOPEDATA = _descriptor.Descriptor(
  name='RedEnvelopeData',
  full_name='dgame.RedEnvelopeData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dgame.RedEnvelopeData.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='dgame.RedEnvelopeData.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product_id', full_name='dgame.RedEnvelopeData.product_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='split_pieces', full_name='dgame.RedEnvelopeData.split_pieces', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='left_pieces', full_name='dgame.RedEnvelopeData.left_pieces', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='piece_gold', full_name='dgame.RedEnvelopeData.piece_gold', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='piece_diamond', full_name='dgame.RedEnvelopeData.piece_diamond', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='giver', full_name='dgame.RedEnvelopeData.giver', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='giver_name', full_name='dgame.RedEnvelopeData.giver_name', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='generated_time', full_name='dgame.RedEnvelopeData.generated_time', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sent_time', full_name='dgame.RedEnvelopeData.sent_time', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expire_time', full_name='dgame.RedEnvelopeData.expire_time', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receiver_list', full_name='dgame.RedEnvelopeData.receiver_list', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_REDENVELOPEDATA_RECEIVERLIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=706,
  serialized_end=1046,
)


_CONSUMEANDLIMITBUYDATA = _descriptor.Descriptor(
  name='ConsumeAndLimitBuyData',
  full_name='dgame.ConsumeAndLimitBuyData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sub_task_id', full_name='dgame.ConsumeAndLimitBuyData.sub_task_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_buy_item_num', full_name='dgame.ConsumeAndLimitBuyData.has_buy_item_num', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_purchased_time', full_name='dgame.ConsumeAndLimitBuyData.last_purchased_time', index=2,
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
  serialized_start=1048,
  serialized_end=1148,
)

_ROLEACCUMRECHARGEACTIVITYDATA_DRAWNREWARDSEQLIST.containing_type = _ROLEACCUMRECHARGEACTIVITYDATA
_ROLEACCUMRECHARGEACTIVITYDATA.fields_by_name['drawn_reward_seq_list'].message_type = _ROLEACCUMRECHARGEACTIVITYDATA_DRAWNREWARDSEQLIST
_ROLEACCUMCONSUMEACTIVITYDATA_DRAWNREWARDSEQLIST.containing_type = _ROLEACCUMCONSUMEACTIVITYDATA
_ROLEACCUMCONSUMEACTIVITYDATA.fields_by_name['drawn_reward_seq_list'].message_type = _ROLEACCUMCONSUMEACTIVITYDATA_DRAWNREWARDSEQLIST
_ROLERECHARGEREBATEACTIVITYDATA_DRAWNREWARDSEQLIST.containing_type = _ROLERECHARGEREBATEACTIVITYDATA
_ROLERECHARGEREBATEACTIVITYDATA.fields_by_name['drawn_reward_seq_list'].message_type = _ROLERECHARGEREBATEACTIVITYDATA_DRAWNREWARDSEQLIST
_REDENVELOPEDATA_RECEIVERLIST.containing_type = _REDENVELOPEDATA
_REDENVELOPEDATA.fields_by_name['receiver_list'].message_type = _REDENVELOPEDATA_RECEIVERLIST
DESCRIPTOR.message_types_by_name['RoleAccumRechargeActivityData'] = _ROLEACCUMRECHARGEACTIVITYDATA
DESCRIPTOR.message_types_by_name['RoleAccumConsumeActivityData'] = _ROLEACCUMCONSUMEACTIVITYDATA
DESCRIPTOR.message_types_by_name['RoleRechargeRebateActivityData'] = _ROLERECHARGEREBATEACTIVITYDATA
DESCRIPTOR.message_types_by_name['RedEnvelopeData'] = _REDENVELOPEDATA
DESCRIPTOR.message_types_by_name['ConsumeAndLimitBuyData'] = _CONSUMEANDLIMITBUYDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoleAccumRechargeActivityData = _reflection.GeneratedProtocolMessageType('RoleAccumRechargeActivityData', (_message.Message,), {

  'DrawnRewardSeqList' : _reflection.GeneratedProtocolMessageType('DrawnRewardSeqList', (_message.Message,), {
    'DESCRIPTOR' : _ROLEACCUMRECHARGEACTIVITYDATA_DRAWNREWARDSEQLIST,
    '__module__' : 'activity_db_pb2'
    # @@protoc_insertion_point(class_scope:dgame.RoleAccumRechargeActivityData.DrawnRewardSeqList)
    })
  ,
  'DESCRIPTOR' : _ROLEACCUMRECHARGEACTIVITYDATA,
  '__module__' : 'activity_db_pb2'
  # @@protoc_insertion_point(class_scope:dgame.RoleAccumRechargeActivityData)
  })
_sym_db.RegisterMessage(RoleAccumRechargeActivityData)
_sym_db.RegisterMessage(RoleAccumRechargeActivityData.DrawnRewardSeqList)

RoleAccumConsumeActivityData = _reflection.GeneratedProtocolMessageType('RoleAccumConsumeActivityData', (_message.Message,), {

  'DrawnRewardSeqList' : _reflection.GeneratedProtocolMessageType('DrawnRewardSeqList', (_message.Message,), {
    'DESCRIPTOR' : _ROLEACCUMCONSUMEACTIVITYDATA_DRAWNREWARDSEQLIST,
    '__module__' : 'activity_db_pb2'
    # @@protoc_insertion_point(class_scope:dgame.RoleAccumConsumeActivityData.DrawnRewardSeqList)
    })
  ,
  'DESCRIPTOR' : _ROLEACCUMCONSUMEACTIVITYDATA,
  '__module__' : 'activity_db_pb2'
  # @@protoc_insertion_point(class_scope:dgame.RoleAccumConsumeActivityData)
  })
_sym_db.RegisterMessage(RoleAccumConsumeActivityData)
_sym_db.RegisterMessage(RoleAccumConsumeActivityData.DrawnRewardSeqList)

RoleRechargeRebateActivityData = _reflection.GeneratedProtocolMessageType('RoleRechargeRebateActivityData', (_message.Message,), {

  'DrawnRewardSeqList' : _reflection.GeneratedProtocolMessageType('DrawnRewardSeqList', (_message.Message,), {
    'DESCRIPTOR' : _ROLERECHARGEREBATEACTIVITYDATA_DRAWNREWARDSEQLIST,
    '__module__' : 'activity_db_pb2'
    # @@protoc_insertion_point(class_scope:dgame.RoleRechargeRebateActivityData.DrawnRewardSeqList)
    })
  ,
  'DESCRIPTOR' : _ROLERECHARGEREBATEACTIVITYDATA,
  '__module__' : 'activity_db_pb2'
  # @@protoc_insertion_point(class_scope:dgame.RoleRechargeRebateActivityData)
  })
_sym_db.RegisterMessage(RoleRechargeRebateActivityData)
_sym_db.RegisterMessage(RoleRechargeRebateActivityData.DrawnRewardSeqList)

RedEnvelopeData = _reflection.GeneratedProtocolMessageType('RedEnvelopeData', (_message.Message,), {

  'ReceiverList' : _reflection.GeneratedProtocolMessageType('ReceiverList', (_message.Message,), {
    'DESCRIPTOR' : _REDENVELOPEDATA_RECEIVERLIST,
    '__module__' : 'activity_db_pb2'
    # @@protoc_insertion_point(class_scope:dgame.RedEnvelopeData.ReceiverList)
    })
  ,
  'DESCRIPTOR' : _REDENVELOPEDATA,
  '__module__' : 'activity_db_pb2'
  # @@protoc_insertion_point(class_scope:dgame.RedEnvelopeData)
  })
_sym_db.RegisterMessage(RedEnvelopeData)
_sym_db.RegisterMessage(RedEnvelopeData.ReceiverList)

ConsumeAndLimitBuyData = _reflection.GeneratedProtocolMessageType('ConsumeAndLimitBuyData', (_message.Message,), {
  'DESCRIPTOR' : _CONSUMEANDLIMITBUYDATA,
  '__module__' : 'activity_db_pb2'
  # @@protoc_insertion_point(class_scope:dgame.ConsumeAndLimitBuyData)
  })
_sym_db.RegisterMessage(ConsumeAndLimitBuyData)


# @@protoc_insertion_point(module_scope)
