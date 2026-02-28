# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class GetUserResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetUserResponseBodyData = None,
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
            temp_model = main_models.GetUserResponseBodyData()
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

class GetUserResponseBodyData(DaraModel):
    def __init__(
        self,
        avatar_url: str = None,
        device_ext: str = None,
        device_id: str = None,
        device_state: str = None,
        display_id: str = None,
        display_name: str = None,
        email: str = None,
        extension: str = None,
        instance_id: str = None,
        login_name: str = None,
        mobile: str = None,
        nickname: str = None,
        role_id: str = None,
        role_name: str = None,
        user_id: str = None,
        work_mode: str = None,
    ):
        self.avatar_url = avatar_url
        self.device_ext = device_ext
        self.device_id = device_id
        self.device_state = device_state
        self.display_id = display_id
        self.display_name = display_name
        self.email = email
        self.extension = extension
        self.instance_id = instance_id
        self.login_name = login_name
        self.mobile = mobile
        self.nickname = nickname
        self.role_id = role_id
        self.role_name = role_name
        self.user_id = user_id
        self.work_mode = work_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url

        if self.device_ext is not None:
            result['DeviceExt'] = self.device_ext

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.device_state is not None:
            result['DeviceState'] = self.device_state

        if self.display_id is not None:
            result['DisplayId'] = self.display_id

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.email is not None:
            result['Email'] = self.email

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.login_name is not None:
            result['LoginName'] = self.login_name

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.nickname is not None:
            result['Nickname'] = self.nickname

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')

        if m.get('DeviceExt') is not None:
            self.device_ext = m.get('DeviceExt')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('DeviceState') is not None:
            self.device_state = m.get('DeviceState')

        if m.get('DisplayId') is not None:
            self.display_id = m.get('DisplayId')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LoginName') is not None:
            self.login_name = m.get('LoginName')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('Nickname') is not None:
            self.nickname = m.get('Nickname')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')

        return self

