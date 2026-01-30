# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDeviceChannelsRequest(DaraModel):
    def __init__(
        self,
        channels: str = None,
        device_status: str = None,
        dsn: str = None,
        id: str = None,
        owner_id: int = None,
    ):
        # This parameter is required.
        self.channels = channels
        self.device_status = device_status
        self.dsn = dsn
        # This parameter is required.
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channels is not None:
            result['Channels'] = self.channels

        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status

        if self.dsn is not None:
            result['Dsn'] = self.dsn

        if self.id is not None:
            result['Id'] = self.id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')

        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')

        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

