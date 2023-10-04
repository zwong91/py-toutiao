# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs_team.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import dgame_define_pb2 as dgame__define__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cs_team.proto',
  package='CS',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rcs_team.proto\x12\x02\x43S\x1a\x12\x64game_define.proto\"\x1c\n\nGetTeamReq\x12\x0e\n\x06unused\x18\x01 \x01(\r\"<\n\nGetTeamRsp\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x1e\n\thero_data\x18\x02 \x03(\x0b\x32\x0b.dgame.Hero\"L\n\x10TeamHeroPosition\x12\x10\n\x08hero_gid\x18\x01 \x01(\x04\x12&\n\x08position\x18\x02 \x01(\x0e\x32\x14.dgame.TEAM_POSITION\"#\n\x0fTeamHeroPlayReq\x12\x10\n\x08hero_gid\x18\x01 \x01(\x04\"^\n\x0fTeamHeroPlayRsp\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x10\n\x08hero_gid\x18\x02 \x01(\x04\x12)\n\x0bto_position\x18\x03 \x01(\x0e\x32\x14.dgame.TEAM_POSITION\"8\n\x12TeamHeroRetreatReq\x12\"\n\x04hero\x18\x01 \x01(\x0b\x32\x14.CS.TeamHeroPosition\"c\n\x12TeamHeroRetreatRsp\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x10\n\x08hero_gid\x18\x02 \x01(\x04\x12+\n\rhero_position\x18\x03 \x01(\x0e\x32\x14.dgame.TEAM_POSITION\"k\n\x1aTeamManageHeroRiseLevelReq\x12\x1b\n\x13rise_level_hero_gid\x18\x01 \x01(\x04\x12\x30\n\x10\x64\x65leted_material\x18\x03 \x03(\x0b\x32\x16.dgame.DeletedMaterial\"\xab\x01\n\x1aTeamManageHeroRiseLevelRsp\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x13\n\x0brised_level\x18\x02 \x01(\r\x12\x11\n\tnew_color\x18\x03 \x01(\r\x12\x11\n\trised_exp\x18\x04 \x01(\r\x12\x10\n\x08gold_num\x18\x05 \x01(\r\x12\x30\n\x10\x64\x65leted_material\x18\x06 \x03(\x0b\x32\x16.dgame.DeletedMaterial\"#\n\x0fHeroRiseStarReq\x12\x10\n\x08hero_gid\x18\x01 \x01(\x04\"5\n\x0fHeroRiseStarRsp\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x12\n\nnew_heroid\x18\x02 \x01(\r\" \n\x0eHeroCombineReq\x12\x0e\n\x06heroid\x18\x01 \x01(\r\";\n\x0eHeroCombineRsp\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x19\n\x04hero\x18\x02 \x01(\x0b\x32\x0b.dgame.Hero\"1\n\x18\x43hangeRecommendedTeamReq\x12\x15\n\rhero_gid_list\x18\x01 \x03(\x04\"J\n\x18\x43hangeRecommendedTeamRsp\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x1e\n\thero_data\x18\x02 \x03(\x0b\x32\x0b.dgame.Hero\";\n\rSwitchHeroReq\x12\x15\n\rfrom_hero_gid\x18\x01 \x01(\x04\x12\x13\n\x0bto_hero_gid\x18\x02 \x01(\x04\"\xc1\x01\n\rSwitchHeroRsp\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x1e\n\tfrom_hero\x18\x02 \x01(\x0b\x32\x0b.dgame.Hero\x12\x1c\n\x07to_hero\x18\x03 \x01(\x0b\x32\x0b.dgame.Hero\x12\x18\n\x10\x63ost_material_id\x18\x04 \x01(\r\x12\x19\n\x11\x63ost_material_num\x18\x05 \x01(\r\x12\x14\n\x0c\x63ost_diamond\x18\x06 \x01(\r\x12\x17\n\x0freturn_gold_num\x18\x07 \x01(\r\"$\n\x10HeroRiseColorReq\x12\x10\n\x08hero_gid\x18\x01 \x01(\x04\"\xa3\x01\n\x10HeroRiseColorRsp\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x10\n\x08hero_gid\x18\x02 \x01(\x04\x12\r\n\x05\x63olor\x18\x03 \x01(\r\x12\x15\n\rcost_gold_num\x18\x04 \x01(\r\x12\x14\n\x0cnew_gold_num\x18\x05 \x01(\r\x12\x18\n\x10\x63ost_diamond_num\x18\x06 \x01(\r\x12\x17\n\x0fnew_diamond_num\x18\x07 \x01(\rb\x06proto3'
  ,
  dependencies=[dgame__define__pb2.DESCRIPTOR,])




