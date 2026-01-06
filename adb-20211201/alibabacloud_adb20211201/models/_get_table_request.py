# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTableRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        db_name: str = None,
        region_id: str = None,
        table_name: str = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the database.
        self.db_name = db_name
        # The ID of the region in which the cluster resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

