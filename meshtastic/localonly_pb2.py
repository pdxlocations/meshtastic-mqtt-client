# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meshtastic/localonly.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from meshtastic import config_pb2 as meshtastic_dot_config__pb2
from meshtastic import module_config_pb2 as meshtastic_dot_module__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ameshtastic/localonly.proto\x1a\x17meshtastic/config.proto\x1a\x1emeshtastic/module_config.proto\"\xb0\x02\n\x0bLocalConfig\x12$\n\x06\x64\x65vice\x18\x01 \x01(\x0b\x32\x14.Config.DeviceConfig\x12(\n\x08position\x18\x02 \x01(\x0b\x32\x16.Config.PositionConfig\x12\"\n\x05power\x18\x03 \x01(\x0b\x32\x13.Config.PowerConfig\x12&\n\x07network\x18\x04 \x01(\x0b\x32\x15.Config.NetworkConfig\x12&\n\x07\x64isplay\x18\x05 \x01(\x0b\x32\x15.Config.DisplayConfig\x12 \n\x04lora\x18\x06 \x01(\x0b\x32\x12.Config.LoRaConfig\x12*\n\tbluetooth\x18\x07 \x01(\x0b\x32\x17.Config.BluetoothConfig\x12\x0f\n\x07version\x18\x08 \x01(\r\"\xb8\x05\n\x11LocalModuleConfig\x12&\n\x04mqtt\x18\x01 \x01(\x0b\x32\x18.ModuleConfig.MQTTConfig\x12*\n\x06serial\x18\x02 \x01(\x0b\x32\x1a.ModuleConfig.SerialConfig\x12G\n\x15\x65xternal_notification\x18\x03 \x01(\x0b\x32(.ModuleConfig.ExternalNotificationConfig\x12\x37\n\rstore_forward\x18\x04 \x01(\x0b\x32 .ModuleConfig.StoreForwardConfig\x12\x31\n\nrange_test\x18\x05 \x01(\x0b\x32\x1d.ModuleConfig.RangeTestConfig\x12\x30\n\ttelemetry\x18\x06 \x01(\x0b\x32\x1d.ModuleConfig.TelemetryConfig\x12\x39\n\x0e\x63\x61nned_message\x18\x07 \x01(\x0b\x32!.ModuleConfig.CannedMessageConfig\x12(\n\x05\x61udio\x18\t \x01(\x0b\x32\x19.ModuleConfig.AudioConfig\x12;\n\x0fremote_hardware\x18\n \x01(\x0b\x32\".ModuleConfig.RemoteHardwareConfig\x12\x37\n\rneighbor_info\x18\x0b \x01(\x0b\x32 .ModuleConfig.NeighborInfoConfig\x12=\n\x10\x61mbient_lighting\x18\x0c \x01(\x0b\x32#.ModuleConfig.AmbientLightingConfig\x12=\n\x10\x64\x65tection_sensor\x18\r \x01(\x0b\x32#.ModuleConfig.DetectionSensorConfig\x12\x0f\n\x07version\x18\x08 \x01(\rBd\n\x13\x63om.geeksville.meshB\x0fLocalOnlyProtosZ\"github.com/meshtastic/go/generated\xaa\x02\x14Meshtastic.Protobufs\xba\x02\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meshtastic.localonly_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\017LocalOnlyProtosZ\"github.com/meshtastic/go/generated\252\002\024Meshtastic.Protobufs\272\002\000'
  _LOCALCONFIG._serialized_start=88
  _LOCALCONFIG._serialized_end=392
  _LOCALMODULECONFIG._serialized_start=395
  _LOCALMODULECONFIG._serialized_end=1091
# @@protoc_insertion_point(module_scope)