_GETTEAMREQ = _descriptor.Descriptor(
  name='GetTeamReq',
  full_name='CS.GetTeamReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='unused', full_name='CS.GetTeamReq.unused', index=0,
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
  serialized_start=41,
  serialized_end=69,
)


_GETTEAMRSP = _descriptor.Descriptor(
  name='GetTeamRsp',
  full_name='CS.GetTeamRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='CS.GetTeamRsp.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hero_data', full_name='CS.GetTeamRsp.hero_data', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=71,
  serialized_end=131,
)


_TEAMHEROPOSITION = _descriptor.Descriptor(
  name='TeamHeroPosition',
  full_name='CS.TeamHeroPosition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero_gid', full_name='CS.TeamHeroPosition.hero_gid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='position', full_name='CS.TeamHeroPosition.position', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=133,
  serialized_end=209,
)


_TEAMHEROPLAYREQ = _descriptor.Descriptor(
  name='TeamHeroPlayReq',
  full_name='CS.TeamHeroPlayReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero_gid', full_name='CS.TeamHeroPlayReq.hero_gid', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=211,
  serialized_end=246,
)


_TEAMHEROPLAYRSP = _descriptor.Descriptor(
  name='TeamHeroPlayRsp',
  full_name='CS.TeamHeroPlayRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='CS.TeamHeroPlayRsp.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hero_gid', full_name='CS.TeamHeroPlayRsp.hero_gid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to_position', full_name='CS.TeamHeroPlayRsp.to_position', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=248,
  serialized_end=342,
)


_TEAMHERORETREATREQ = _descriptor.Descriptor(
  name='TeamHeroRetreatReq',
  full_name='CS.TeamHeroRetreatReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero', full_name='CS.TeamHeroRetreatReq.hero', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=344,
  serialized_end=400,
)


_TEAMHERORETREATRSP = _descriptor.Descriptor(
  name='TeamHeroRetreatRsp',
  full_name='CS.TeamHeroRetreatRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='CS.TeamHeroRetreatRsp.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hero_gid', full_name='CS.TeamHeroRetreatRsp.hero_gid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hero_position', full_name='CS.TeamHeroRetreatRsp.hero_position', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=402,
  serialized_end=501,
)


_TEAMMANAGEHERORISELEVELREQ = _descriptor.Descriptor(
  name='TeamManageHeroRiseLevelReq',
  full_name='CS.TeamManageHeroRiseLevelReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rise_level_hero_gid', full_name='CS.TeamManageHeroRiseLevelReq.rise_level_hero_gid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deleted_material', full_name='CS.TeamManageHeroRiseLevelReq.deleted_material', index=1,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=503,
  serialized_end=610,
)


_TEAMMANAGEHERORISELEVELRSP = _descriptor.Descriptor(
  name='TeamManageHeroRiseLevelRsp',
  full_name='CS.TeamManageHeroRiseLevelRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='CS.TeamManageHeroRiseLevelRsp.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rised_level', full_name='CS.TeamManageHeroRiseLevelRsp.rised_level', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_color', full_name='CS.TeamManageHeroRiseLevelRsp.new_color', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rised_exp', full_name='CS.TeamManageHeroRiseLevelRsp.rised_exp', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gold_num', full_name='CS.TeamManageHeroRiseLevelRsp.gold_num', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deleted_material', full_name='CS.TeamManageHeroRiseLevelRsp.deleted_material', index=5,
      number=6, type=11, cpp_type=10, label=3,
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
  serialized_start=613,
  serialized_end=784,
)


