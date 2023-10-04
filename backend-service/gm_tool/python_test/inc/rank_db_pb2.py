# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rank_db.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import dgame_define_pb2
import cs_arena_pb2
import login_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rank_db.proto',
  package='dgame',
  serialized_pb='\n\rrank_db.proto\x12\x05\x64game\x1a\x12\x64game_define.proto\x1a\x0e\x63s_arena.proto\x1a\x0blogin.proto\"O\n\x15\x41renaHeroBattleRecord\x12\x10\n\x08hero_gid\x18\x01 \x01(\x04\x12\x12\n\nalive_time\x18\x02 \x01(\x02\x12\x10\n\x08\x66inal_HP\x18\x03 \x01(\r\"\xc5\x02\n\x0e\x41renaReportRec\x12\x12\n\nrecord_gid\x18\x01 \x01(\x04\x12\x0f\n\x07is_rise\x18\x02 \x01(\x08\x12\x19\n\x11is_self_challenge\x18\x03 \x01(\x08\x12\x11\n\trank_diff\x18\x04 \x01(\r\x12\x0e\n\x06is_win\x18\x05 \x01(\x08\x12)\n\x0eself_role_info\x18\x06 \x01(\x0b\x32\x11.CS.ArenaRoleInfo\x12*\n\x0f\x65nemy_role_info\x18\x07 \x01(\x0b\x32\x11.CS.ArenaRoleInfo\x12;\n\x15self_hero_record_list\x18\x08 \x03(\x0b\x32\x1c.dgame.ArenaHeroBattleRecord\x12<\n\x16\x65nemy_hero_record_list\x18\t \x03(\x0b\x32\x1c.dgame.ArenaHeroBattleRecord\"6\n\x0b\x41renaReport\x12\'\n\x08rec_list\x18\x01 \x03(\x0b\x32\x15.dgame.ArenaReportRec\"\x97\x05\n\rRoleArenaData\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\n\n\x02lv\x18\x03 \x01(\r\x12\x0c\n\x04head\x18\x04 \x01(\r\x12\x0c\n\x04rank\x18\x05 \x01(\r\x12\x14\n\x0chighest_rank\x18\x06 \x01(\r\x12\r\n\x05score\x18\x07 \x01(\r\x12\x11\n\tdefend_fc\x18\x08 \x01(\r\x12\x38\n\rdefend_heroes\x18\t \x01(\x0b\x32!.dgame.RoleArenaData.DefendHeroes\x12\x32\n\nmatch_data\x18\n \x01(\x0b\x32\x1e.dgame.RoleArenaData.MatchData\x12\x34\n\x0b\x62\x61ttle_data\x18\x0b \x01(\x0b\x32\x1f.dgame.RoleArenaData.BattleData\x1a\x30\n\x0c\x44\x65\x66\x65ndHeroes\x12 \n\x04hero\x18\x01 \x03(\x0b\x32\x12.CS.ClientHeroData\x1a\xa7\x01\n\tMatchData\x12@\n\x12last_matched_enemy\x18\x01 \x03(\x0b\x32$.dgame.RoleArenaData.MatchData.Enemy\x12\x1a\n\x12last_match_my_rank\x18\x02 \x01(\r\x1a<\n\x05\x45nemy\x12\x0c\n\x04rank\x18\x01 \x01(\r\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x19\n\x11\x63\x61n_be_challenged\x18\x03 \x01(\x08\x1a\x8b\x01\n\nBattleData\x12\x16\n\x0eis_challenging\x18\x01 \x01(\x08\x12\x1b\n\x13is_being_challenged\x18\x02 \x01(\x08\x12\r\n\x05\x65nemy\x18\x03 \x01(\x04\x12\x12\n\nstart_time\x18\x04 \x01(\r\x12\x12\n\nis_expired\x18\x05 \x01(\x08\x12\x11\n\texpire_ts\x18\x06 \x01(\r')




