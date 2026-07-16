# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PushMessageToiOSRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        body: str = None,
        job_key: str = None,
        store_offline: bool = None,
        target: str = None,
        target_value: str = None,
        title: str = None,
    ):
        # AppKey information.
        # 
        # This parameter is required.
        self.app_key = app_key
        # The content of the message.
        # 
        # This parameter is required.
        self.body = body
        # The custom ID for the push Job. If JobKey is not empty, this field is included in the receipt log. For receipt logs, see [Receipt Logs](https://help.aliyun.com/document_detail/434651.html).
        self.job_key = job_key
        # Whether to store the message offline. StoreOffline is set to false by default.
        # 
        # If stored, and the user is offline during the push, the message is sent again when the user comes online within the time-to-live (TTL). The default time-to-live (TTL) is 72 hours.
        self.store_offline = store_offline
        # Push target. Valid values:
        # 
        # - **DEVICE**: Push by device
        # 
        # - **ACCOUNT**: Push by account
        # 
        # - **ALIAS**: Push by alias
        # 
        # - **TAG**: Push by tag
        # 
        # - **ALL**: Push to all devices
        # 
        # This parameter is required.
        self.target = target
        # Set based on Target. Separate multiple values with commas. If the limit is exceeded, push multiple times.
        # 
        # - Target=DEVICE. Example values: `deviceid111,deviceid1111` (supports up to 1,000).
        # 
        # - Target=ACCOUNT. Example values: `account111,account222` (supports up to 1,000).
        # 
        # - Target=ALIAS. Example values: `alias111,alias222` (supports up to 1,000).
        # 
        # - Target=TAG. Supports single and multiple tags. For format, see [Tag Format](https://help.aliyun.com/document_detail/434847.html).
        # 
        # - Target=ALL. Value is **all**.
        # 
        # This parameter is required.
        self.target_value = target_value
        # The title of the message.
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

