# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: find_laureate_by_name.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'find_laureate_by_name.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x66ind_laureate_by_name.proto\x12\x05prize\"@\n\x19\x46indLaureateByNameRequest\x12\x11\n\tfirstname\x18\x01 \x01(\t\x12\x10\n\x08lastname\x18\x02 \x01(\t\"D\n\x1a\x46indLaureateByNameResponse\x12&\n\tlaureates\x18\x01 \x03(\x0b\x32\x13.prize.LaureateInfo\"C\n\x0cLaureateInfo\x12\x0c\n\x04year\x18\x01 \x01(\x05\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x13\n\x0bmotivations\x18\x03 \x03(\t2p\n\x19\x46indLaureateByNameService\x12S\n\x0c\x46indLaureate\x12 .prize.FindLaureateByNameRequest\x1a!.prize.FindLaureateByNameResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'find_laureate_by_name_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FINDLAUREATEBYNAMEREQUEST']._serialized_start=38
  _globals['_FINDLAUREATEBYNAMEREQUEST']._serialized_end=102
  _globals['_FINDLAUREATEBYNAMERESPONSE']._serialized_start=104
  _globals['_FINDLAUREATEBYNAMERESPONSE']._serialized_end=172
  _globals['_LAUREATEINFO']._serialized_start=174
  _globals['_LAUREATEINFO']._serialized_end=241
  _globals['_FINDLAUREATEBYNAMESERVICE']._serialized_start=243
  _globals['_FINDLAUREATEBYNAMESERVICE']._serialized_end=355
# @@protoc_insertion_point(module_scope)
