# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meshtastic/telemetry.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ameshtastic/telemetry.proto\x12\nmeshtastic\"i\n\rDeviceMetrics\x12\x15\n\rbattery_level\x18\x01 \x01(\r\x12\x0f\n\x07voltage\x18\x02 \x01(\x02\x12\x1b\n\x13\x63hannel_utilization\x18\x03 \x01(\x02\x12\x13\n\x0b\x61ir_util_tx\x18\x04 \x01(\x02\"\x9b\x01\n\x12\x45nvironmentMetrics\x12\x13\n\x0btemperature\x18\x01 \x01(\x02\x12\x19\n\x11relative_humidity\x18\x02 \x01(\x02\x12\x1b\n\x13\x62\x61rometric_pressure\x18\x03 \x01(\x02\x12\x16\n\x0egas_resistance\x18\x04 \x01(\x02\x12\x0f\n\x07voltage\x18\x05 \x01(\x02\x12\x0f\n\x07\x63urrent\x18\x06 \x01(\x02\"\x8c\x01\n\x0cPowerMetrics\x12\x13\n\x0b\x63h1_voltage\x18\x01 \x01(\x02\x12\x13\n\x0b\x63h1_current\x18\x02 \x01(\x02\x12\x13\n\x0b\x63h2_voltage\x18\x03 \x01(\x02\x12\x13\n\x0b\x63h2_current\x18\x04 \x01(\x02\x12\x13\n\x0b\x63h3_voltage\x18\x05 \x01(\x02\x12\x13\n\x0b\x63h3_current\x18\x06 \x01(\x02\"\xbf\x02\n\x11\x41irQualityMetrics\x12\x15\n\rpm10_standard\x18\x01 \x01(\r\x12\x15\n\rpm25_standard\x18\x02 \x01(\r\x12\x16\n\x0epm100_standard\x18\x03 \x01(\r\x12\x1a\n\x12pm10_environmental\x18\x04 \x01(\r\x12\x1a\n\x12pm25_environmental\x18\x05 \x01(\r\x12\x1b\n\x13pm100_environmental\x18\x06 \x01(\r\x12\x16\n\x0eparticles_03um\x18\x07 \x01(\r\x12\x16\n\x0eparticles_05um\x18\x08 \x01(\r\x12\x16\n\x0eparticles_10um\x18\t \x01(\r\x12\x16\n\x0eparticles_25um\x18\n \x01(\r\x12\x16\n\x0eparticles_50um\x18\x0b \x01(\r\x12\x17\n\x0fparticles_100um\x18\x0c \x01(\r\"\x89\x02\n\tTelemetry\x12\x0c\n\x04time\x18\x01 \x01(\x07\x12\x33\n\x0e\x64\x65vice_metrics\x18\x02 \x01(\x0b\x32\x19.meshtastic.DeviceMetricsH\x00\x12=\n\x13\x65nvironment_metrics\x18\x03 \x01(\x0b\x32\x1e.meshtastic.EnvironmentMetricsH\x00\x12<\n\x13\x61ir_quality_metrics\x18\x04 \x01(\x0b\x32\x1d.meshtastic.AirQualityMetricsH\x00\x12\x31\n\rpower_metrics\x18\x05 \x01(\x0b\x32\x18.meshtastic.PowerMetricsH\x00\x42\t\n\x07variant*\xd4\x01\n\x13TelemetrySensorType\x12\x10\n\x0cSENSOR_UNSET\x10\x00\x12\n\n\x06\x42ME280\x10\x01\x12\n\n\x06\x42ME680\x10\x02\x12\x0b\n\x07MCP9808\x10\x03\x12\n\n\x06INA260\x10\x04\x12\n\n\x06INA219\x10\x05\x12\n\n\x06\x42MP280\x10\x06\x12\t\n\x05SHTC3\x10\x07\x12\t\n\x05LPS22\x10\x08\x12\x0b\n\x07QMC6310\x10\t\x12\x0b\n\x07QMI8658\x10\n\x12\x0c\n\x08QMC5883L\x10\x0b\x12\t\n\x05SHT31\x10\x0c\x12\x0c\n\x08PMSA003I\x10\r\x12\x0b\n\x07INA3221\x10\x0e\x42\x64\n\x13\x63om.geeksville.meshB\x0fTelemetryProtosZ\"github.com/meshtastic/go/generated\xaa\x02\x14Meshtastic.Protobufs\xba\x02\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meshtastic.telemetry_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.geeksville.meshB\017TelemetryProtosZ\"github.com/meshtastic/go/generated\252\002\024Meshtastic.Protobufs\272\002\000'
  _globals['_TELEMETRYSENSORTYPE']._serialized_start=1041
  _globals['_TELEMETRYSENSORTYPE']._serialized_end=1253
  _globals['_DEVICEMETRICS']._serialized_start=42
  _globals['_DEVICEMETRICS']._serialized_end=147
  _globals['_ENVIRONMENTMETRICS']._serialized_start=150
  _globals['_ENVIRONMENTMETRICS']._serialized_end=305
  _globals['_POWERMETRICS']._serialized_start=308
  _globals['_POWERMETRICS']._serialized_end=448
  _globals['_AIRQUALITYMETRICS']._serialized_start=451
  _globals['_AIRQUALITYMETRICS']._serialized_end=770
  _globals['_TELEMETRY']._serialized_start=773
  _globals['_TELEMETRY']._serialized_end=1038
# @@protoc_insertion_point(module_scope)
