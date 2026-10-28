# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchDBInstanceHARequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
        switch_time: str = None,
        switch_time_mode: str = None,
        target_primary_azone_id: str = None,
        target_primary_region_id: str = None,
    ):
        # The name of the PolarDB-X instance.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The specified switchover time. This parameter is required when SwitchTimeMode is set to 2. The time must be in UTC and in the YYYY-MM-DDThh:mm:ssZ format.
        self.switch_time = switch_time
        # The switchover mode. Valid values: 0: Immediate switchover. 1: Switchover during the O&M window. 2: Switchover at a specified time.
        self.switch_time_mode = switch_time_mode
        # The zone ID of the primary node after the switchover.
        self.target_primary_azone_id = target_primary_azone_id
        # The region ID of the primary node after the switchover.
        self.target_primary_region_id = target_primary_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode

        if self.target_primary_azone_id is not None:
            result['TargetPrimaryAzoneId'] = self.target_primary_azone_id

        if self.target_primary_region_id is not None:
            result['TargetPrimaryRegionId'] = self.target_primary_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')

        if m.get('TargetPrimaryAzoneId') is not None:
            self.target_primary_azone_id = m.get('TargetPrimaryAzoneId')

        if m.get('TargetPrimaryRegionId') is not None:
            self.target_primary_region_id = m.get('TargetPrimaryRegionId')

        return self

