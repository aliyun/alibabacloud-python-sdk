# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAccountsRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        dbcluster_id: str = None,
        engine: str = None,
        owner_id: str = None,
    ):
        # The name of the database account.
        # 
        # > If you do not specify this parameter, the information about all database accounts in the cluster is returned.
        self.account_name = account_name
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The database engine of the cluster. Valid values:
        # 
        # *   **AnalyticDB** (default): the AnalyticDB for MySQL engine.
        # *   **Clickhouse**: the wide table engine.
        self.engine = engine
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

