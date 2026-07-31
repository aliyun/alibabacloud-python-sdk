# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateSqlBySemanticSqlRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        schema_name: str = None,
        sql: str = None,
    ):
        # The ID of the ADB cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The schema name.
        self.schema_name = schema_name
        # The SQL statement that queries the semantic view.
        # 
        # This parameter is required.
        self.sql = sql

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.sql is not None:
            result['Sql'] = self.sql

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        return self

