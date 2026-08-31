# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryColumnarLogRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        max_result_rows: int = None,
        region_id: str = None,
        sql: str = None,
    ):
        # The ID of the PolarDB-X instance for which you want to query column store audit logs.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The maximum number of result rows to return for this request. Valid values: 1 to 1000. Default value: 100. The actual number of returned rows is also subject to the top-level LIMIT clause in the SQL statement and the current service policy.
        self.max_result_rows = max_result_rows
        # The region ID of the request. The region ID must be the same as the region where the SQLQuery service is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The read-only query statement to execute. Only a single MySQL SELECT statement is supported, and it must access the fully qualified polardbx_sls table. Multi-statement queries, write operations, locks, user variables, dynamic placeholders, and reserved hints are not supported.
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
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.max_result_rows is not None:
            result['MaxResultRows'] = self.max_result_rows

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sql is not None:
            result['SQL'] = self.sql

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('MaxResultRows') is not None:
            self.max_result_rows = m.get('MaxResultRows')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SQL') is not None:
            self.sql = m.get('SQL')

        return self

