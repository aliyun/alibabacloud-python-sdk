# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloseEngineMigrationRequest(DaraModel):
    def __init__(
        self,
        continue_enable_binlog: str = None,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.continue_enable_binlog = continue_enable_binlog
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.continue_enable_binlog is not None:
            result['ContinueEnableBinlog'] = self.continue_enable_binlog

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContinueEnableBinlog') is not None:
            self.continue_enable_binlog = m.get('ContinueEnableBinlog')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

