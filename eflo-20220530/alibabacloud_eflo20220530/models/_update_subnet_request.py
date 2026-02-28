# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSubnetRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        subnet_id: str = None,
        subnet_name: str = None,
        vpd_id: str = None,
        zone_id: str = None,
    ):
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The subnet instance ID.
        # 
        # This parameter is required.
        self.subnet_id = subnet_id
        # The new name for the subnet instance.
        self.subnet_name = subnet_name
        # The ID of the VPD to which the subnet belongs.
        # 
        # This parameter is required.
        self.vpd_id = vpd_id
        # The zone ID.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id

        if self.subnet_name is not None:
            result['SubnetName'] = self.subnet_name

        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')

        if m.get('SubnetName') is not None:
            self.subnet_name = m.get('SubnetName')

        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

