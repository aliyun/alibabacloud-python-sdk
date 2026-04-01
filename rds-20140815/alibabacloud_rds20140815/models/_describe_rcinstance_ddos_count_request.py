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
        # The region ID of the asset.
        self.ddos_region_id = ddos_region_id
        # The type of the asset that is assigned a public IP address. Fixed value: **ecs**.
        self.instance_type = instance_type
        # The ID of the region in which the RDS Custom instance resides.
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

