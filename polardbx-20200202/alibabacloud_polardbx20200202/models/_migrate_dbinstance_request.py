# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MigrateDBInstanceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        primary_zone_id: str = None,
        region_id: str = None,
        secondary_zone_id: str = None,
        switch_mode: str = None,
        tertiary_zone_id: str = None,
        topology_type: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # This parameter is required.
        self.primary_zone_id = primary_zone_id
        # This parameter is required.
        self.region_id = region_id
        self.secondary_zone_id = secondary_zone_id
        self.switch_mode = switch_mode
        self.tertiary_zone_id = tertiary_zone_id
        # This parameter is required.
        self.topology_type = topology_type
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.primary_zone_id is not None:
            result['PrimaryZoneId'] = self.primary_zone_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id

        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode

        if self.tertiary_zone_id is not None:
            result['TertiaryZoneId'] = self.tertiary_zone_id

        if self.topology_type is not None:
            result['TopologyType'] = self.topology_type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('PrimaryZoneId') is not None:
            self.primary_zone_id = m.get('PrimaryZoneId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')

        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')

        if m.get('TertiaryZoneId') is not None:
            self.tertiary_zone_id = m.get('TertiaryZoneId')

        if m.get('TopologyType') is not None:
            self.topology_type = m.get('TopologyType')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

