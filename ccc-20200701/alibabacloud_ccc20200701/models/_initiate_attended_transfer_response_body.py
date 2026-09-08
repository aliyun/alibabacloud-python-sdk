# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class InitiateAttendedTransferResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.InitiateAttendedTransferResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        # Response code.
        self.code = code
        # Data.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Response message.
        self.message = message
        # List of response parameters.
        self.params = params
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.InitiateAttendedTransferResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class InitiateAttendedTransferResponseBodyData(DaraModel):
    def __init__(
        self,
        call_context: main_models.InitiateAttendedTransferResponseBodyDataCallContext = None,
        context_id: int = None,
        user_context: main_models.InitiateAttendedTransferResponseBodyDataUserContext = None,
    ):
        # Call context environment.
        self.call_context = call_context
        # System auto increment ID. Customers do not need to concern themselves with this field.
        self.context_id = context_id
        # Agent context environment.
        self.user_context = user_context

    def validate(self):
        if self.call_context:
            self.call_context.validate()
        if self.user_context:
            self.user_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_context is not None:
            result['CallContext'] = self.call_context.to_map()

        if self.context_id is not None:
            result['ContextId'] = self.context_id

        if self.user_context is not None:
            result['UserContext'] = self.user_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallContext') is not None:
            temp_model = main_models.InitiateAttendedTransferResponseBodyDataCallContext()
            self.call_context = temp_model.from_map(m.get('CallContext'))

        if m.get('ContextId') is not None:
            self.context_id = m.get('ContextId')

        if m.get('UserContext') is not None:
            temp_model = main_models.InitiateAttendedTransferResponseBodyDataUserContext()
            self.user_context = temp_model.from_map(m.get('UserContext'))

        return self

class InitiateAttendedTransferResponseBodyDataUserContext(DaraModel):
    def __init__(
        self,
        break_code: str = None,
        device_id: str = None,
        extension: str = None,
        heartbeat: int = None,
        instance_id: str = None,
        job_id: str = None,
        mobile: str = None,
        outbound_scenario: bool = None,
        reserved: int = None,
        signed_skill_group_id_list: List[str] = None,
        user_id: str = None,
        user_state: str = None,
        work_mode: str = None,
    ):
        # Break status code, which can be either System-defined or Custom-defined. System-defined break codes include: Warm-up (temporary break state after an agent is published and before becoming idle), RingingTimeout (break caused by agent ringing timeout), and RejectCall (break caused by agent call rejection). There are no restrictions on Custom-defined status codes; customers can define them as needed for their business.
        self.break_code = break_code
        # Device ID, the identity ID of a browser-based Web Real-Time Communication (WebRTC) softphone or a physical phone device. Only one type of device can be registered at a time.
        self.device_id = device_id
        # The agent\\"s extension number.
        self.extension = extension
        # The time when the last heartbeat was received from the agent, in UNIX timestamp format with millisecond precision.
        self.heartbeat = heartbeat
        # Instance ID.
        self.instance_id = instance_id
        # Call ID.
        self.job_id = job_id
        # The agent\\"s personal phone number.
        self.mobile = mobile
        # Indicates whether the agent is in outbound-only mode.
        self.outbound_scenario = outbound_scenario
        # The most recent time when the agent was reserved. Being reserved means an incoming call will be assigned to the agent shortly. The value is formatted as a UNIX timestamp in milliseconds.
        self.reserved = reserved
        # List of skill group IDs that the agent has signed into.
        self.signed_skill_group_id_list = signed_skill_group_id_list
        # Agent ID.
        self.user_id = user_id
        # Agent status.
        self.user_state = user_state
        # Work mode.
        self.work_mode = work_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.break_code is not None:
            result['BreakCode'] = self.break_code

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.heartbeat is not None:
            result['Heartbeat'] = self.heartbeat

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.outbound_scenario is not None:
            result['OutboundScenario'] = self.outbound_scenario

        if self.reserved is not None:
            result['Reserved'] = self.reserved

        if self.signed_skill_group_id_list is not None:
            result['SignedSkillGroupIdList'] = self.signed_skill_group_id_list

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_state is not None:
            result['UserState'] = self.user_state

        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BreakCode') is not None:
            self.break_code = m.get('BreakCode')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('Heartbeat') is not None:
            self.heartbeat = m.get('Heartbeat')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('OutboundScenario') is not None:
            self.outbound_scenario = m.get('OutboundScenario')

        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')

        if m.get('SignedSkillGroupIdList') is not None:
            self.signed_skill_group_id_list = m.get('SignedSkillGroupIdList')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserState') is not None:
            self.user_state = m.get('UserState')

        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')

        return self

