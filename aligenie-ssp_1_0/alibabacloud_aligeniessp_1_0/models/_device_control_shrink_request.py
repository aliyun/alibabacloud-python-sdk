# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeviceControlShrinkRequest(DaraModel):
    def __init__(
        self,
        control_request_shrink: str = None,
        device_info_shrink: str = None,
    ):
        # Input parameters for volume control
        self.control_request_shrink = control_request_shrink
        # List of device ID information.
        # 
        # This parameter is required.
        self.device_info_shrink = device_info_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.control_request_shrink is not None:
            result['ControlRequest'] = self.control_request_shrink

        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlRequest') is not None:
            self.control_request_shrink = m.get('ControlRequest')

        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')

        return self

