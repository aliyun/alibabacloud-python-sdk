# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchVccConnectionRequest(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        connection_type: str = None,
        region_id: str = None,
        v_switch_id: str = None,
        vcc_id: str = None,
        vpc_id: str = None,
    ):
        # CEN
        self.cen_id = cen_id
        # Connection type, CENTR/VPC
        self.connection_type = connection_type
        # Region ID
        # 
        # This parameter is required.
        self.region_id = region_id
        # vSwitch ID
        self.v_switch_id = v_switch_id
        # Cloud Connect Network (CCN) ID
        # 
        # This parameter is required.
        self.vcc_id = vcc_id
        # VPC ID
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

