# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTableSchemaRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        database: str = None,
        region_id: str = None,
        table: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The database name.
        # 
        # This parameter is required.
        self.database = database
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The table name.
        # 
        # This parameter is required.
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.database is not None:
            result['Database'] = self.database

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.table is not None:
            result['Table'] = self.table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Table') is not None:
            self.table = m.get('Table')

        return self

