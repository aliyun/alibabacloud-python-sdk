# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteFaceDeviceGroupRequest(DaraModel):
    def __init__(
        self,
        device_group_id: str = None,
        isolation_id: str = None,
    ):
        # The device group ID.
        # 
        # This parameter is required.
        self.device_group_id = device_group_id
        # The isolation ID.
        # 
        # This parameter is required.
        self.isolation_id = isolation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id

        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')

        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')

        return self

