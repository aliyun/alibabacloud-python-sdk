# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDeviceGroupRequest(DaraModel):
    def __init__(
        self,
        device_group_id: str = None,
    ):
        # The device label ID. You can obtain this value from:
        # - [ListDeviceGroups](~~ListDeviceGroups~~): Lists device labels.
        # - [CreateDeviceGroup](~~CreateDeviceGroup~~): Creates a device label.
        # 
        # This parameter is required.
        self.device_group_id = device_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')

        return self

