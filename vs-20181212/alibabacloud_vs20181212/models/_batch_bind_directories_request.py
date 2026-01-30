# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchBindDirectoriesRequest(DaraModel):
    def __init__(
        self,
        device_id: str = None,
        directory_id: str = None,
        owner_id: int = None,
    ):
        # This parameter is required.
        self.device_id = device_id
        # This parameter is required.
        self.directory_id = directory_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

