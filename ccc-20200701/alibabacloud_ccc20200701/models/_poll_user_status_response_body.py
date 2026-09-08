# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class PollUserStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.PollUserStatusResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        # The response code.
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
            temp_model = main_models.PollUserStatusResponseBodyData()
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

class PollUserStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        call_context: main_models.PollUserStatusResponseBodyDataCallContext = None,
        chat_contexts: List[main_models.PollUserStatusResponseBodyDataChatContexts] = None,
        context_id: int = None,
        user_context: main_models.PollUserStatusResponseBodyDataUserContext = None,
    ):
        # Call context environment.
        self.call_context = call_context
        # Session context environment.
        self.chat_contexts = chat_contexts
        # System auto increment ID. Customers do not need to concern themselves with this.
        self.context_id = context_id
        # Agent context environment.
        self.user_context = user_context

    def validate(self):
        if self.call_context:
            self.call_context.validate()
        if self.chat_contexts:
            for v1 in self.chat_contexts:
                 if v1:
                    v1.validate()
        if self.user_context:
            self.user_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_context is not None:
            result['CallContext'] = self.call_context.to_map()

        result['ChatContexts'] = []
        if self.chat_contexts is not None:
            for k1 in self.chat_contexts:
                result['ChatContexts'].append(k1.to_map() if k1 else None)

        if self.context_id is not None:
            result['ContextId'] = self.context_id

        if self.user_context is not None:
            result['UserContext'] = self.user_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallContext') is not None:
            temp_model = main_models.PollUserStatusResponseBodyDataCallContext()
            self.call_context = temp_model.from_map(m.get('CallContext'))

        self.chat_contexts = []
        if m.get('ChatContexts') is not None:
            for k1 in m.get('ChatContexts'):
                temp_model = main_models.PollUserStatusResponseBodyDataChatContexts()
                self.chat_contexts.append(temp_model.from_map(k1))

        if m.get('ContextId') is not None:
            self.context_id = m.get('ContextId')

        if m.get('UserContext') is not None:
            temp_model = main_models.PollUserStatusResponseBodyDataUserContext()
            self.user_context = temp_model.from_map(m.get('UserContext'))

        return self

class PollUserStatusResponseBodyDataUserContext(DaraModel):
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
        parallel_job_list: List[main_models.PollUserStatusResponseBodyDataUserContextParallelJobList] = None,
        reserved: int = None,
        signed_skill_group_id_list: List[str] = None,
        user_id: str = None,
        user_state: str = None,
        work_mode: str = None,
    ):
        # Break status code, which can be either System-defined or Customer-defined. System-defined break codes include: Warm-up (temporary break state after an agent is published and before becoming idle), RingingTimeout (break caused by agent ringing timeout), and RejectCall (break caused by agent call rejection). There are no restrictions on Customer-defined status codes, and customers can define them according to their business needs.
        self.break_code = break_code
        # Device ID, the identity ID of a browser-based Web Real-Time Communication (WebRTC) softphone or a physical phone device. Only one type of device can be registered at a time.
        self.device_id = device_id
        # Agent extension number.
        self.extension = extension
        # The time when the last heartbeat was received from the agent, in Unix timestamp format, in milliseconds.
        self.heartbeat = heartbeat
        # Instance ID.
        self.instance_id = instance_id
        # Call ID.
        self.job_id = job_id
        # The agent\\"s personal phone number.
        self.mobile = mobile
        # Indicates whether the agent is in outbound-only mode.
        self.outbound_scenario = outbound_scenario
        # Chat sessions currently being handled or already handled by the agent
        self.parallel_job_list = parallel_job_list
        # The UNIX timestamp (in milliseconds) indicating when the agent was most recently reserved. Being reserved means an incoming call will soon be assigned to the agent.
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
        if self.parallel_job_list:
            for v1 in self.parallel_job_list:
                 if v1:
                    v1.validate()

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

        result['ParallelJobList'] = []
        if self.parallel_job_list is not None:
            for k1 in self.parallel_job_list:
                result['ParallelJobList'].append(k1.to_map() if k1 else None)

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

        self.parallel_job_list = []
        if m.get('ParallelJobList') is not None:
            for k1 in m.get('ParallelJobList'):
                temp_model = main_models.PollUserStatusResponseBodyDataUserContextParallelJobList()
                self.parallel_job_list.append(temp_model.from_map(k1))

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

