# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnbindParentPlatformDeviceRequest(DaraModel):
    def __init__(
        self,
        device_id: str = None,
        owner_id: int = None,
        parent_platform_id: str = None,
    ):
        # This parameter is required.
        self.device_id = device_id
        self.owner_id = owner_id
        # This parameter is required.
        self.parent_platform_id = parent_platform_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.parent_platform_id is not None:
            result['ParentPlatformId'] = self.parent_platform_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ParentPlatformId') is not None:
            self.parent_platform_id = m.get('ParentPlatformId')

        return self

