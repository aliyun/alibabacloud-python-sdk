# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PushMessageToAndroidRequest(DaraModel):
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
        # The AppKey.
        # 
        # This parameter is required.
        self.app_key = app_key
        # The content of the message.
        # 
        # This parameter is required.
        self.body = body
        # A custom ID for the push task. If \\`JobKey\\` is not empty, this field is included in the receipt logs. For more information, see [Receipt logs](https://help.aliyun.com/document_detail/434651.html).
        self.job_key = job_key
        # Specifies whether to store the message offline. The default value is false.
        # 
        # If you store the message and the user is offline, the message is sent again when the user comes online within the time-to-live (TTL) period. The default TTL is 72 hours.
        self.store_offline = store_offline
        # The push target. Valid values:
        # 
        # - **DEVICE**: Pushes messages to devices.
        # 
        # - **ACCOUNT**: Pushes messages to accounts.
        # 
        # - **ALIAS**: Pushes messages to aliases.
        # 
        # - **TAG**: Pushes messages to tags.
        # 
        # - **ALL**: Pushes messages to all devices.
        # 
        # This parameter is required.
        self.target = target
        # Set this parameter based on the value of \\`Target\\`. Use commas (,) to separate multiple values. If you exceed the limit, send the pushes in batches.
        # 
        # - If \\`Target\\` is set to \\`DEVICE\\`, specify device IDs. Example: `deviceid111,deviceid1111`. You can specify up to 1,000 device IDs.
        # 
        # - If \\`Target\\` is set to \\`ACCOUNT\\`, specify account IDs. Example: `account111,account222`. You can specify up to 1,000 account IDs.
        # 
        # - If \\`Target\\` is set to \\`ALIAS\\`, specify aliases. Example: `alias111,alias222`. You can specify up to 1,000 aliases.
        # 
        # - If \\`Target\\` is set to \\`TAG\\`, you can specify one or more tags. For more information about the format, see [Tag format](https://help.aliyun.com/document_detail/434847.html).
        # 
        # - If \\`Target\\` is set to \\`ALL\\`, set the value to **all**.
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