_ARENAHEROBATTLERECORD = _descriptor.Descriptor(
  name='ArenaHeroBattleRecord',
  full_name='dgame.ArenaHeroBattleRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero_gid', full_name='dgame.ArenaHeroBattleRecord.hero_gid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alive_time', full_name='dgame.ArenaHeroBattleRecord.alive_time', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='final_HP', full_name='dgame.ArenaHeroBattleRecord.final_HP', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=73,
  serialized_end=152,
)


_ARENAREPORTREC = _descriptor.Descriptor(
  name='ArenaReportRec',
  full_name='dgame.ArenaReportRec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record_gid', full_name='dgame.ArenaReportRec.record_gid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_rise', full_name='dgame.ArenaReportRec.is_rise', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_self_challenge', full_name='dgame.ArenaReportRec.is_self_challenge', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank_diff', full_name='dgame.ArenaReportRec.rank_diff', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_win', full_name='dgame.ArenaReportRec.is_win', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='self_role_info', full_name='dgame.ArenaReportRec.self_role_info', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enemy_role_info', full_name='dgame.ArenaReportRec.enemy_role_info', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='self_hero_record_list', full_name='dgame.ArenaReportRec.self_hero_record_list', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enemy_hero_record_list', full_name='dgame.ArenaReportRec.enemy_hero_record_list', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=155,
  serialized_end=480,
)


_ARENAREPORT = _descriptor.Descriptor(
  name='ArenaReport',
  full_name='dgame.ArenaReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rec_list', full_name='dgame.ArenaReport.rec_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=482,
  serialized_end=536,
)


_ROLEARENADATA_DEFENDHEROES = _descriptor.Descriptor(
  name='DefendHeroes',
  full_name='dgame.RoleArenaData.DefendHeroes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero', full_name='dgame.RoleArenaData.DefendHeroes.hero', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=842,
  serialized_end=890,
)

_ROLEARENADATA_MATCHDATA_ENEMY = _descriptor.Descriptor(
  name='Enemy',
  full_name='dgame.RoleArenaData.MatchData.Enemy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rank', full_name='dgame.RoleArenaData.MatchData.Enemy.rank', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='dgame.RoleArenaData.MatchData.Enemy.id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='can_be_challenged', full_name='dgame.RoleArenaData.MatchData.Enemy.can_be_challenged', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1000,
  serialized_end=1060,
)

_ROLEARENADATA_MATCHDATA = _descriptor.Descriptor(
  name='MatchData',
  full_name='dgame.RoleArenaData.MatchData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='last_matched_enemy', full_name='dgame.RoleArenaData.MatchData.last_matched_enemy', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_match_my_rank', full_name='dgame.RoleArenaData.MatchData.last_match_my_rank', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ROLEARENADATA_MATCHDATA_ENEMY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=893,
  serialized_end=1060,
)

_ROLEARENADATA_BATTLEDATA = _descriptor.Descriptor(
  name='BattleData',
  full_name='dgame.RoleArenaData.BattleData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_challenging', full_name='dgame.RoleArenaData.BattleData.is_challenging', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_being_challenged', full_name='dgame.RoleArenaData.BattleData.is_being_challenged', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enemy', full_name='dgame.RoleArenaData.BattleData.enemy', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='dgame.RoleArenaData.BattleData.start_time', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_expired', full_name='dgame.RoleArenaData.BattleData.is_expired', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expire_ts', full_name='dgame.RoleArenaData.BattleData.expire_ts', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1063,
  serialized_end=1202,
)

_ROLEARENADATA = _descriptor.Descriptor(
  name='RoleArenaData',
  full_name='dgame.RoleArenaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dgame.RoleArenaData.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='dgame.RoleArenaData.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lv', full_name='dgame.RoleArenaData.lv', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='head', full_name='dgame.RoleArenaData.head', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank', full_name='dgame.RoleArenaData.rank', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='highest_rank', full_name='dgame.RoleArenaData.highest_rank', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='dgame.RoleArenaData.score', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='defend_fc', full_name='dgame.RoleArenaData.defend_fc', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='defend_heroes', full_name='dgame.RoleArenaData.defend_heroes', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match_data', full_name='dgame.RoleArenaData.match_data', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_data', full_name='dgame.RoleArenaData.battle_data', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ROLEARENADATA_DEFENDHEROES, _ROLEARENADATA_MATCHDATA, _ROLEARENADATA_BATTLEDATA, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=539,
  serialized_end=1202,
)