_HERORISESTARREQ = _descriptor.Descriptor(
  name='HeroRiseStarReq',
  full_name='CS.HeroRiseStarReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero_gid', full_name='CS.HeroRiseStarReq.hero_gid', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=786,
  serialized_end=821,
)


_HERORISESTARRSP = _descriptor.Descriptor(
  name='HeroRiseStarRsp',
  full_name='CS.HeroRiseStarRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='CS.HeroRiseStarRsp.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_heroid', full_name='CS.HeroRiseStarRsp.new_heroid', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=823,
  serialized_end=876,
)


_HEROCOMBINEREQ = _descriptor.Descriptor(
  name='HeroCombineReq',
  full_name='CS.HeroCombineReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='heroid', full_name='CS.HeroCombineReq.heroid', index=0,
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
  serialized_start=878,
  serialized_end=910,
)


_HEROCOMBINERSP = _descriptor.Descriptor(
  name='HeroCombineRsp',
  full_name='CS.HeroCombineRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='CS.HeroCombineRsp.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hero', full_name='CS.HeroCombineRsp.hero', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=912,
  serialized_end=971,
)


_CHANGERECOMMENDEDTEAMREQ = _descriptor.Descriptor(
  name='ChangeRecommendedTeamReq',
  full_name='CS.ChangeRecommendedTeamReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero_gid_list', full_name='CS.ChangeRecommendedTeamReq.hero_gid_list', index=0,
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
  serialized_start=973,
  serialized_end=1022,
)


_CHANGERECOMMENDEDTEAMRSP = _descriptor.Descriptor(
  name='ChangeRecommendedTeamRsp',
  full_name='CS.ChangeRecommendedTeamRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='CS.ChangeRecommendedTeamRsp.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hero_data', full_name='CS.ChangeRecommendedTeamRsp.hero_data', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=1024,
  serialized_end=1098,
)


_SWITCHHEROREQ = _descriptor.Descriptor(
  name='SwitchHeroReq',
  full_name='CS.SwitchHeroReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_hero_gid', full_name='CS.SwitchHeroReq.from_hero_gid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to_hero_gid', full_name='CS.SwitchHeroReq.to_hero_gid', index=1,
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
  serialized_start=1100,
  serialized_end=1159,
)


_SWITCHHERORSP = _descriptor.Descriptor(
  name='SwitchHeroRsp',
  full_name='CS.SwitchHeroRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='CS.SwitchHeroRsp.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='from_hero', full_name='CS.SwitchHeroRsp.from_hero', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to_hero', full_name='CS.SwitchHeroRsp.to_hero', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cost_material_id', full_name='CS.SwitchHeroRsp.cost_material_id', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cost_material_num', full_name='CS.SwitchHeroRsp.cost_material_num', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cost_diamond', full_name='CS.SwitchHeroRsp.cost_diamond', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='return_gold_num', full_name='CS.SwitchHeroRsp.return_gold_num', index=6,
      number=7, type=13, cpp_type=3, label=1,
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
  serialized_start=1162,
  serialized_end=1355,
)


_HERORISECOLORREQ = _descriptor.Descriptor(
  name='HeroRiseColorReq',
  full_name='CS.HeroRiseColorReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero_gid', full_name='CS.HeroRiseColorReq.hero_gid', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=1357,
  serialized_end=1393,
)


_HERORISECOLORRSP = _descriptor.Descriptor(
  name='HeroRiseColorRsp',
  full_name='CS.HeroRiseColorRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='CS.HeroRiseColorRsp.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hero_gid', full_name='CS.HeroRiseColorRsp.hero_gid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='color', full_name='CS.HeroRiseColorRsp.color', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cost_gold_num', full_name='CS.HeroRiseColorRsp.cost_gold_num', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_gold_num', full_name='CS.HeroRiseColorRsp.new_gold_num', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cost_diamond_num', full_name='CS.HeroRiseColorRsp.cost_diamond_num', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_diamond_num', full_name='CS.HeroRiseColorRsp.new_diamond_num', index=6,
      number=7, type=13, cpp_type=3, label=1,
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
  serialized_start=1396,
  serialized_end=1559,
)

