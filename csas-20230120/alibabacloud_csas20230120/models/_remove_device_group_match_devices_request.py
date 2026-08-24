# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RemoveDeviceGroupMatchDevicesRequest(DaraModel):
    def __init__(
        self,
        dev_tags: List[str] = None,
        device_group_id: str = None,
    ):
        # The collection of terminal device IDs to be removed. At least one ID must be specified, and duplicate values are not allowed.
        # 
        # This parameter is required.
        self.dev_tags = dev_tags
        # The device label ID.
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
        if self.dev_tags is not None:
            result['DevTags'] = self.dev_tags

        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevTags') is not None:
            self.dev_tags = m.get('DevTags')

        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')

        return self

