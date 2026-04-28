# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CloudListOnlineAgentResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CloudListOnlineAgentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CloudListOnlineAgentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CloudListOnlineAgentResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_statuses: List[main_models.CloudListOnlineAgentResponseBodyDataAgentStatuses] = None,
    ):
        # 座席状态数组
        self.agent_statuses = agent_statuses

    def validate(self):
        if self.agent_statuses:
            for v1 in self.agent_statuses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AgentStatuses'] = []
        if self.agent_statuses is not None:
            for k1 in self.agent_statuses:
                result['AgentStatuses'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agent_statuses = []
        if m.get('AgentStatuses') is not None:
            for k1 in m.get('AgentStatuses'):
                temp_model = main_models.CloudListOnlineAgentResponseBodyDataAgentStatuses()
                self.agent_statuses.append(temp_model.from_map(k1))

        return self

class CloudListOnlineAgentResponseBodyDataAgentStatuses(DaraModel):
    def __init__(
        self,
        bind_tel: str = None,
        cno: str = None,
        device_status: int = None,
        device_status_duration: int = None,
        login_status: int = None,
        login_status_duration: int = None,
        login_time: str = None,
        name: str = None,
        state: str = None,
    ):
        # 绑定电话
        self.bind_tel = bind_tel
        # 座席工号
        self.cno = cno
        # 设备状态，-1 失效，0 空闲，1 已锁定，2 呼叫中，3 响铃，4 通话中
        self.device_status = device_status
        # 设备状态时长
        self.device_status_duration = device_status_duration
        # 登录状态，0离线，1在线，2置忙，3整理
        self.login_status = login_status
        # 登录状态时长
        self.login_status_duration = login_status_duration
        # 登录时间
        self.login_time = login_time
        # 座席名称
        self.name = name
        # 座席状态（结合了登录状态和设备状态），失效，空闲，置忙，整理，呼叫中，响铃，通话
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_tel is not None:
            result['BindTel'] = self.bind_tel

        if self.cno is not None:
            result['Cno'] = self.cno

        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status

        if self.device_status_duration is not None:
            result['DeviceStatusDuration'] = self.device_status_duration

        if self.login_status is not None:
            result['LoginStatus'] = self.login_status

        if self.login_status_duration is not None:
            result['LoginStatusDuration'] = self.login_status_duration

        if self.login_time is not None:
            result['LoginTime'] = self.login_time

        if self.name is not None:
            result['Name'] = self.name

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindTel') is not None:
            self.bind_tel = m.get('BindTel')

        if m.get('Cno') is not None:
            self.cno = m.get('Cno')

        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')

        if m.get('DeviceStatusDuration') is not None:
            self.device_status_duration = m.get('DeviceStatusDuration')

        if m.get('LoginStatus') is not None:
            self.login_status = m.get('LoginStatus')

        if m.get('LoginStatusDuration') is not None:
            self.login_status_duration = m.get('LoginStatusDuration')

        if m.get('LoginTime') is not None:
            self.login_time = m.get('LoginTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

