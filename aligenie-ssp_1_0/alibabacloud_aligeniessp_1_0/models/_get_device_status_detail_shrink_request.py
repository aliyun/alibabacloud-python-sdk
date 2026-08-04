# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDeviceStatusDetailShrinkRequest(DaraModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        keys_shrink: str = None,
    ):
        # List of device identification information.
        # 
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # A collection of specified keys for device settings:  
        # Player: player  
        # Device volume: speaker  
        # Battery level: power
        # 
        # This parameter is required.
        self.keys_shrink = keys_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink

        if self.keys_shrink is not None:
            result['Keys'] = self.keys_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')

        if m.get('Keys') is not None:
            self.keys_shrink = m.get('Keys')

        return self

