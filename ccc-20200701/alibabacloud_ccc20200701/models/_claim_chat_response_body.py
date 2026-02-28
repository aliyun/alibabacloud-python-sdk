# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ClaimChatResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ClaimChatResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.params = params
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
            temp_model = main_models.ClaimChatResponseBodyData()
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

class ClaimChatResponseBodyData(DaraModel):
    def __init__(
        self,
        chat_contexts: List[main_models.ClaimChatResponseBodyDataChatContexts] = None,
        context_id: int = None,
        user_context: main_models.ClaimChatResponseBodyDataUserContext = None,
    ):
        self.chat_contexts = chat_contexts
        self.context_id = context_id
        self.user_context = user_context

    def validate(self):
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
        self.chat_contexts = []
        if m.get('ChatContexts') is not None:
            for k1 in m.get('ChatContexts'):
                temp_model = main_models.ClaimChatResponseBodyDataChatContexts()
                self.chat_contexts.append(temp_model.from_map(k1))

        if m.get('ContextId') is not None:
            self.context_id = m.get('ContextId')

        if m.get('UserContext') is not None:
            temp_model = main_models.ClaimChatResponseBodyDataUserContext()
            self.user_context = temp_model.from_map(m.get('UserContext'))

        return self

class ClaimChatResponseBodyDataUserContext(DaraModel):
    def __init__(
        self,
        break_code: str = None,
        device_id: str = None,
        device_state: str = None,
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
        self.break_code = break_code
        self.device_id = device_id
        self.device_state = device_state
        self.extension = extension
        self.heartbeat = heartbeat
        self.instance_id = instance_id
        self.job_id = job_id
        self.mobile = mobile
        self.outbound_scenario = outbound_scenario
        self.reserved = reserved
        self.signed_skill_group_id_list = signed_skill_group_id_list
        self.user_id = user_id
        self.user_state = user_state
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

        if self.device_state is not None:
            result['DeviceState'] = self.device_state

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

        if m.get('DeviceState') is not None:
            self.device_state = m.get('DeviceState')

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

class ClaimChatResponseBodyDataChatContexts(DaraModel):
    def __init__(
        self,
        access_channel_id: str = None,
        access_channel_name: str = None,
        access_channel_type: str = None,
        being_assigned: bool = None,
        call_variables: str = None,
        chat_type: str = None,
        instance_id: str = None,
        job_id: str = None,
    ):
        self.access_channel_id = access_channel_id
        self.access_channel_name = access_channel_name
        self.access_channel_type = access_channel_type
        self.being_assigned = being_assigned
        self.call_variables = call_variables
        self.chat_type = chat_type
        self.instance_id = instance_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_channel_id is not None:
            result['AccessChannelId'] = self.access_channel_id

        if self.access_channel_name is not None:
            result['AccessChannelName'] = self.access_channel_name

        if self.access_channel_type is not None:
            result['AccessChannelType'] = self.access_channel_type

        if self.being_assigned is not None:
            result['BeingAssigned'] = self.being_assigned

        if self.call_variables is not None:
            result['CallVariables'] = self.call_variables

        if self.chat_type is not None:
            result['ChatType'] = self.chat_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessChannelId') is not None:
            self.access_channel_id = m.get('AccessChannelId')

        if m.get('AccessChannelName') is not None:
            self.access_channel_name = m.get('AccessChannelName')

        if m.get('AccessChannelType') is not None:
            self.access_channel_type = m.get('AccessChannelType')

        if m.get('BeingAssigned') is not None:
            self.being_assigned = m.get('BeingAssigned')

        if m.get('CallVariables') is not None:
            self.call_variables = m.get('CallVariables')

        if m.get('ChatType') is not None:
            self.chat_type = m.get('ChatType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        return self

