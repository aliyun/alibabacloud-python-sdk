# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wyota20210420 import models as main_models
from darabonba.model import DaraModel

class ListTerminalResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListTerminalResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListTerminalResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTerminalResponseBodyData(DaraModel):
    def __init__(
        self,
        alias: str = None,
        bind_user_count: int = None,
        bind_user_id: str = None,
        build_id: str = None,
        client_type: int = None,
        desktop_id: str = None,
        in_manage: bool = None,
        ipv_4: str = None,
        last_login_user: str = None,
        location_info: str = None,
        lock_settings: bool = None,
        login_user: str = None,
        model: str = None,
        online_status: bool = None,
        serial_number: str = None,
        terminal_group_id: str = None,
        uuid: str = None,
    ):
        self.alias = alias
        self.bind_user_count = bind_user_count
        self.bind_user_id = bind_user_id
        self.build_id = build_id
        self.client_type = client_type
        self.desktop_id = desktop_id
        self.in_manage = in_manage
        self.ipv_4 = ipv_4
        self.last_login_user = last_login_user
        self.location_info = location_info
        self.lock_settings = lock_settings
        self.login_user = login_user
        self.model = model
        self.online_status = online_status
        self.serial_number = serial_number
        self.terminal_group_id = terminal_group_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.bind_user_count is not None:
            result['BindUserCount'] = self.bind_user_count

        if self.bind_user_id is not None:
            result['BindUserId'] = self.bind_user_id

        if self.build_id is not None:
            result['BuildId'] = self.build_id

        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.in_manage is not None:
            result['InManage'] = self.in_manage

        if self.ipv_4 is not None:
            result['Ipv4'] = self.ipv_4

        if self.last_login_user is not None:
            result['LastLoginUser'] = self.last_login_user

        if self.location_info is not None:
            result['LocationInfo'] = self.location_info

        if self.lock_settings is not None:
            result['LockSettings'] = self.lock_settings

        if self.login_user is not None:
            result['LoginUser'] = self.login_user

        if self.model is not None:
            result['Model'] = self.model

        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.terminal_group_id is not None:
            result['TerminalGroupId'] = self.terminal_group_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('BindUserCount') is not None:
            self.bind_user_count = m.get('BindUserCount')

        if m.get('BindUserId') is not None:
            self.bind_user_id = m.get('BindUserId')

        if m.get('BuildId') is not None:
            self.build_id = m.get('BuildId')

        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('InManage') is not None:
            self.in_manage = m.get('InManage')

        if m.get('Ipv4') is not None:
            self.ipv_4 = m.get('Ipv4')

        if m.get('LastLoginUser') is not None:
            self.last_login_user = m.get('LastLoginUser')

        if m.get('LocationInfo') is not None:
            self.location_info = m.get('LocationInfo')

        if m.get('LockSettings') is not None:
            self.lock_settings = m.get('LockSettings')

        if m.get('LoginUser') is not None:
            self.login_user = m.get('LoginUser')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('TerminalGroupId') is not None:
            self.terminal_group_id = m.get('TerminalGroupId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

