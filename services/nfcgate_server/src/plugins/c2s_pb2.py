# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: c2s.proto
# Protobuf Python Version: 5.27.1
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
    1,
    '',
    'c2s.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tc2s.proto\x12*de.tu_darmstadt.seemoo.nfcgate.network.c2s\"\xa3\x01\n\nServerData\x12M\n\x06opcode\x18\x01 \x01(\x0e\x32=.de.tu_darmstadt.seemoo.nfcgate.network.c2s.ServerData.Opcode\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"8\n\x06Opcode\x12\n\n\x06OP_PSH\x10\x00\x12\n\n\x06OP_SYN\x10\x01\x12\n\n\x06OP_ACK\x10\x02\x12\n\n\x06OP_FIN\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'c2s_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SERVERDATA']._serialized_start=58
  _globals['_SERVERDATA']._serialized_end=221
  _globals['_SERVERDATA_OPCODE']._serialized_start=165
  _globals['_SERVERDATA_OPCODE']._serialized_end=221
# @@protoc_insertion_point(module_scope)