_GETTEAMRSP.fields_by_name['hero_data'].message_type = dgame__define__pb2._HERO
_TEAMHEROPOSITION.fields_by_name['position'].enum_type = dgame__define__pb2._TEAM_POSITION
_TEAMHEROPLAYRSP.fields_by_name['to_position'].enum_type = dgame__define__pb2._TEAM_POSITION
_TEAMHERORETREATREQ.fields_by_name['hero'].message_type = _TEAMHEROPOSITION
_TEAMHERORETREATRSP.fields_by_name['hero_position'].enum_type = dgame__define__pb2._TEAM_POSITION
_TEAMMANAGEHERORISELEVELREQ.fields_by_name['deleted_material'].message_type = dgame__define__pb2._DELETEDMATERIAL
_TEAMMANAGEHERORISELEVELRSP.fields_by_name['deleted_material'].message_type = dgame__define__pb2._DELETEDMATERIAL
_HEROCOMBINERSP.fields_by_name['hero'].message_type = dgame__define__pb2._HERO
_CHANGERECOMMENDEDTEAMRSP.fields_by_name['hero_data'].message_type = dgame__define__pb2._HERO
_SWITCHHERORSP.fields_by_name['from_hero'].message_type = dgame__define__pb2._HERO
_SWITCHHERORSP.fields_by_name['to_hero'].message_type = dgame__define__pb2._HERO
DESCRIPTOR.message_types_by_name['GetTeamReq'] = _GETTEAMREQ
DESCRIPTOR.message_types_by_name['GetTeamRsp'] = _GETTEAMRSP
DESCRIPTOR.message_types_by_name['TeamHeroPosition'] = _TEAMHEROPOSITION
DESCRIPTOR.message_types_by_name['TeamHeroPlayReq'] = _TEAMHEROPLAYREQ
DESCRIPTOR.message_types_by_name['TeamHeroPlayRsp'] = _TEAMHEROPLAYRSP
DESCRIPTOR.message_types_by_name['TeamHeroRetreatReq'] = _TEAMHERORETREATREQ
DESCRIPTOR.message_types_by_name['TeamHeroRetreatRsp'] = _TEAMHERORETREATRSP
DESCRIPTOR.message_types_by_name['TeamManageHeroRiseLevelReq'] = _TEAMMANAGEHERORISELEVELREQ
DESCRIPTOR.message_types_by_name['TeamManageHeroRiseLevelRsp'] = _TEAMMANAGEHERORISELEVELRSP
DESCRIPTOR.message_types_by_name['HeroRiseStarReq'] = _HERORISESTARREQ
DESCRIPTOR.message_types_by_name['HeroRiseStarRsp'] = _HERORISESTARRSP
DESCRIPTOR.message_types_by_name['HeroCombineReq'] = _HEROCOMBINEREQ
DESCRIPTOR.message_types_by_name['HeroCombineRsp'] = _HEROCOMBINERSP
DESCRIPTOR.message_types_by_name['ChangeRecommendedTeamReq'] = _CHANGERECOMMENDEDTEAMREQ
DESCRIPTOR.message_types_by_name['ChangeRecommendedTeamRsp'] = _CHANGERECOMMENDEDTEAMRSP
DESCRIPTOR.message_types_by_name['SwitchHeroReq'] = _SWITCHHEROREQ
DESCRIPTOR.message_types_by_name['SwitchHeroRsp'] = _SWITCHHERORSP
DESCRIPTOR.message_types_by_name['HeroRiseColorReq'] = _HERORISECOLORREQ
DESCRIPTOR.message_types_by_name['HeroRiseColorRsp'] = _HERORISECOLORRSP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetTeamReq = _reflection.GeneratedProtocolMessageType('GetTeamReq', (_message.Message,), {
  'DESCRIPTOR' : _GETTEAMREQ,
  '__module__' : 'cs_team_pb2'
  # @@protoc_insertion_point(class_scope:CS.GetTeamReq)
  })
