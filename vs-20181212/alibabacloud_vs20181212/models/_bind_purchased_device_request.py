# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindPurchasedDeviceRequest(DaraModel):
    def __init__(
        self,
        device_id: str = None,
        group_id: str = None,
        owner_id: int = None,
        region: str = None,
    ):
        # This parameter is required.
        self.device_id = device_id
        # This parameter is required.
        self.group_id = group_id
        self.owner_id = owner_id
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

