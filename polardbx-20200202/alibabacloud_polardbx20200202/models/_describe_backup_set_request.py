# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupSetRequest(DaraModel):
    def __init__(
        self,
        backup_set_id: str = None,
        dbinstance_name: str = None,
        dest_cross_region: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.backup_set_id = backup_set_id
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        self.dest_cross_region = dest_cross_region
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dest_cross_region is not None:
            result['DestCrossRegion'] = self.dest_cross_region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DestCrossRegion') is not None:
            self.dest_cross_region = m.get('DestCrossRegion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