_ARENAREPORTREC.fields_by_name['self_role_info'].message_type = cs_arena_pb2._ARENAROLEINFO
_ARENAREPORTREC.fields_by_name['enemy_role_info'].message_type = cs_arena_pb2._ARENAROLEINFO
_ARENAREPORTREC.fields_by_name['self_hero_record_list'].message_type = _ARENAHEROBATTLERECORD
_ARENAREPORTREC.fields_by_name['enemy_hero_record_list'].message_type = _ARENAHEROBATTLERECORD
_ARENAREPORT.fields_by_name['rec_list'].message_type = _ARENAREPORTREC
_ROLEARENADATA_DEFENDHEROES.fields_by_name['hero'].message_type = login_pb2._CLIENTHERODATA
_ROLEARENADATA_DEFENDHEROES.containing_type = _ROLEARENADATA;
_ROLEARENADATA_MATCHDATA_ENEMY.containing_type = _ROLEARENADATA_MATCHDATA;
_ROLEARENADATA_MATCHDATA.fields_by_name['last_matched_enemy'].message_type = _ROLEARENADATA_MATCHDATA_ENEMY
_ROLEARENADATA_MATCHDATA.containing_type = _ROLEARENADATA;
_ROLEARENADATA_BATTLEDATA.containing_type = _ROLEARENADATA;
_ROLEARENADATA.fields_by_name['defend_heroes'].message_type = _ROLEARENADATA_DEFENDHEROES
_ROLEARENADATA.fields_by_name['match_data'].message_type = _ROLEARENADATA_MATCHDATA
_ROLEARENADATA.fields_by_name['battle_data'].message_type = _ROLEARENADATA_BATTLEDATA
DESCRIPTOR.message_types_by_name['ArenaHeroBattleRecord'] = _ARENAHEROBATTLERECORD
DESCRIPTOR.message_types_by_name['ArenaReportRec'] = _ARENAREPORTREC
DESCRIPTOR.message_types_by_name['ArenaReport'] = _ARENAREPORT
DESCRIPTOR.message_types_by_name['RoleArenaData'] = _ROLEARENADATA

class ArenaHeroBattleRecord(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ARENAHEROBATTLERECORD

  # @@protoc_insertion_point(class_scope:dgame.ArenaHeroBattleRecord)

class ArenaReportRec(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ARENAREPORTREC

  # @@protoc_insertion_point(class_scope:dgame.ArenaReportRec)

class ArenaReport(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ARENAREPORT

  # @@protoc_insertion_point(class_scope:dgame.ArenaReport)

class RoleArenaData(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class DefendHeroes(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _ROLEARENADATA_DEFENDHEROES

    # @@protoc_insertion_point(class_scope:dgame.RoleArenaData.DefendHeroes)

  class MatchData(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType

    class Enemy(_message.Message):
      __metaclass__ = _reflection.GeneratedProtocolMessageType
      DESCRIPTOR = _ROLEARENADATA_MATCHDATA_ENEMY

      # @@protoc_insertion_point(class_scope:dgame.RoleArenaData.MatchData.Enemy)
    DESCRIPTOR = _ROLEARENADATA_MATCHDATA

    # @@protoc_insertion_point(class_scope:dgame.RoleArenaData.MatchData)

  class BattleData(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _ROLEARENADATA_BATTLEDATA

    # @@protoc_insertion_point(class_scope:dgame.RoleArenaData.BattleData)
  DESCRIPTOR = _ROLEARENADATA

  # @@protoc_insertion_point(class_scope:dgame.RoleArenaData)


# @@protoc_insertion_point(module_scope)