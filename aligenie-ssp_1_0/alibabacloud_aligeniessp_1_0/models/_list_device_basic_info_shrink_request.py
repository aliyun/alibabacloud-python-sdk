# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDeviceBasicInfoShrinkRequest(DaraModel):
    def __init__(
        self,
        device_infos_shrink: str = None,
    ):
        # List of device identity information.
        self.device_infos_shrink = device_infos_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_infos_shrink is not None:
            result['DeviceInfos'] = self.device_infos_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfos') is not None:
            self.device_infos_shrink = m.get('DeviceInfos')

        return self

