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
        # > If SwitchTimeMode is set to SpecifyTime, you must use this parameter to specify the upgrade time.
        self.switch_time = switch_time
        # Specifies whether to upgrade the minor engine version immediately. Valid values:
        # - **Immediate**: Upgrades immediately.
        # - **MaintainTime**: Upgrades within the O&M window.
        # - **SpecifyTime**: Upgrades at a specified time.
        self.switch_time_mode = switch_time_mode
        # The target minor engine version.
        # > By default, this parameter is left empty, and the minor engine version is upgraded to the latest version.
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

