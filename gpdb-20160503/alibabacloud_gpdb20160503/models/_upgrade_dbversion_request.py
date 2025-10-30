# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeDBVersionRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        major_version: str = None,
        minor_version: str = None,
        owner_id: int = None,
        region_id: str = None,
        switch_time: str = None,
        switch_time_mode: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is no longer used and does not need to be specified.
        self.major_version = major_version
        # The minor version of the instance.
        self.minor_version = minor_version
        self.owner_id = owner_id
        # The region ID of the instance.
        self.region_id = region_id
        # This parameter is no longer used and does not need to be specified.
        self.switch_time = switch_time
        # This parameter is no longer used and does not need to be specified.
        self.switch_time_mode = switch_time_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.major_version is not None:
            result['MajorVersion'] = self.major_version

        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')

        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')

        return self

