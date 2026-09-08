# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class SignOutGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.SignOutGroupResponseBodyData = None,
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
            temp_model = main_models.SignOutGroupResponseBodyData()
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

class SignOutGroupResponseBodyData(DaraModel):
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
        # Break status code, which can be either System-defined or Custom-defined. System-defined break codes include: Warm-up (temporary break status after the agent is published but before becoming idle), RingingTimeout (break caused by ringing timeout), and RejectCall (break caused by the agent rejecting a call). There are no restrictions on Custom-defined status codes; customers can define them according to their business needs.
        self.break_code = break_code
        # Device ID, which is the identity of a browser-based Web Real-Time Communication (WebRTC) softphone or a physical phone device. Only one type of device can be registered at a time.
        self.device_id = device_id
        # Agent extension number.
        self.extension = extension
        # Time of the last received agent heartbeat, formatted as a UNIX timestamp in milliseconds.
        self.heartbeat = heartbeat
        # Instance ID.
        self.instance_id = instance_id
        # Call ID.
        self.job_id = job_id
        # The agent\\"s personal phone number.
        self.mobile = mobile
        # Indicates whether the agent is in outbound-only mode.
        self.outbound_scenario = outbound_scenario
        # The UNIX timestamp (in milliseconds) indicating the most recent time the agent was reserved. Being reserved means an incoming call will be assigned to the agent shortly.
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

