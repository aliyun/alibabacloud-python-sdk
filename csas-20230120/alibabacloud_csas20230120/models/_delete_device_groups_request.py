# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteDeviceGroupsRequest(DaraModel):
    def __init__(
        self,
        device_group_ids: List[str] = None,
    ):
        # The collection of instance tag IDs to delete. Duplicate values are not allowed.
        self.device_group_ids = device_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_group_ids is not None:
            result['DeviceGroupIds'] = self.device_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupIds') is not None:
            self.device_group_ids = m.get('DeviceGroupIds')

        return self

