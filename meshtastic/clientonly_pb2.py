# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meshtastic/clientonly.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from meshtastic import localonly_pb2 as meshtastic_dot_localonly__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bmeshtastic/clientonly.proto\x12\nmeshtastic\x1a\x1ameshtastic/localonly.proto\"\x8d\x02\n\rDeviceProfile\x12\x16\n\tlong_name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x17\n\nshort_name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0b\x63hannel_url\x18\x03 \x01(\tH\x02\x88\x01\x01\x12,\n\x06\x63onfig\x18\x04 \x01(\x0b\x32\x17.meshtastic.LocalConfigH\x03\x88\x01\x01\x12\x39\n\rmodule_config\x18\x05 \x01(\x0b\x32\x1d.meshtastic.LocalModuleConfigH\x04\x88\x01\x01\x42\x0c\n\n_long_nameB\r\n\x0b_short_nameB\x0e\n\x0c_channel_urlB\t\n\x07_configB\x10\n\x0e_module_configBe\n\x13\x63om.geeksville.meshB\x10\x43lientOnlyProtosZ\"github.com/meshtastic/go/generated\xaa\x02\x14Meshtastic.Protobufs\xba\x02\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meshtastic.clientonly_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.geeksville.meshB\020ClientOnlyProtosZ\"github.com/meshtastic/go/generated\252\002\024Meshtastic.Protobufs\272\002\000'
  _globals['_DEVICEPROFILE']._serialized_start=72
  _globals['_DEVICEPROFILE']._serialized_end=341
# @@protoc_insertion_point(module_scope)
