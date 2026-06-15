# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PushNoticeToAndroidRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        body: str = None,
        ext_parameters: str = None,
        job_key: str = None,
        store_offline: bool = None,
        target: str = None,
        target_value: str = None,
        title: str = None,
    ):
        # Your AppKey.
        # 
        # This parameter is required.
        self.app_key = app_key
        # The body of the notification.
        # 
        # This parameter is required.
        self.body = body
        # Custom key-value pairs for Android-specific extensions. Pass this as a JSON object.
        self.ext_parameters = ext_parameters
        # A custom ID for the push task. If you specify a non-empty JobKey, it appears in the delivery receipt log. For more information, see [Delivery receipt logs](https://help.aliyun.com/document_detail/434651.html).
        self.job_key = job_key
        # Whether to store the notification for offline delivery. Default: false.
        # 
        # If enabled, the notification is redelivered when the user comes online within the time-to-live (TTL) period. Default TTL: 72 hours.
        self.store_offline = store_offline
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
        # Set this based on the Target value. Separate multiple values with commas. If you exceed the limit, send multiple requests.
        # 
        # - If Target=DEVICE, use values such as `deviceid111,deviceid1111`. Maximum: 1000 devices.
        # 
        # - If Target=ACCOUNT, use values such as `account111,account222`. Maximum: 1000 accounts.
        # 
        # - If Target=ALIAS, use values such as `alias111,alias222`. Maximum: 1000 aliases.
        # 
        # - If Target=TAG, support single or multiple tags. For format details, see [Tag format](https://help.aliyun.com/document_detail/434847.html).
        # 
        # - If Target=ALL, set this to **ALL**.
        # 
        # This parameter is required.
        self.target_value = target_value
        # The title of the notification.
        # 
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.body is not None:
            result['Body'] = self.body

        if self.ext_parameters is not None:
            result['ExtParameters'] = self.ext_parameters

        if self.job_key is not None:
            result['JobKey'] = self.job_key

        if self.store_offline is not None:
            result['StoreOffline'] = self.store_offline

        if self.target is not None:
            result['Target'] = self.target

        if self.target_value is not None:
            result['TargetValue'] = self.target_value

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('Body') is not None:
            self.body = m.get('Body')

        if m.get('ExtParameters') is not None:
            self.ext_parameters = m.get('ExtParameters')

        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')

        if m.get('StoreOffline') is not None:
            self.store_offline = m.get('StoreOffline')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

