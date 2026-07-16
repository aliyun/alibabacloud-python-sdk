# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindAliasRequest(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        app_key: int = None,
        device_id: str = None,
    ):
        # The alias to attach.
        # 
        # You can attach up to 10 aliases in one request. Separate multiple aliases with commas. Each alias can be up to 128 bytes long. Chinese characters count as three bytes each. A device can have up to 128 aliases attached. An alias can be attached to up to 128 devices.
        # 
        # This parameter is required.
        self.alias_name = alias_name
        # Your AppKey.
        # 
        # This parameter is required.
        self.app_key = app_key
        # The unique identifier of the device in Mobile Push. It is 32 characters long and contains only numbers and lowercase letters.
        # 
        # This parameter is required.
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        return self

