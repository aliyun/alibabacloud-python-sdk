# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeDBInstanceKernelVersionRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        minor_version: str = None,
        region_id: str = None,
        switch_mode: str = None,
    ):
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        self.minor_version = minor_version
        # This parameter is required.
        self.region_id = region_id
        self.switch_mode = switch_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')

        return self

