# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserDeviceRequest(DaraModel):
    def __init__(
        self,
        device_tag: str = None,
    ):
        # This parameter is required.
        self.device_tag = device_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')

        return self

