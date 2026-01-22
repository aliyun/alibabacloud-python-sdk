# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AlignStoragePrimaryAzoneRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
        storage_instance_name: str = None,
        switch_time: str = None,
        switch_time_mode: str = None,
    ):
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # This parameter is required.
        self.region_id = region_id
        self.storage_instance_name = storage_instance_name
        self.switch_time = switch_time
        self.switch_time_mode = switch_time_mode

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

        if self.storage_instance_name is not None:
            result['StorageInstanceName'] = self.storage_instance_name

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StorageInstanceName') is not None:
            self.storage_instance_name = m.get('StorageInstanceName')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')

        return self

