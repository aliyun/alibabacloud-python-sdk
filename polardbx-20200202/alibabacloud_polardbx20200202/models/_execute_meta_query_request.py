# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteMetaQueryRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
        sql: str = None,
        storage_inst_id: str = None,
    ):
        # The primary instance ID.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The SQL statement to execute.
        # 
        # This parameter is required.
        self.sql = sql
        # The data node (DN) instance ID.
        self.storage_inst_id = storage_inst_id

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

        if self.sql is not None:
            result['Sql'] = self.sql

        if self.storage_inst_id is not None:
            result['StorageInstId'] = self.storage_inst_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        if m.get('StorageInstId') is not None:
            self.storage_inst_id = m.get('StorageInstId')

        return self

