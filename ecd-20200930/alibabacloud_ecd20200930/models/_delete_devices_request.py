# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteDevicesRequest(DaraModel):
    def __init__(
        self,
        client_type: int = None,
        device_ids: List[str] = None,
        force: int = None,
        region_id: str = None,
    ):
        # The type of the client.
        # 
        # Valid values:
        # 
        # *   1: hardware client.
        # *   2: software client.
        # 
        # This parameter is required.
        self.client_type = client_type
        # The IDs of the devices. You can specify up to 200 IDs.
        # 
        # This parameter is required.
        self.device_ids = device_ids
        # Specifies whether to forcefully delete the device if the device is bound to a user.
        # 
        # Valid values:
        # 
        # *   0: do not forcefully delete the device.
        # *   1: forcefully delete the device.
        # 
        # This parameter is required.
        self.force = force
        # The ID of the region. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the regions supported by WUYING Workspace.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.device_ids is not None:
            result['DeviceIds'] = self.device_ids

        if self.force is not None:
            result['Force'] = self.force

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('DeviceIds') is not None:
            self.device_ids = m.get('DeviceIds')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

