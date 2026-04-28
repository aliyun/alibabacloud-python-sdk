# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CloudBatchGetAgentStatusResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CloudBatchGetAgentStatusResponseBodyData = None,
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
            temp_model = main_models.CloudBatchGetAgentStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CloudBatchGetAgentStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        device_status: str = None,
        login_status: str = None,
        main_unique_id: str = None,
        state: str = None,
        state_action: str = None,
    ):
        # 座席设备状态，座席登录状态不是离线时返回  -1：错误的状态  0：空闲状态  1：锁定状态   2：邀请中状态  3：响铃状态  4：使用中状态
        self.device_status = device_status
        # 座席登录状态   0：离线状态  1：在线状态  2：置忙状态  3：整理状态
        self.login_status = login_status
        # 座席当前参与的通话唯一标识，座席设备状态为1/2/3/4时返回
        self.main_unique_id = main_unique_id
        # 座席状态描述（结合了登录状态和设备状态），离线，空闲，置忙，整理，呼叫中，响铃，保持，通话
        self.state = state
        # 状态对应的动作，座席登录状态不是离线时返回。详见[座席状态动作说明](../../工具条/座席状态动作.md)
        self.state_action = state_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status

        if self.login_status is not None:
            result['LoginStatus'] = self.login_status

        if self.main_unique_id is not None:
            result['MainUniqueId'] = self.main_unique_id

        if self.state is not None:
            result['State'] = self.state

        if self.state_action is not None:
            result['StateAction'] = self.state_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')

        if m.get('LoginStatus') is not None:
            self.login_status = m.get('LoginStatus')

        if m.get('MainUniqueId') is not None:
            self.main_unique_id = m.get('MainUniqueId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('StateAction') is not None:
            self.state_action = m.get('StateAction')

        return self

