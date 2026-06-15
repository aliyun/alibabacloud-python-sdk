# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PushNoticeToiOSRequest(DaraModel):
    def __init__(
        self,
        apns_env: str = None,
        app_key: int = None,
        body: str = None,
        ext_parameters: str = None,
        job_key: str = None,
        target: str = None,
        target_value: str = None,
        title: str = None,
    ):
        # iOS notifications use Apple’s APNs service. Specify the environment.
        # 
        # - DEV: Development environment.
        # 
        # - PRODUCT: Production environment.
        # 
        # This parameter is required.
        self.apns_env = apns_env
        # Your AppKey.
        # 
        # This parameter is required.
        self.app_key = app_key
        # The body text of the notification.
        # 
        # This parameter is required.
        self.body = body
        # A custom key-value map for developer extensions.
        # 
        # > For iOS devices, pass this parameter as a JSON object. Otherwise, parsing fails.
        self.ext_parameters = ext_parameters
        # A custom ID for the push task. If you specify a JobKey, the delivery log includes this field. For more information, see [Delivery logs](https://help.aliyun.com/document_detail/434651.html).
        self.job_key = job_key
        # The target of the push. Valid values:
        # 
        # - **DEVICE**: Push to specific devices.
        # 
        # - **ACCOUNT**: Push to specific accounts.
        # 
        # - **ALIAS**: Push to users with specific aliases.
        # 
        # - **TAG**: Push to users with specific tags.
        # 
        # - **ALL**: Push to all devices.
        # 
        # This parameter is required.
        self.target = target
        # Values depend on the Target value. Separate multiple values with commas. If you exceed the limit, send multiple requests.
        # 
        # - If Target=DEVICE, use values such as `deviceid111,deviceid1111`. Maximum: 1000.
        # 
        # - If Target=ACCOUNT, use values such as `account111,account222`. Maximum: 1000.
        # 
        # - If Target=ALIAS, use values such as `alias111,alias222`. Maximum: 1000.
        # 
        # - If Target=TAG, support single or multiple tags. For format details, see [Tag format](https://help.aliyun.com/document_detail/434847.html).
        # 
        # - If Target=ALL, set this to **ALL**.
        # 
        # This parameter is required.
        self.target_value = target_value
        # The title of the notification.
        # 
        # - iOS 10 and later: Displays as the notification title.
        # 
        # - iOS 8.2 through iOS 9.x: Replaces the app name in the notification.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apns_env is not None:
            result['ApnsEnv'] = self.apns_env

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.body is not None:
            result['Body'] = self.body

        if self.ext_parameters is not None:
            result['ExtParameters'] = self.ext_parameters

        if self.job_key is not None:
            result['JobKey'] = self.job_key

        if self.target is not None:
            result['Target'] = self.target

        if self.target_value is not None:
            result['TargetValue'] = self.target_value

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApnsEnv') is not None:
            self.apns_env = m.get('ApnsEnv')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('Body') is not None:
            self.body = m.get('Body')

        if m.get('ExtParameters') is not None:
            self.ext_parameters = m.get('ExtParameters')

        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

