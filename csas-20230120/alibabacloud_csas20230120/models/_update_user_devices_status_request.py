# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateUserDevicesStatusRequest(DaraModel):
    def __init__(
        self,
        device_action: str = None,
        device_tags: List[str] = None,
    ):
        # This parameter is required.
        self.device_action = device_action
        # This parameter is required.
        self.device_tags = device_tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_action is not None:
            result['DeviceAction'] = self.device_action

        if self.device_tags is not None:
            result['DeviceTags'] = self.device_tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceAction') is not None:
            self.device_action = m.get('DeviceAction')

        if m.get('DeviceTags') is not None:
            self.device_tags = m.get('DeviceTags')

        return self

