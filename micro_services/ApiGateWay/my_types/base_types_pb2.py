# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base_types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x62\x61se_types.proto\"+\n\x0c\x42\x61seResponse\x12\r\n\x05state\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\"\x84\x01\n\x0b\x42otResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08tg_token\x18\x02 \x01(\t\x12\x14\n\x0cgoogle_token\x18\x03 \x01(\t\x12\r\n\x05owner\x18\x04 \x01(\x05\x12\x15\n\rbot_survey_id\x18\x05 \x01(\x05\x12\r\n\x05state\x18\x06 \x01(\t\x12\x0c\n\x04\x63ode\x18\x07 \x01(\x05\"Z\n\x06Module\x12\x10\n\x08question\x18\x01 \x01(\t\x12\x10\n\x08next_ids\x18\x02 \x03(\x05\x12\x0f\n\x07\x61nswers\x18\x03 \x03(\x05\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\r\n\x05title\x18\x05 \x01(\t\"j\n\x07Journal\x12&\n\x07modules\x18\x01 \x03(\x0b\x32\x15.Journal.ModulesEntry\x1a\x37\n\x0cModulesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x16\n\x05value\x18\x02 \x01(\x0b\x32\x07.Module:\x02\x38\x01\";\n\x04User\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontact\x18\x03 \x01(\t\"`\n\x0cUserResponse\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontact\x18\x03 \x01(\t\x12\r\n\x05state\x18\x04 \x01(\t\x12\x0c\n\x04\x63ode\x18\x05 \x01(\x05\x42\x19\xaa\x02\x16\x44\x61taBaseService.Protosb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'base_types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\026DataBaseService.Protos'
  _JOURNAL_MODULESENTRY._options = None
  _JOURNAL_MODULESENTRY._serialized_options = b'8\001'
  _BASERESPONSE._serialized_start=20
  _BASERESPONSE._serialized_end=63
  _BOTRESPONSE._serialized_start=66
  _BOTRESPONSE._serialized_end=198
  _MODULE._serialized_start=200
  _MODULE._serialized_end=290
  _JOURNAL._serialized_start=292
  _JOURNAL._serialized_end=398
  _JOURNAL_MODULESENTRY._serialized_start=343
  _JOURNAL_MODULESENTRY._serialized_end=398
  _USER._serialized_start=400
  _USER._serialized_end=459
  _USERRESPONSE._serialized_start=461
  _USERRESPONSE._serialized_end=557
# @@protoc_insertion_point(module_scope)