_sym_db.RegisterMessage(GetTeamReq)

GetTeamRsp = _reflection.GeneratedProtocolMessageType('GetTeamRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETTEAMRSP,
  '__module__' : 'cs_team_pb2'
  # @@protoc_insertion_point(class_scope:CS.GetTeamRsp)
  })
_sym_db.RegisterMessage(GetTeamRsp)

TeamHeroPosition = _reflection.GeneratedProtocolMessageType('TeamHeroPosition', (_message.Message,), {
  'DESCRIPTOR' : _TEAMHEROPOSITION,
  '__module__' : 'cs_team_pb2'
  # @@protoc_insertion_point(class_scope:CS.TeamHeroPosition)
  })
_sym_db.RegisterMessage(TeamHeroPosition)

TeamHeroPlayReq = _reflection.GeneratedProtocolMessageType('TeamHeroPlayReq', (_message.Message,), {
  'DESCRIPTOR' : _TEAMHEROPLAYREQ,
  '__module__' : 'cs_team_pb2'
  # @@protoc_insertion_point(class_scope:CS.TeamHeroPlayReq)
  })
_sym_db.RegisterMessage(TeamHeroPlayReq)

TeamHeroPlayRsp = _reflection.GeneratedProtocolMessageType('TeamHeroPlayRsp', (_message.Message,), {
  'DESCRIPTOR' : _TEAMHEROPLAYRSP,
  '__module__' : 'cs_team_pb2'
  # @@protoc_insertion_point(class_scope:CS.TeamHeroPlayRsp)
  })
_sym_db.RegisterMessage(TeamHeroPlayRsp)

TeamHeroRetreatReq = _reflection.GeneratedProtocolMessageType('TeamHeroRetreatReq', (_message.Message,), {
  'DESCRIPTOR' : _TEAMHERORETREATREQ,
  '__module__' : 'cs_team_pb2'
  # @@protoc_insertion_point(class_scope:CS.TeamHeroRetreatReq)
  })
_sym_db.RegisterMessage(TeamHeroRetreatReq)

TeamHeroRetreatRsp = _reflection.GeneratedProtocolMessageType('TeamHeroRetreatRsp', (_message.Message,), {
  'DESCRIPTOR' : _TEAMHERORETREATRSP,
  '__module__' : 'cs_team_pb2'
  # @@protoc_insertion_point(class_scope:CS.TeamHeroRetreatRsp)
  })
_sym_db.RegisterMessage(TeamHeroRetreatRsp)

TeamManageHeroRiseLevelReq = _reflection.GeneratedProtocolMessageType('TeamManageHeroRiseLevelReq', (_message.Message,), {
  'DESCRIPTOR' : _TEAMMANAGEHERORISELEVELREQ,
  '__module__' : 'cs_team_pb2'
  # @@protoc_insertion_point(class_scope:CS.TeamManageHeroRiseLevelReq)
  })
_sym_db.RegisterMessage(TeamManageHeroRiseLevelReq)

TeamManageHeroRiseLevelRsp = _reflection.GeneratedProtocolMessageType('TeamManageHeroRiseLevelRsp', (_message.Message,), {
  'DESCRIPTOR' : _TEAMMANAGEHERORISELEVELRSP,
  '__module__' : 'cs_team_pb2'
  # @@protoc_insertion_point(class_scope:CS.TeamManageHeroRiseLevelRsp)
  })
_sym_db.RegisterMessage(TeamManageHeroRiseLevelRsp)

HeroRiseStarReq = _reflection.GeneratedProtocolMessageType('HeroRiseStarReq', (_message.Message,), {
  'DESCRIPTOR' : _HERORISESTARREQ,
  '__module__' : 'cs_team_pb2'
  # @@protoc_insertion_point(class_scope:CS.HeroRiseStarReq)
  })