class InitiateAttendedTransferResponseBodyDataCallContext(DaraModel):
    def __init__(
        self,
        call_type: str = None,
        channel_contexts: List[main_models.InitiateAttendedTransferResponseBodyDataCallContextChannelContexts] = None,
        instance_id: str = None,
        job_id: str = None,
    ):
        # Call type.
        self.call_type = call_type
        # List of call channels.
        self.channel_contexts = channel_contexts
        # Instance ID.
        self.instance_id = instance_id
        # Call ID.
        self.job_id = job_id

    def validate(self):
        if self.channel_contexts:
            for v1 in self.channel_contexts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_type is not None:
            result['CallType'] = self.call_type

        result['ChannelContexts'] = []
        if self.channel_contexts is not None:
            for k1 in self.channel_contexts:
                result['ChannelContexts'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')

        self.channel_contexts = []
        if m.get('ChannelContexts') is not None:
            for k1 in m.get('ChannelContexts'):
                temp_model = main_models.InitiateAttendedTransferResponseBodyDataCallContextChannelContexts()
                self.channel_contexts.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        return self

class InitiateAttendedTransferResponseBodyDataCallContextChannelContexts(DaraModel):
    def __init__(
        self,
        call_type: str = None,
        channel_flags: str = None,
        channel_id: str = None,
        channel_state: str = None,
        destination: str = None,
        index: int = None,
        job_id: str = None,
        originator: str = None,
        release_initiator: str = None,
        release_reason: str = None,
        skill_group_id: str = None,
        timestamp: int = None,
        user_extension: str = None,
        user_id: str = None,
    ):
        # The call type of the call channel.
        self.call_type = call_type
        # Channel flags.
        self.channel_flags = channel_flags
        # Channel ID.
        self.channel_id = channel_id
        # The status of the call channel.
        self.channel_state = channel_state
        # The callee of the call channel.
        self.destination = destination
        # Records the order in which this channel was created during the call.
        self.index = index
        # The call ID.
        self.job_id = job_id
        # The originator of the channel.
        self.originator = originator
        # The party that initiated the release of the call channel, indicating who hung up first.
        self.release_initiator = release_initiator
        # The hang-up reason for the voice channel, indicating why the current voice channel was disconnected. The value comes from the response codes defined in the SIP protocol. Customers should refer to the SIP protocol to analyze the hang-up reason.
        self.release_reason = release_reason
        # The skill group ID associated with the voice channel. In inbound scenarios, the associated skill group ID is determined by the agent transfer module configured in the IVR. In outbound scenarios, the associated skill group ID is the first skill group the agent signed into.
        self.skill_group_id = skill_group_id
        # The UNIX timestamp of the most recent status change of the voice channel, in milliseconds.
        self.timestamp = timestamp
        # The extension number of the agent associated with the channel.
        self.user_extension = user_extension
        # The agent ID associated with the channel. This field is empty for a Customer channel.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_type is not None:
            result['CallType'] = self.call_type

        if self.channel_flags is not None:
            result['ChannelFlags'] = self.channel_flags

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.channel_state is not None:
            result['ChannelState'] = self.channel_state

        if self.destination is not None:
            result['Destination'] = self.destination

        if self.index is not None:
            result['Index'] = self.index

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.originator is not None:
            result['Originator'] = self.originator

        if self.release_initiator is not None:
            result['ReleaseInitiator'] = self.release_initiator

        if self.release_reason is not None:
            result['ReleaseReason'] = self.release_reason

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.user_extension is not None:
            result['UserExtension'] = self.user_extension

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')

        if m.get('ChannelFlags') is not None:
            self.channel_flags = m.get('ChannelFlags')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('ChannelState') is not None:
            self.channel_state = m.get('ChannelState')

        if m.get('Destination') is not None:
            self.destination = m.get('Destination')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Originator') is not None:
            self.originator = m.get('Originator')

        if m.get('ReleaseInitiator') is not None:
            self.release_initiator = m.get('ReleaseInitiator')

        if m.get('ReleaseReason') is not None:
            self.release_reason = m.get('ReleaseReason')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('UserExtension') is not None:
            self.user_extension = m.get('UserExtension')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

