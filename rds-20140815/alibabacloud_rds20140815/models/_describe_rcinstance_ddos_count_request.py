# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRCInstanceDdosCountRequest(DaraModel):
    def __init__(
        self,
        ddos_region_id: str = None,
        instance_type: str = None,
        region_id: str = None,
    ):
        # The region ID of the assets that are assigned public IP addresses to query.
        self.ddos_region_id = ddos_region_id
        # The instance type of the assets that are assigned public IP addresses to query. Set the value to **ecs**.
        self.instance_type = instance_type
        # The region ID of the RDS Custom instance.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