_sym_db.RegisterMessage(HeroRiseStarReq)

HeroRiseStarRsp = _reflection.GeneratedProtocolMessageType('HeroRiseStarRsp', (_message.Message,), {
  'DESCRIPTOR' : _HERORISESTARRSP,
  '__module__' : 'cs_team_pb2'
  # @@protoc_insertion_point(class_scope:CS.HeroRiseStarRsp)
  })
_sym_db.RegisterMessage(HeroRiseStarRsp)

HeroCombineReq = _reflection.GeneratedProtocolMessageType('HeroCombineReq', (_message.Message,), {
  'DESCRIPTOR' : _HEROCOMBINEREQ,
  '__module__' : 'cs_team_pb2'
  # @@protoc_insertion_point(class_scope:CS.HeroCombineReq)
  })
_sym_db.RegisterMessage(HeroCombineReq)

HeroCombineRsp = _reflection.GeneratedProtocolMessageType('HeroCombineRsp', (_message.Message,), {
  'DESCRIPTOR' : _HEROCOMBINERSP,
  '__module__' : 'cs_team_pb2'
  # @@protoc_insertion_point(class_scope:CS.HeroCombineRsp)
  })
_sym_db.RegisterMessage(HeroCombineRsp)

ChangeRecommendedTeamReq = _reflection.GeneratedProtocolMessageType('ChangeRecommendedTeamReq', (_message.Message,), {
  'DESCRIPTOR' : _CHANGERECOMMENDEDTEAMREQ,
  '__module__' : 'cs_team_pb2'
  # @@protoc_insertion_point(class_scope:CS.ChangeRecommendedTeamReq)
  })
_sym_db.RegisterMessage(ChangeRecommendedTeamReq)

ChangeRecommendedTeamRsp = _reflection.GeneratedProtocolMessageType('ChangeRecommendedTeamRsp', (_message.Message,), {
  'DESCRIPTOR' : _CHANGERECOMMENDEDTEAMRSP,
  '__module__' : 'cs_team_pb2'
  # @@protoc_insertion_point(class_scope:CS.ChangeRecommendedTeamRsp)
  })
_sym_db.RegisterMessage(ChangeRecommendedTeamRsp)

SwitchHeroReq = _reflection.GeneratedProtocolMessageType('SwitchHeroReq', (_message.Message,), {
  'DESCRIPTOR' : _SWITCHHEROREQ,
  '__module__' : 'cs_team_pb2'
  # @@protoc_insertion_point(class_scope:CS.SwitchHeroReq)
  })
_sym_db.RegisterMessage(SwitchHeroReq)

SwitchHeroRsp = _reflection.GeneratedProtocolMessageType('SwitchHeroRsp', (_message.Message,), {
  'DESCRIPTOR' : _SWITCHHERORSP,
  '__module__' : 'cs_team_pb2'
  # @@protoc_insertion_point(class_scope:CS.SwitchHeroRsp)
  })
_sym_db.RegisterMessage(SwitchHeroRsp)

HeroRiseColorReq = _reflection.GeneratedProtocolMessageType('HeroRiseColorReq', (_message.Message,), {
  'DESCRIPTOR' : _HERORISECOLORREQ,
  '__module__' : 'cs_team_pb2'
  # @@protoc_insertion_point(class_scope:CS.HeroRiseColorReq)
  })
_sym_db.RegisterMessage(HeroRiseColorReq)

HeroRiseColorRsp = _reflection.GeneratedProtocolMessageType('HeroRiseColorRsp', (_message.Message,), {
  'DESCRIPTOR' : _HERORISECOLORRSP,
  '__module__' : 'cs_team_pb2'
  # @@protoc_insertion_point(class_scope:CS.HeroRiseColorRsp)
  })
_sym_db.RegisterMessage(HeroRiseColorRsp)


# @@protoc_insertion_point(module_scope)
