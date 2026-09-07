# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddDevicesRequest(DaraModel):
    def __init__(
        self,
        client_type: int = None,
        device_ids: List[str] = None,
        region_id: str = None,
    ):
        # The device type.
        # 
        # This parameter is required.
        self.client_type = client_type
        # The list of device IDs. You can specify 1 to 200 device IDs.
        # 
        # This parameter is required.
        self.device_ids = device_ids
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by Elastic Desktop Service.
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('DeviceIds') is not None:
            self.device_ids = m.get('DeviceIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