class PollUserStatusResponseBodyDataUserContextParallelJobList(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        status: str = None,
        timestamp: int = None,
    ):
        # Session ID.
        self.job_id = job_id
        # The agent\\"s status in this session.
        # 
        # ### Enumeration values:
        # 
        # - RINGING
        # 
        # - TALKING
        # 
        # - RELEASED (End)
        # 
        # - MISSED (Missed)
        self.status = status
        # The time when the status changed.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.status is not None:
            result['Status'] = self.status

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class PollUserStatusResponseBodyDataChatContexts(DaraModel):
    def __init__(
        self,
        call_variables: str = None,
        chat_type: str = None,
        instance_id: str = None,
        job_id: str = None,
        members: List[main_models.PollUserStatusResponseBodyDataChatContextsMembers] = None,
    ):
        # Ingest endpoint data.
        self.call_variables = call_variables
        # Session type.
        self.chat_type = chat_type
        # Instance ID.
        self.instance_id = instance_id
        # Call job ID.
        self.job_id = job_id
        # Information about the agents and customers participating in this chat session.
        self.members = members

    def validate(self):
        if self.members:
            for v1 in self.members:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_variables is not None:
            result['CallVariables'] = self.call_variables

        if self.chat_type is not None:
            result['ChatType'] = self.chat_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        result['Members'] = []
        if self.members is not None:
            for k1 in self.members:
                result['Members'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallVariables') is not None:
            self.call_variables = m.get('CallVariables')

        if m.get('ChatType') is not None:
            self.chat_type = m.get('ChatType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        self.members = []
        if m.get('Members') is not None:
            for k1 in m.get('Members'):
                temp_model = main_models.PollUserStatusResponseBodyDataChatContextsMembers()
                self.members.append(temp_model.from_map(k1))

        return self

class PollUserStatusResponseBodyDataChatContextsMembers(DaraModel):
    def __init__(
        self,
        index: int = None,
        release_initiator: str = None,
        release_reason: str = None,
        skill_group_id: str = None,
        status: str = None,
        user_id: str = None,
        user_type: str = None,
    ):
        # System auto increment ID. Customers do not need to concern themselves with this value.
        self.index = index
        # The party that initiated the hang-up.
        self.release_initiator = release_initiator
        # The hang-up reason for the call channel, indicating why the current call channel was terminated. The value is derived from the response codes defined in the SIP protocol. Customers should refer to the SIP protocol for analysis of the hang-up reason.
        self.release_reason = release_reason
        # Skill group ID.
        self.skill_group_id = skill_group_id
        # The status of the agent in this session.
        # 
        # Enumeration values:
        # 
        # - RINGING
        # 
        # - TALKING
        # 
        # - RELEASED (End)
        # 
        # - MISSED (Missed)
        self.status = status
        # Agent ID.
        self.user_id = user_id
        # User type.
        # 
        # Enumeration values:
        # 
        # - CUSTOMER: Customer
        # 
        # - AGENT: Agent
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['Index'] = self.index

        if self.release_initiator is not None:
            result['ReleaseInitiator'] = self.release_initiator

        if self.release_reason is not None:
            result['ReleaseReason'] = self.release_reason

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('ReleaseInitiator') is not None:
            self.release_initiator = m.get('ReleaseInitiator')

        if m.get('ReleaseReason') is not None:
            self.release_reason = m.get('ReleaseReason')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

class PollUserStatusResponseBodyDataCallContext(DaraModel):
    def __init__(
        self,
        call_type: str = None,
        call_variables: str = None,
        channel_contexts: List[main_models.PollUserStatusResponseBodyDataCallContextChannelContexts] = None,
        instance_id: str = None,
        job_id: str = None,
    ):
        # Call type.
        self.call_type = call_type
        # Ingest endpoint data. Custom data passed through SIP signaling.
        self.call_variables = call_variables
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

        if self.call_variables is not None:
            result['CallVariables'] = self.call_variables

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

        if m.get('CallVariables') is not None:
            self.call_variables = m.get('CallVariables')

        self.channel_contexts = []
        if m.get('ChannelContexts') is not None:
            for k1 in m.get('ChannelContexts'):
                temp_model = main_models.PollUserStatusResponseBodyDataCallContextChannelContexts()
                self.channel_contexts.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        return self

class PollUserStatusResponseBodyDataCallContextChannelContexts(DaraModel):
    def __init__(
        self,
        call_type: str = None,
        channel_flags: str = None,
        channel_id: str = None,
        channel_state: str = None,
        channel_variables: str = None,
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
        # The call type of the channel.
        self.call_type = call_type
        # Call channel flags.
        self.channel_flags = channel_flags
        # The channel ID.
        self.channel_id = channel_id
        # The status of the call channel.
        self.channel_state = channel_state
        # Channel-associated data.
        self.channel_variables = channel_variables
        # Callee of the call channel.
        self.destination = destination
        # Auto-incremented system ID. Customers do not need to concern themselves with this value.
        self.index = index
        # The call ID.
        self.job_id = job_id
        # The calling party of the call channel.
        self.originator = originator
        # The party that initiated the hang-up of the call channel, indicating who first terminated the call.
        self.release_initiator = release_initiator
        # The hang-up reason for the call channel, indicating why the current call channel was disconnected. The value comes from the response codes defined in the SIP protocol. Customers should refer to the SIP protocol to analyze the hang-up reason.
        self.release_reason = release_reason
        # The skill group ID associated with the channel. In inbound scenarios, the associated skill group ID is determined by the skill group configured in the IVR transfer-to-agent module. In outbound scenarios, the associated skill group ID is the first skill group the agent signed into.
        self.skill_group_id = skill_group_id
        # The UNIX timestamp indicating the most recent status change of the channel, in milliseconds.
        self.timestamp = timestamp
        # The extension number of the agent associated with the voice channel.
        self.user_extension = user_extension
        # The agent ID associated with the voice channel. This field is empty if the channel belongs to a customer.
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

        if self.channel_variables is not None:
            result['ChannelVariables'] = self.channel_variables

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

        if m.get('ChannelVariables') is not None:
            self.channel_variables = m.get('ChannelVariables')

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

