# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mlagents/envs/communicator_objects/unity_rl_output.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mlagents.envs.communicator_objects import agent_info_proto_pb2 as mlagents_dot_envs_dot_communicator__objects_dot_agent__info__proto__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mlagents/envs/communicator_objects/unity_rl_output.proto',
  package='communicator_objects',
  syntax='proto3',
  serialized_options=_b('\252\002\034MLAgents.CommunicatorObjects'),
  serialized_pb=_b('\n8mlagents/envs/communicator_objects/unity_rl_output.proto\x12\x14\x63ommunicator_objects\x1a\x39mlagents/envs/communicator_objects/agent_info_proto.proto\"\x94\x02\n\rUnityRLOutput\x12G\n\nagentInfos\x18\x02 \x03(\x0b\x32\x33.communicator_objects.UnityRLOutput.AgentInfosEntry\x1aI\n\x12ListAgentInfoProto\x12\x33\n\x05value\x18\x01 \x03(\x0b\x32$.communicator_objects.AgentInfoProto\x1ai\n\x0f\x41gentInfosEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x45\n\x05value\x18\x02 \x01(\x0b\x32\x36.communicator_objects.UnityRLOutput.ListAgentInfoProto:\x02\x38\x01J\x04\x08\x01\x10\x02\x42\x1f\xaa\x02\x1cMLAgents.CommunicatorObjectsb\x06proto3')
  ,
  dependencies=[mlagents_dot_envs_dot_communicator__objects_dot_agent__info__proto__pb2.DESCRIPTOR,])




_UNITYRLOUTPUT_LISTAGENTINFOPROTO = _descriptor.Descriptor(
  name='ListAgentInfoProto',
  full_name='communicator_objects.UnityRLOutput.ListAgentInfoProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='communicator_objects.UnityRLOutput.ListAgentInfoProto.value', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=232,
  serialized_end=305,
)

_UNITYRLOUTPUT_AGENTINFOSENTRY = _descriptor.Descriptor(
  name='AgentInfosEntry',
  full_name='communicator_objects.UnityRLOutput.AgentInfosEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='communicator_objects.UnityRLOutput.AgentInfosEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='communicator_objects.UnityRLOutput.AgentInfosEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=307,
  serialized_end=412,
)

_UNITYRLOUTPUT = _descriptor.Descriptor(
  name='UnityRLOutput',
  full_name='communicator_objects.UnityRLOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agentInfos', full_name='communicator_objects.UnityRLOutput.agentInfos', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UNITYRLOUTPUT_LISTAGENTINFOPROTO, _UNITYRLOUTPUT_AGENTINFOSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=418,
)

_UNITYRLOUTPUT_LISTAGENTINFOPROTO.fields_by_name['value'].message_type = mlagents_dot_envs_dot_communicator__objects_dot_agent__info__proto__pb2._AGENTINFOPROTO
_UNITYRLOUTPUT_LISTAGENTINFOPROTO.containing_type = _UNITYRLOUTPUT
_UNITYRLOUTPUT_AGENTINFOSENTRY.fields_by_name['value'].message_type = _UNITYRLOUTPUT_LISTAGENTINFOPROTO
_UNITYRLOUTPUT_AGENTINFOSENTRY.containing_type = _UNITYRLOUTPUT
_UNITYRLOUTPUT.fields_by_name['agentInfos'].message_type = _UNITYRLOUTPUT_AGENTINFOSENTRY
DESCRIPTOR.message_types_by_name['UnityRLOutput'] = _UNITYRLOUTPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UnityRLOutput = _reflection.GeneratedProtocolMessageType('UnityRLOutput', (_message.Message,), dict(

  ListAgentInfoProto = _reflection.GeneratedProtocolMessageType('ListAgentInfoProto', (_message.Message,), dict(
    DESCRIPTOR = _UNITYRLOUTPUT_LISTAGENTINFOPROTO,
    __module__ = 'mlagents.envs.communicator_objects.unity_rl_output_pb2'
    # @@protoc_insertion_point(class_scope:communicator_objects.UnityRLOutput.ListAgentInfoProto)
    ))
  ,

  AgentInfosEntry = _reflection.GeneratedProtocolMessageType('AgentInfosEntry', (_message.Message,), dict(
    DESCRIPTOR = _UNITYRLOUTPUT_AGENTINFOSENTRY,
    __module__ = 'mlagents.envs.communicator_objects.unity_rl_output_pb2'
    # @@protoc_insertion_point(class_scope:communicator_objects.UnityRLOutput.AgentInfosEntry)
    ))
  ,
  DESCRIPTOR = _UNITYRLOUTPUT,
  __module__ = 'mlagents.envs.communicator_objects.unity_rl_output_pb2'
  # @@protoc_insertion_point(class_scope:communicator_objects.UnityRLOutput)
  ))
_sym_db.RegisterMessage(UnityRLOutput)
_sym_db.RegisterMessage(UnityRLOutput.ListAgentInfoProto)
_sym_db.RegisterMessage(UnityRLOutput.AgentInfosEntry)


DESCRIPTOR._options = None
_UNITYRLOUTPUT_AGENTINFOSENTRY._options = None
# @@protoc_insertion_point(module_scope)
