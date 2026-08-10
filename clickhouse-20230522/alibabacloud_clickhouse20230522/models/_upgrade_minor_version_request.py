# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeMinorVersionRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        region_id: str = None,
        switch_time: str = None,
        switch_time_mode: str = None,
        target_minor_version: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The specified upgrade time. Format: yyyy-MM-ddTHH:mm:ssZ (UTC).
        # > This parameter is required when SwitchTimeMode is set to SpecifyTime.
        self.switch_time = switch_time
        # Specifies when to upgrade. Valid values:
        # - **Immediate**: upgrades immediately.
        # - **MaintainTime**: upgrades during the O&M window.
        # - **SpecifyTime**: upgrades at a specified time.
        self.switch_time_mode = switch_time_mode
        # The target minor engine version.
        # >By default, leave this parameter empty to upgrade to the latest minor engine version.
        self.target_minor_version = target_minor_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode

        if self.target_minor_version is not None:
            result['TargetMinorVersion'] = self.target_minor_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')

        if m.get('TargetMinorVersion') is not None:
            self.target_minor_version = m.get('TargetMinorVersion')

        return self

