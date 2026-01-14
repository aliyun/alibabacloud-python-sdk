# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeIpSetRequest(DaraModel):
    def __init__(
        self,
        ip_set_id: str = None,
        region_id: str = None,
    ):
        # The ID of the acceleration region.
        # 
        # You can call the [ListIpSets](https://help.aliyun.com/document_detail/2253273.html) operation to query the IDs of acceleration regions of a specific GA instance.
        # 
        # This parameter is required.
        self.ip_set_id = ip_set_id
        # The ID of the region where the Global Accelerator (GA) instance is deployed. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

