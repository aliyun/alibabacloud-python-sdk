# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateUserDevicesSharingStatusRequest(DaraModel):
    def __init__(
        self,
        device_tags: List[str] = None,
        sharing_status: bool = None,
    ):
        # This parameter is required.
        self.device_tags = device_tags
        # This parameter is required.
        self.sharing_status = sharing_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_tags is not None:
            result['DeviceTags'] = self.device_tags

        if self.sharing_status is not None:
            result['SharingStatus'] = self.sharing_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceTags') is not None:
            self.device_tags = m.get('DeviceTags')

        if m.get('SharingStatus') is not None:
            self.sharing_status = m.get('SharingStatus')

        return self

