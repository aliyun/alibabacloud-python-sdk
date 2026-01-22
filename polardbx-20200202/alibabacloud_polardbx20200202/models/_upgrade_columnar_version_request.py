# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeColumnarVersionRequest(DaraModel):
    def __init__(
        self,
        columnar_version: str = None,
        dbinstance_name: str = None,
        instance_name: str = None,
        region_id: str = None,
        switch_mode: str = None,
    ):
        self.columnar_version = columnar_version
        self.dbinstance_name = dbinstance_name
        self.instance_name = instance_name
        self.region_id = region_id
        self.switch_mode = switch_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.columnar_version is not None:
            result['ColumnarVersion'] = self.columnar_version

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnarVersion') is not None:
            self.columnar_version = m.get('ColumnarVersion')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')

        return self

