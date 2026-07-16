# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emas_appmonitor20190611 import models as main_models
from darabonba.model import DaraModel

class GetTlogDeviceInfoResponseBody(DaraModel):
    def __init__(
        self,
        error_code: int = None,
        message: str = None,
        model: main_models.GetTlogDeviceInfoResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.model is not None:
            result['Model'] = self.model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Model') is not None:
            temp_model = main_models.GetTlogDeviceInfoResponseBodyModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetTlogDeviceInfoResponseBodyModel(DaraModel):
    def __init__(
        self,
        app_build: str = None,
        app_id: str = None,
        app_key: str = None,
        app_version: str = None,
        brand: str = None,
        client_time: int = None,
        device_id: str = None,
        device_model: str = None,
        geo: str = None,
        id: str = None,
        imsi: str = None,
        ip: str = None,
        os: str = None,
        os_version: str = None,
        server_time: int = None,
        update_time: int = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.app_build = app_build
        self.app_id = app_id
        # appKey
        self.app_key = app_key
        self.app_version = app_version
        self.brand = brand
        self.client_time = client_time
        self.device_id = device_id
        self.device_model = device_model
        self.geo = geo
        self.id = id
        self.imsi = imsi
        self.ip = ip
        self.os = os
        self.os_version = os_version
        self.server_time = server_time
        self.update_time = update_time
        # userId
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_build is not None:
            result['AppBuild'] = self.app_build

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.brand is not None:
            result['Brand'] = self.brand

        if self.client_time is not None:
            result['ClientTime'] = self.client_time

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.device_model is not None:
            result['DeviceModel'] = self.device_model

        if self.geo is not None:
            result['Geo'] = self.geo

        if self.id is not None:
            result['Id'] = self.id

        if self.imsi is not None:
            result['Imsi'] = self.imsi

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.os is not None:
            result['Os'] = self.os

        if self.os_version is not None:
            result['OsVersion'] = self.os_version

        if self.server_time is not None:
            result['ServerTime'] = self.server_time

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppBuild') is not None:
            self.app_build = m.get('AppBuild')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('Brand') is not None:
            self.brand = m.get('Brand')

        if m.get('ClientTime') is not None:
            self.client_time = m.get('ClientTime')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')

        if m.get('Geo') is not None:
            self.geo = m.get('Geo')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Imsi') is not None:
            self.imsi = m.get('Imsi')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('OsVersion') is not None:
            self.os_version = m.get('OsVersion')

        if m.get('ServerTime') is not None:
            self.server_time = m.get('ServerTime')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

