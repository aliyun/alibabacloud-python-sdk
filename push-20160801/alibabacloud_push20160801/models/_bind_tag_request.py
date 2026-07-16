# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindTagRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        client_key: str = None,
        key_type: str = None,
        tag_name: str = None,
    ):
        # The AppKey of your application.
        # 
        # This parameter is required.
        self.app_key = app_key
        # The ID of the target device. You can specify a maximum of 1,000 device IDs.
        # 
        # This parameter is required.
        self.client_key = client_key
        # The type of the `ClientKey`. Valid value:
        # 
        # - **DEVICE**: Indicates a device target.
        # 
        # This parameter is required.
        self.key_type = key_type
        # The tags to bind. Separate multiple tags with commas (,). You can bind up to 10 tags per request.
        # A tag name can be up to 128 characters long (each Chinese character counts as 1 character). Each application can have up to 10,000 tags. A single device can be bound to multiple tags.
        # 
        # >Notice: 
        # 
        # Do not bind a single tag to more than 100,000 devices. This practice can increase push processing time and increase response time.
        # 
        # - Use the full push feature to send notifications to all devices.
        # 
        # - Split the device set into multiple fine-grained tags and call the push API in batches.
        # 
        # 
        # 
        # > - If you attempt to bind the same tag multiple times, the system automatically removes the duplicates.
        # >
        # > - When a user uninstalls the application from a device, the tags associated with that device are automatically unbound. This unbinding process may be slightly delayed.
        # 
        # This parameter is required.
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.client_key is not None:
            result['ClientKey'] = self.client_key

        if self.key_type is not None:
            result['KeyType'] = self.key_type

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('ClientKey') is not None:
            self.client_key = m.get('ClientKey')

        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

