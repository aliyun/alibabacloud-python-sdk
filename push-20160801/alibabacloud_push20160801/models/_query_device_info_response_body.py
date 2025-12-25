# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_push20160801 import models as main_models
from darabonba.model import DaraModel

class QueryDeviceInfoResponseBody(DaraModel):
    def __init__(
        self,
        device_info: main_models.QueryDeviceInfoResponseBodyDeviceInfo = None,
        request_id: str = None,
    ):
        self.device_info = device_info
        self.request_id = request_id

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = main_models.QueryDeviceInfoResponseBodyDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryDeviceInfoResponseBodyDeviceInfo(DaraModel):
    def __init__(
        self,
        account: str = None,
        alias: str = None,
        brand: str = None,
        device_id: str = None,
        device_token: str = None,
        device_type: str = None,
        last_online_time: str = None,
        model: str = None,
        online: bool = None,
        phone_number: str = None,
        push_enabled: bool = None,
        tags: str = None,
    ):
        self.account = account
        self.alias = alias
        self.brand = brand
        self.device_id = device_id
        self.device_token = device_token
        self.device_type = device_type
        self.last_online_time = last_online_time
        self.model = model
        self.online = online
        self.phone_number = phone_number
        self.push_enabled = push_enabled
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.alias is not None:
            result['Alias'] = self.alias

        if self.brand is not None:
            result['Brand'] = self.brand

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.device_token is not None:
            result['DeviceToken'] = self.device_token

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.last_online_time is not None:
            result['LastOnlineTime'] = self.last_online_time

        if self.model is not None:
            result['Model'] = self.model

        if self.online is not None:
            result['Online'] = self.online

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.push_enabled is not None:
            result['PushEnabled'] = self.push_enabled

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('Brand') is not None:
            self.brand = m.get('Brand')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('LastOnlineTime') is not None:
            self.last_online_time = m.get('LastOnlineTime')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Online') is not None:
            self.online = m.get('Online')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('PushEnabled') is not None:
            self.push_enabled = m.get('PushEnabled')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

