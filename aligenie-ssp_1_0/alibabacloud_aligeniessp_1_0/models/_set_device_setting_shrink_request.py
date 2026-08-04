# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class SetDeviceSettingShrinkRequest(DaraModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        key: str = None,
        value: Any = None,
    ):
        # List of user identifier information.
        # 
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # The collection of keys specified for device settings:  
        # Do Not Disturb mode: nightMode
        # 
        # This parameter is required.
        self.key = key
        # Attribute Value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink

        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

